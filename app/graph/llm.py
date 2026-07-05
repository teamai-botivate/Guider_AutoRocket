from langchain_openai import ChatOpenAI

from app.config import get_settings


def get_llm_for_tenant(api_key: str) -> ChatOpenAI:
    """
    Build a ChatOpenAI instance scoped to one tenant's own OpenAI key.
    Not cached — each request may belong to a different tenant, and the
    key can change at any time via the tenant's Company Profile settings.
    """
    settings = get_settings()
    return ChatOpenAI(
        model=settings.openai_chat_model,
        api_key=api_key,
        temperature=0.2,
        streaming=True,
    )
