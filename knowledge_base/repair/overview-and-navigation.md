---
title: Repair Module Overview and Navigation
module: repair
tags: [repair, maintenancepro, repair-system, navigation, overview]
---

# Repair Module Overview and Navigation

The codebase currently exposes two repair-related areas, and they should not be confused:

1. **Maintenance Pro > Repair** (`/maintenancepro/repair-tasks`) is the visible sidebar item named "Repair". It works on Maintenance Pro work orders whose activity type is `REPAIR`.
2. **Maintenance Pro > Repair subpages** (`/maintenancepro/repair/...`) are RBIndent / outhouse repair-system pages. Some of these are visible in the Maintenance Pro sidebar, and some exist as direct routes only.

## Visible Maintenance Pro repair navigation

Under **Maintenance Pro**, the normal sidebar includes:

| Sidebar label | Path | What it does |
| --- | --- | --- |
| Repair | `/maintenancepro/repair-tasks` | Create, process, and review repair work orders from the Schedule Maintenance & Jobs system |
| Part and Vendor | `/maintenancepro/repair/part-and-vendor` | Search/export repair history grouped by replaced parts and vendors |
| AMC | `/maintenancepro/repair/amc` | Cost analytics for machine repairs and vendor spend |

## Direct repair-system routes

These pages exist in the app and use real `/repair-system/*` APIs, but they are not listed in the main sidebar:

| Page | Path | Purpose |
| --- | --- | --- |
| Machine Dispatch | `/maintenancepro/repair/sentmachine` | Send an outhouse-repair machine to an external service center |
| Store In Verification | `/maintenancepro/repair/storein` | Receive the repaired machine, inspect it, and log the vendor bill |
| Vendor Settlement | `/maintenancepro/repair/payment` | Match the bill and complete final vendor payment |
| Daily Activity Report | `/maintenancepro/repair/dailyreport` | Daily report of repair tasks, technician activity, and machine status |
| Calendar | `/maintenancepro/repair/calendar` | Calendar-style view with repair/indent/maintenance activity examples |

## Important implementation note

The frontend API client and backend expose a larger RBIndent workflow: indent creation, approval as Inhouse/Outhouse, technician assignment, work tracking, inspection, outhouse vendor selection, offer entry, rate approval, dispatch, store-in, and payment. In the current UI, only the last three outhouse operational pages (Dispatch, Store-In, Payment) plus reporting pages were found as actual screens. Do not tell users to open missing screens for indent creation, approval, technician assignment, work tracking, inspection, vendor selection, offer entry, or rate approval unless those screens are added later.

