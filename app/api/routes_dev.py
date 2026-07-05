from datetime import datetime, timedelta, timezone

import jwt
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.config import get_settings

router = APIRouter(prefix="/api/dev", tags=["dev"])


class DevLoginRequest(BaseModel):
    username: str
    password: str


class DevLoginResponse(BaseModel):
    token: str
    user: dict


DEV_USERS = {
    "purchase": {
        "password": "purchase123",
        "name": "Purchase Demo User",
        "department": "purchase",
        "sample": "How do I create a purchase indent?",
    },
    "sales": {
        "password": "sales123",
        "name": "Sales Demo User",
        "department": "sales",
        "sample": "How do I create a lead?",
    },
    "maintenance": {
        "password": "maintenance123",
        "name": "Maintenance Demo User",
        "department": "maintenance",
        "sample": "How do I create a maintenance plan?",
    },
    "accounts": {
        "password": "accounts123",
        "name": "Accounts Demo User",
        "department": "accounts",
        "sample": "How do I approve a petty cash expense?",
    },
    "hr": {
        "password": "hr123",
        "name": "HR Demo User",
        "department": "hr",
        "sample": "How do I manage employee attendance?",
    },
}


@router.get("/users")
async def dev_users() -> dict:
    _ensure_dev_enabled()
    return {
        "users": [
            {
                "username": username,
                "name": user["name"],
                "department": user["department"],
                "sample": user["sample"],
            }
            for username, user in DEV_USERS.items()
        ]
    }


@router.post("/login", response_model=DevLoginResponse)
async def dev_login(request: DevLoginRequest) -> DevLoginResponse:
    _ensure_dev_enabled()
    user = DEV_USERS.get(request.username.lower().strip())
    if not user or request.password != user["password"]:
        raise HTTPException(status_code=401, detail="Invalid demo username or password")

    settings = get_settings()
    now = datetime.now(timezone.utc)
    payload = {
        "userId": f"demo-{request.username.lower().strip()}",
        "tenantId": "demo-tenant",
        "role": "USER",
        "email": f"{request.username.lower().strip()}@demo.autorocket.local",
        "name": user["name"],
        "departments": [user["department"]],
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(hours=8)).timestamp()),
    }
    token = jwt.encode(payload, settings.jwt_secret, algorithm="HS256")
    return DevLoginResponse(
        token=token,
        user={
            "username": request.username.lower().strip(),
            "name": user["name"],
            "department": user["department"],
            "sample": user["sample"],
        },
    )


def _ensure_dev_enabled() -> None:
    if get_settings().app_env.lower() not in {"development", "dev", "local", "test"}:
        raise HTTPException(status_code=404, detail="Not found")
