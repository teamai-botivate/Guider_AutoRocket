---
title: Full Kitting Check and Starting Production (Job Card Creation)
module: production_planning
tags: [kitting, material-check, job-card, start-production, indent]
---

# Full Kitting Check and Starting Production

Before a job card exists, every production-eligible order goes through a raw-material
availability check called "Full Kitting" / "Kitting Verification". This is where a job card is
actually born.

## Where

**Production Planning → Full Kitting** (`/production-planning/pending-checks`). Page heading:
"Full Kitting"; card title "Kitting Verification".

## 1. Review the kitting list

1. The page shows two tabs: **Pending** (orders not yet completed) and **History** (orders whose
   linked job cards are all completed).
2. KPI cards at the top: **Ready to Produce**, **Partial Stock**, **Material Shortage**, **No BOM
   Defined** — counts of orders in each kit status.
3. Each row shows: Prod No, Order No, Party, Product, Planned Qty, To Produce (= order qty minus
   FG already in stock), Due Date, **Kit Status** (Ready / Partial / Shortage / No BOM Defined),
   Production Status, and a Planned At/Delay indicator.
4. Use **Group By: All / Party / Product** (top right buttons) to collapse rows into groups, or
   the search box to filter by order/product text. **Refresh Data** reloads BOMs, orders, and job
   cards.

## 2. Open the kitting detail for an order

1. Click the eye icon on a row to open "Kitting Detail — <Prod No> (<Product>)".
2. The dialog shows Order No, Party, Planned Qty, FG Available, and an editable **Production Qty
   to Manufacture** field (defaults to the shortfall between planned qty and FG stock on hand).
3. Below that, a **Financial Analysis** block (hidden if no BOM exists) lets you enter **Selling
   Amount (₹)** and **Extra Amount (₹)** (overhead/labour) and shows live Material Cost, Extra
   Amount, Total Cost, Profit/Loss, and Profit/Loss % — all recalculated as you change the
   production quantity.
4. A raw-material table lists, per BOM line: Raw Material, Unit, Rate, Required Qty, Available
   Qty, Shortage, Total Price, and a Status badge (OK / Partial / Shortage). Rows with a shortage
   show a **Create Indent** link (routes to `/purchase/indent`).

## 3a. If material is short — raise an indent

1. If Kit Status is **Partial** or **Shortage** and the order isn't already in progress, click
   **Raise Purchase Indent**.
2. This shows a success toast listing the shorted materials and quantities (e.g. "Purchase Indent
   raised successfully for: Steel (Shortage: 12 kg)") and closes the dialog. This action does not
   call the Purchase/Indent backend from this screen — it is a notification only; use the Purchase
   module directly (or the Create Indent link) to actually raise a formal indent.

## 3b. If material is sufficient — start production

1. If Production Qty > 0 and the order is not already in progress, click **Start Production**.
2. This creates a new **Job Card** (auto-numbered `JC-000x`) with status "Running", copies over
   the production quantity, party, and material check snapshot (including any Selling/Extra
   amounts you entered), and marks the underlying order as **IN_PROGRESS**.
3. Success toast: "Production started for <Prod No>! Job card created." The dialog closes and the
   order now shows "Production In Progress" in future views.
4. If Production Qty is 0, the dialog shows: "Finished goods stock is sufficient for this order.
   Production is not required."

## Notes

- If no BOM exists for the product, the dialog shows "No Bill of Materials (BOM) has been defined
  for <product>" with a **Define BOM Now** button linking to the BOM List page — you must create
  a BOM before this order can be kitted or started.
