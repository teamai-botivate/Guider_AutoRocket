from langchain_core.prompts import ChatPromptTemplate

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


def make_retrieve_node(vector_store: VectorStoreClient):
    async def retrieve_node(state: AssistantState) -> dict:
        allowed = state["allowed_modules"]
        module_filter = None if allowed == ["*"] else ([registry.COMMON_MODULE] + allowed)

        chunks = vector_store.similarity_search(state["user_message"], k=5, module_filter=module_filter)
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

        probe = vector_store.similarity_search(state["user_message"], k=3, module_filter=None)
        if probe:
            return {"in_scope": False, "requested_module_hint": probe[0].module}

        return {"in_scope": True}

    return scope_decision_node


def route_after_scope(state: AssistantState) -> str:
    return "refuse" if not state["in_scope"] else "generate"


async def refuse_node(state: AssistantState) -> dict:
    module_display = registry.display_name(state.get("requested_module_hint"))
    return {"answer": REFUSAL_TEMPLATE.format(module_display=module_display), "sources": []}


def _to_langchain_history(conversation_history) -> list[tuple[str, str]]:
    messages = []
    for turn in conversation_history:
        role = "human" if turn.role == "user" else "ai"
        messages.append((role, turn.content))
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
        result = await chain.ainvoke({"context": context, "question": state["user_message"]})
        return {"answer": result.content, "sources": state["retrieved_docs"]}

    return generate_node
