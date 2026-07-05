# AutoRocket AI Assistant

Independent FastAPI + LangChain + LangGraph service providing a role/department-scoped,
RAG-based "how do I use this software" assistant for the AutoRocket / Botivate OS platform.

Phase 1 scope: answers are drawn only from the curated Markdown knowledge base in
`knowledge_base/` — it does not query live tenant data.

See `SETUP.md` for how to install, configure, and run this service locally or via Docker.

## Project layout

- `app/` — FastAPI app, auth, module registry, retrieval, LangGraph flow
- `knowledge_base/` — curated Markdown docs, one directory per business module
- `config/department_module_map.yaml` — maps tenant department names to module access
- `scripts/ingest.py` — offline pipeline that embeds `knowledge_base/` into the vector store
- `scripts/smoke_test.sh` — curl-based end-to-end check against a running instance
- `tests/` — pytest suite (auth, department mapping, graph nodes, API routes, ingestion)

## How it connects to the rest of AutoRocket

- Verifies the same JWT (`JWT_SECRET`) issued by `backend_botivate_os` — no new backend
  endpoint or backend code change is required.
- Resolves the caller's department by calling the existing `GET /me` endpoint on the Node
  backend with the caller's own bearer token.
- `botivate_os_frontend`'s `ChatWidget.tsx` is intended to call `POST /api/v1/chat` on this
  service (via the existing shared axios client) as a follow-up integration step.

## Development test console

Run the service with `uvicorn app.main:app --reload --port 8000`, then open
`http://localhost:8000/`. The built-in console is plain HTML/CSS/JS under `app/web/` and provides
five demo logins:

- `purchase` / `purchase123`
- `sales` / `sales123`
- `maintenance` / `maintenance123`
- `accounts` / `accounts123`
- `hr` / `hr123`

These users are for local testing only and are exposed by `/api/dev/*` when `APP_ENV` is
`development`, `dev`, `local`, or `test`. Their JWTs include a `departments` claim so the assistant
can test department-scoped retrieval without requiring the Node backend `/me` call.
