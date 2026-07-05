import pytest

from app.config import get_settings
from app.core.exceptions import AuthError
from tests.conftest import make_token


@pytest.fixture(autouse=True)
def _clear_settings_cache():
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


def test_valid_token_decodes(valid_token):
    from app.auth.jwt_verifier import decode_and_verify_jwt

    decoded = decode_and_verify_jwt(valid_token)
    assert decoded.user_id == "user-1"
    assert decoded.tenant_id == "tenant-1"
    assert decoded.role == "USER"


def test_expired_token_raises(expired_token):
    from app.auth.jwt_verifier import decode_and_verify_jwt

    with pytest.raises(AuthError):
        decode_and_verify_jwt(expired_token)


def test_wrong_secret_raises():
    from app.auth.jwt_verifier import decode_and_verify_jwt

    token = make_token(secret="a-different-secret")
    with pytest.raises(AuthError):
        decode_and_verify_jwt(token)


def test_missing_claims_raises():
    import jwt as pyjwt

    from app.auth.jwt_verifier import decode_and_verify_jwt

    token = pyjwt.encode({"exp": 9_999_999_999}, "test-secret", algorithm="HS256")
    with pytest.raises(AuthError):
        decode_and_verify_jwt(token)
