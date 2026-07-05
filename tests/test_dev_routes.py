import jwt
from fastapi.testclient import TestClient


def test_dev_users_and_login_issue_department_token():
    from app.main import app

    client = TestClient(app)

    users_response = client.get("/api/dev/users")
    assert users_response.status_code == 200
    users = users_response.json()["users"]
    assert {user["username"] for user in users} >= {
        "purchase",
        "sales",
        "maintenance",
        "accounts",
        "hr",
    }

    login_response = client.post(
        "/api/dev/login",
        json={"username": "purchase", "password": "purchase123"},
    )
    assert login_response.status_code == 200

    body = login_response.json()
    decoded = jwt.decode(body["token"], "test-secret", algorithms=["HS256"])
    assert decoded["departments"] == ["purchase"]
    assert body["user"]["department"] == "purchase"
