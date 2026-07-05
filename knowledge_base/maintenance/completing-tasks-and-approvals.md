---
title: Completing Maintenance Tasks and Admin Approval
module: maintenance
tags: [maintenance, tasks, work-orders, task-completion, approval, breakdown]
---

Day-to-day maintenance work is tracked as individual **Work Orders/Tasks** generated from Maintenance Plans. Technicians report progress on their assigned tasks; completions go through an admin approval step before being final.

## Viewing and reporting on your tasks

1. Go to **Maintenance Pro > Schedule Maintenance & Jobs** (`/maintenancepro/unique_task`). Admins see all tasks across the team; regular users see only tasks assigned to them (the page subtitle states which view you're in).
2. Use the stat tiles at the top (Total Tasks, Pending, Completed, Overdue, History) as quick filters — click a tile to filter the table to that status.
3. Use the search box ("Search by task name, machine, asset code, assignee...") and the Status / Frequency dropdown filters, plus the **Date** toggle for a Due-From/Due-To range filter.
4. In the Actions column for a task: click the eye icon to **View details** (shows machine, assignee, given by, due/scheduled/started/completed dates, activity type, replacements, status history, etc.), or click the edit/pencil icon to **Report update** on the task.
   - The report button is disabled once a task is Completed ("Task completed — cannot update") or already Awaiting Approval ("Awaiting admin approval — cannot update").

## Reporting a task update (the "Report Update" form)

1. Click the edit/pencil icon on a task row to open the **Report Update** modal.
2. Choose a **Task Status**:
   - **Complete — Submit for admin approval**
   - **Task shift for repair**
   - **Breakdown**
3. If marking **Complete**, answer **Is Anything Replaced?** (Yes/No). If Yes, fill in one or more **Replacement Details** rows (Item Name, Qty, Cost in ₹) — use **Add More** to add rows, or the trash icon to remove one (at least one row must remain).
4. Add optional **Notes** describing observations/findings/remarks.
5. Click **Submit Report**. For a Complete report you'll see the toast "Submitted for admin approval — awaiting review" — the task status becomes **Awaiting Approval** and is locked from further edits until an admin reviews it. Other status updates show "Task updated successfully."
6. Note: if the plan has "Require Attachment" enabled, a completion image is mandatory to mark the task Completed (enforced by the backend).

## Admin approval of completed tasks

1. Admins go to the **Admin Approval** screen (Pending Approval feature, under Maintenance Pro) which has two tabs: **Pending Approvals** and **History**, plus three summary cards (Awaiting Approval, Approved, Rejected) that also act as quick filters.
2. In the Pending tab, each row shows the task/plan, machine, who submitted it, and when it was completed. Click the eye icon to **View details**, or the review icon to open the **Review Work Order** modal.
3. In the Review modal, you can read the technician's submission note and completion time, optionally add an **Admin note**, then click **Approve** or **Reject**.
   - Approving shows "Work order approved successfully" and moves the task to Completed history.
   - Rejecting shows "Work order rejected" and sets status to **Completion Rejected**, sending it back for rework.
4. The **History** tab lists previously reviewed tasks with Submitted By, Completed At, Reviewed By, Reviewed At, and the Approved/Rejected decision.

## Breakdown reporting

1. Go to the **Breakdown Log** page (`/maintenancepro/breakdown-log`) to log unplanned equipment failures separately from scheduled maintenance.
2. Click to open the breakdown form and fill in: Machine, Failure Type (Electrical, Mechanical, Software, Operator Error, Hydraulic, Pneumatic, Other), Description, Severity (Critical / Major / Minor), Estimated Downtime (hours), who to assign it to, and Remarks.
3. Existing breakdown reports can be filtered by machine and status (Open, In Progress, Resolved, Closed) and updated as work progresses or marked Resolved.

## Daily Machine Log

For plants tracking daily running metrics independent of maintenance tasks, use **Daily Machine Log** (`/maintenancepro/daily-machine-log`) to record, per machine per day: start/end meter readings, Runtime Hours (0–24), Temperature (0–500°C), Load (0–100%), Operator Name, and Remarks. Submitting shows "Daily log submitted successfully!"
