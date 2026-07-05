import pytest

from app.config import get_settings
from app.retrieval import factory as factory_module
from scripts.ingest import ingest


@pytest.fixture(autouse=True)
def _clear_caches():
    get_settings.cache_clear()
    factory_module.get_vector_store_client.cache_clear()
    yield
    get_settings.cache_clear()
    factory_module.get_vector_store_client.cache_clear()


class FakeVectorStore:
    def __init__(self):
        self.upserted = []
        self.deleted = []
        self._hashes = {}

    def upsert(self, chunks):
        self.upserted.extend(chunks)
        for c in chunks:
            self._hashes[c.source_path] = c.doc_version_hash

    def similarity_search(self, query, k, module_filter):
        return []

    def delete_by_source_path(self, source_path):
        self.deleted.append(source_path)
        self._hashes.pop(source_path, None)

    def get_version_hash(self, source_path):
        return self._hashes.get(source_path)


@pytest.fixture
def kb_dir(tmp_path, monkeypatch):
    kb = tmp_path / "kb"
    kb.mkdir()
    (kb / "common").mkdir()
    (kb / "common" / "doc1.md").write_text(
        "---\ntitle: Doc One\nmodule: common\n---\n\nSome content here about logging in.",
        encoding="utf-8",
    )
    monkeypatch.setenv("KNOWLEDGE_BASE_DIR", str(kb))
    return kb


def test_ingest_dry_run_does_not_write(kb_dir):
    exit_code = ingest(dry_run=True)
    assert exit_code == 0


def test_ingest_rejects_invalid_module(tmp_path, monkeypatch):
    kb = tmp_path / "kb"
    kb.mkdir()
    (kb / "bad.md").write_text("---\ntitle: Bad\nmodule: not_a_real_module\n---\n\nContent.", encoding="utf-8")
    monkeypatch.setenv("KNOWLEDGE_BASE_DIR", str(kb))

    exit_code = ingest(dry_run=True)
    assert exit_code == 1


def test_ingest_skips_unchanged_file(kb_dir, monkeypatch):
    fake_store = FakeVectorStore()
    monkeypatch.setattr(factory_module, "get_vector_store_client", lambda: fake_store)

    first = ingest()
    assert first == 0
    assert len(fake_store.upserted) > 0

    fake_store.upserted.clear()
    second = ingest()
    assert second == 0
    assert len(fake_store.upserted) == 0  # skipped, unchanged
