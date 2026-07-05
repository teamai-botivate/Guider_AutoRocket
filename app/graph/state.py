from typing import TypedDict

from app.schemas.chat import ConversationTurn, SourceRef


class AssistantState(TypedDict, total=False):
    # ---- input (set before graph.invoke) ----
    bearer_token: str
    user_message: str
    conversation_history: list[ConversationTurn]

    # ---- populated by auth_node ----
    user_id: str
    tenant_id: str
    role: str
    token_department_names: list[str]
    auth_error: str | None

    # ---- populated by tenant_key_node ----
    tenant_api_key: str | None

    # ---- populated by department_node ----
    department_names: list[str]
    allowed_modules: list[str]
    department_error: str | None

    # ---- populated by retrieve_node / scope_decision_node ----
    requested_module_hint: str | None
    in_scope: bool
    retrieved_docs: list[SourceRef]
    retrieved_chunks_text: list[str]

    # ---- populated by generate_node / refuse_node ----
    answer: str
    sources: list[SourceRef]
