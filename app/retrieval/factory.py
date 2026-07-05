from functools import lru_cache

from app.config import get_settings
from app.retrieval.base import VectorStoreClient
from app.retrieval.chroma_client import ChromaVectorStoreClient


@lru_cache
def get_vector_store_client() -> VectorStoreClient:
    settings = get_settings()
    if settings.vector_store_backend == "chroma":
        return ChromaVectorStoreClient(persist_dir=settings.chroma_persist_dir)
    raise ValueError(f"Unsupported VECTOR_STORE_BACKEND: {settings.vector_store_backend}")
