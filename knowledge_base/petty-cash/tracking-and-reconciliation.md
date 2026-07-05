---
title: Tracking and Reconciling Petty Cash
module: petty_cash
tags: [petty-cash, ledger, dashboard, reports, reconciliation, head-master, settings]
---

## Dashboard — at-a-glance overview

Go to **Petty Cash → Dashboard** (`/petty-cash/dashboard`), titled "Petty Cash Dashboard" with subtitle "Overview of approved cash activity." Pick a date range with the two date pickers at the top right. It shows:

- **KPI row**: Total Income, Total Expense, Net Balance, **Pending Approvals** (count awaiting review), **Pending Deletes** (count of open delete requests).
- **15-Day Cash Flow** chart: a daily bar chart of income vs. expense, built only from approved activity.
- **Top Expense Categories**: a ranked list of categories by approved spend.

## Ledger — combined transaction history

Go to **Petty Cash → Ledger** (`/petty-cash/ledger`), subtitle "Combined chronological view — approved expenses & petty cash." This merges two sources into one dated list:
- Approved rows from **Expenses** (flow IN → shown as CREDIT, flow OUT → DEBIT), using the voucher number as the reference and the expense description (or Group Head, if no description) as the line text.
- All rows from **Petty Cash** (CASH_RECEIVED/CASH_RETURNED → CREDIT, EXPENSE → DEBIT), referenced as `PC-<last 6 chars of id>`.

Summary cards at the top show **Total Credit (In)**, **Total Debit (Out)**, and **Closing Balance** (credits minus debits) for the currently filtered set. Use the search box (searches reference and description) and the two date pickers to narrow the view. The table columns are Date, Reference, Description, Type (CREDIT/DEBIT badge), Amount, and Status.

## Reports — aggregated summaries for a period

Go to **Petty Cash → Reports** (`/petty-cash/reports`). Choose a **Report Type** from the toggle buttons and a **Date Range**, then review:
- **Total Entries**, **Total Amount**, **Approved Amount**, **Pending Count** summary cards.
- A records table (Voucher, Date, Flow, Category, Amount, Branch, Status) for the selected range.

An **Export** button is present in the page header (top right) for exporting the report.

## Head Master — set up categories and branches before recording expenses

Go to **Petty Cash → Head Master** (`/petty-cash/head-master`) to configure the category hierarchy and branch list used by the Expenses form:

1. Click **Add Category** to open **Add Category Group**. Enter a **Group Head** (e.g. "Operations", "Sales", "Admin"), then optionally add one or more **Expense Heads** under it (click **Add Expense Head**), and under each Expense Head optionally add one or more **Sub Heads** (click **Add Sub Head**). Click **Save Category Group** when done.
2. Click **Add Branch** to open the **Add Branch** dialog, type a **Branch Name** (e.g. "Mumbai", "Delhi HQ", "Warehouse 2"), and click **Save Branch**.
3. The **Category Hierarchy** panel shows a collapsible tree (Group → Expense Head → Sub Head); hovering a row reveals a trash icon to delete that group, expense head, or sub head.
4. The **Branches** panel lists all configured branches with a delete option per row; a branch named/containing "Head Office" gets an **HQ** badge.

These Group Head / Expense Head / Sub Head / Branch values are exactly what populate the dropdowns on the **Add Expense** form.

## Settings — who has access

Go to **Petty Cash → Settings** (`/petty-cash/settings`) to view:
- **Users** card: a searchable list of members with access, each showing name, email, and a role badge (SUPERADMIN, ADMIN, or USER).
- **Branches** card: a read-only list of configured branches (same data as Head Master); if none exist yet it prompts "Add branches in Head Master."

This page is informational only — actual category/branch changes are made on the Head Master page.

## Reconciliation tip

Because Expenses and Petty Cash are two independent logs that only meet in the **Ledger**, reconcile the drawer by checking the Ledger's **Closing Balance** against physical cash, and cross-check the **Dashboard**'s Pending Approvals/Pending Deletes counts to make sure no expense is sitting unresolved before treating a period as closed.
