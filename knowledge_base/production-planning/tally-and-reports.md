---
title: Tally Entry (Production Costing), Reports, and Dashboard
module: production_planning
tags: [tally, costing, reports, dashboard, material-consumption, fg-inventory]
---

# Tally Entry, Reports, and Dashboard

These are the read-only, downstream reporting views of Production Planning — no data entry
happens here except filtering.

## Tally Entry — Production Costing

**Where:** Production Planning → Tally Entry (`/production-planning/tally`). Page heading: "Tally
Entry — Production Costing"; subtitle: "Production cost summary for completed job cards (Tally
integration)."

1. Summary cards: **Material Cost**, **Extra Amount**, **Selling Amount**, **Profit / Loss**
   (totals across the currently filtered rows).
2. Filters: free-text search (job card/product/party), **From Date**, **To Date**, **Party Name**
   dropdown, **Product Name** dropdown, plus a **Clear Filters** button when any filter is active.
3. Table "Production Cost Ledger" columns: Job Card No, Prod No, Order No, Product, Party, Date,
   Produced Qty, Material Cost (₹), Extra (₹), Selling (₹), Profit/Loss (₹), Status (always shown
   as "Posted").
4. Only **Completed** job cards appear here. Material Cost is computed primarily from the actual
   quantities/rates stored on the job card's material check snapshot; if that's unavailable it
   falls back to `BOM perUnitQty × perUnitRate × producedQty`.

## Production Dashboard

**Where:** Production Planning → Dashboard (`/production-planning/dashboard`). Page heading:
"Production Dashboard"; subtitle: "Live overview — production status, inventory, material cost,
QC results and full reports."

1. Time filter buttons: **Today / This Week / This Month / All Time**.
2. KPI cards: Total Orders, Job Cards, Total Produced, Planned Qty, Completion Rate, QC Passed.
3. Charts: Production Status (bar), Top 5 Products by Produced Qty (horizontal bar), Top 5
   Parties by Orders (horizontal bar), Material Cost by Product (bar), QC Results (donut/pie).
4. "Production Reports" tabbed section at the bottom: **Daily Production**, **Material
   Consumption**, **QC Records** — same underlying data as the dedicated Reports page below, just
   period-filtered.

## Reports & Analytics

**Where:** Production Planning → Reports (`/production-planning/reports`). Page heading: "Reports
& Analytics"; subtitle: "Production performance, material consumption, FG inventory, and
rejection analysis."

1. KPI cards: Total Produced, Total Rejected, Completion Rate, Total Job Cards.
2. Five tabs:
   - **Daily Production** — every job card with Date, Job Card No, Prod No, Order No, Product,
     Supervisor, Shift, Planned/Produced/Rejected qty, Status.
   - **Material Consumption** — per completed/running job card, per BOM raw material: Planned
     Qty, Used Qty, Variance, Cost (₹); shows a running "Total Cost".
   - **FG Inventory** — finished-good products with SKU, Unit, Stock Qty, and an In Stock/Out of
     Stock badge.
   - **Rejection Report** — Produced vs Rejected qty and a computed Rejection % per job card;
     rejection percentages above 5% are highlighted in bold red.
   - **Raw Material Stock** — raw-material products with SKU, Unit, Stock Qty, Available/Out of
     Stock badge.

## Production List (alternate orders view)

**Where:** Production Planning → Production List (`/production-planning/production-list`). Page
heading: "Production List"; subtitle: "Manage and track all production orders." Auto-refreshes
every 5 seconds. Pending (Pending/In Progress) and History (Completed) tabs, columns: Prod No,
Order No, Party Name, Product, Planned Qty, Supervisor, Shift, Start Date, Priority, Status. This
is view-only — no actions are available on this particular page.

## Note on production.md vs actual code

The backend's `production.md` describes a conceptual flow: Order Received → BOM Calculation →
Inventory Check → **Indent Creation** → Production Planning → Machine/Supervisor Assignment →
Production Start → Raw Material Consumption → FG Production → Quality Testing → Tally Entry → FG
Inventory → Reports. The actual shipped frontend/backend code matches this at a high level, with
one notable gap: the "Indent Creation" step, as wired into the Full Kitting page's **Raise
Purchase Indent** button, only shows a toast message — it does not call a real
Purchase/Indent-creation API in this flow (a separate manual "Create Indent" link exists that
routes to `/purchase/indent`, presumably the actual Purchase module, but that is a different
module's own page and out of scope here).
