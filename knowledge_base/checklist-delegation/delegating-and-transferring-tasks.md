---
title: Working Your Delegation Inbox and Transferring Tasks
module: checklist_delegation
tags: [delegation, transfer, assign, complete, skip, extend]
---

# Working Your Delegation Inbox and Transferring Tasks

The **Delegation** page (sidebar: **Checklist & Delegation → Delegation**) is your inbox for one-time tasks
and any tasks that have been transferred to you. It's also where you forward ("delegate") a task you've been
assigned to someone else.

## Viewing and filtering your tasks

1. Go to **Checklist & Delegation → Delegation**.
2. Admins can switch between **All Tasks** and **My Tasks**.
3. Switch between the **Pending** and **History** tabs.
4. Filter using the clickable stat cards: **Pending Tasks**, **Completed Tasks**, **Overdue Tasks**,
   **Transferred**.
5. Use the Frequency filter, the **Sort by** dropdown (Due Date, Priority, Received, Sender), or the search
   box ("Search tasks by title, sender, or ID…"). Click **Clear** to reset filters.
6. The table shows columns: Actions, #, Task, Extensions, From, Due Date, Status.
7. Status values you'll see: **Pending**, **In Progress**, **Approved**, **Completed**, **Skipped**,
   **Cancelled**, **Expired**, **Rejected**, **Awaiting Approval**.
8. Priority shows as **High**, **Medium**, or **Low**.

## Completing a task

1. Click **View Details** to review a task, or use the **In Process** control on the row to act directly.
2. Choose **Mark Complete** from the row control (or open it via the expanded row) to open **Mark Task
   Complete**.
3. Set **Status** to:
   - **Done** — optionally add **Remarks** ("Add any completion notes or remarks…"), then confirm with
     **Mark Complete**.
   - **Extend** — fill in a required **Extend Date** (must be tomorrow or later) and **Extend Reason**, then
     confirm with **Extend Task**.
4. Cancel at any point with **Cancel**.

Toast confirmations include "Completed: {task}", "Task extended: {task}", or their failure equivalents.

## Skipping a task

1. From the row control, choose the skip/"not done" option to open **Skip Task**.
2. Enter a required reason ("Reason for skipping (required)").
3. Confirm with **Skip Task** (or **Cancel**).

## Transferring ("delegating") a task to someone else

1. From the row control, choose the transfer option to open **Transfer Task**.
2. Pick a person under **Transfer to** (placeholder "Select a person…").
3. Enter a reason — labeled **"Reason (optional)"** for admins, or **"Reason (required for approval)"** for
   everyone else (non-admin transfers need admin sign-off).
4. Click **Transfer Task** (admin) or **Request Transfer** (non-admin) to confirm, or **Cancel**.

Non-admins see a notice: "Your request will be sent to an admin for approval before the task is transferred."
Once sent, the row shows an **Awaiting Approval** badge; toast confirms "Transfer request sent — awaiting
admin approval" or, once approved, "Transferred: {task}".

## Admin Reply

Admins can click **Admin Reply** on a row to open the **Admin Reply** dialog, write a message ("Write your
reply for this task…"), and click **Send Reply**. The reply then shows on the task as an "Admin Reply" chip
visible to the assignee.

## How Delegation differs from Assign Task and Checklist

- **Assign Task** creates a brand-new task and hands it to someone for the first time.
- **Delegation** is where you act on tasks already assigned to you (complete/skip/extend), and where you
  forward an existing task occurrence to someone else (transfer).
- **Checklist** is the equivalent action screen, but specifically for recurring tasks; **Delegation**'s task
  list is primarily one-time tasks (type `ONE_TIME_TASK`) plus any tasks that arrived via transfer
  (`TRANSFERRED_OCCURRENCE`).
