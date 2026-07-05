from fastapi import Header

from app.core.exceptions import AuthError


async def get_bearer_token(authorization: str | None = Header(default=None)) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise AuthError("Missing or malformed Authorization header")
    return authorization.removeprefix("Bearer ").strip()
