from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes_dev import router as dev_router
from app.api.routes_chat import router as chat_router
from app.api.routes_health import router as health_router
from app.api.routes_ui import WEB_DIR, router as ui_router
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_logging

configure_logging()

app = FastAPI(title="AutoRocket AI Assistant", version="0.1.0")

register_exception_handlers(app)

app.mount("/static", StaticFiles(directory=WEB_DIR / "static"), name="static")

app.include_router(health_router)
app.include_router(dev_router)
app.include_router(chat_router, prefix="/api/v1")
app.include_router(ui_router)
