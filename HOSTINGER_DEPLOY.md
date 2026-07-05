# Guide Bot (`autorocket_ai_assistant`) — Hostinger Deployment Guide

## Domain: guide.autorocket.in

This service is deployed **independently** — its own Docker container, its own Nginx site, its own subdomain — exactly the same pattern as AI Boardroom (`agent-botivateOS` → `ai-boardroom.autorocket.in`). It shares the same VPS and the same Postgres database as `backend_botivate_os` and AI Boardroom, but runs as its own container.

Frontend integration (`botivate_os_frontend`) is a separate step, covered in `FRONTEND_INTEGRATION_FOR_AUTOROCKET_DEV.md` in this repo — hand that doc to whoever owns the frontend.

---

## End-to-end request flow (login → OpenAI → answer)

```
1. User logs into botivate_os_frontend
   → backend_botivate_os sets an httpOnly `accessToken` cookie
     JWT payload: { userId, email, role, tenantId, name }

2. User opens the ChatWidget on any dashboard page and asks a question
   → Browser calls a Next.js SERVER route (POST /api/ai-assistant/chat) —
     not this service directly. That route runs on the Next.js server,
     so it CAN read the httpOnly cookie (browsers can't).

3. The Next.js route forwards to:
     POST https://guide.autorocket.in/api/v1/chat/stream
     Authorization: Bearer <same JWT>

4. Guide Bot — auth_node
   → verifies the JWT (same JWT_SECRET as backend_botivate_os)
   → extracts userId, tenantId, role

5. Guide Bot — tenant_key_node (added in this refactor)
   → looks up Tenant.openaiApiKey directly in the shared Postgres DB via DATABASE_URL
   → if NULL → stream ends immediately with an "OpenAI key not configured" error
     (same per-tenant-key model as AI Boardroom — no shared/global billing)

6. Guide Bot — department_node
   → calls backend_botivate_os's own GET /me (server-to-server, same JWT)
   → resolves the user's department(s) → which knowledge_base/ folders they may see
   → ADMIN/SUPERADMIN roles bypass this and see all modules

7. Guide Bot — retrieve_node
   → searches the Chroma vector store for relevant knowledge_base chunks,
     filtered to the modules resolved in step 6

8. Guide Bot — scope_decision_node
   → if the question falls outside the user's allowed modules → refuse_node
     (a scoped "that's outside your access" reply, no LLM call made)
   → otherwise → generate_node

9. Guide Bot — generate_node
   → builds a ChatOpenAI instance using the tenant's OWN key from step 5
     (per-request, not shared across tenants or cached)
   → sends the retrieved context + conversation history + question to OpenAI
   → OpenAI generates the answer text

10. Guide Bot streams the response back over SSE:
      data: {"type": "delta", "content": "..."}     (repeated, chunked answer text)
      data: {"type": "sources", "sources": [...]}   (which knowledge_base docs were used)
      data: {"type": "done"}

11. The Next.js route relays that SSE stream back to the browser unmodified

12. ChatWidget.tsx renders it progressively: markdown formatting (bold, lists),
    backtick-quoted internal routes turned into clickable links, and sources
    shown alongside the answer
```

Everything from step 4 onward is fully tenant-isolated: the OpenAI key, the department scoping, and the knowledge base filtering are all resolved per-request from the verified JWT — there is no shared state between tenants.

---

## What changed in this repo before deploying (already done)

These code changes have already been made in `autorocket_ai_assistant` so it can use **per-tenant OpenAI keys** (same model as AI Boardroom) instead of one global key, and so it can stream answers over SSE:

| File | Change |
|---|---|
| `app/db.py` (new) | `get_tenant_api_key(tenant_id)` — reads `Tenant.openaiApiKey` from the shared Postgres DB |
| `app/config.py` | Added `database_url` setting |
| `app/graph/llm.py` | `get_llm()` (global, cached) → `get_llm_for_tenant(api_key)` (per-request, not cached, `streaming=True`) |
| `app/graph/state.py` | Added `tenant_api_key` field |
| `app/graph/nodes.py` | Added `tenant_key_node` (fetches the tenant's key right after JWT auth) + `route_after_tenant_key`; `make_generate_node()` no longer takes an `llm` argument — it builds the LLM per-request from `state["tenant_api_key"]` |
| `app/graph/builder.py` | `build_graph(vector_store)` — no longer takes `llm`; wires the new `tenant_key` node between `auth` and `department` |
| `app/graph/compiled.py` | No longer builds an LLM at import time |
| `app/api/routes_chat.py` | Added `POST /api/v1/chat/stream` — SSE endpoint alongside the original `POST /api/v1/chat` |
| `requirements.txt` | Added `asyncpg` |
| `.env.example` | Added `DATABASE_URL`; noted `OPENAI_API_KEY` is no longer read for chat calls |
| `docker-compose.yml` | Container renamed `autorocket-ai-assistant`, bound to `127.0.0.1:8001`, joined to the shared `botivate_network` (external) |
| `Dockerfile` | Base image pinned to `python:3.10-slim` (was `3.12-slim` — this repo now matches AI Boardroom's Python version); added `build-essential` (for `asyncpg`'s C extension, in case no prebuilt wheel matches the VPS architecture) |
| `.python-version` (new) | `3.10.13` — pins local/dev tooling to the same version as the Docker image |
| `.dockerignore` (new) | Standard excludes (`.venv`, `.git`, `tests`, etc.) |
| `.gitignore` | Clarified that `data/chroma/` (the vector store) is never committed — it's fully regenerated by `scripts/ingest.py` on every deploy |
| `app/auth/node_backend_client.py` | Fixed a response-shape bug: `fetch_me()` now unwraps `backend_botivate_os`'s `{success, message, data}` envelope before reading profile fields — see `FRONTEND_INTEGRATION_FOR_AUTOROCKET_DEV.md` §2.5 for details. Without this fix, every non-admin user's request would fail with a `KeyError` inside `department_node`. |
| `tests/test_graph_nodes.py`, `tests/test_chat_route.py` | Updated to mock `get_tenant_api_key` / `get_llm_for_tenant` instead of injecting an `llm` object directly |
| `tests/test_node_backend_client.py` (new) | Covers the envelope-unwrap fix above — verifies `fetch_me()` against both a wrapped and an unwrapped `/me` response |

All 21 relevant tests pass (`pytest -q`, excluding 3 pre-existing `test_ingest.py` failures caused by a local Windows temp-directory permission issue, unrelated to any change here — verify independently on the VPS if in doubt).

**Important consequence:** `OPENAI_API_KEY` is **no longer used** for actual chat/answer generation. Each tenant's own key is fetched live from `Tenant.openaiApiKey` (the same column AI Boardroom reads) via `DATABASE_URL`. If a tenant hasn't configured a key yet (via Company Profile settings in `botivate_os_frontend`), the graph short-circuits with `auth_error: "OpenAI key not configured for this tenant"`, which the API layer returns as a 401 with that message.

`OPENAI_EMBEDDING_MODEL` is still used — for the knowledge-base ingestion step (`scripts/ingest.py`), which currently still uses the global embedding pipeline. This does not require per-tenant billing since ingestion is an internal, one-time-per-content-update operation, not a per-user chat call.

---

## Prerequisites

- SSH access to the same Hostinger VPS already running `backend_botivate_os` and `agent-botivateOS` (AI Boardroom)
- The same shared Postgres `DATABASE_URL` already used by AI Boardroom (same `botivate_network` Docker network, same `botivate_db` container — confirm this is still accurate on your VPS before copying values)
- The same `JWT_SECRET` used by `backend_botivate_os`
- Docker + Docker Compose + Nginx + Certbot already installed on the VPS (already true if AI Boardroom is deployed there)
- DNS access to add a new `guide` subdomain under `autorocket.in`

---

## STEP 1 — Get the code onto the VPS

```bash
cd ~/projects
git clone <autorocket_ai_assistant-repo-url> autorocket_ai_assistant
cd autorocket_ai_assistant
```

If it's already cloned and you're updating it:

```bash
cd ~/projects/autorocket_ai_assistant
git pull
```

---

## STEP 2 — Confirm the shared Docker network name

This service's `docker-compose.yml` expects an **external** network named `botivate_network` (the same one `backend_botivate_os`'s Postgres container and AI Boardroom already use). Confirm it exists and note the Postgres container's actual name:

```bash
docker network ls
docker ps | grep -i postgres
```

If the network name on your VPS is different from `botivate_network`, edit `docker-compose.yml`'s `networks:` section (bottom of the file) to match the actual name before proceeding.

---

## STEP 3 — Create `.env`

```bash
cd ~/projects/autorocket_ai_assistant
cp .env.example .env
nano .env
```

Fill in:

```env
OPENAI_CHAT_MODEL=gpt-4o-mini
OPENAI_EMBEDDING_MODEL=text-embedding-3-small

# Must exactly match backend_botivate_os's JWT_SECRET
JWT_SECRET=<same value as backend_botivate_os and agent-botivateOS>

# Node backend's own container name + port on the shared network
# (confirm the actual service/container name with `docker ps` if unsure)
NODE_BACKEND_URL=http://backend:5000/api/auth

# Same DB as backend_botivate_os / AI Boardroom — use the Postgres
# container's name as the host (not "db" unless that's the real container name)
DATABASE_URL=postgresql://botivate:REAL_PASSWORD@botivate_db:5432/botivate_db

VECTOR_STORE_BACKEND=chroma
CHROMA_PERSIST_DIR=./data/chroma
KNOWLEDGE_BASE_DIR=./knowledge_base
DEPARTMENT_MODULE_MAP_PATH=./config/department_module_map.yaml

APP_ENV=production
LOG_LEVEL=INFO
```

Notes:

- `NODE_BACKEND_URL` must point up to (and including) `/api/auth` — this service internally appends `/me`, so the final call becomes `.../api/auth/me`. Confirm this matches `backend_botivate_os`'s actual profile route (`GET /me` mounted under `/auth` per its `auth.routes.ts`).
- If the Postgres container's real name on your VPS is different from `botivate_db` (check with `docker ps`), use that name instead — Docker's internal DNS resolves containers by their container name, not by an arbitrary label.
- `OPENAI_API_KEY` is intentionally **not** in this list — it's no longer read anywhere in the chat path after the code changes above.

```bash
chmod 600 .env
```

---

## STEP 4 — Build, ingest, and start — as one sequence

The Chroma vector store must be populated from `knowledge_base/*.md` **before** the container is worth serving traffic — an un-ingested store means every question comes back with "no matching documentation found". Treat build → ingest → up as a single deploy step, not three separate ones you might forget to run in order:

```bash
cd ~/projects/autorocket_ai_assistant
docker compose build \
  && docker compose run --rm ai-assistant python scripts/ingest.py \
  && docker compose up -d
```

Or use the helper script committed in this repo (`deploy.sh`), which runs exactly that sequence and stops on the first failure:

```bash
cd ~/projects/autorocket_ai_assistant
chmod +x deploy.sh   # first time only
./deploy.sh
```

Whenever `knowledge_base/*.md` content changes on its own (no code change), re-run just the ingest + restart:

```bash
docker compose run --rm ai-assistant python scripts/ingest.py
docker compose restart ai-assistant
```

---

## STEP 5 — Verify the container

```bash
docker compose ps
docker compose logs -f
```

In another terminal:

```bash
curl http://127.0.0.1:8001/healthz
```

Expected:

```json
{"status": "ok", "vector_store_backend": "chroma"}
```

If the container fails to start, check `docker compose logs --tail=100` for:
- `DATABASE_URL is not set` — `.env` missing or not loaded
- `Temporary failure in name resolution` on the DB host — the Postgres container name in `DATABASE_URL` doesn't match its actual container name, or this service isn't on the same Docker network as Postgres (re-check STEP 2)
- Missing `NODE_BACKEND_URL` connectivity — confirm `backend` (or whatever the real service name is) is reachable on `botivate_network`

---

## STEP 6 — Nginx reverse proxy

```bash
nano /etc/nginx/sites-available/guide
```

```nginx
server {
    listen 80;
    server_name guide.autorocket.in;

    location / {
        proxy_pass http://127.0.0.1:8001;
        proxy_http_version 1.1;

        # Required for SSE streaming (/api/v1/chat/stream)
        proxy_set_header Connection "";
        proxy_buffering off;
        proxy_cache off;
        chunked_transfer_encoding on;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_read_timeout 300s;
        proxy_connect_timeout 75s;
    }
}
```

```bash
ln -s /etc/nginx/sites-available/guide /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

---

## STEP 7 — DNS (Hostinger panel)

```
Domains → autorocket.in → DNS Zone Editor → Add Record
Type:  A
Name:  guide
Value: <VPS IP>
TTL:   300
```

Check propagation:

```bash
ping guide.autorocket.in
```

---

## STEP 8 — HTTPS

```bash
certbot --nginx -d guide.autorocket.in
```

Choose redirect HTTP → HTTPS when prompted.

```bash
certbot renew --dry-run
```

---

## STEP 9 — Final verification

```bash
curl https://guide.autorocket.in/healthz
```

Full end-to-end smoke test (once `botivate_os_frontend` has the integration from `FRONTEND_INTEGRATION_FOR_AUTOROCKET_DEV.md` in place):

1. Log into `botivate_os_frontend` as a real tenant user who has an OpenAI key configured (Company Profile settings).
2. Open the chat widget, ask a question relevant to the user's department (e.g. Purchase user asks "How do I raise an indent?").
3. Confirm the answer streams in progressively, with Markdown formatting and any source links rendered correctly.
4. Ask a question outside the user's department — confirm a scoped refusal, not a generic/leaked answer.
5. Test with a tenant that has **no** OpenAI key configured — confirm a clear error surfaces instead of a hang or crash.

---

## Common Docker commands

```bash
cd ~/projects/autorocket_ai_assistant

docker compose ps
docker compose logs -f
docker compose restart

# After a code update:
git pull
docker compose up -d --build

# After a knowledge_base/*.md content update:
docker compose run --rm ai-assistant python scripts/ingest.py
docker compose restart ai-assistant

# Update .env:
nano .env
docker compose restart

docker exec -it autorocket-ai-assistant sh
docker compose down
```

---

## Security checklist

- [ ] `.env` is not committed to git, permissions set to `600`
- [ ] Container bound to `127.0.0.1:8001` only — not directly exposed publicly (Nginx handles public traffic)
- [ ] `JWT_SECRET` matches `backend_botivate_os` exactly
- [ ] `DATABASE_URL` points at the same shared Postgres instance, using its real container name as host
- [ ] No tenant OpenAI key is ever logged, returned in API responses, or exposed to the frontend — it stays server-side in this container's memory during the LLM call only
- [ ] HTTPS certificate active and auto-renewing

---

## Final URLs

| Purpose | URL |
|---|---|
| Health check | `https://guide.autorocket.in/healthz` |
| Non-streaming chat (legacy) | `POST https://guide.autorocket.in/api/v1/chat` |
| Streaming chat (SSE) | `POST https://guide.autorocket.in/api/v1/chat/stream` |
| API docs | `https://guide.autorocket.in/docs` |
| Local test console (dev only — do not rely on in production) | `https://guide.autorocket.in/` when `APP_ENV` is `development`/`dev`/`local`/`test` |
