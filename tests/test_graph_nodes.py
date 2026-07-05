from unittest.mock import AsyncMock, patch

import pytest
from langchain_core.language_models.fake_chat_models import FakeListChatModel

from app.config import get_settings
from app.graph.builder import build_graph
from app.retrieval.base import RetrievedChunk
from tests.conftest import make_token


@pytest.fixture(autouse=True)
def _clear_settings_cache():
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


class FakeVectorStore:
    def __init__(self, filtered_results=None, unfiltered_results=None):
        self.filtered_results = filtered_results or []
        self.unfiltered_results = unfiltered_results if unfiltered_results is not None else self.filtered_results

    def upsert(self, chunks):
        pass

    def similarity_search(self, query, k, module_filter):
        if module_filter is None:
            return self.unfiltered_results
        return self.filtered_results

    def delete_by_source_path(self, source_path):
        pass

    def get_version_hash(self, source_path):
        return None


def _indent_chunk():
    return RetrievedChunk(
        text="To raise an indent, go to Purchase > New Indent...",
        module="purchase_sfms_indent",
        doc_title="Raising an Indent",
        source_path="purchase-sfms-indent/raising-an-indent.md",
        chunk_index=0,
        score=0.1,
    )


def _patch_tenant_key(monkeypatch, key="fake-tenant-key"):
    monkeypatch.setattr(
        "app.graph.nodes.get_tenant_api_key", AsyncMock(return_value=key)
    )


def _patch_llm(monkeypatch, response_text):
    monkeypatch.setattr(
        "app.graph.nodes.get_llm_for_tenant",
        lambda api_key: FakeListChatModel(responses=[response_text]),
    )


@pytest.mark.asyncio
async def test_invalid_jwt_short_circuits_graph(monkeypatch):
    _patch_tenant_key(monkeypatch)
    _patch_llm(monkeypatch, "should not be called")
    graph = build_graph(vector_store=FakeVectorStore())

    result = await graph.ainvoke({"bearer_token": "not-a-real-token", "user_message": "hi", "conversation_history": []})

    assert result["auth_error"]
    assert "answer" not in result


@pytest.mark.asyncio
async def test_in_scope_question_generates_answer(monkeypatch):
    token = make_token(role="USER")
    _patch_tenant_key(monkeypatch)
    _patch_llm(monkeypatch, "Here is how you raise an indent.")
    graph = build_graph(vector_store=FakeVectorStore(filtered_results=[_indent_chunk()]))

    with patch(
        "app.graph.nodes.fetch_me",
        new=AsyncMock(return_value=_fake_profile_with_department("Purchase")),
    ):
        result = await graph.ainvoke(
            {"bearer_token": token, "user_message": "How do I raise an indent?", "conversation_history": []}
        )

    assert result["in_scope"] is True
    assert result["answer"] == "Here is how you raise an indent."
    assert result["sources"][0].module == "purchase_sfms_indent"


@pytest.mark.asyncio
async def test_out_of_scope_question_is_refused_without_calling_llm(monkeypatch):
    token = make_token(role="USER")
    _patch_tenant_key(monkeypatch)
    _patch_llm(monkeypatch, "should not be called")
    # Sales user has no results in their allowed (purchase-scoped) filter, but an unfiltered
    # probe finds a match in a module they aren't permitted to see (e.g. financial).
    vector_store = FakeVectorStore(
        filtered_results=[],
        unfiltered_results=[
            RetrievedChunk(
                text="financial content",
                module="financial",
                doc_title="Budgets",
                source_path="financial/budgets.md",
                chunk_index=0,
                score=0.1,
            )
        ],
    )
    graph = build_graph(vector_store=vector_store)

    with patch(
        "app.graph.nodes.fetch_me",
        new=AsyncMock(return_value=_fake_profile_with_department("Sales")),
    ):
        result = await graph.ainvoke(
            {"bearer_token": token, "user_message": "How do I approve a budget?", "conversation_history": []}
        )

    assert result["in_scope"] is False
    assert "financial" in result["requested_module_hint"]
    assert "Financial" in result["answer"] or "financial" in result["answer"].lower()


@pytest.mark.asyncio
async def test_admin_bypasses_department_filter_entirely(monkeypatch):
    token = make_token(role="ADMIN")
    _patch_tenant_key(monkeypatch)
    _patch_llm(monkeypatch, "Admin sees everything.")
    graph = build_graph(vector_store=FakeVectorStore(filtered_results=[_indent_chunk()]))

    # fetch_me should never be called for admins
    with patch("app.graph.nodes.fetch_me", new=AsyncMock(side_effect=AssertionError("should not be called"))):
        result = await graph.ainvoke(
            {"bearer_token": token, "user_message": "How do I raise an indent?", "conversation_history": []}
        )

    assert result["allowed_modules"] == ["*"]
    assert result["answer"] == "Admin sees everything."


def _fake_profile_with_department(name: str):
    from app.schemas.auth import DepartmentRef, UserProfile

    return UserProfile(id="user-1", role="USER", department=DepartmentRef(id="d1", name=name), user_departments=[])
