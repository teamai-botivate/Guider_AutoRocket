# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**Guide Bot** (`autorocket_ai_assistant`) is a "how do I use this software" help assistant for the Autorocket OS platform — an independent FastAPI + LangChain + LangGraph service, RAG-based over a curated Markdown knowledge base.

It is **not** AI Boardroom (`agent-botivateOS`, a separate repo). The two are easy to confuse — keep them distinct:

| | Guide Bot (this repo) | AI Boardroom (`agent-botivateOS`) |
|---|---|---|
| Purpose | "How do I use this software" help | Business-data chat (CFO/HR/Sales/etc. agents) |
| Data source | Curated Markdown in `knowledge_base/`, embedded into Chroma | Live PostgreSQL business tables (raw SQL) |
| Deployed at | `https://guide.autorocket.in` | `https://ai-boardroom.autorocket.in` |
| Frontend home | `botivate_os_frontend`'s `ChatWidget.tsx` (floating widget, all dashboard pages) | `botivate_os_frontend`'s `ai-boardroom/page.tsx` (dedicated page) |
| Scoping | Per-user department (via `backend_botivate_os`'s `GET /me`) | Per-tenant (via JWT `tenantId`, every SQL query filtered) |

Phase 1 scope: answers are drawn only from `knowledge_base/` — it does not query live tenant business data (that's AI Boardroom's job).

## How it connects to the rest of Autorocket

- Verifies the **same JWT** (`JWT_SECRET`) issued by `backend_botivate_os` — no new backend endpoint or backend code change is required for JWT delivery.
- Resolves the caller's department by calling `backend_botivate_os`'s existing `GET /me` endpoint, server-to-server, using the caller's own bearer token (see `app/auth/node_backend_client.py`).
- Resolves the caller's own OpenAI key by reading `Tenant.openaiApiKey` directly from the **same shared Postgres DB** that `backend_botivate_os` and AI Boardroom use — same per-tenant-key model as AI Boardroom, no shared/global billing for actual chat calls.
- `botivate_os_frontend`'s `ChatWidget.tsx` calls a Next.js server route (`POST /api/ai-assistant/chat`), which reads the `accessToken` httpOnly cookie server-side and forwards it as `Authorization: Bearer <JWT>` to this service's `POST /api/v1/chat/stream`. See `FRONTEND_INTEGRATION_FOR_AUTOROCKET_DEV.md` for the exact frontend code/files needed (not yet implemented in `botivate_os_frontend` as of this writing).

## Production deployment status

- ✅ **Deployed and live** at `https://guide.autorocket.in` on the same Hostinger VPS as `backend_botivate_os` and AI Boardroom, sharing the same `botivate_network` Docker network and the same Postgres (`botivate_db` container).
- Container name: `autorocket-ai-assistant`, bound to `127.0.0.1:8001`, reverse-proxied by Nginx with HTTPS via Certbot.
- `.env` on the VPS has `DATABASE_URL` pointed at `botivate_db`, `JWT_SECRET` matching `backend_botivate_os`, and `OPENAI_API_KEY` set (used **only** for `scripts/ingest.py`'s embeddings — never for tenant chat calls, see below).
- Health check confirmed: `GET /healthz` → `{"status": "ok", "vector_store_backend": "chroma"}`.
- **Still pending:** the `botivate_os_frontend` side of the integration (the proxy route + `ChatWidget.tsx` rewrite in `FRONTEND_INTEGRATION_FOR_AUTOROCKET_DEV.md`) has not been implemented yet — until then, this service is reachable but nothing in the live frontend calls it.
- See `HOSTINGER_DEPLOY.md` in this repo for the full deploy runbook (already executed once; use it again for redeploys/updates).

## Per-tenant OpenAI key — IMPORTANT distinction

Two different OpenAI keys exist in this system and they are **not interchangeable**:

1. **`OPENAI_API_KEY` in `.env`** — used **only** by `scripts/ingest.py` to generate embeddings when populating the Chroma vector store from `knowledge_base/*.md`. This is an internal, infrequent (content-update-triggered) operation billed to Autorocket's own OpenAI account. It is never read anywhere in the live chat request path.
2. **`Tenant.openaiApiKey`** (fetched via `app/db.py:get_tenant_api_key()`) — used for every actual chat/answer-generation call (`app/graph/llm.py:get_llm_for_tenant()`), fetched fresh per-request from the tenant's own row in the shared Postgres DB. This is billed to the tenant's own OpenAI account, exactly like AI Boardroom.

If a tenant has no `openaiApiKey` configured, `tenant_key_node` (in `app/graph/nodes.py`) short-circuits the LangGraph flow with `auth_error: "OpenAI key not configured for this tenant"` before any LLM call is attempted.

## Commands

```bash
python3.10 -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env        # fill JWT_SECRET, DATABASE_URL, NODE_BACKEND_URL, OPENAI_API_KEY (for ingest)
python scripts/ingest.py    # populate the Chroma vector store — required before first run
uvicorn app.main:app --reload --port 8000
```

App at `http://127.0.0.1:8000`. Runtime is **Python 3.10** (`.python-version` = `3.10.13`, `Dockerfile` base image `python:3.10-slim`) — matches AI Boardroom's Python version by convention, even though this is an independent deploy.

**Local dev test console:** open `http://localhost:8000/` (only served when `APP_ENV` is `development`/`dev`/`local`/`test`). Five demo department logins are available via `/api/dev/*`:

```
purchase / purchase123
sales / sales123
maintenance / maintenance123
accounts / accounts123
hr / hr123
```

These are local-testing-only users whose JWTs include a `departments` claim, letting you test department-scoped retrieval without a live `backend_botivate_os` `/me` call.

## Deployment

```bash
chmod +x deploy.sh
./deploy.sh
```

Runs build → `scripts/ingest.py` → `docker compose up -d` → health check, as one sequence — **never skip the ingest step**, an un-ingested Chroma store means every question returns "no matching documentation found." See `HOSTINGER_DEPLOY.md` for the full VPS runbook (network setup, `.env` values, Nginx, DNS, Certbot).

Re-run ingestion alone whenever `knowledge_base/*.md` content changes without any code change:

```bash
docker compose run --rm ai-assistant python scripts/ingest.py
docker compose restart ai-assistant
```

## Environment variables

| Var | Purpose |
|---|---|
| `OPENAI_CHAT_MODEL` | Chat model name (e.g. `gpt-4o-mini`) — used with each tenant's own key |
| `OPENAI_EMBEDDING_MODEL` | Embedding model for ingestion |
| `OPENAI_API_KEY` | **Ingestion only** — see "Per-tenant OpenAI key" above. Not used for tenant chat. |
| `JWT_SECRET` | Must match `backend_botivate_os` exactly |
| `NODE_BACKEND_URL` | Base URL up to and including `/api/auth` — this service appends `/me` internally, so the final call is `.../api/auth/me` |
| `DATABASE_URL` | Same shared Postgres as `backend_botivate_os` / AI Boardroom — required for `Tenant.openaiApiKey` lookups |
| `VECTOR_STORE_BACKEND` | Currently only `chroma` is implemented |
| `CHROMA_PERSIST_DIR` | Default `./data/chroma` — **never commit this**, it's regenerated by `ingest.py` |
| `KNOWLEDGE_BASE_DIR` | Default `./knowledge_base` |
| `DEPARTMENT_MODULE_MAP_PATH` | Default `./config/department_module_map.yaml` |
| `APP_ENV` | `production` disables the dev test console and `/api/dev/*` routes |

## Request flow (LangGraph pipeline)

Defined in `app/graph/builder.py`, executed per-request via `app/graph/compiled.py:get_compiled_graph()`:

```
auth_node          → verify JWT (JWT_SECRET), extract userId/tenantId/role
   ↓ (route_after_auth)
tenant_key_node     → fetch Tenant.openaiApiKey from DB; short-circuit if missing
   ↓ (route_after_tenant_key)
department_node    → ADMIN/SUPERADMIN bypass; otherwise call backend_botivate_os GET /me,
                      resolve department(s) → allowed_modules via config/department_module_map.yaml
   ↓
retrieve_node       → search Chroma, filtered to allowed_modules
   ↓
scope_decision_node → in-scope? otherwise refuse without an LLM call
   ↓ (route_after_scope)
refuse_node  OR  generate_node → generate_node builds a per-tenant ChatOpenAI
                                   (app/graph/llm.py:get_llm_for_tenant) and answers
```

`POST /api/v1/chat` (JSON, whole answer at once) and `POST /api/v1/chat/stream` (SSE, chunked `delta`/`sources`/`done` frames) both run this same graph — streaming just re-chunks the already-generated answer for progressive rendering, it does not token-stream from the LLM itself.

## Adding a new knowledge-base module

1. Add a new folder under `knowledge_base/{module-key}/` with Markdown files (frontmatter optional, see existing files for the convention).
2. Register the module key in `app/modules/registry.py` (`is_valid_module` must accept it).
3. Map department name(s)/code(s) to it in `config/department_module_map.yaml` — the comment at the top of that file explains the normalization rules (lowercase, alphanumeric only) and that `"common"` is always implicitly included.
4. Run `python scripts/ingest.py` (or `docker compose run --rm ai-assistant python scripts/ingest.py` in production) to embed the new content.

## Known backend response-shape gotcha (already fixed here)

`backend_botivate_os`'s `GET /me` route wraps its response in `{success, message, data: {...profile}}` (its shared `ApiResponse.success()` convention). `app/auth/node_backend_client.py:fetch_me()` unwraps this (`payload.get("data", payload)`) before parsing profile fields — this fix lives entirely in this repo, `backend_botivate_os` was not changed. If `backend_botivate_os`'s `/me` route or its envelope shape ever changes, re-verify this unwrap logic (`tests/test_node_backend_client.py` covers both the wrapped and unwrapped cases).

## Other documentation

| File | Contents |
|---|---|
| `README.md` | Project layout, local dev test console, demo logins |
| `PRODUCTION_INTEGRATION.md` | Original integration plan (JWT flow, env vars, Docker Compose service block, frontend proxy pattern) — largely superseded by the two docs below, which reflect the actually-deployed setup |
| `HOSTINGER_DEPLOY.md` | **Current/most accurate** — full Hostinger VPS deployment runbook actually used, plus a summary of every code change made to support per-tenant keys + streaming |
| `FRONTEND_INTEGRATION_FOR_AUTOROCKET_DEV.md` | Exact file paths, line numbers, and code for whoever owns `botivate_os_frontend` to wire up `ChatWidget.tsx` — this integration is **not yet implemented** as of this writing |
| `SETUP.md` | Local setup from scratch |
| `deploy.sh` | One-command build → ingest → up → health-check sequence used for every deploy/redeploy |
