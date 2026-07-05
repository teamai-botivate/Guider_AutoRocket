---
title: Production Planning — Overview and Navigation
module: production_planning
tags: [production-planning, navigation, overview, workflow]
---

# Production Planning — Overview

Production Planning covers the manufacturing lifecycle from a sales order that needs to be
manufactured, through raw material availability checks, job card creation, actual production
recording, quality control (lab test), and production costing (Tally entry).

## Where to find it

All pages live under **Production Planning** in the left navigation (route group
`(dashboard)/(system)/production-planning`):

1. **Dashboard** (`/production-planning/dashboard`) — KPI cards (Total Orders, Job Cards, Total
   Produced, Planned Qty, Completion Rate, QC Passed), charts (Production Status, Top 5 Products,
   Top 5 Parties, Material Cost by Product, QC Results pie), and a tabbed report section (Daily
   Production / Material Consumption / QC Records). Has a period filter: **Today / This Week /
   This Month / All Time**.
2. **BOM List** (`/production-planning/bom-list`) — "Bill of Materials (BOM)" — define/manage
   which raw materials go into each finished good.
3. **Production** (`/production-planning/orders`) — read-only list of production orders pulled
   from Order-to-Dispatch (only orders with `availability = PRODUCTION_PLANNING`).
4. **Full Kitting** (`/production-planning/pending-checks`) — "Kitting Verification" — checks raw
   material availability against BOM for each pending order and lets you start production.
5. **Job Cards** (`/production-planning/job-cards`) — plan/update machine-level job cards created
   from Full Kitting.
6. **Actual Production** (`/production-planning/actual-production`) — record actual quantity
   produced and machine hours; this is what updates FG/raw-material stock.
7. **Quality Control (Lab Test)** (`/production-planning/lab-test-1`) — QC approval step for
   completed job cards, gates entry into Finished Goods inventory.
8. **Tally Entry** (`/production-planning/tally`) — "Tally Entry — Production Costing" — cost
   ledger of completed job cards (material cost, extra cost, selling amount, profit/loss).
9. **Production List** (`/production-planning/production-list`) — another production-orders view
   (auto-refreshes every 5 seconds) with Pending/History tabs.
10. **Reports** (`/production-planning/reports`) — "Reports & Analytics": Daily Production,
    Material Consumption, FG Inventory, Rejection Report, Raw Material Stock tabs.

## End-to-end flow (as implemented in code)

```
Order (from Order-to-Dispatch, availability = PRODUCTION_PLANNING)
   ↓
Full Kitting page — BOM-based raw material availability check ("Kit Status": Ready / Partial /
Shortage / No BOM Defined)
   ↓
"Start Production" → creates a Job Card (status "Running") and marks the order IN_PROGRESS
   ↓
Job Cards page — supervisor/shift/date planning, BOM raw-material sufficiency re-check
   ↓
Actual Production page — record actual produced qty + machine hours → updates FG stock (+) and
raw material stock (-) via the stock-update API, and auto-creates a Lab Test record (status
"Pending")
   ↓
Quality Control (Lab Test) page — Quality Auditor approves ("Pass" → Finished Goods Inventory) or
rejects ("Fail" → sent to Rework, per the on-screen message)
   ↓
Tally Entry page — production costing ledger becomes available for completed job cards
   ↓
Reports / Dashboard — aggregated views
```

Note: the "Raise Purchase Indent" button on the Full Kitting detail dialog only shows a success
toast naming the shortage items — it does not appear to create a real Purchase/Indent record in
this code path (no API call to the purchase/indent module was found tied to that button).

## Key terminology used on screen

- **Prod No / Production No** — displayed as `PRD-<order PO number>`, derived from the linked
  Order-to-Dispatch order.
- **Job Card No** — auto-generated as `JC-0001`, `JC-0002`, etc.
- **Kit Status** — Ready / Partial / Shortage / No BOM Defined (Full Kitting page only).
- **FG** — Finished Good; **RM** — Raw Material.
