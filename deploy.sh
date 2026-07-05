#!/usr/bin/env bash
# Guide Bot (autorocket_ai_assistant) — build, ingest, and (re)start as one step.
#
# The Chroma vector store must be populated from knowledge_base/*.md before the
# container is worth serving traffic, so this script always runs ingest between
# build and up rather than leaving it as a separate manual step someone can forget.
#
# Usage: ./deploy.sh
set -euo pipefail

cd "$(dirname "$0")"

echo "==> Building image"
docker compose build

echo "==> Ingesting knowledge_base/ into the Chroma vector store"
docker compose run --rm ai-assistant python scripts/ingest.py

echo "==> Starting container"
docker compose up -d

echo "==> Done. Waiting a moment before health check..."
sleep 2
curl -sf http://127.0.0.1:8001/healthz && echo "" && echo "==> Healthy" || {
  echo "==> Health check failed — check: docker compose logs --tail=100"
  exit 1
}
