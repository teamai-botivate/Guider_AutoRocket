---
title: Tracking and Updating Action Item Status (Follow-ups)
module: mom_system
tags: [mom-system, follow-ups, action-items, kanban, status-tracking]
---

# Tracking and Updating Action Item Status (Follow-ups)

Every action item created inside a MOM (see `creating-minutes-and-action-items.md`) shows up on the **Follow-ups** page, which is the central place to monitor and update progress on assigned tasks.

## 1. Open the Follow-ups page

Go to **MOM System > Follow-ups** (`/mom-system/follow-ups`). Header: "Follow-ups & Action Items", subtitle "Track and update action items from meetings."

Stat cards: Total, Pending, In Progress, Delayed, Done.

## 2. Switching views

Top-right toggle switches between:
- **Table** view — a sortable/filterable data table.
- **Kanban** view — four columns: Pending, In Progress, Delayed, Done.

## 3. Filtering

Available filters (all combinable): free-text Search (task or person), **Assigned To** dropdown, **Department** dropdown, **Priority** (All/High/Medium/Low), **Status** (All/Pending/In Progress/Delayed/Done). A **Clear** button appears once any filter is active, resetting all of them.

## 4. Reading the list

### Table view
Columns: Task (with its ID underneath), Meeting (title it came from), Assigned To (avatar + name), Dept, Deadline (shown in red with a warning icon if overdue and not Done), Priority (colored dot + label), Status (badge), and an **Actions** column with a status dropdown.

### Kanban view
Each card shows the task text, source meeting title, assignee (avatar + first name), priority dot, deadline (with overdue warning), and a compact status dropdown at the bottom of the card.

## 5. Updating an action item's status

In either view, use the **status dropdown** on the item's row/card and pick one of: **Pending**, **In Progress**, **Done**, **Delayed**. The change saves immediately (no separate save button) and the item moves to the corresponding Kanban column / updates its badge in the table.

An item is visually flagged as overdue (red text/background, warning icon) when its deadline has passed and its status is not yet Done — this is a display-only cue, not a separate status value.

## 6. Where action items originate

Action items are not created directly from the Follow-ups page — they are added while creating a MOM (Step 3 — Action Items, see `creating-minutes-and-action-items.md`). Follow-ups is purely for monitoring and status updates across all meetings' action items in one place.
