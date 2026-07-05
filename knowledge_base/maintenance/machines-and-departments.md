---
title: Setting Up Departments and Machines (Maintenance Pro)
module: maintenance
tags: [maintenance, machines, departments, asset-setup, machine-parts]
---

Maintenance Pro tracks your factory/plant equipment as **Machines**, grouped under **Departments**. Set these up before creating maintenance plans, since every machine must belong to a department, and every maintenance plan needs a machine.

## Viewing and finding machines

1. Go to **Maintenance Pro > Machines** (`/maintenancepro/machines`). This shows the "Equipment Master List" — a table (or cards on mobile) of every machine with columns for Machine Name, Department, Part Names, Status, Task Assignment, Repair Count, and a computed Health percentage.
2. Use the search box ("Search machines, parts, assigned users...") or the **All Departments** / **All Status** dropdown filters to narrow the list. Status options are Operational, Under Maintenance, Breakdown, Idle, and Decommissioned.
3. Click the refresh icon to reload the list, or use the page-number controls at the bottom to move between pages (10 machines per page).
4. In the Actions column, click the document icon to open a machine's **View Details** page, or the wrench icon to go to that machine's **Parts & Work Orders** page.

## Adding a new machine

1. From the Machines list, click **Add Machine** (top right). This opens the "Add New Machine" form.
2. Fill in **Machine Information**: Machine Name, Serial Number, Model, Manufacturer, and **Department** (a dropdown populated from your tenant's departments — must be selected), plus optional Location.
3. Fill in **Purchase & Maintenance Details**: Purchase Date, Purchase Price, Vendor, Warranty Expiration, tick any applicable **Maintenance Schedule** checkboxes (Monthly/Quarterly/Bi-annual/Annual), optionally list up to 5 **Maintenance Parts**, and set an **Initial Maintenance Date**.
4. Optionally upload a **Machine Image** (PNG/JPG up to 5MB), a **User Manual**, and a **Specifications Sheet** (PDF/DOC/XLS up to 10MB) in the Documentation section.
5. Optionally add free-form **Additional Specifications** (name/value pairs) and **Notes**.
6. Click **Save Machine** to create it, or **Cancel** to discard and return to the machines list. On success you'll see "Machine successfully added to inventory" and be returned to the Machines list.

## Machine detail page and parts

1. Clicking a machine's name/detail icon opens its detail page with tabs: **Overview**, **Maintenance**, **Repair History**, **Parts**, **Purchases**, **Documents**, and **Analytics**.
2. To manage a machine's components, go to its **Parts & Work Orders** page (`/maintenancepro/machines/[id]/parts`), titled "Machine Components & Parts". Use the search box ("Search parts by name or number...") to find existing parts.
3. Click the add-part control to open the part form and record a part's name, part number, and description; parts you add here are what later shows up as selectable "Part Name" options when assigning maintenance tasks against that machine.
4. Parts can be edited or deleted (with a confirmation prompt: "Are you sure you want to delete this part?").

## Departments

Departments (e.g., "Mechanical") are a simple tenant-wide master list — each has a Name, optional Code, optional Description, and Active/Inactive status. They are managed via the `/api/maintenance/departments` backend endpoints (create/update/soft-delete) and consumed as a dropdown wherever a department must be selected (Add Machine form, Assign Task form). There isn't a separate department-management screen identified among the Maintenance Pro pages — departments are populated/selected inline from these dropdowns; ask your admin if you need a new department added if it's missing from the list.

## Notes on machine status and health

- Status badges (Operational, Under Maintenance, Breakdown, Idle, Decommissioned) drive the color-coded dot shown in lists.
- The "Health" percentage shown per machine is calculated in the frontend from the machine's status and its breakdown/repair count — it is a display heuristic, not a stored backend field.
