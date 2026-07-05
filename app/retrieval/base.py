from dataclasses import dataclass
from typing import Protocol


@dataclass
class ChunkToIndex:
    text: str
    module: str
    doc_title: str
    source_path: str
    chunk_index: int
    doc_version_hash: str


@dataclass
class RetrievedChunk:
    text: str
    module: str
    doc_title: str
    source_path: str
    chunk_index: int
    score: float


class VectorStoreClient(Protocol):
    def upsert(self, chunks: list[ChunkToIndex]) -> None: ...

    def similarity_search(
        self, query: str, k: int, module_filter: list[str] | None
    ) -> list[RetrievedChunk]: ...

    def delete_by_source_path(self, source_path: str) -> None: ...

    def get_version_hash(self, source_path: str) -> str | None:
        """Return the stored doc_version_hash for a source_path, if any chunk exists."""
        ...
