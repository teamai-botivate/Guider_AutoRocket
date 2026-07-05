---
title: Creating and Managing Maintenance Plans (Assign Task)
module: maintenance
tags: [maintenance, maintenance-plans, assign-task, scheduling, recurring-tasks, bulk-import]
---

A **Maintenance Plan** is a recurring (or one-time) schedule of work against a machine, assigned to a technician. Once created, the system automatically generates individual **Work Orders / Tasks** from the plan (e.g., a DAILY plan generates a rolling 7-day window of tasks; other frequencies generate one task per due date).

## Creating a plan via "Assign Task" (recommended, most detailed form)

1. Go to **Maintenance Pro > Schedule Maintenance & Jobs** (the "Tasks" list, `/maintenancepro/unique_task`) and click **Add Task**, or navigate directly to `/maintenancepro/assign_task`. The page is titled **Assign Maintenance Task** ("Create recurring maintenance plans for your machines").
2. Fill in **Task Type** (activity type, e.g., Inspection, Repair, Cleaning, etc.) and note **Requested By** is auto-filled read-only from your profile.
3. Choose **Assigned To** (technician) and **Machine Name** from the dropdowns.
4. Optionally choose a **Part Name** (only enabled once a machine is selected — options come from that machine's recorded parts) and, for non-repair tasks, whether **Temperature** monitoring applies.
5. Enter a **Work Description** (labeled "Issue Details" if Task Type is Repair) describing what to do.
6. Optionally attach a **Task Document** (PDF or image, max 10 MB) — labeled "Machine/Damage area" for Repair tasks.
7. If Task Type is **Repair**, the plan is automatically forced to a one-time schedule: you'll be asked for an **Expected Completion Date** only, and submitting routes you to `/maintenancepro/repair-tasks` after creation.
8. For non-repair tasks, choose a **Frequency** (Daily, Weekly, Fortnightly, Monthly, Quarterly, Half-Yearly, Yearly, One Time, Running Hours, Meter Based). If Frequency is "One Time" you set an Expected Completion Date/Time instead of a start date; otherwise set **Task Start Date** and optional **Task Time**. A schedule summary banner confirms what will be created.
9. Toggle **Require Attachment** if the assignee must upload a photo/file when they mark the task complete.
10. Click **Assign Task** to submit. On success you'll see "Maintenance plan assigned successfully!" and the form resets. Click **View All Tasks** (top right) at any time to jump to the task list.

## Creating/editing a plan from the Plans page

1. Go to **Maintenance Pro > Maintenance Plans** (`/maintenancepro/plans`), subtitled "Strategic Asset Scheduling". This page shows stat tiles (Total Plans, Active, Paused, Drafts) and a card grid of existing plans with search and Frequency/Status filters.
2. Click **New Plan** to open the "Establish New Schedule" form (or click a plan's edit icon to "Modify Strategic Plan"), fill in Machine Asset, Technician, Plan Title, Frequency, Start Date, and Priority Level, then click **Initialize Plan** (or **Commit Changes** when editing).
3. On each plan card you can: click the edit icon to modify it, click the pause icon to **Suspend Schedule** (status becomes Paused) or the play icon to **Resume Schedule**, and click the archive icon to **Archive Plan** (asks to confirm: "Permanently archive this strategic plan?").

## Bulk-importing plans from Excel

1. From the task list (`/maintenancepro/unique_task`), click **Import from Excel**.
2. Download the sample template if needed (columns: Title, Description, Machine, Assignee, Frequency, StartDate, AssetCode, ActivityType, GivenBy) — Machine and Assignee values must exactly match existing machine names/asset codes and user names.
3. Upload your filled `.xlsx`/`.xls`/`.csv` file. The system parses and validates each row (flagging missing fields, unknown machines, or unknown assignees), shows a preview of tasks to be created, and lets you select which rows to import before confirming.

## How scheduling behaves behind the scenes

- **Daily** plans generate the next 6 days of tasks on creation, then a rolling 7-day window is topped up automatically every day (skipping holidays).
- Other frequencies (Weekly, Fortnightly, Monthly, Quarterly, Half-Yearly, Yearly) create just one task for the next due date at a time.
- **One-Time** plans create a single task with the same start and end date.
- If the primary assignee is on leave/holiday for a due date, the task is automatically reassigned to the **backup user** if one is set on the plan; if both are unavailable, the system falls back to another active user in the same department with the fewest pending tasks.
- Editing a plan's **description** updates the instructions shown on upcoming (not-yet-generated) tasks.
