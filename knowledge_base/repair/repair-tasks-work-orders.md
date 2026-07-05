---
title: Repair Tasks Work Orders
module: repair
tags: [repair, repair-tasks, work-orders, maintenancepro, machine-repair]
---

# Repair Tasks Work Orders

Use **Maintenance Pro > Repair** (`/maintenancepro/repair-tasks`) to manage repair-type work orders from the Schedule Maintenance & Jobs system. This page is separate from the RBIndent / outhouse-repair flow used by the `/maintenancepro/repair/*` pages.

## Viewing repair tasks

1. Open **Maintenance Pro > Repair**. The page heading is **Repair Tasks**.
2. Use the **All Tasks / My Tasks** toggle to switch between all repair work orders and only tasks assigned to you.
3. Use **Active Tasks** and **History** tabs:
   - Active Tasks shows repair work orders still in progress/pending.
   - History shows completed repair work orders.
4. Use the search box ("Search by machine, task, or person...") and date range fields to filter.
5. Table columns include Action, ID, Machine, Activity Type, Task, Requested By, Assigned To, Vendor, Bill Amt, Date, and Status.
6. Use **Refresh** to reload and **Export** to download a CSV of the current list.

## Creating a new repair task

1. Click **+ New Repair Task**.
2. The **New Repair Task** dialog creates a one-time maintenance plan with Task Type fixed to **Repair**.
3. Fill in:
   - **Assigned To** - technician/user responsible for the repair.
   - **Machine Name** - selected from registered machines.
   - **Part Name** - optional; enabled after selecting a machine.
   - **Issue Details** - what is wrong or what needs repair.
   - **Machine/Damage area** - optional PDF/image upload, max 10 MB.
   - **Expected Completion Date** - required.
   - **Require Attachment** - if enabled, completion requires a file.
4. Click **Assign Repair Task**. On success the UI shows "Repair task assigned successfully!".

## Processing a repair task

1. Click the row action to open **Process Repair** for a work order.
2. Choose a status:
   - **In Progress** - captures only remarks.
   - **Completed** - opens the full completion form.
   - **Cancel** - cancels the repair work order.
3. When marking Completed, fill relevant fields:
   - **Type of Work** - In House or Out Source.
   - **Part Replaced** - selected from the machine's parts.
   - **Warranty & Guarantee** - optional checkbox that reveals From/To dates.
   - **Vendor Name** - required only for Out Source; populated from SERVICE vendors.
   - **Bill Amount**
   - **Work Photo** upload
   - **Bill Copy** upload
   - **Remarks**
4. If the needed service vendor is missing, use **+ Add Vendor** inside the modal. It opens an **Add Service Vendor** form with Vendor Name, Nature of Business, Email, Mobile Number, Contact Person, GST Number, TDS Applied, State, and Address.
5. Click **Save Changes**. The success toast is "Repair processed successfully".

## Viewing details and statuses

The detail modal **Repair Task Details** shows Machine & Task, People & Dates, any Completion Rejected notice, Repair Process details, and Process History.

Status badges render these values:

| Stored value | Display |
| --- | --- |
| `in_progress` / `IN_PROGRESS` | In Progress |
| `completed` / `COMPLETED` | Completed |
| `COMPLETED_LATE` | Completed Late |
| `cancelled` / `CANCELLED` | Cancelled |
| `PENDING_APPROVAL` | Pending Approval |
| `COMPLETION_REJECTED` | Rejected |
| Other/blank | Pending |

