import logging
import re

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from app.auth.jwt_verifier import decode_and_verify_jwt
from app.auth.node_backend_client import collect_department_names, fetch_me
from app.core.exceptions import UpstreamMeError
from app.db import get_tenant_api_key
from app.graph.llm import get_llm_for_tenant
from app.graph.prompts import REFUSAL_TEMPLATE, SYSTEM_PROMPT
from app.graph.state import AssistantState
from app.modules import registry
from app.modules.department_mapping import resolve_allowed_modules
from app.retrieval.base import VectorStoreClient
from app.schemas.chat import SourceRef

ADMIN_ROLES = {"SUPERADMIN", "ADMIN"}

logger = logging.getLogger("autorocket_ai_assistant.graph")

FOLLOWUP_HISTORY_TURNS = 10  # the schema allows 20; the follow-up steps only need the recent ones
FOLLOWUP_TURN_MAX_CHARS = 3000


async def auth_node(state: AssistantState) -> dict:
    try:
        decoded = decode_and_verify_jwt(state["bearer_token"])
    except Exception as exc:  # AuthError, propagated as a state field so the graph can branch
        return {"auth_error": str(exc)}
    return {
        "user_id": decoded.user_id,
        "tenant_id": decoded.tenant_id,
        "role": decoded.role,
        "token_department_names": decoded.departments,
        "auth_error": None,
    }


def route_after_auth(state: AssistantState) -> str:
    return "end" if state.get("auth_error") else "continue"


async def tenant_key_node(state: AssistantState) -> dict:
    key = await get_tenant_api_key(state["tenant_id"])
    if not key:
        return {
            "tenant_api_key": None,
            "auth_error": "OpenAI key not configured for this tenant",
        }
    return {"tenant_api_key": key, "auth_error": None}


def route_after_tenant_key(state: AssistantState) -> str:
    return "end" if state.get("auth_error") else "continue"


async def department_node(state: AssistantState) -> dict:
    if state["role"] in ADMIN_ROLES:
        return {"department_names": [], "allowed_modules": ["*"], "department_error": None}

    token_department_names = state.get("token_department_names") or []
    if token_department_names:
        allowed = resolve_allowed_modules(token_department_names)
        return {
            "department_names": token_department_names,
            "allowed_modules": allowed,
            "department_error": None,
        }

    try:
        profile = await fetch_me(state["bearer_token"])
    except UpstreamMeError:
        # fail closed to common-only access if we can't resolve department
        return {"department_names": [], "allowed_modules": [], "department_error": "me_unreachable"}

    dept_names = collect_department_names(profile)
    allowed = resolve_allowed_modules(dept_names)
    return {"department_names": dept_names, "allowed_modules": allowed, "department_error": None}


def _search_query(state: AssistantState) -> str:
    # For a "refine" follow-up this is the rewritten standalone question; otherwise the user's own message.
    return state.get("search_query") or state["user_message"]


# ---------------------------------------------------------------------------------------------
# Follow-up handling: "ab hindi me batao", "uske baad kya karna hai?" must not be searched as-is.
# ---------------------------------------------------------------------------------------------

# Reformat / translate / shorten / explain the PREVIOUS ANSWER (English + Hinglish + Devanagari).
_TRANSFORM_RE = re.compile(
    r"\b(hindi|hinglish|english|angrezi|marathi|gujarati|translate|translation|anuvad"
    r"|short|shorter|brief|briefly|summary|summarize|summarise|chhota|chota|chhoti|sankshep|sankshipt|"
    r"step\s*by\s*step|steps?\s*(me|mein|wise)|bullet|bullets|points?\s*(me|mein)|list\s*(me|mein|form)"
    r"|explain|samjha\w*|samjh\w*|dobara|dubara|phir\s*se|once\s*again|again|repeat|simple|simply|easy|aasan|asaan)\b"
    r"|हिंदी|हिन्दी|अंग्रेजी|संक्षेप|समझा\w*|दोबारा",
    re.IGNORECASE,
)
_TRANSFORM_MAX_WORDS = 6

# Needs the subject of the previous question: connectors, pronouns, "same" words.
_REFINE_START_RE = re.compile(
    r"^\s*(aur|और|also|and|then|phir|fir|uske|iske|uska|iska|uski|iski|usme|isme|usse|isse|wahi|wohi|vahi|same|"
    r"what\s+about|how\s+about|what\s+next|next|after\s+that|and\s+then|ok(ay)?\s+(and|then))\b",
    re.IGNORECASE,
)
_REFINE_ANY_RE = re.compile(
    r"\b(uske\s*baad|iske\s*baad|after\s+that|aur\s+kya|what\s+else|isme|usme|isse|usse|isko|usko|uska|iska|uski|iski"
    r"|us\s+wale|is\s+wale|wahi|wohi|vahi|same\s+(one|lead|task|module|thing)|this|that|it|them|those|these)\b",
    re.IGNORECASE,
)
_NEW_QUESTION_START_RE = re.compile(
    r"^\s*(how\s+(do|can|to|should)|where|what\s+is|what\s+are|kaise|kese|kahan|kaha|kya|kab|which|"
    r"mujhe|main|mai|i\s+(want|need)|can\s+i|how\s+does)\b",
    re.IGNORECASE,
)


def followup_kind(message: str, history) -> str | None:
    """
    Keyword classifier for the latest message. "transform" = reformat/translate/shorten/explain the previous answer,
    "refine" = needs the previous question's subject, "new" = a standalone question, None = unsure (ask the LLM).
    With no history it is always "new".
    """
    if not history:
        return "new"
    text = (message or "").strip()
    if not text:
        return "new"
    words = re.findall(r"\w+", text, flags=re.UNICODE)
    n = len(words)

    if n <= _TRANSFORM_MAX_WORDS and _TRANSFORM_RE.search(text):
        return "transform"
    if _REFINE_START_RE.search(text):
        return "refine"
    if n <= 8 and _REFINE_ANY_RE.search(text):
        return "refine"
    if n <= 3:
        return "refine"
    if n >= 9:
        return "new"
    if n >= 4 and _NEW_QUESTION_START_RE.search(text):
        return "new"
    return None


def _recent_history(state: AssistantState) -> list:
    """Last FOLLOWUP_HISTORY_TURNS turns, each content capped, as (role, text) pairs."""
    turns = (state.get("conversation_history") or [])[-FOLLOWUP_HISTORY_TURNS:]
    return [(t.role, (t.content or "")[:FOLLOWUP_TURN_MAX_CHARS]) for t in turns]


def _content_text(content) -> str:
    # Claude can return a list of content blocks, OpenAI a plain string.
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            b if isinstance(b, str) else (b.get("text", "") if isinstance(b, dict) else "") for b in content
        )
    return str(content or "")


_CLASSIFY_PROMPT = (
    "You classify the LATEST user message of a chat with a software help assistant, given the recent conversation.\n"
    "Reply with exactly one word:\n"
    "TRANSFORM - the user wants the previous assistant answer translated, shortened, reformatted, repeated or "
    "explained more simply (no new information needed).\n"
    "REFINE - the user asks a new question that only makes sense with the previous question's subject "
    "(e.g. 'and after that?', 'for the same lead', 'what about approval?').\n"
    "NEW - a standalone question that does not depend on the conversation."
)

_REWRITE_PROMPT = (
    "Rewrite the LATEST user message into ONE standalone question, using the recent conversation to fill in what "
    "it refers to. Keep all names and module/page names exactly. Write it in the same language the user used. "
    "If it is already standalone, return it unchanged. Output ONLY the question, nothing else."
)

_TRANSFORM_PROMPT = (
    "You are the AutoRocket Assistant. The user wants the PREVIOUS ANSWER below changed as they ask in their latest "
    "message (translate, shorten, step by step, bullets, explain simply, repeat...). Use ONLY the previous answer: "
    "keep every step, button, page and name exactly as written, never add or invent anything. Reply in the language "
    "and format the user asks for; if they do not say, use the language of their message. "
    "Keep Markdown links as they are."
)


def _transcript(pairs) -> str:
    return "\n".join(f"{'User' if role == 'user' else 'Assistant'}: {text}" for role, text in pairs)


async def _classify_with_llm(llm, message: str, pairs) -> str:
    """One tiny LLM call for messages the keywords cannot decide. Any failure counts as "new"."""
    try:
        result = await llm.bind(max_tokens=10).ainvoke(
            [
                SystemMessage(content=_CLASSIFY_PROMPT),
                HumanMessage(content=f"Conversation:\n{_transcript(pairs[-4:])}\n\nLATEST user message: {message}"),
            ]
        )
        word = _content_text(result.content).strip().upper()
        if word.startswith("TRANSFORM"):
            return "transform"
        if word.startswith("REFINE"):
            return "refine"
    except Exception:
        logger.warning("follow-up classification failed; treating as a new question", exc_info=True)
    return "new"


async def _rewrite_standalone(llm, message: str, pairs) -> str:
    try:
        result = await llm.bind(max_tokens=150).ainvoke(
            [
                SystemMessage(content=_REWRITE_PROMPT),
                HumanMessage(content=f"Conversation:\n{_transcript(pairs[-3:])}\n\nLATEST user message: {message}"),
            ]
        )
        rewritten = _content_text(result.content).strip().strip('"').strip("'").strip()
        if rewritten and len(rewritten) <= 600:
            return rewritten
    except Exception:
        logger.warning("follow-up rewrite failed; using the original message", exc_info=True)
    return message


async def followup_node(state: AssistantState) -> dict:
    message = state["user_message"]
    pairs = _recent_history(state)
    kind = followup_kind(message, pairs)
    llm = None
    if pairs and (kind is None or kind == "refine"):
        llm = get_llm_for_tenant(state["tenant_api_key"])
    if kind is None:
        kind = await _classify_with_llm(llm, message, pairs)

    if kind == "transform" and not any(role == "assistant" for role, _ in pairs):
        kind = "refine"  # nothing to transform: fall back to a search with the context
        llm = llm or get_llm_for_tenant(state["tenant_api_key"])

    if kind == "refine":
        rewritten = await _rewrite_standalone(llm, message, pairs)
        logger.info("follow-up rewrite: %r -> %r", message, rewritten)
        return {"followup_kind": "refine", "search_query": rewritten}
    return {"followup_kind": kind, "search_query": message}


def route_after_followup(state: AssistantState) -> str:
    return "transform" if state.get("followup_kind") == "transform" else "retrieve"


async def transform_node(state: AssistantState) -> dict:
    """Answer a reformat/translate request from the previous assistant answer only: no retrieval, no scope check."""
    pairs = _recent_history(state)
    previous = next((text for role, text in reversed(pairs) if role == "assistant"), "")
    llm = get_llm_for_tenant(state["tenant_api_key"])
    result = await llm.ainvoke(
        [
            SystemMessage(content=_TRANSFORM_PROMPT),
            HumanMessage(
                content=f"PREVIOUS ANSWER:\n{previous}\n\nUser's latest message: {state['user_message']}"
            ),
        ]
    )
    return {"in_scope": True, "answer": _content_text(result.content), "sources": []}


def make_retrieve_node(vector_store: VectorStoreClient):
    async def retrieve_node(state: AssistantState) -> dict:
        allowed = state["allowed_modules"]
        module_filter = None if allowed == ["*"] else ([registry.COMMON_MODULE] + allowed)

        chunks = vector_store.similarity_search(_search_query(state), k=5, module_filter=module_filter)
        sources = [
            SourceRef(module=c.module, doc_title=c.doc_title, source_path=c.source_path) for c in chunks
        ]
        return {
            "retrieved_docs": sources,
            "retrieved_chunks_text": [c.text for c in chunks],
        }

    return retrieve_node


def make_scope_decision_node(vector_store: VectorStoreClient):
    async def scope_decision_node(state: AssistantState) -> dict:
        if state["retrieved_docs"]:
            return {"in_scope": True}

        if state["allowed_modules"] == ["*"]:
            return {"in_scope": True}

        probe = vector_store.similarity_search(_search_query(state), k=3, module_filter=None)
        if probe:
            return {"in_scope": False, "requested_module_hint": probe[0].module}

        return {"in_scope": True}

    return scope_decision_node


def route_after_scope(state: AssistantState) -> str:
    return "refuse" if not state["in_scope"] else "generate"


async def refuse_node(state: AssistantState) -> dict:
    module_display = registry.display_name(state.get("requested_module_hint"))
    return {"answer": REFUSAL_TEMPLATE.format(module_display=module_display), "sources": []}


def _to_langchain_history(conversation_history) -> list[BaseMessage]:
    # Real message objects, NOT (role, text) tuples: ChatPromptTemplate treats tuple strings as
    # templates, so a "{" or "}" in an earlier answer (JSON, code) would crash the whole request.
    messages: list[BaseMessage] = []
    for turn in conversation_history:
        messages.append(HumanMessage(content=turn.content) if turn.role == "user" else AIMessage(content=turn.content))
    return messages


def make_generate_node():
    async def generate_node(state: AssistantState) -> dict:
        context = "\n\n---\n\n".join(state["retrieved_chunks_text"]) or "(no matching documentation found)"
        history_msgs = _to_langchain_history(state.get("conversation_history", []))

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", SYSTEM_PROMPT),
                *history_msgs,
                ("human", "Context:\n{context}\n\nQuestion: {question}"),
            ]
        )
        llm = get_llm_for_tenant(state["tenant_api_key"])
        chain = prompt | llm
        result = await chain.ainvoke(
            {"history": history_msgs, "context": context, "question": state["user_message"]}
        )
        return {"answer": result.content, "sources": state["retrieved_docs"]}

    return generate_node
