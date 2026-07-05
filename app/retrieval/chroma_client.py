from langchain_chroma import Chroma

from app.retrieval.base import ChunkToIndex, RetrievedChunk
from app.retrieval.embeddings import get_embeddings

_COLLECTION_NAME = "autorocket_knowledge_base"


class ChromaVectorStoreClient:
    def __init__(self, persist_dir: str):
        self._store = Chroma(
            collection_name=_COLLECTION_NAME,
            embedding_function=get_embeddings(),
            persist_directory=persist_dir,
        )

    def upsert(self, chunks: list[ChunkToIndex]) -> None:
        if not chunks:
            return
        ids = [f"{c.source_path}::{c.chunk_index}" for c in chunks]
        texts = [c.text for c in chunks]
        metadatas = [
            {
                "module": c.module,
                "doc_title": c.doc_title,
                "source_path": c.source_path,
                "chunk_index": c.chunk_index,
                "doc_version_hash": c.doc_version_hash,
            }
            for c in chunks
        ]
        self._store.add_texts(texts=texts, metadatas=metadatas, ids=ids)

    def similarity_search(
        self, query: str, k: int, module_filter: list[str] | None
    ) -> list[RetrievedChunk]:
        where = None
        if module_filter is not None:
            where = {"module": {"$in": module_filter}}

        results = self._store.similarity_search_with_score(query, k=k, filter=where)
        return [
            RetrievedChunk(
                text=doc.page_content,
                module=doc.metadata["module"],
                doc_title=doc.metadata["doc_title"],
                source_path=doc.metadata["source_path"],
                chunk_index=doc.metadata["chunk_index"],
                score=score,
            )
            for doc, score in results
        ]

    def delete_by_source_path(self, source_path: str) -> None:
        existing = self._store.get(where={"source_path": source_path})
        ids = existing.get("ids") or []
        if ids:
            self._store.delete(ids=ids)

    def get_version_hash(self, source_path: str) -> str | None:
        existing = self._store.get(where={"source_path": source_path}, limit=1)
        metadatas = existing.get("metadatas") or []
        if not metadatas:
            return None
        return metadatas[0].get("doc_version_hash")
