from functools import lru_cache

from app.graph.builder import build_graph
from app.retrieval.factory import get_vector_store_client


@lru_cache
def get_compiled_graph():
    return build_graph(vector_store=get_vector_store_client())
