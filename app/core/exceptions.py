from fastapi import Request
from fastapi.responses import JSONResponse


class AuthError(Exception):
    """Raised when a bearer token is missing, malformed, or fails verification."""


class UpstreamMeError(Exception):
    """Raised when the Node backend's GET /me call fails or returns unusable data."""


async def auth_error_handler(request: Request, exc: AuthError) -> JSONResponse:
    return JSONResponse(status_code=401, content={"detail": str(exc) or "Unauthorized"})


def register_exception_handlers(app) -> None:
    app.add_exception_handler(AuthError, auth_error_handler)
