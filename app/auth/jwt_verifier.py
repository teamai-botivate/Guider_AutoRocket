import jwt

from app.config import get_settings
from app.core.exceptions import AuthError
from app.schemas.auth import DecodedToken


def decode_and_verify_jwt(token: str) -> DecodedToken:
    settings = get_settings()
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret,
            algorithms=["HS256"],
            options={"require": ["exp"]},
        )
    except jwt.ExpiredSignatureError as exc:
        raise AuthError("Token has expired") from exc
    except jwt.InvalidTokenError as exc:
        raise AuthError("Invalid token") from exc

    user_id = payload.get("userId")
    tenant_id = payload.get("tenantId")
    role = payload.get("role")
    if not user_id or not tenant_id or not role:
        raise AuthError("Token payload missing required claims")

    return DecodedToken(
        user_id=user_id,
        email=payload.get("email"),
        role=role,
        tenant_id=tenant_id,
        name=payload.get("name"),
        departments=_normalize_departments(payload.get("departments") or payload.get("department")),
    )


def _normalize_departments(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value.strip() else []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    return []
