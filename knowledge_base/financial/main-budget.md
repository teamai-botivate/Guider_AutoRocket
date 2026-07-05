---
title: Creating and Managing the Main Budget
module: financial
tags: [financial-system, budget, allocations, fiscal-year]
---

## Where to find it

Go to **Financial System > Main Budget** in the left sidebar (URL: `/financial-system/main-budget`). The other two items in this sidebar group are **Dashboard** and **Financial Details**.

## Creating a budget

1. On the Main Budget page, click **+ New Budget** (top right).
2. Fill in the "Create New Budget" form:
   - **Fiscal Year** (required) — free text, e.g. `2025-2026`.
   - **Period Type** (required) — dropdown: Monthly, Quarterly, or Yearly.
   - **Start Date** and **End Date** (required) — date pickers. They default to April 1 of the current year through March 31 of the next year.
   - **Budget Name** (optional) — auto-generated if left blank.
   - **Notes** (optional) — free text.
3. Click **Create Budget**.
4. On creation, the system automatically builds a full set of budget line items covering the company's standard expense/revenue categories (Budget Sales, Production Costs, Salaries & Benefits, Admin & Office Expenses, Vehicle & Factory Costs, Interest Costs, and Other Costs — roughly 35+ line items total), each starting at ₹0 allocated/used. You do not create these line items yourself; you only set amounts for them afterward.

Only one budget can be "active" per fiscal year context at a time in the selector, but multiple budget periods can exist per fiscal year (e.g. if using Monthly or Quarterly period types) — use the fiscal year dropdown and, when more than one budget period exists for that year, the adjacent period dropdown to switch between them.

## Setting allocation and usage amounts

1. With a budget open, scroll to the **Module Budget Allocation** table.
2. Each row is a budget category/module, tagged **AUTO** (usage is synced automatically from live data elsewhere in the system, e.g. Store PO + freight, Purchase Orders, Spare part costs, Outhouse repair payments, Subscriptions + payments, Petrol expenses, Petty cash expenses) or **MANUAL** (usage is typed in by hand — most categories are manual).
3. Edit the **Allocated (₹)** field for any row directly in the table.
4. For MANUAL rows, also edit the **Used (₹)** field directly. AUTO rows show usage as read-only (with a lightning-bolt icon) and cannot be typed into.
5. Click **Save Changes** to persist your edits. The button shows "Saving…" then a green "✓ Saved" confirmation.
6. To force AUTO rows to re-pull the latest figures from their source modules, click **Sync Usage** near the top of the page (shows "Syncing…" while in progress, and "Usage synced at [time]" once done).

The table also shows running totals for Allocated, Used, Remaining (highlighted red if a row goes over budget), and Utilization % with a progress bar per row.

## Editing budget details or deleting a budget

- The info strip below the header shows the budget's **Period** (start–end dates), **Status** (Draft/Active/Archived, color-coded), and **Notes** if any.
- To delete the current budget, click **Delete** (top right), then confirm in the "Delete Budget?" dialog. This permanently removes the budget and all its module allocations — this action cannot be undone.
- If no budget exists yet for the selected fiscal year, the page shows an empty state with a **+ Create Budget** button.

## Notes on unclear/inconsistent behavior

The "AUTO" vs "MANUAL" designation in the allocation table is hardcoded in the frontend for a fixed short list of category keys (store, purchase, maintenance, repair, admin, logistics, petty_cash). However, the actual budget line items created by the backend use a different, more detailed set of accounting category keys (e.g. "Budgeted Sales Revenue", "Factory electricity", "Director Salary & Benefits"). In practice this means most or all visible rows may show as MANUAL even though the underlying design intends some categories to sync automatically — if a row you expect to auto-sync doesn't update after clicking Sync Usage, this mismatch is the likely cause, not a bug in your data entry.
