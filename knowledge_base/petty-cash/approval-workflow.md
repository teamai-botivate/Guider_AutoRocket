---
title: Petty Cash Approval Workflow
module: petty_cash
tags: [petty-cash, approval, reject, hold, delete-request, workflow]
---

## How petty cash expense approval works

Only entries created on the **Expenses** page (`/petty-cash/expenses`) go through approval. Entries logged on the **Petty Cash** page have no approval step (see the recording doc).

### Statuses an expense can have

- **PENDING** — newly submitted, awaiting a decision.
- **APPROVED** — accepted; counts toward Inflow/Outflow/Net Balance totals and appears in the Ledger.
- **REJECTED** — declined.
- **HOLD** — parked for later review (still actionable, does not count as approved).

Separately, every expense also has a **delete status**: **ACTIVE** (normal), **PENDING_DELETE** (a delete request was raised and is awaiting a decision), or **DELETED** (delete request approved / entry removed from active views).

### Auto-approval rule

When an **Admin** or **Superadmin** creates an expense with **Flow Direction = Income (IN)**, it is approved automatically at creation — it never enters the PENDING queue. Every other case (any OUT/expense entry, or an IN entry created by a regular User) starts as PENDING and needs a manual decision.

### Reviewing and deciding on expenses

1. Go to **Petty Cash → Approval Panel** (`/petty-cash/approval-panel`).
2. Use the top-level tab **Expense Approval** (badge shows the count of PENDING items) or **Delete Approval** (badge shows the count of PENDING_DELETE items).
3. Under **Expense Approval**, sub-tabs filter the list:
   - **Pending** — status = PENDING
   - **Hold** — status = HOLD
   - **Rejected** — status = REJECTED
   - **History** — status = APPROVED
4. Only the **Pending** and **Hold** sub-tabs show action buttons; **Rejected** and **History** are view-only. For each actionable row you can click:
   - **Approve** — sets status to APPROVED
   - **Hold** — sets status to HOLD
   - **Reject** — sets status to REJECTED
5. Clicking any of these opens a **Confirm Action** dialog where you can optionally type a **Remark** (e.g. reason for rejection), then click **Confirm**.
6. A restriction is enforced server-side: **an Admin cannot approve their own submitted expense** — that action will be rejected with an error. Approval must come from someone else (e.g. another Admin or Superadmin).

### Reviewing delete requests

1. Still on the **Approval Panel**, switch to the **Delete Approval** tab.
2. Sub-tabs: **Pending Delete** (deleteStatus = PENDING_DELETE) and **Deleted History** (deleteStatus = DELETED).
3. On a row under **Pending Delete** you can:
   - **Approve Delete** — confirms removal, moving deleteStatus to DELETED (entry disappears from the active Expenses list).
   - **Restore** — rejects the delete request, moving deleteStatus back to ACTIVE (entry stays active as if nothing happened).
4. Both actions open the same **Confirm Action** dialog with an optional remark before you click **Confirm**.

### Where approved data shows up

- Approved expenses (and all Petty Cash page entries, which need no approval) feed the **Ledger** (`/petty-cash/ledger`) as chronological CREDIT/DEBIT entries.
- The **Dashboard** (`/petty-cash/dashboard`) KPI row shows a live **Pending Approvals** count and **Pending Deletes** count, plus Total Income, Total Expense, and Net Balance computed from approved activity only.
- **Reports** (`/petty-cash/reports`) summarizes totals including a **Pending Count**.

Note: the on-screen "Submitted By" column in the Approval Panel table currently displays the raw user ID rather than a display name — this appears to be the current UI behavior rather than a documented feature.
