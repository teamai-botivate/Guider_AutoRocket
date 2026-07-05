---
title: Repair Reports, AMC, Calendar, and Part/Vendor History
module: repair
tags: [repair, reports, amc, calendar, part-vendor, daily-report]
---

# Repair Reports, AMC, Calendar, and Part/Vendor History

These screens are mostly reporting/analysis views for repair work and repair costs.

## Part and Vendor

Path: `/maintenancepro/repair/part-and-vendor`

This page reads from `/maintenance/parts-and-vendors` and lists completed repair records with vendor and replaced-part information. Use it to search repair history, filter by vendor or part, and export/audit repair records. The API also exposes unique-vendor and unique-part endpoints for the filter dropdowns, plus delete support for a repair record by task ID.

This page is part of Maintenance Pro sidebar navigation.

## AMC

Path: `/maintenancepro/repair/amc`

The AMC page reads `/repair-system/amc` and has two tabs:

1. **Machine AMC / Machine Repairs** - cost and status view by machine.
2. **Vendor AMC / Vendor Analysis** - aggregated expenditure per vendor.

Machine Repairs shows:

- All-Time Total repair cost.
- Annual Cost for the selected year.
- Cost per machine table.
- Machine distribution pie chart.
- Year buttons for 2024, 2025, and 2026.
- Status filters: All, Pending, Completed.
- Search by machine name.
- Repair table columns: Machine Name, Status, Source, Bill Amount.

Vendor Analysis shows:

- Total Vendor Expense.
- Unique Vendors count.
- Costs per Vendor table.
- Vendor Distribution pie chart.

This page is part of Maintenance Pro sidebar navigation.

## Daily Activity Report

Path: `/maintenancepro/repair/dailyreport`

The Daily Activity Report reads `/repair-system/daily-report` and summarizes repair activity for the day.

1. Header: **Daily Activity Report**, with the current date.
2. Admin users see **Master View** and can filter by technician.
3. Statistic cards show Total Tasks Today, Completed, In Progress, and Pending.
4. **Asset Status Summary** shows Operational, Maintenance, and Down machine counts.
5. **Live Activity Log** lists repair/indent/work updates with title, description, status, machine ID, assigned technician, and created time.
6. **Performance Metrics** shows Resolvability Rate and Service Coverage.

This route exists, but it is not listed in the main Maintenance Pro sidebar.

## Repair Calendar

Path: `/maintenancepro/repair/calendar`

The Repair Calendar page has **day**, **week**, and **month** views. It displays calendar activity types for indent, repair, and maintenance, with status icons for completed, pending, in-progress, and approved.

Important: the current component generates mock tasks client-side for the selected month. It is useful as a UI calendar view, but do not treat it as a live repair-system calendar unless the page is later wired to real backend data.

This route exists, but it is not listed in the main Maintenance Pro sidebar.

