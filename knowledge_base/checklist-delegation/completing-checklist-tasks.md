---
title: Completing Recurring Checklist Tasks
module: checklist_delegation
tags: [checklist, complete-task, submit, transfer]
---

# Completing Recurring Checklist Tasks

Use the **Checklist** page for your day-to-day recurring tasks (anything with a Frequency other than
"One Time"). One-time tasks instead show up under **Delegation** (see
`delegating-and-transferring-tasks.md`).

## Steps

1. Go to **Checklist & Delegation → Checklist** in the sidebar.
2. If you're an admin, use the sub-tabs **All Tasks** / **My Tasks** to switch between everyone's tasks and
   just your own.
3. Use the **Pending** / **History** tabs (each shows a live count) to see tasks awaiting action versus
   already-completed tasks.
4. Optionally narrow the list with:
   - The search box ("Search by task, department, assignee...")
   - The Frequency filter dropdown ("All Frequencies", Daily, Weekly, Fortnightly, Monthly, Quarterly,
     Half Yearly, Yearly, Running Hours, Meter Based)
   - The clickable stat cards **Pending Tasks**, **Overdue Tasks**, **Transferred** (click a card to filter
     the table to that status)
5. For each task row, use the **Action** column dropdown to record the outcome:
   - **Done** — marks the task complete
   - **Not Done** (admin only) — marks it not completed
   - **Transfer** (admin only) — opens the **Transfer Task** dialog to reassign the task
   - Add any notes in the **Remarks** column next to it.
6. Click **Details** on a row to open the **Task Details** modal, which shows Department, Assigned To,
   Frequency, any required-attachment notice, delegation info (if the task was transferred to you), and a
   Notes section ("Your Notes" / "Admin Note").
7. When you're done marking rows, click **Submit All** to send your selections. Use **Reset** first if you
   want to discard unsaved changes.

### What happens after you submit

- If you (or an admin acting on their own task) mark something **Done**, and no approval is required, it
  completes immediately: toast "'{task}' completed successfully".
- If you're a regular staff member, marking a task Done instead sends it for review: toast "'{task}' marked
  complete — sent for approval". The row then shows an **Awaiting Approval** badge until an admin approves or
  rejects it on the **Approval Pending** page (see `approvals.md`).
- If a submission is later rejected, the Task Details modal shows a **Submission Rejected** banner with
  Rejected Date & Time, Rejected By, and Rejection Notes.

### Transferring a task from the Checklist page

1. Choose **Transfer** in a row's Action dropdown (admin only) to open **Transfer Task** ("Reassign to another
   team member").
2. Pick a person in **Transfer to** (placeholder "Select team member…").
3. Enter a **Reason / Note** (placeholder "Why is this being transferred?").
4. Click **Confirm Transfer** (or **Cancel** to back out).

You'll see "Transfer request sent — awaiting admin approval" or, once approved, "Task transferred to {name}".
A transferred row shows a **View Only** badge and can no longer be actioned from this screen.

## Requirements to watch for

- If **Req. Attachment** was enabled when the task was created, you must attach an image before you can
  submit it as Done — you'll see "Attachment required for N task(s)" if you try to submit without one.
- Marking a task **Not Done** requires a Remark — you'll see "Remarks required for N 'Not Done' task(s)"
  otherwise.
