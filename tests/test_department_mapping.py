import pytest

from app.modules.department_mapping import _load_mappings, resolve_allowed_modules


@pytest.fixture(autouse=True)
def _clear_mapping_cache():
    _load_mappings.cache_clear()
    yield
    _load_mappings.cache_clear()


def test_exact_match_resolves_module():
    assert resolve_allowed_modules(["Purchase"]) == ["purchase_sfms_indent"]


def test_multiple_departments_union_modules():
    result = resolve_allowed_modules(["Purchase", "HR"])
    assert set(result) == {"purchase_sfms_indent", "hrfms"}


def test_substring_fallback_matches_unlisted_department_name():
    # "Production Dept" isn't an exact YAML key, but should fall back via substring match
    result = resolve_allowed_modules(["Production Dept"])
    assert "production_planning" in result


def test_unmapped_department_resolves_to_no_extra_modules():
    assert resolve_allowed_modules(["Some Totally Unknown Team"]) == []


def test_empty_department_list_resolves_to_no_extra_modules():
    assert resolve_allowed_modules([]) == []
