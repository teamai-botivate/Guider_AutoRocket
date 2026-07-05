---
title: Registering and Managing Assets
module: asset_management
tags: [asset-management, add-asset, registration, assignment, export, qr-code]
---

# Registering and Managing Assets

This covers the **All Assets** list page (route: `/asset-management/assets`), where you register new assets and browse/search existing ones.

## Getting to the list

From the Asset Management dashboard, click **View All Assets**, or navigate directly to All Assets. The breadcrumb at the top reads "Asset Management > All Assets".

## Registering a new asset

1. On the All Assets page, click **Add Asset** (top right, blue button).
2. In the **Add Asset** dialog ("Create a new asset record with assignment, warranty, and maintenance details"), fill in the fields:
   - **Product name*** — required. This is a dropdown populated from your Store/Inventory products (only items marked as store-type items, or with a SKU starting `ST-`, appear here). Selecting a product auto-fills its SKU if available.
   - **Category** — one of: IT, Electronics, Furniture, Machinery, Tools, Vehicle.
   - **Brand**, **Model**, **Serial number**, **SKU** — free text.
   - **Date** field (defaults to today) — the asset's acquisition/asset date.
   - **Cost** — purchase cost (numeric). This also becomes the initial asset value.
   - **Quantity** — defaults to 1.
   - **Location** — free text (e.g. "Warehouse A", "IT Server Room").
   - **Department** — free text (e.g. IT, Admin, Production, Finance, HR).
   - **Assigned to** — the person the asset is assigned to.
   - **Responsible person** — a separate accountable person (may differ from "Assigned to").
   - **Warranty** dropdown — "No Warranty" or "Warranty Available". If "Warranty Available" is selected, a warranty end date field becomes enabled.
   - **Maintenance** dropdown — "No Maintenance" or "Maintenance Required". If "Maintenance Required" is selected, a **Priority** dropdown becomes enabled (Low / Medium / High).
3. Click **Add Asset** in the dialog footer to save (or **Cancel** to discard).
4. The new asset appears at the top of the list immediately with status "Active".

Note: when maintenance is marked required, the asset is tagged internally with maintenance type "Preventive" by default; the specific maintenance schedule/frequency and next-service date are not set from this dialog and default to blank — they show up once maintenance activity exists for the asset (see the Maintenance & Repair History doc).

## Browsing, filtering, and searching

1. Use the **status tabs** (All, Active, Inactive, Under Repair) near the top to filter by status; each tab shows a live count.
2. Use the **search box** ("Search name, SN, brand, assigned to…") to filter by asset name, serial number, brand, assignee, or department.
3. Use the **Category** dropdown to filter to a single category, or **Department** dropdown to filter to a single department.
4. Click **Clear filters** (appears once any filter/search is active) to reset search, category, and department filters at once.
5. On desktop, assets display as a sortable-looking table with columns: Asset, SN, Category, Department, Assigned To, Location, Value, Warranty, Maintenance, Status. The table footer shows the count of assets currently shown and their combined total value.
6. On mobile/narrow screens, assets display as cards showing the same key details (department, location, value, assigned to, asset date, and next service date if maintenance is due).
7. Click **Details** (on a card) or the chevron arrow (in a table row) to open that asset's full detail page.

## Exporting and QR codes

1. Click **Export** (top right) to download the currently filtered asset list as a CSV file (named `assets_<date>.csv`), including SN, name, category, type, brand, model, serial number, department, assigned to, location, status, value, warranty end date, and maintenance flag.
2. Click **QR PDF** (top right) to generate a printable PDF of QR codes for every asset currently shown in the filtered list. Each QR code encodes the asset's serial number (SN) and the printout shows the SN, asset name, category, department, and status underneath each code. This opens your browser's print dialog automatically.

## Notes / things not fully wired in the UI

- The asset detail page has a QR icon and a pencil (edit) icon next to the status badge, but as of this writing they are not connected to any action — there is no in-app "Edit Asset" screen yet; asset registration only happens through the Add Asset dialog described above.
