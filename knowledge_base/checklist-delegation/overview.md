---
title: Checklist & Delegation — Module Overview
module: checklist_delegation
tags: [checklist, delegation, overview, navigation]
---

# Checklist & Delegation — Overview

The **Checklist & Delegation** module lives in the sidebar under **Systems → Checklist & Delegation**. Its
page URL segment is spelled `checklist&deligation` (a typo in the codebase for "delegation"), but this does
not affect anything visible to end users.

## Sidebar pages

1. **Dashboard** — overview stats, charts, and today's/upcoming tasks for both checklist and delegation tasks.
2. **Unique Task** — on-screen titled "Task Management"; a combined admin table for bulk-managing both
   checklist (recurring) and delegation (one-time) tasks, including Excel import.
3. **Assign Task** — the form used to create and assign a brand-new task to someone ("Assign New Task").
4. **Delegation** — your task inbox: action recurring/one-time tasks assigned to you (or, for admins, to
   anyone), and transfer tasks to someone else.
5. **Checklist** — a day-to-day action screen for recurring task occurrences: mark each scheduled item Done,
   Not Done, or Transfer, then Submit All.
6. **Approval Pending** — where admins review and approve/reject completed-task submissions and task-transfer
   requests.

Visiting the bare module URL (`/checklist&deligation`) redirects straight to the **Dashboard**.

There is also a **Leave Management** page (`/checklist&deligation/leave-management`, titled "Leave Management
& Delegation") and a **Calendar** page, plus a **Settings** area (Holidays, Working Days) shared with other
org-wide settings.

## Core concepts

- **Task (master definition)** — created once via Assign Task, with a title, description, assignee, department,
  and a **Frequency**. If Frequency is anything other than "One Time" (Daily, Weekly, Fortnightly, Monthly,
  Quarterly, Half Yearly, Yearly, Alternate Days, Running Hours, Meter Based), the task is recurring.
- **Occurrence** — a single scheduled instance of a recurring task (e.g., "today's" copy of a Daily task). A
  background job automatically generates upcoming occurrences every night at midnight — this is why a
  recurring checklist task shows up on someone's list each day/week/month without anyone manually re-creating
  it (see `automatic-recurring-tasks.md`).
- **Checklist vs. Delegation, as used on the "Unique Task" / Task Management screen**: "Checklist" = recurring
  tasks (any frequency except One Time); "Delegation" = one-off tasks (Frequency must be One Time). The system
  enforces this — you cannot save a Checklist-type task as One Time, or a Delegation-type task as anything
  other than One Time.
- **Delegation (transfer)**, as used on the **Delegation** page — a *different* meaning: forwarding/reassigning
  an already-assigned task occurrence to another team member, with an optional admin-approval step.
- **Approval** — when a non-admin marks a task Done, it is not immediately final: it becomes "Awaiting
  Approval" until an admin approves or rejects it on the Approval Pending page. Admins marking their own tasks
  done can bypass this and complete immediately.

## Related files (for reference)

See `creating-and-assigning-tasks.md`, `completing-checklist-tasks.md`, `delegating-and-transferring-tasks.md`,
`approvals.md`, `dashboard-and-tracking.md`, `leave-holidays-and-settings.md`, and
`automatic-recurring-tasks.md` for step-by-step journeys.
