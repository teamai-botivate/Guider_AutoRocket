from fastapi import APIRouter

from app.config import get_settings
from app.schemas.chat import HealthResponse

router = APIRouter()


@router.get("/healthz", response_model=HealthResponse)
async def healthz() -> HealthResponse:
    settings = get_settings()
    return HealthResponse(status="ok", vector_store_backend=settings.vector_store_backend)
