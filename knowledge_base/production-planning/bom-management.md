---
title: Creating and Managing a Bill of Materials (BOM)
module: production_planning
tags: [bom, bill-of-materials, raw-material, finished-good]
---

# Creating and Managing a Bill of Materials (BOM)

A BOM defines which raw materials (and how much of each) are needed to make one unit of a
finished good. Every other step in Production Planning (kitting checks, job cards, actual
production, costing) reads from the BOM you define here.

## Where

**Production Planning → BOM List** (`/production-planning/bom-list`). Page heading: "Bill of
Materials (BOM)".

## 1. View existing BOMs

1. Open the BOM List page. Each row is one finished good ("FG Row"), showing: S.No, Finished
   Good (FG) name plus its computed **Total Cost/unit**, a badge showing the raw material count
   (e.g. "3 Materials"), Description, and Edit/Delete actions.
2. Click anywhere on a row to expand/collapse it and see the raw-material breakdown table: Raw
   Material, Unit, Qty / FG, Rate (₹), and line Total (₹), with a "Total Cost per FG Unit" summary
   row at the bottom.

## 2. Create a new BOM

1. Click **Create BOM** (top right).
2. In the dialog:
   - **Finished Good (FG)** — required dropdown, populated from products flagged as finished
     goods. Selecting one shows its SKU and Unit for reference.
   - **Description (Optional)** — free text field.
   - **Raw Materials** section — starts with one row:
     - **Raw Material** — required dropdown of raw-material products. Selecting one auto-fills
       Unit and Rate/Unit from that product's master data.
     - **Unit** — read-only, auto-filled from the selected raw material.
     - **Qty / FG unit** — required number (how much of this raw material is needed per 1 unit of
       the finished good), supports decimals (step 0.001).
     - **Rate / Unit (₹)** — auto-filled but editable.
     - Each row shows a live "Cost per FG unit" once material + qty are set.
   - Click **Add Material** to add more raw-material rows; the trash icon removes a row (disabled
     if it's the only row left).
3. Click **Save BOM**. You must select a Finished Good and have at least one raw material with a
   name filled in, or the form shows an error toast ("Please select a Finished Good" / "At least
   one raw material is required").
4. On success: toast "BOM created successfully" and the dialog closes.

## 3. Edit a BOM

1. Click the edit (pencil) icon on a BOM row.
2. The same dialog opens pre-filled with the existing FG, description, and raw material rows.
3. Make changes and click **Save BOM** — success toast is "BOM updated successfully".

## 4. Delete a BOM

1. Click the trash icon on a BOM row.
2. Confirm the browser dialog: "Are you sure you want to delete this BOM? All its items will be
   removed."
3. On success: toast "BOM deleted successfully".

## Notes / mechanism details

- BOM cost per unit is computed client-side as `sum(perUnitQty × perUnitRate)` across all raw
  material lines — this is the number shown as "Total Cost/unit" and used everywhere downstream
  (Full Kitting, Job Cards, Actual Production, Tally) as the material cost basis.
- If a finished good has no BOM defined, downstream screens (Full Kitting, Actual Production)
  show "No BOM Defined" / "No BOM configured" states and link back to this page (Full Kitting's
  detail dialog has a **Define BOM Now** button that routes here).
