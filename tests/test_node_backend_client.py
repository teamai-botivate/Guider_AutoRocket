import httpx
import pytest

from app.auth.node_backend_client import fetch_me


class _StubTransport(httpx.BaseTransport):
    def __init__(self, json_body, status_code: int = 200):
        self._json_body = json_body
        self._status_code = status_code

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        return httpx.Response(self._status_code, json=self._json_body)


@pytest.mark.asyncio
async def test_fetch_me_unwraps_api_response_envelope(monkeypatch):
    # backend_botivate_os wraps every response in {"success", "message", "data"}.
    wrapped_body = {
        "success": True,
        "message": "Profile fetched successfully",
        "data": {
            "id": "user-1",
            "role": "USER",
            "department": {"id": "dept-1", "name": "Purchase", "code": "PUR"},
            "userDepartments": [],
        },
    }

    async def _fake_get(self, url, headers=None):
        transport = _StubTransport(wrapped_body)
        request = httpx.Request("GET", url, headers=headers)
        return transport.handle_request(request)

    monkeypatch.setattr(httpx.AsyncClient, "get", _fake_get)

    profile = await fetch_me("fake-bearer-token")

    assert profile.id == "user-1"
    assert profile.role == "USER"
    assert profile.department.name == "Purchase"


@pytest.mark.asyncio
async def test_fetch_me_tolerates_unwrapped_response(monkeypatch):
    # Defensive fallback: if /me is ever changed to return fields at the top level
    # (no ApiResponse envelope), fetch_me should still parse it correctly.
    unwrapped_body = {
        "id": "user-2",
        "role": "ADMIN",
        "department": None,
        "userDepartments": [],
    }

    async def _fake_get(self, url, headers=None):
        transport = _StubTransport(unwrapped_body)
        request = httpx.Request("GET", url, headers=headers)
        return transport.handle_request(request)

    monkeypatch.setattr(httpx.AsyncClient, "get", _fake_get)

    profile = await fetch_me("fake-bearer-token")

    assert profile.id == "user-2"
    assert profile.role == "ADMIN"
    assert profile.department is None
