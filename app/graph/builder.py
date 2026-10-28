from langgraph.graph import END, StateGraph

from app.graph.nodes import (
    auth_node,
    department_node,
    followup_node,
    make_generate_node,
    make_retrieve_node,
    make_scope_decision_node,
    refuse_node,
    route_after_auth,
    route_after_followup,
    route_after_scope,
    route_after_tenant_key,
    tenant_key_node,
    transform_node,
)
from app.graph.state import AssistantState
from app.retrieval.base import VectorStoreClient


def build_graph(vector_store: VectorStoreClient):
    graph = StateGraph(AssistantState)

    graph.add_node("auth", auth_node)
    graph.add_node("tenant_key", tenant_key_node)
    graph.add_node("department", department_node)
    graph.add_node("followup", followup_node)
    graph.add_node("transform", transform_node)
    graph.add_node("retrieve", make_retrieve_node(vector_store))
    graph.add_node("scope_decision", make_scope_decision_node(vector_store))
    graph.add_node("refuse", refuse_node)
    graph.add_node("generate", make_generate_node())

    graph.set_entry_point("auth")
    graph.add_conditional_edges("auth", route_after_auth, {"end": END, "continue": "tenant_key"})
    graph.add_conditional_edges(
        "tenant_key", route_after_tenant_key, {"end": END, "continue": "department"}
    )
    graph.add_edge("department", "followup")
    graph.add_conditional_edges(
        "followup", route_after_followup, {"transform": "transform", "retrieve": "retrieve"}
    )
    graph.add_edge("transform", END)
    graph.add_edge("retrieve", "scope_decision")
    graph.add_conditional_edges(
        "scope_decision", route_after_scope, {"refuse": "refuse", "generate": "generate"}
    )
    graph.add_edge("refuse", END)
    graph.add_edge("generate", END)

    return graph.compile()
