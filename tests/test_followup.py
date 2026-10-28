from unittest.mock import AsyncMock, patch

import pytest
from langchain_core.language_models.fake_chat_models import FakeListChatModel
from langchain_core.messages import HumanMessage

from app.config import get_settings
from app.graph import nodes
from app.graph.builder import build_graph
from app.graph.nodes import followup_kind
from app.retrieval.base import RetrievedChunk
from app.schemas.chat import ConversationTurn
from tests.conftest import make_token

HISTORY = [
    ConversationTurn(role="user", content="Indent kaise banate hain?"),
    ConversationTurn(role="assistant", content="1. Purchase > New Indent kholo.\n2. Item chuno.\n3. Submit dabao."),
]


@pytest.fixture(autouse=True)
def _clear_settings_cache():
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


class RecordingStore:
    def __init__(self, filtered=None, unfiltered=None):
        self.filtered = filtered or []
        self.unfiltered = unfiltered if unfiltered is not None else self.filtered
        self.queries = []

    def similarity_search(self, query, k, module_filter):
        self.queries.append(query)
        return self.unfiltered if module_filter is None else self.filtered

    def upsert(self, chunks):
        pass

    def delete_by_source_path(self, p):
        pass

    def get_version_hash(self, p):
        return None


def _chunk(module="purchase_sfms_indent"):
    return RetrievedChunk(
        text="Go to Purchase > New Indent", module=module, doc_title="Raising an Indent",
        source_path="purchase-sfms-indent/raising-an-indent.md", chunk_index=0, score=0.1,
    )


def _setup(monkeypatch, responses):
    llm = FakeListChatModel(responses=responses)
    monkeypatch.setattr("app.graph.nodes.get_tenant_api_key", AsyncMock(return_value="k"))
    monkeypatch.setattr("app.graph.nodes.get_llm_for_tenant", lambda api_key: llm)
    return llm


def _profile(dept):
    from app.schemas.auth import DepartmentRef, UserProfile

    return UserProfile(id="u1", role="USER", department=DepartmentRef(id="d1", name=dept), user_departments=[])


async def _run(store, message, history, role="USER", dept="Purchase"):
    graph = build_graph(vector_store=store)
    with patch("app.graph.nodes.fetch_me", new=AsyncMock(return_value=_profile(dept))):
        return await graph.ainvoke(
            {"bearer_token": make_token(role=role), "user_message": message, "conversation_history": history}
        )


# ---------------- keyword classifier ----------------

@pytest.mark.parametrize(
    "message",
    ["ab hindi me batao", "in english please", "short me batao", "thoda chhota karo", "step by step batao",
     "isko explain karo", "samjhao", "bullets me do", "dobara batao", "translate to hindi", "repeat",
     "simple words me batao", "हिंदी में बताओ"],
)
def test_transform_keywords(message):
    assert followup_kind(message, HISTORY) == "transform"


@pytest.mark.parametrize(
    "message",
    ["aur uske baad kya karna hai?", "wahi lead wale ke liye", "what about approval?", "isme kya fill karna hai",
     "and then?", "uske baad?", "how do I approve it", "same for the vendor"],
)
def test_refine_keywords(message):
    assert followup_kind(message, HISTORY) == "refine"


@pytest.mark.parametrize(
    "message",
    ["How do I create a new purchase order for a vendor in the system",
     "mujhe sales order ka status kahan dekhna hai system me",
     "how to add a new employee"],
)
def test_new_keywords(message):
    assert followup_kind(message, HISTORY) == "new"


def test_unsure_and_empty_history():
    assert followup_kind("approval process batao please", HISTORY) is None
    for m in ["ab hindi me batao", "uske baad kya karna hai?", "hello there my friend"]:
        assert followup_kind(m, []) == "new"
    assert followup_kind("ab hindi me batao", None) == "new"


def test_long_translate_request_is_not_transform():
    assert followup_kind("how do I translate a purchase order into a sales invoice in the software", HISTORY) == "new"


# ---------------- graph behaviour ----------------

@pytest.mark.asyncio
async def test_transform_skips_retrieval_and_is_not_refused(monkeypatch):
    _setup(monkeypatch, ["1. Purchase > New Indent kholo (Hindi)."])
    # Sales-like user, filtered search empty, unfiltered would match: a normal search would refuse.
    store = RecordingStore(filtered=[], unfiltered=[_chunk("financial")])
    result = await _run(store, "ab hindi me batao", HISTORY, dept="Sales")
    assert store.queries == []
    assert result["in_scope"] is True
    assert result["answer"] == "1. Purchase > New Indent kholo (Hindi)."
    assert result["sources"] == []


@pytest.mark.asyncio
async def test_refine_retrieves_with_rewritten_question(monkeypatch):
    _setup(monkeypatch, ["Indent banane ke baad approval kaise karte hain?", "Approval steps..."])
    store = RecordingStore(filtered=[_chunk()])
    result = await _run(store, "uske baad kya karna hai?", HISTORY)
    assert store.queries == ["Indent banane ke baad approval kaise karte hain?"]
    assert result["answer"] == "Approval steps..."
    assert result["user_message"] == "uske baad kya karna hai?"
    assert result["sources"][0].module == "purchase_sfms_indent"


@pytest.mark.asyncio
async def test_refine_scope_decision_uses_rewritten_question(monkeypatch):
    _setup(monkeypatch, ["rewritten"])
    store = RecordingStore(filtered=[], unfiltered=[_chunk("financial")])
    result = await _run(store, "aur uske baad?", HISTORY, dept="Sales")
    assert store.queries == ["rewritten", "rewritten"]
    assert result["in_scope"] is False


@pytest.mark.asyncio
async def test_new_question_untouched(monkeypatch):
    _setup(monkeypatch, ["Answer."])  # a single response: any extra LLM call would repeat it, so check queries
    store = RecordingStore(filtered=[_chunk()])
    msg = "How do I create a new purchase order for a vendor in the system"
    result = await _run(store, msg, HISTORY)
    assert store.queries == [msg]
    assert result["followup_kind"] == "new"
    assert result["answer"] == "Answer."


@pytest.mark.asyncio
async def test_new_out_of_scope_still_refused(monkeypatch):
    _setup(monkeypatch, ["unused"])
    store = RecordingStore(filtered=[], unfiltered=[_chunk("financial")])
    msg = "How do I approve a budget for the next financial year in the system"
    result = await _run(store, msg, HISTORY, dept="Sales")
    assert result["in_scope"] is False


@pytest.mark.asyncio
async def test_empty_history_never_rewrites(monkeypatch):
    def boom(api_key):
        raise AssertionError("no LLM call expected before generate")

    _setup(monkeypatch, ["Answer."])
    called = []
    orig = nodes._rewrite_standalone

    async def spy(*a, **k):
        called.append(1)
        return await orig(*a, **k)

    monkeypatch.setattr(nodes, "_rewrite_standalone", spy)
    store = RecordingStore(filtered=[_chunk()])
    await _run(store, "uske baad kya karna hai?", [])
    assert called == []
    assert store.queries == ["uske baad kya karna hai?"]


@pytest.mark.asyncio
async def test_unsure_uses_llm_classifier(monkeypatch):
    _setup(monkeypatch, ["REFINE", "Standalone approval question", "Final."])
    store = RecordingStore(filtered=[_chunk()])
    result = await _run(store, "approval process batao please", HISTORY)
    assert result["followup_kind"] == "refine"
    assert store.queries == ["Standalone approval question"]


@pytest.mark.asyncio
async def test_unsure_classifier_transform(monkeypatch):
    _setup(monkeypatch, ["TRANSFORM", "Shorter version."])
    store = RecordingStore(filtered=[_chunk()])
    result = await _run(store, "approval process batao please", HISTORY)
    assert result["answer"] == "Shorter version."
    assert store.queries == []


class BoomLLM:
    def bind(self, **kw):
        return self

    async def ainvoke(self, *a, **k):
        raise RuntimeError("llm down")


@pytest.mark.asyncio
async def test_classifier_failure_is_new():
    assert await nodes._classify_with_llm(BoomLLM(), "x y z w", [("user", "q")]) == "new"


@pytest.mark.asyncio
async def test_rewrite_failure_uses_original():
    assert await nodes._rewrite_standalone(BoomLLM(), "uske baad?", [("user", "q")]) == "uske baad?"


@pytest.mark.asyncio
async def test_followup_node_failure_paths(monkeypatch):
    monkeypatch.setattr("app.graph.nodes.get_llm_for_tenant", lambda k: BoomLLM())
    state = {"user_message": "uske baad kya karna hai?", "conversation_history": HISTORY, "tenant_api_key": "k"}
    out = await nodes.followup_node(state)
    assert out == {"followup_kind": "refine", "search_query": "uske baad kya karna hai?"}
    state["user_message"] = "approval process batao please"
    out = await nodes.followup_node(state)
    assert out["followup_kind"] == "new"


@pytest.mark.asyncio
async def test_history_is_trimmed_to_10_turns_and_3000_chars():
    many = [ConversationTurn(role="user" if i % 2 == 0 else "assistant", content="x" * 5000) for i in range(20)]
    pairs = nodes._recent_history({"conversation_history": many})
    assert len(pairs) == 10
    assert all(len(t) == 3000 for _, t in pairs)


def test_claude_path_sends_no_temperature():
    from app.graph.llm import get_llm_for_tenant

    llm = get_llm_for_tenant("sk-ant-test")
    payload = llm.bind(max_tokens=10).bound._get_request_payload([HumanMessage(content="hi")], max_tokens=10)
    assert "temperature" not in payload
    assert payload["max_tokens"] == 10
