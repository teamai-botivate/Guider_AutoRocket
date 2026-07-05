"""Offline ingestion CLI: walks knowledge_base/, chunks + embeds + upserts into the vector store.

Usage:
    python -m scripts.ingest [--force] [--dry-run]
"""

import argparse
import hashlib
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import frontmatter
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import get_settings
from app.modules.registry import is_valid_module
from app.retrieval import factory as factory_module
from app.retrieval.base import ChunkToIndex


def _content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def ingest(force: bool = False, dry_run: bool = False) -> int:
    settings = get_settings()
    kb_root = Path(settings.knowledge_base_dir)
    if not kb_root.exists():
        print(f"Knowledge base directory not found: {kb_root}", file=sys.stderr)
        return 1

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    client = None if dry_run else factory_module.get_vector_store_client()

    total_files = 0
    total_chunks = 0
    skipped = 0
    errors = 0

    for md_file in sorted(kb_root.rglob("*.md")):
        total_files += 1
        post = frontmatter.load(md_file)
        module = post.get("module")
        title = post.get("title", md_file.stem)
        body = post.content

        if not module or not is_valid_module(module):
            print(f"  [ERROR] {md_file}: invalid or missing 'module' front-matter ({module!r})")
            errors += 1
            continue

        source_path = md_file.relative_to(kb_root).as_posix()
        content_hash = _content_hash(body)

        if not force and not dry_run:
            existing_hash = client.get_version_hash(source_path)
            if existing_hash == content_hash:
                print(f"  [SKIP] {source_path} (unchanged)")
                skipped += 1
                continue

        chunks = splitter.split_text(body)

        if dry_run:
            print(f"  [DRY-RUN] {source_path}: module={module}, {len(chunks)} chunk(s)")
            total_chunks += len(chunks)
            continue

        client.delete_by_source_path(source_path)
        client.upsert(
            [
                ChunkToIndex(
                    text=chunk,
                    module=module,
                    doc_title=title,
                    source_path=source_path,
                    chunk_index=i,
                    doc_version_hash=content_hash,
                )
                for i, chunk in enumerate(chunks)
            ]
        )
        print(f"  [OK] {source_path}: module={module}, {len(chunks)} chunk(s) ingested")
        total_chunks += len(chunks)

    print(
        f"\nDone. files={total_files} chunks={total_chunks} skipped={skipped} errors={errors}"
    )
    return 1 if errors else 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest knowledge_base markdown into the vector store")
    parser.add_argument("--force", action="store_true", help="Re-embed even unchanged files")
    parser.add_argument("--dry-run", action="store_true", help="Validate front-matter and chunking without writing")
    args = parser.parse_args()

    sys.exit(ingest(force=args.force, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
