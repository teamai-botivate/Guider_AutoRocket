import re
from functools import lru_cache

import yaml

from app.config import get_settings
from app.modules import registry


def _normalize(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.lower())


@lru_cache
def _load_mappings() -> dict[str, list[str]]:
    settings = get_settings()
    with open(settings.department_module_map_path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return {_normalize(k): v for k, v in (data.get("mappings") or {}).items()}


def resolve_allowed_modules(department_names: list[str]) -> list[str]:
    """Resolve a user's department name/code list to allowed module keys.

    Fails closed: departments that don't match anything contribute no extra
    modules (the caller is still expected to add `common` separately).
    """
    mappings = _load_mappings()
    resolved: set[str] = set()

    for raw_name in department_names:
        normalized = _normalize(raw_name)
        if not normalized:
            continue

        if normalized in mappings:
            resolved.update(mappings[normalized])
            continue

        # substring fallback against module keys/aliases in the registry
        for module_key in registry.non_common_module_keys():
            candidates = [module_key] + registry.aliases_for(module_key)
            if any(
                normalized in _normalize(candidate) or _normalize(candidate) in normalized
                for candidate in candidates
            ):
                resolved.add(module_key)

    return sorted(resolved)
