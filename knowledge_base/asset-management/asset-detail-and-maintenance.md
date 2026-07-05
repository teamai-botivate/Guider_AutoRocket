---
title: Asset Detail Page, Maintenance & Repair History
module: asset_management
tags: [asset-management, maintenance, repair-history, warranty, amc, depreciation]
---

# Asset Detail Page, Maintenance & Repair History

Opening any asset from the All Assets list or the Dashboard's Recent Assets takes you to its detail page (route: `/asset-management/asset/[id]`).

## Layout of the detail page

1. **Breadcrumb**: Asset Management > All Assets > <asset name>.
2. **Hero card** at the top — shows the asset's icon (colored by category), name, brand/model, status badge (Active / Inactive / Under Repair / Disposed), category badge, serial number, type, and a "Maintenance Due" badge if maintenance is required. Below that, four quick-glance tiles: Purchase Cost, Current Value, Department, Assigned To. A QR icon and a pencil (edit) icon sit next to the status badge, though neither currently opens a working action.
3. Six detail sections, in this order:

### Product Information
Serial No, SKU, Category, Type, Brand, Model, Mfg Date, Country of Origin.

### Asset & Financial Info
Asset Date, Invoice No, Purchase Cost, Quantity, Supplier, Payment Mode, Current Book Value, Depreciation Method.

### Location & Ownership
Location, Department, Assigned To, Responsible Person.

### Warranty & AMC
Warranty Available (Yes/No) and, if Yes, Warranty Valid Till date. AMC (Yes/No) and, if Yes, AMC Valid Till date.

### Maintenance
- **Total Maintenance** — a count of completed maintenance work orders linked to this asset.
- **Last Maintenance Date** — shown only if the maintenance count is greater than 0.
- **Maintenance Required** (Yes/No).
- If Yes: **Type** (e.g. Preventive, Breakdown), **Frequency** (e.g. Monthly, Quarterly, Yearly), **Next Service Date**, and **Priority** (Low/Medium/High, color-coded — red for High, amber for Medium, green for Low).

### Repair History
- **Total Repairs** — count of completed repair records linked to this asset.
- If repairs exist: **Last Repair Date**, **Last Repair Cost**, **Total Repair Cost** (sum across all repairs), **Parts Changed** (Yes/No), and if parts were changed, a list of **Parts Replaced** as tags.
- If no repairs exist: shows "No repair history".
- **Created By** — who registered the asset record.

## How maintenance and repair data get populated

This is important to understand: the Maintenance and Repair History sections are **not manually filled in** on the asset record. They are automatically computed by matching this asset's product name, serial number, or asset code (SN) against:

- Completed work orders in the **Maintenance Pro** module (matched to a machine record sharing the same name / asset code / serial number), which drive "Total Maintenance" and "Last Maintenance Date".
- Completed repair indents in the **Repair/SFMS** module (matched by machine name or serial number), which drive "Total Repairs", "Last Repair Date", "Last Repair Cost", "Total Repair Cost", and "Parts Replaced".

In practice, this means:

1. To see maintenance history appear on an asset, log and complete the corresponding maintenance work order in Maintenance Pro using the **same product/asset name or serial number** as the asset record.
2. To see repair history appear on an asset, complete the corresponding repair/inspection in the Repair module, again keyed on matching name/serial number.
3. There is no "Log Maintenance" or "Log Repair" button directly on the Asset Management screens — maintenance and repairs are recorded in their own modules and simply roll up here for visibility.

## Notes

- "Current Book Value" (asset value) reflects depreciation and can differ from the original "Purchase Cost" — the depreciation method (e.g. Straight Line, WDV) is recorded per asset but the depreciation calculation/schedule itself is not exposed as an interactive feature on this page.
- If an asset can't be found (e.g. bad link or deleted asset), the page shows "Asset not found" with a "← Back to Assets" link.
