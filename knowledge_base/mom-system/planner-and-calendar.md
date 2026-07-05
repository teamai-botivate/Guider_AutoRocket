---
title: Director Planner, Calendar, and Meeting Repository
module: mom_system
tags: [mom-system, planner, calendar, repository, personal-tasks]
---

# Director Planner, Calendar, and Meeting Repository

These three MOM System pages are supporting views alongside Meetings, MOM, and Follow-ups.

## 1. Planner (`/mom-system/planner`)

Header: "Director Personal Planner", subtitle "Managed by Executive Assistant." This is a standalone personal task list — separate from meeting-derived action items.

Stat cards: Total Tasks, Due Today, High Priority, Completed.

Tasks are grouped by due date into sections: **Today**, **Tomorrow**, **This Week**, **Later** (a section is hidden if it has no tasks). A collapsed **Completed** section at the bottom can be expanded/collapsed.

### Adding a task
1. Click **Add Task** (top right).
2. Fill in: **Task*** (free text), **Category** (Personal, Family, Travel, Call, Follow-up, Reminder, Event — each with an icon), **Priority** (High/Medium/Low), **Due Date***, **Due Time**, **Notes**, and a **Recurring task** toggle.
3. Click **Add Task** in the dialog footer to save, or **Cancel**.

### Managing a task
Each task card has three actions:
- **Done** (checkmark button) — marks the task complete; it moves to the Completed section.
- Edit icon — opens the same form pre-filled, titled "Edit Task"; save via **Save Changes**.
- X icon — deletes the task.

Completed tasks show an **Undo** button to move them back to Pending.

## 2. Calendar (`/mom-system/calendar`)

Header: "Calendar", subtitle "Visual overview of all scheduled meetings." A color legend maps meeting types (Internal, External, Client, Vendor, Team, Personal) to colored dots.

Three view toggles:
- **Month** — a full month grid; click a day cell to see that day's meetings listed below the grid. Navigate months with the left/right chevrons in the header.
- **Week** — an hour-by-hour (7 AM–7 PM) grid for the current week, with meetings rendered as colored blocks positioned by start time/duration.
- **Agenda** — meetings grouped by date in a scrollable list, with today's group highlighted.

This page is read-only for browsing; meetings are created from the Meetings page.

## 3. Meeting Repository (`/mom-system/repository`)

Header: "Meeting Repository", subtitle "Search and browse all past meetings and MOMs." Not currently linked in the sidebar navigation — accessed by direct URL.

- A large search bar searches by keyword, client, topic, or participant.
- Filter chips: **Type** (All/Internal/External/Client/Vendor/Team/Personal), **Period** (All Time/This Month/This Quarter/This Year), **MOM** (All/With MOM/Without MOM).
- Results are meeting cards sorted newest-first. Each card shows the date, title, type/status/priority badges, duration, participant avatars, and whether a MOM exists ("MOM Created" or "No MOM").
- Click **View Details** on a card to expand it in place, showing Meeting ID, full date/time, Created By, location/meet links, the full participant list, and — if a MOM exists — a "MOM Summary" panel with key discussion points, decisions, and the linked action items with their current status.

This page is a read-only archive/search tool; it does not create or edit meetings or MOMs.
