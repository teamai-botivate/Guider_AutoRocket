---
title: Recording Actual Production (Stock and Inventory Update)
module: production_planning
tags: [actual-production, stock-update, inventory, fg-inventory, raw-material]
---

# Recording Actual Production

This is the step that turns planned quantities into real inventory movement: it increases
Finished Goods stock and deducts Raw Material stock, and it automatically kicks off Quality
Control.

## Where

**Production Planning → Actual Production** (`/production-planning/actual-production`). Page
heading: "Actual Production"; subtitle: "Record actual produced quantity and machine working
hours for planned job cards. FG inventory and raw material stock update on save."

## 1. Review job cards awaiting entry

1. Stats cards: **Total**, **Pending Entry**, **Recorded**.
2. Two tabs: **Pending** (`actualRecorded` is false) and **History** (`actualRecorded` is true).
   Table columns: Action, Job Card No, Prod No, Product, Supervisor, Shift, Date, Planned Qty,
   Produced Qty, Actual Qty, Machine Hrs, Status, Planned At/Delay.
3. In Pending, click **Enter** on a row; in History, click **View** (read-only).

## 2. Enter actual production for a job card

1. The "Actual Production — <Job Card No>" dialog shows:
   - **Order Details** block: Job Card No, Production No, Order No, Product, Party Name, Date,
     Supervisor, Shift.
   - **Production Summary**: Planned Qty vs Produced Qty.
   - **BOM — Raw Material Usage** table (if a BOM exists for the product): Raw Material, Unit,
     Rate (₹), Required Qty (BOM qty × produced qty), and an editable **Actual Qty** field per raw
     material (defaults to the required quantity but can be adjusted for over/under-consumption),
     with a running Total Amount per row and a **Total Material Cost** footer.
2. Fill in:
   - **Actual Qty Produced** — number of finished units actually produced (defaults to the
     planned/produced qty). Helper text: "FG inventory will increase by this quantity. Raw
     material will be deducted per BOM."
   - **Machine Working Hours** — decimal hours the machine ran (helper text: "Total hours the
     machine ran to produce this batch.").
   - **Remarks** — optional notes.
   - **Financial Analysis** (if any BOM rate is set) — enter **Selling Amount (₹)** and **Extra
     Amount (₹)**; the dialog live-computes Total Material Cost, Total Cost (material + extra),
     Profit/Loss, and Profit/Loss %.
3. Click **Save & Update Inventory**.

## What happens on save (mechanism)

1. The job card is updated with `actualQty`, `machineHours`, `remarks`, and the edited
   `materialChecks` (actual raw-material quantities used) — this marks the job card
   `actualRecorded = true` and status `Completed`, and also marks the linked sales order
   `COMPLETED`.
2. A stock-update call runs (non-blocking, so it won't stop the rest of the flow even if it
   fails): for each raw material in the BOM, its stock quantity is decreased by the required
   amount (floored at 0); the finished good's stock quantity is increased by the actual produced
   quantity.
3. A **Lab Test** record is auto-created with result `Pending` for the same job card, to trigger
   the QC step (silently skipped if one already exists for this job card).
4. A "Production Recorded — Next Steps" confirmation dialog appears summarizing: (1) Actual
   Production Recorded — FG inventory & raw material stock updated; (2) Lab Test Created — QC
   Pending; (3) Tally Entry Ready. Buttons: **Go to Lab Test** (routes to the Lab Test page),
   **Go to Tally** (routes to the Tally page), or **Stay on this page**.

## Notes

- If viewing a History (already-recorded) row, all fields are read-only ("View Production").
- Stock updates match raw materials and finished goods by product name (case-insensitive) against
  the product master — if a name doesn't match any product, that line is silently skipped.
