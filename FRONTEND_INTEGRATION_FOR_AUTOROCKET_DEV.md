# Guide Bot — Frontend Integration Guide (for the Autorocket OS / `botivate_os_frontend` developer)

> **Scope of this doc:** This describes changes needed in **`botivate_os_frontend`**. `backend_botivate_os` needs **zero route/code changes** for the JWT-delivery part (unlike AI Boardroom, which needed a new `/auth/boardroom-token` endpoint) — but there is **one confirmed response-shape mismatch** between `backend_botivate_os`'s existing `GET /me` route and what Guide Bot expects from it. That mismatch has been fixed entirely inside `autorocket_ai_assistant` (see §2.5) — no `backend_botivate_os` code needs to change because of it either. `autorocket_ai_assistant` is deployed and maintained independently — treat it as an external HTTPS API once deployed at `https://guide.autorocket.in`.
>
> This is a plan/spec only — no code in `botivate_os_frontend` has been changed. Everything below is written for whoever owns that repo to implement.

---

## 0. What this service is

`autorocket_ai_assistant` (nickname: **Guide Bot**) is a "how do I use this software" help assistant — separate from **AI Boardroom** (the business-data chat at `ai-boardroom.autorocket.in`). It answers questions like "How do I create a purchase indent?" using a curated knowledge base, scoped to the logged-in user's department. It does **not** query live tenant business data.

It will be deployed independently at:

```
https://guide.autorocket.in
```

It already has a `ChatWidget.tsx` home in the frontend — you don't need to build new UI from scratch, just rewire an existing component.

---

## 1. Where the existing widget lives (already in the codebase)

| File | Role |
|---|---|
| `botivate_os_frontend/src/components/ui/ChatWidget.tsx` | The actual floating chat widget UI — button, panel, message list, input box. Currently answers from a **hardcoded local FAQ array**, not a real backend. |
| `botivate_os_frontend/src/components/ui/ChatWidgetLoader.tsx` | Loader wrapper for the widget. |
| `botivate_os_frontend/src/app/(dashboard)/layout.tsx` | Already mounts the widget on every dashboard page. **No change needed here.** |

Confirmed today: the widget is already visible on every dashboard page (bottom-right floating button, "AI Assistant" tooltip). The only problem is that `ChatWidget.tsx`'s answers come from a local keyword-matching array (see `ChatWidget.tsx:14-167`, the `FAQ` array and `findAnswer()` function), not from any API call.

---

## 2. How auth works for this service (same JWT, different delivery than AI Boardroom)

Guide Bot verifies the **same JWT** already issued by `backend_botivate_os` (same `JWT_SECRET`) — no new backend endpoint is required for JWT delivery.

Unlike AI Boardroom (which needs the JWT inside a URL because it's opened as a separate page/tab), Guide Bot is called **server-side from a Next.js API route**, so it can read the `accessToken` httpOnly cookie directly — no new "issue me a token" endpoint is needed on `backend_botivate_os` for that part.

**However**, Guide Bot's `department_node` also calls `backend_botivate_os`'s existing `GET /me` route directly (server-to-server, using the same JWT) to resolve the user's department for knowledge-base scoping. That route's actual response shape was verified against the live code and required a fix — see §2.5 below. That fix has been made entirely inside `autorocket_ai_assistant`; `backend_botivate_os` needed no change for it.

```
Browser (ChatWidget.tsx)
   │  fetch('/api/ai-assistant/chat', { message, conversation_history })
   ▼
Next.js server route (NEW FILE — runs server-side, can read httpOnly cookie)
   │  reads accessToken cookie
   │  forwards as: Authorization: Bearer <JWT>
   ▼
https://guide.autorocket.in/api/v1/chat/stream   (deployed independently)
   │  verifies JWT with JWT_SECRET (same secret as backend_botivate_os)
   │  extracts userId, tenantId, role from JWT
   │  calls backend_botivate_os's own GET /me endpoint (using the same JWT) to resolve department
   │  fetches Tenant.openaiApiKey from the shared DB for that tenantId
   │  streams back an SSE response
   ▼
Next.js server route relays the SSE stream back to the browser
   ▼
ChatWidget.tsx renders it progressively, with markdown + source links
```

Key point: because this proxy route runs on the Next.js server (not in browser JS), it **can** read the httpOnly `accessToken` cookie safely — this is different from the AI Boardroom case, which needed a brand-new token because the browser had to put it into a cross-domain URL.

### 2.5 — `GET /me` response-shape mismatch (found, fixed inside Guide Bot only)

This is worth knowing about even though it required no change on your side, in case `/me`'s shape ever changes and this breaks again.

`backend_botivate_os`'s `/me` route (`src/routes/core/auth.routes.ts:49` → `getProfileController` in `auth.controller.ts:419-448`) wraps every response in the shared `ApiResponse.success()` envelope:

```json
{
  "success": true,
  "message": "Profile fetched successfully",
  "data": {
    "id": "...",
    "role": "...",
    "department": { "id": "...", "name": "...", "code": "..." },
    "userDepartments": [ { "isPrimary": true, "department": { "id": "...", "name": "...", "code": "..." } } ]
  }
}
```

Guide Bot's original `node_backend_client.py` was written expecting the profile fields at the **top level** of the response (`data["id"]`, `data["role"]`, etc.) with no `data`/`success`/`message` wrapper — which would have caused a `KeyError` on `data["id"]` for every non-admin user (admins skip this call entirely per `route_after_auth`).

**Fix applied (inside `autorocket_ai_assistant/app/auth/node_backend_client.py` only):** `fetch_me()` now unwraps the envelope — it reads `response.json()["data"]` (falling back to the raw payload if the response ever comes back unwrapped) before parsing `id`, `role`, `department`, `userDepartments`. `backend_botivate_os` was **not** changed to make this work.

If `backend_botivate_os`'s `/me` route or its `ApiResponse` envelope shape ever changes, re-check this parsing logic in `node_backend_client.py`.

---

## 3. Required changes — exact files, exact code

### 3.1 — New file: `src/app/api/ai-assistant/chat/route.ts`

This is the only new backend-facing code needed in this repo. It's a thin proxy: reads the cookie, forwards the request, streams the response back unchanged.

```ts
import { cookies } from 'next/headers';
import { NextResponse } from 'next/server';

const AI_ASSISTANT_URL = process.env.AI_ASSISTANT_URL ?? 'http://localhost:8001';

export async function POST(request: Request) {
  const cookieStore = await cookies();
  const token = cookieStore.get('accessToken')?.value;

  if (!token) {
    return NextResponse.json({ message: 'Not authenticated' }, { status: 401 });
  }

  const body = await request.json();

  const upstream = await fetch(`${AI_ASSISTANT_URL}/api/v1/chat/stream`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  });

  return new NextResponse(upstream.body, {
    status: upstream.status,
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      Connection: 'keep-alive',
    },
  });
}
```

Notes:

- `cookies()` is async in current Next.js versions — adjust to `const cookieStore = cookies();` (sync) if your Next.js version requires that instead; check how other routes in this repo already call `cookies()` for the exact convention used.
- This route does **not** need `NEXT_PUBLIC_` prefix on its env var, because it only runs server-side (see §3.2).
- `upstream.body` is a `ReadableStream` — passing it straight through to `NextResponse` preserves the SSE stream instead of buffering the whole response, which is required for the widget to render text progressively.

### 3.2 — Environment variable

Add to `botivate_os_frontend/.env` (local) and to the production hosting environment config:

```env
AI_ASSISTANT_URL=https://guide.autorocket.in
```

For local development against a locally-run Guide Bot instance:

```env
AI_ASSISTANT_URL=http://localhost:8001
```

Do **not** prefix this with `NEXT_PUBLIC_` — the browser never calls Guide Bot directly, only the Next.js server does (via the proxy route above). Keeping it server-side avoids any CORS configuration on the Guide Bot side.

### 3.3 — Rewrite `ChatWidget.tsx`'s answer logic

File: `src/components/ui/ChatWidget.tsx`

**Current state (lines 14-167):** A hardcoded `FAQ` array plus `findAnswer()`, a keyword-matching function with no real backend call. **Delete this block entirely** — it's fully replaced by the real API.

**Current state (lines 231-255) — `sendMessage`:**

```ts
const sendMessage = (text: string) => {
  if (!text.trim()) return;

  const userMsg: Message = {
    id: Date.now().toString(),
    role: 'user',
    text: text.trim(),
    ts: new Date(),
  };
  setMessages((prev) => [...prev, userMsg]);
  setInput('');
  setTyping(true);

  /* simulate bot thinking */
  setTimeout(() => {
    setTyping(false);
    const botMsg: Message = {
      id: (Date.now() + 1).toString(),
      role: 'bot',
      text: findAnswer(text),
      ts: new Date(),
    };
    setMessages((prev) => [...prev, botMsg]);
  }, 900);
};
```

**Replace with** (async, calls the real proxy route, reads the SSE stream, updates the bot message incrementally):

```ts
const sendMessage = async (text: string) => {
  if (!text.trim()) return;

  const userMsg: Message = {
    id: Date.now().toString(),
    role: 'user',
    text: text.trim(),
    ts: new Date(),
  };
  setMessages((prev) => [...prev, userMsg]);
  setInput('');
  setTyping(true);

  const botId = (Date.now() + 1).toString();
  setMessages((prev) => [...prev, { id: botId, role: 'bot', text: '', ts: new Date() }]);

  try {
    const response = await fetch('/api/ai-assistant/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: text,
        conversation_history: messages.slice(-10).map((m) => ({
          role: m.role === 'bot' ? 'assistant' : 'user',
          content: m.text,
        })),
      }),
    });

    if (!response.ok || !response.body) {
      throw new Error(`Request failed with status ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = '';

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });

      const events = buffer.split('\n\n');
      buffer = events.pop() ?? '';

      for (const evtRaw of events) {
        if (!evtRaw.startsWith('data: ')) continue;
        const evt = JSON.parse(evtRaw.slice(6));

        if (evt.type === 'delta') {
          setMessages((prev) =>
            prev.map((m) => (m.id === botId ? { ...m, text: m.text + evt.content } : m))
          );
        }
        if (evt.type === 'sources' && Array.isArray(evt.sources) && evt.sources.length) {
          const sourceLines = evt.sources
            .map((s: { doc_title: string; source_path: string }) => `- ${s.doc_title}`)
            .join('\n');
          setMessages((prev) =>
            prev.map((m) =>
              m.id === botId ? { ...m, text: `${m.text}\n\n**Sources:**\n${sourceLines}` } : m
            )
          );
        }
        if (evt.type === 'error') {
          setMessages((prev) =>
            prev.map((m) => (m.id === botId ? { ...m, text: `⚠️ ${evt.message}` } : m))
          );
        }
      }
    }
  } catch (error) {
    setMessages((prev) =>
      prev.map((m) =>
        m.id === botId ? { ...m, text: "Sorry, I couldn't reach the assistant. Please try again." } : m
      )
    );
  } finally {
    setTyping(false);
  }
};
```

### 3.4 — Markdown rendering (bold, lists, clickable routes/links)

Guide Bot's answers use Markdown-style formatting (`**bold**`, numbered/bulleted lists, and backtick-quoted internal routes like `` `/purchase/indent` ``). The current widget's `RenderText` component (`ChatWidget.tsx:179-194`) only handles `**bold**` — it does not handle lists or turn backtick-quoted routes into links.

**Add this markdown renderer** (place near `RenderText`, or replace it for bot messages):

```tsx
function escapeHtml(value: string): string {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function renderInlineMarkdown(value: string): string {
  const links: string[] = [];

  let rendered = escapeHtml(value).replace(
    /\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g,
    (_match, label: string, url: string) => {
      const token = `@@LINK_${links.length}@@`;
      links.push(`<a href="${url}" target="_blank" rel="noreferrer">${label}</a>`);
      return token;
    }
  );

  rendered = rendered
    .replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noreferrer">$1</a>')
    .replace(/`([^`]+)`/g, (_match, code: string) => {
      const route = code.trim();
      if (route.startsWith('/')) {
        // internal app route quoted in backticks -> turn into a clickable absolute link
        return `<a href="https://autorocket.in${route}" target="_blank" rel="noreferrer">${route}</a>`;
      }
      return `<code>${code}</code>`;
    })
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/\*([^*]+)\*/g, '<em>$1</em>');

  links.forEach((link, i) => {
    rendered = rendered.replace(`@@LINK_${i}@@`, link);
  });

  return rendered;
}

function renderMarkdownBlock(value: string): string {
  const lines = value.replace(/\r\n/g, '\n').split('\n');
  const html: string[] = [];
  let listType: 'ol' | 'ul' | null = null;

  const closeList = () => {
    if (listType) {
      html.push(`</${listType}>`);
      listType = null;
    }
  };

  lines.forEach((line) => {
    const trimmed = line.trim();
    if (!trimmed) {
      closeList();
      return;
    }

    const ordered = trimmed.match(/^\d+\.\s+(.+)$/);
    if (ordered) {
      if (listType !== 'ol') {
        closeList();
        html.push('<ol>');
        listType = 'ol';
      }
      html.push(`<li>${renderInlineMarkdown(ordered[1])}</li>`);
      return;
    }

    const unordered = trimmed.match(/^[-*]\s+(.+)$/);
    if (unordered) {
      if (listType !== 'ul') {
        closeList();
        html.push('<ul>');
        listType = 'ul';
      }
      html.push(`<li>${renderInlineMarkdown(unordered[1])}</li>`);
      return;
    }

    closeList();
    html.push(`<p>${renderInlineMarkdown(trimmed)}</p>`);
  });

  closeList();
  return html.join('');
}

function MarkdownMessage({ text }: { text: string }) {
  // eslint-disable-next-line react/no-danger -- content is HTML-escaped in renderInlineMarkdown before any tags are injected
  return <div dangerouslySetInnerHTML={{ __html: renderMarkdownBlock(text) }} />;
}
```

This logic is a direct port of the renderer already used and tested in `autorocket_ai_assistant`'s own local test console (`app/web/static/app.js`), so its behavior is already known-good.

**Then in the message-rendering JSX** (`ChatWidget.tsx`, around lines 401-412), swap `<RenderText text={msg.text} />` for bot messages only:

```tsx
{msg.role === 'bot' ? <MarkdownMessage text={msg.text} /> : <RenderText text={msg.text} />}
```

(Keep `RenderText` for user messages — they're plain text the user typed, no need to run them through the Markdown/HTML path.)

> Security note: `renderInlineMarkdown` calls `escapeHtml()` on the full string **before** injecting any `<a>`/`<strong>`/`<code>` tags, so raw user- or model-provided `<script>`-like content is neutralized first. Don't remove that escape step if you modify this function later.

### 3.5 — Sources as clickable links

The backend's SSE `sources` event includes `{ module, doc_title, source_path }` for each retrieved knowledge-base document. The code above (§3.3) already appends them as a `**Sources:**` markdown list, which `MarkdownMessage` will then render as bold text + bullet list.

If you want each source to be an actual clickable link (not just a title), you'll need a public URL scheme for the knowledge base docs — decide this with whoever owns the docs site:

- If `knowledge_base/*.md` files are also published as help pages on `autorocket.in` (e.g. `https://autorocket.in/help/purchase-sfms-indent/raising-an-indent`), change the source line construction to:
  ```ts
  const sourceLines = evt.sources
    .map((s: { doc_title: string; source_path: string }) =>
      `- [${s.doc_title}](https://autorocket.in/help/${s.source_path.replace(/\.md$/, '')})`
    )
    .join('\n');
  ```
  This produces a `[label](url)` markdown link, which `renderInlineMarkdown` (§3.4) already turns into a real `<a href>`.
- If there's no public help-docs site yet, keep sources as plain titles (current behavior) until one exists — don't invent a URL that 404s.

---

## 4. Summary of changes (this repo only)

| # | File | Type | What |
|---|---|---|---|
| 1 | `src/app/api/ai-assistant/chat/route.ts` | New | Server-side proxy: reads `accessToken` cookie, forwards to Guide Bot as `Authorization: Bearer`, streams SSE response back |
| 2 | `.env` (+ production hosting env) | Modify | Add `AI_ASSISTANT_URL=https://guide.autorocket.in` (no `NEXT_PUBLIC_` prefix) |
| 3 | `src/components/ui/ChatWidget.tsx` | Modify | Remove hardcoded `FAQ`/`findAnswer` (lines 14-167); rewrite `sendMessage` (lines 231-255) to call the proxy route and read the SSE stream; add Markdown renderer; swap bot-message rendering to use it |

No changes needed in:
- `ChatWidgetLoader.tsx`
- `layout.tsx`
- `backend_botivate_os` (any file)
- Prisma schema

---

## 5. Testing checklist

- [ ] `guide.autorocket.in` is deployed and its `/healthz` returns `{"status": "ok", ...}` (confirm with whoever deploys `autorocket_ai_assistant`)
- [ ] `AI_ASSISTANT_URL` set correctly in both local `.env` and production hosting env
- [ ] Log into `botivate_os_frontend`, open the chat widget, ask "How do I create a purchase indent?"
- [ ] Confirm the answer streams in progressively (not all at once)
- [ ] Confirm `**bold**` and numbered/bulleted lists render as real formatting, not literal asterisks
- [ ] Confirm a question outside the user's department (e.g. a Sales user asking an HR-only question) gets a scoped refusal message, not a generic answer
- [ ] Confirm a SUPERADMIN/ADMIN user gets answers across all modules (department filter bypass)
- [ ] Confirm that if the tenant has no OpenAI key configured yet, the widget shows a clear error rather than hanging or crashing
