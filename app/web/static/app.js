const loginPanel = document.querySelector('#loginPanel');
const chatPanel = document.querySelector('#chatPanel');
const userGrid = document.querySelector('#userGrid');
const loginForm = document.querySelector('#loginForm');
const loginError = document.querySelector('#loginError');
const usernameInput = document.querySelector('#username');
const passwordInput = document.querySelector('#password');
const logoutButton = document.querySelector('#logoutButton');
const sessionMeta = document.querySelector('#sessionMeta');
const messages = document.querySelector('#messages');
const chatForm = document.querySelector('#chatForm');
const messageInput = document.querySelector('#messageInput');
const sendButton = document.querySelector('#sendButton');

const state = {
  token: localStorage.getItem('ar_assistant_token') || '',
  user: JSON.parse(localStorage.getItem('ar_assistant_user') || 'null'),
  history: [],
};

const passwordByUser = {
  purchase: 'purchase123',
  sales: 'sales123',
  maintenance: 'maintenance123',
  accounts: 'accounts123',
  hr: 'hr123',
};

function setSession(token, user) {
  state.token = token;
  state.user = user;
  state.history = [];
  localStorage.setItem('ar_assistant_token', token);
  localStorage.setItem('ar_assistant_user', JSON.stringify(user));
  renderSession();
}

function clearSession() {
  state.token = '';
  state.user = null;
  state.history = [];
  localStorage.removeItem('ar_assistant_token');
  localStorage.removeItem('ar_assistant_user');
  messages.innerHTML = '';
  renderSession();
}

function renderSession() {
  const loggedIn = Boolean(state.token && state.user);
  loginPanel.classList.toggle('hidden', loggedIn);
  chatPanel.classList.toggle('hidden', !loggedIn);
  if (!loggedIn) return;

  sessionMeta.textContent = `${state.user.name} · ${state.user.department}`;
  if (messages.children.length === 0) {
    appendMessage(
      'assistant',
      `Logged in as ${state.user.name}. Try: "${state.user.sample}"`
    );
  }
  messageInput.focus();
}

async function loadUsers() {
  try {
    const res = await fetch('/api/dev/users');
    if (!res.ok) throw new Error('Demo users are disabled');
    const data = await res.json();
    userGrid.innerHTML = '';
    data.users.forEach((user) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'user-card';
      button.innerHTML = `<strong>${user.name}</strong><span>${user.username} / ${passwordByUser[user.username]}</span>`;
      button.addEventListener('click', () => {
        usernameInput.value = user.username;
        passwordInput.value = passwordByUser[user.username] || '';
      });
      userGrid.appendChild(button);
    });
  } catch (error) {
    userGrid.innerHTML = '';
    loginError.textContent = error.message;
  }
}

async function login(event) {
  event.preventDefault();
  loginError.textContent = '';
  const username = usernameInput.value.trim();
  const password = passwordInput.value;

  try {
    const res = await fetch('/api/dev/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Login failed');
    setSession(data.token, data.user);
  } catch (error) {
    loginError.textContent = error.message;
  }
}

function escapeHtml(value) {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function renderInlineMarkdown(value) {
  const links = [];
  let rendered = escapeHtml(value).replace(
    /\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g,
    (_, label, url) => {
      const token = `@@LINK_${links.length}@@`;
      links.push(`<a href="${url}" target="_blank" rel="noreferrer">${label}</a>`);
      return token;
    }
  );

  rendered = rendered
    .replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noreferrer">$1</a>')
    .replace(/`([^`]+)`/g, (_, codeValue) => {
      const route = codeValue.trim();
      if (route.startsWith('/')) {
        return `<a href="https://autorocket.in${route}" target="_blank" rel="noreferrer">${route}</a>`;
      }
      return `<code>${codeValue}</code>`;
    })
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/\*([^*]+)\*/g, '<em>$1</em>');

  links.forEach((link, index) => {
    rendered = rendered.replace(`@@LINK_${index}@@`, link);
  });

  return rendered;
}

function renderMarkdown(value) {
  const lines = value.replace(/\r\n/g, '\n').split('\n');
  const html = [];
  let listType = null;

  function closeList() {
    if (!listType) return;
    html.push(`</${listType}>`);
    listType = null;
  }

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

function appendMessage(role, text, sources = []) {
  const el = document.createElement('div');
  el.className = `message ${role}`;

  const body = document.createElement('div');
  body.className = 'message-body';
  if (role === 'assistant') {
    body.innerHTML = renderMarkdown(text);
  } else {
    body.textContent = text;
  }
  el.appendChild(body);

  if (sources.length) {
    const sourceBox = document.createElement('div');
    sourceBox.className = 'sources';
    sourceBox.innerHTML = '<strong>Sources</strong>';
    sources.forEach((source) => {
      const row = document.createElement('div');
      row.textContent = `${source.module} · ${source.doc_title} · ${source.source_path}`;
      sourceBox.appendChild(row);
    });
    el.appendChild(sourceBox);
  }

  messages.appendChild(el);
  messages.scrollTop = messages.scrollHeight;
}

async function sendMessage(event) {
  event.preventDefault();
  const text = messageInput.value.trim();
  if (!text || !state.token) return;

  appendMessage('user', text);
  messageInput.value = '';
  sendButton.disabled = true;
  sendButton.textContent = 'Thinking...';

  try {
    const res = await fetch('/api/v1/chat', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${state.token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: text,
        conversation_history: state.history.slice(-10),
      }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Chat request failed');

    appendMessage('assistant', data.answer, data.sources || []);
    state.history.push({ role: 'user', content: text });
    state.history.push({ role: 'assistant', content: data.answer });
  } catch (error) {
    appendMessage('assistant', `Error: ${error.message}`);
  } finally {
    sendButton.disabled = false;
    sendButton.textContent = 'Send';
    messageInput.focus();
  }
}

loginForm.addEventListener('submit', login);
logoutButton.addEventListener('click', clearSession);
chatForm.addEventListener('submit', sendMessage);
messageInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault();
    chatForm.requestSubmit();
  }
});

loadUsers();
renderSession();
