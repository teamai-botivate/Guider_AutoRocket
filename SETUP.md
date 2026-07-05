# SETUP.md — Manual Setup Guide (AutoRocket AI Assistant)

Ye guide follow karke aap is naye `autorocket_ai_assistant` service ko apne machine pe khud
setup, configure, aur run kar sakte ho. Koi bhi command yahan maine chalaya nahi hai — sab
aapko khud terminal me run karna hai.

Assumed: aap `c:\Users\prabh\Desktop\Autorocket\autorocket_ai_assistant` folder me ho.

---

## 1. Python virtual environment banao

PowerShell me:

```powershell
cd c:\Users\prabh\Desktop\Autorocket\autorocket_ai_assistant
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Agar `Activate.ps1` chalne me execution-policy error de, to (ek baar, apne user scope me):

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Activate hone ke baad terminal prompt me `(.venv)` dikhna chahiye.

---

## 2. Dependencies install karo

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Isme FastAPI, LangChain, LangGraph, ChromaDB, PyJWT, pytest, etc. sab install ho jayenge.
Pehli baar `chromadb`/`langchain` install hone me kuch minute lag sakte hain.

---

## 3. `.env` file banao

`.env.example` ko copy karke `.env` banao:

```powershell
Copy-Item .env.example .env
```

Ab `.env` file ko kholke ye values bharo:

| Variable | Kya bharna hai |
|---|---|
| `OPENAI_API_KEY` | Aapki OpenAI API key (platform.openai.com se) |
| `JWT_SECRET` | **`backend_botivate_os/.env` me jo `JWT_SECRET` hai, wahi exact value yahan bhi daalo** — dono services ka secret match hona zaroori hai, warna token verify nahi hoga |
| `NODE_BACKEND_URL` | Aapke backend ka base URL, e.g. `http://localhost:5000/api` (jo bhi port pe `backend_botivate_os` chal raha hai) |

Baaki defaults (`OPENAI_CHAT_MODEL`, `VECTOR_STORE_BACKEND`, `CHROMA_PERSIST_DIR`, etc.) abhi
chhed'ne ki zaroorat nahi — wo already sahi defaults ke saath aate hain.

---

## 4. Backend chalao (agar already nahi chal raha)

Isi service ko test karne ke liye `backend_botivate_os` ka bhi chalu hona zaroori hai (kyunki
ye service `GET /me` call karta hai department resolve karne ke liye):

```powershell
cd ..\backend_botivate_os
npm run dev
```

Ye alag terminal window me chalao, is service ke saath parallel.

---

## 5. Knowledge base ingest karo (Chroma me embed karo)

Wapas `autorocket_ai_assistant` folder me (venv activated):

```powershell
cd c:\Users\prabh\Desktop\Autorocket\autorocket_ai_assistant
python -m scripts.ingest
```

Ye `knowledge_base/*.md` files ko padhega, chunks banake OpenAI embeddings se vectorize karega,
aur `./data/chroma` folder me store karega. Output me har file ke liye `[OK]` ya `[SKIP]` dikhna
chahiye.

Dobara run karne pe (agar files nahi badli) `[SKIP] (unchanged)` dikhega — ye normal hai
(idempotent ingestion).

Agar sirf validate karna hai bina likhe:
```powershell
python -m scripts.ingest --dry-run
```

---

## 6. Service run karo

```powershell
uvicorn app.main:app --reload --port 8000
```

Browser me `http://localhost:8000/healthz` khol ke check karo — `{"status":"ok",...}` aana
chahiye.

---

## 7. Built-in test frontend se test karo

Browser me open karo:

```text
http://localhost:8000/
```

Local testing ke liye five demo logins available hain:

| Department | Username | Password |
| --- | --- | --- |
| Purchase | `purchase` | `purchase123` |
| Sales | `sales` | `sales123` |
| Maintenance | `maintenance` | `maintenance123` |
| Accounts | `accounts` | `accounts123` |
| HR | `hr` | `hr123` |

Ye demo JWT local assistant service generate karta hai using `.env` ka `JWT_SECRET`.
Token me department claim hota hai, isliye quick local testing ke liye Node backend `/me`
required nahi hota. `/api/dev/*` routes sirf `APP_ENV=development/dev/local/test` me enabled hain.

---

## 8. Real JWT token se test karo

1. `backend_botivate_os` ke normal login API se ek token lo (ya aapki `jwt_tokens for testing.txt`
   file me pehle se saved token use karo, agar wahi secret match karta hai jo `.env` me hai).
2. PowerShell me:

```powershell
$TOKEN = "yaha_apna_JWT_token_paste_karo"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/chat" `
  -Method Post `
  -Headers @{ Authorization = "Bearer $TOKEN" } `
  -ContentType "application/json" `
  -Body '{"message": "How do I raise a purchase indent?", "conversation_history": []}'
```

Ya agar Git Bash / WSL use kar rahe ho (curl available hai):
```bash
./scripts/smoke_test.sh "$TOKEN"
```

Expected: JSON response jisme `answer`, `in_scope`, aur `sources` (kaunsi knowledge-base file se
jawab aaya) honge.

---

## 9. Tests chalao (optional but recommended)

```powershell
pytest tests/ -v
```

Sab tests mocked hain (koi real OpenAI call ya real backend call nahi hoti tests me) — ye sirf
logic verify karte hain (JWT verify, department mapping, LangGraph flow, API routes, ingestion).

---

## 10. Docker se run karna ho to (optional)

```powershell
docker compose up --build
```

Isse `.env` file automatically container me load hogi (`env_file: .env` docker-compose.yml me
set hai). Same smoke test commands upar wale is container ke against bhi chalenge.

---

## Troubleshooting

- **401 Unauthorized har request pe** → check karo `.env` ka `JWT_SECRET`
  `backend_botivate_os/.env` ke `JWT_SECRET` se **exactly** match karta hai.
- **`/me` fetch error / department empty aa raha hai** → check karo `NODE_BACKEND_URL` sahi hai
  aur backend chal raha hai us URL pe.
- **OpenAI errors** → check karo `OPENAI_API_KEY` sahi hai aur account me credits/quota hai.
- **Ingestion ke baad bhi jawab "I don't have documentation on that"** → matlab abhi us topic
  ka koi `.md` file `knowledge_base/` me nahi hai, ya ingestion dobara nahi chali — naye/edited
  `.md` file ke baad hamesha `python -m scripts.ingest` dobara chalao.
