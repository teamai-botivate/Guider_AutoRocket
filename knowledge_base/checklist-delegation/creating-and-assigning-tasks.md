---
title: Creating and Assigning a New Task
module: checklist_delegation
tags: [assign-task, create-task, delegation, frequency]
---

# Creating and Assigning a New Task

Use this when you need to create a brand-new task (either a recurring checklist item or a one-time task)
and hand it to someone.

## Steps

1. Go to **Checklist & Delegation → Assign Task** in the sidebar. The page heading reads **"Assign New Task"**
   (subtitle: "Checklist & Delegation System").
2. In the **Assignment** section:
   - Optionally toggle **"Self Assign Task"** if you're assigning the task to yourself.
   - **Given By** — pre-filled/locked to your own name.
   - **Department** — select from the dropdown (placeholder "Select Department"). If it fails to load, click
     **Retry**.
   - **Doer Name** — select who the task is for (placeholder "Select doer"; you must pick a department first).
     If the selected doer has upcoming approved leave, a banner appears: "This doer has N approved leave(s)
     upcoming" with a **View Leave Schedule** link.
   - **Frequency** — choose how often the task repeats:
     - **One Time** — runs only once (set an end date)
     - **Daily**, **Alternate Days**, **Weekly**, **Fortnightly**, **Monthly**, **Quarterly**,
       **Half Yearly**, **Yearly**, **Running Hours**, **Meter Based**
     - If you pick **Alternate Days**, an extra required field appears: **"Gap between occurrences (days)"**.
3. In the **Task Details** section:
   - **Task Title** (required) — e.g. placeholder text "Quarterly Financial Review".
   - **Task Description** (required) — shows a live character counter (max 500).
4. In the **Reference** section (optional), attach a reference by choosing a type: **Web Link**, **Image**,
   **PDF**, **Video**, or **Voice Note**. For a Web Link, fill in **URL** and optional **Label**, then click
   **Add Link**.
5. In the **Schedule** section:
   - **Time** (required).
   - **Target Date** (if Frequency is One Time) or **Start Date** (required) otherwise.
6. Optionally toggle **Reminders** and **Req. Attachment** (require an attachment before the task can be
   marked complete).
7. Use the **Live Preview** panel on the right to confirm Given By / Doer / Department / date / reference
   before saving. The **Doer's Tasks** panel shows what that person already has scheduled on the chosen date.
8. To submit, click one of:
   - **Assign Task** — saves this single task immediately.
   - **Add to List** then **Assign All (N)** — queue up several tasks (shown in the **Task Queue** panel) and
     submit them together.
   - **Save Draft** — keeps the form filled without submitting (shows a "Saved as draft" confirmation; this is
     local only, not a persisted draft record).
   - **Clear Form** — resets all fields.

On success you'll see a toast like "N task(s) assigned successfully". Required-field validation messages
include "Select a department", "Select a doer", "Task title is required", "Description is required", and
"Pick a date".

## Notes

- A task's **Frequency** determines whether it behaves as a recurring **Checklist** item or a one-off
  **Delegation** item elsewhere in the module — anything other than "One Time" is recurring.
- Bulk-creating many tasks at once (e.g. from a spreadsheet) is done from the **Unique Task** page's
  **Import from Excel** feature instead of this form — see `dashboard-and-tracking.md`.
