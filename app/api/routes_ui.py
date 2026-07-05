from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(tags=["ui"])

WEB_DIR = Path(__file__).resolve().parents[1] / "web"


@router.get("/", include_in_schema=False)
async def index() -> FileResponse:
    return FileResponse(WEB_DIR / "index.html")


@router.get("/login", include_in_schema=False)
async def login() -> FileResponse:
    return FileResponse(WEB_DIR / "index.html")
