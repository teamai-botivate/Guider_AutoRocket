---
title: Recording a Petty Cash Expense
module: petty_cash
tags: [petty-cash, expense, create, submit, voucher]
---

## How to record an expense

The **Petty Cash** module has two separate ways to log cash movement — use **Expenses** for transactions that need approval and category tracking; use **Petty Cash** for a raw, no-approval cash in/out log. Both live under the **Petty Cash** section in the sidebar.

### Option A — Expenses (with approval workflow)

1. Go to **Petty Cash → Expenses** (`/petty-cash/expenses`).
2. Click **Add Expense** (top right).
3. In the **Add Expense** dialog, fill in:
   - **Flow Direction** — choose **Expense (OUT)** or **Income (IN)**.
   - **Date** (required).
   - **Payment Mode** — Cash, Bank Transfer, Cheque, Online, or UPI.
   - **Group Head** (required) — top-level category, e.g. Operations/Sales/Admin. Options come from **Head Master**.
   - **Expense Head** (required) — narrows once a Group Head is picked.
   - **Sub Head** (optional) — narrows further once an Expense Head is picked.
   - **Branch** (required) — pulled from branches configured in Head Master.
   - **Amount (₹)** (required, must be greater than 0).
   - **Paid To / Vendor** (optional free text).
   - **Description** (optional notes).
4. Click **Submit Expense**. The button is disabled until Group Head, Expense Head, Branch, and a positive Amount are all filled in.
5. The new row appears in the Expenses table with an auto-generated **Voucher** number (format `VCH-<year>-<sequence>`, e.g. `VCH-2026-001`), and a **Status** badge:
   - If you are an **Admin or Superadmin** and the flow is **Income (IN)**, the entry is **auto-approved** immediately.
   - Otherwise (all Expense/OUT entries, and IN entries from regular Users) the entry starts as **PENDING** and must go through the Approval Panel (see the approval-workflow doc).
6. To remove an entry you created, use the delete (trash) icon in its row — this does not delete it outright; it raises a **delete request** (status becomes PENDING DEL) that must also be approved (see approval-workflow doc).

The **Expenses** page header shows three running totals calculated from **approved** entries only: **Total Inflow**, **Total Outflow**, **Net Balance**. Use the filter bar above the table to filter by flow (All / Inflow / Outflow), a date range, or search by voucher/category/vendor text.

### Option B — Petty Cash (raw cash log, no approval)

1. Go to **Petty Cash → Petty Cash** (`/petty-cash/petty-cash`). The page subtitle explicitly says: "Raw cash in/out log — no approval workflow."
2. Click **Add Entry** (top right). This opens the **Add Cash Entries** dialog, which supports adding several rows in one go.
3. For each row, fill in:
   - **Date**
   - **Type** — Cash Received, Expense, or Cash Returned
   - **Amount**
   - **Description** (free-text note)
4. Click **Add Another Row** to log multiple movements at once, or use the row's minus/remove icon to delete a row before saving (at least one row must remain).
5. Click **Save All** to submit every row in the batch at once. There is no approval step here — entries post immediately and adjust the **Running Balance** shown at the top of the page (Cash Received and Cash Returned add to the balance; Expense subtracts).
6. Any entry can be permanently removed later using the trash icon in its table row — this is an outright delete, unlike the "request delete" behavior in Expenses.

### Which one should I use?

Use **Expenses** when the transaction needs categorization (Group Head/Expense Head/Sub Head), a branch, a vendor, and manager sign-off. Use **Petty Cash** for quick day-to-day cash drawer movements that don't need review.
