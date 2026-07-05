#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:8000}"
TOKEN="${1:?Usage: smoke_test.sh <bearer_token> [message]}"
MESSAGE="${2:-How do I raise a purchase indent?}"

echo "== Health check =="
curl -sf "$BASE_URL/healthz" | jq .

echo
echo "== Chat: \"$MESSAGE\" =="
curl -sf -X POST "$BASE_URL/api/v1/chat" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg msg "$MESSAGE" '{message: $msg, conversation_history: []}')" | jq .
