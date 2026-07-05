from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient
from langchain_core.language_models.fake_chat_models import FakeListChatModel

from app.config import get_settings
from app.graph import compiled as compiled_module
from app.retrieval.base import RetrievedChunk
from tests.conftest import make_token
from tests.test_graph_nodes import FakeVectorStore, _fake_profile_with_department, _indent_chunk


@pytest.fixture(autouse=True)
def _clear_caches():
    get_settings.cache_clear()
    compiled_module.get_compiled_graph.cache_clear()
    yield
    get_settings.cache_clear()
    compiled_module.get_compiled_graph.cache_clear()


@pytest.fixture
def client():
    from app.main import app

    return TestClient(app)


def test_chat_requires_authorization_header(client):
    response = client.post("/api/v1/chat", json={"message": "hi"})
    assert response.status_code == 401


def test_chat_rejects_invalid_token(client):
    response = client.post(
        "/api/v1/chat",
        json={"message": "hi"},
        headers={"Authorization": "Bearer not-a-real-token"},
    )
    assert response.status_code == 401


def test_chat_returns_answer_for_in_scope_question(client, monkeypatch):
    token = make_token(role="USER")
    monkeypatch.setattr(
        "app.graph.nodes.get_tenant_api_key", AsyncMock(return_value="fake-tenant-key")
    )
    monkeypatch.setattr(
        "app.graph.nodes.get_llm_for_tenant",
        lambda api_key: FakeListChatModel(responses=["Here is how you raise an indent."]),
    )
    fake_graph = _build_fake_graph_returning(
        vector_store=FakeVectorStore(filtered_results=[_indent_chunk()]),
    )

    with (
        patch.object(compiled_module, "get_compiled_graph", return_value=fake_graph),
        patch(
            "app.graph.nodes.fetch_me",
            new=AsyncMock(return_value=_fake_profile_with_department("Purchase")),
        ),
    ):
        response = client.post(
            "/api/v1/chat",
            json={"message": "How do I raise an indent?", "conversation_history": []},
            headers={"Authorization": f"Bearer {token}"},
        )

    assert response.status_code == 200
    body = response.json()
    assert body["answer"] == "Here is how you raise an indent."
    assert body["in_scope"] is True
    assert body["sources"][0]["module"] == "purchase_sfms_indent"


def _build_fake_graph_returning(vector_store):
    from app.graph.builder import build_graph

    return build_graph(vector_store=vector_store)
