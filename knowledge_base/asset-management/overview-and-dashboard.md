---
title: Asset Management Overview & Dashboard
module: asset_management
tags: [asset-management, dashboard, overview, navigation]
---

# Asset Management Overview & Dashboard

The Asset Management module tracks, manages, and monitors all company assets (IT equipment, electronics, furniture, machinery, tools, vehicles) — including who they're assigned to, their financial value, warranty/AMC status, and maintenance/repair history.

## Where to find it

Navigate to **Asset Management** in the app (route: `/asset-management/dashboard`). This is the module's landing page.

## What the Dashboard shows

1. **Header** — title "Asset Management" with the subtitle "Track, manage and monitor all company assets", and a **View All Assets** button that takes you to the full asset list.
2. **Summary stat cards**:
   - **Total Assets** — count of all assets, with total purchase cost shown underneath.
   - **Active Assets** — count of assets with status "Active", with a utilization percentage.
   - **Maintenance Due** — count of assets flagged as needing maintenance, plus how many are currently "Under Repair".
   - **Total Value** — sum of all assets' current (depreciated) book value.
3. **Asset Status** panel — a breakdown bar per status (Active, Inactive, Under Repair, Maintenance Due) showing count out of total, plus an "Active Rate" percentage and an "Under Warranty" count.
4. **By Category** panel — bar breakdown of asset counts per category (IT, Electronics, Furniture, Machinery, Tools, Vehicle).
5. **By Department** panel — bar breakdown of asset counts per department (e.g. IT, Admin, Production, Finance, HR — departments are free text set per asset, not a fixed list).
6. **Recent Assets** — the 5 most recently added assets, each clickable to open its detail page. Shows name, serial number (SN), brand, department, current book value, and status.
7. **Alerts & Reminders** panel — three types of alerts, in this order:
   - Assets with maintenance required and a scheduled next-service date ("Service due <date>"), shown with priority badge.
   - Assets currently "Under Repair".
   - Assets that have warranty coverage, showing "Warranty till <date>".

## Steps to use the dashboard

1. Open **Asset Management** from the main navigation.
2. Review the four summary stat cards at the top for a quick health check of your asset fleet.
3. Check the **Asset Status**, **By Category**, and **By Department** panels to see how assets are distributed.
4. Scan the **Alerts & Reminders** panel on the right for assets needing attention (maintenance due, under repair, or warranty coverage ending).
5. Click **View All Assets** (top right) or **View All** (above the Recent Assets list) to go to the full asset list, or click any row under Recent Assets to jump straight to that asset's detail page.

## Notes

- All figures on the dashboard are computed live from the current asset list — there is no separate configuration step.
- "Total Value" reflects each asset's current depreciated value, not the original purchase cost.
