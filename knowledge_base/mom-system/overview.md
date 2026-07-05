---
title: MOM System Overview
module: mom_system
tags: [mom-system, overview, navigation, meetings, minutes-of-meeting]
---

# MOM System Overview

The MOM System (Minutes of Meeting) module lives under the sidebar group **MOM System** and covers scheduling meetings, recording their minutes, assigning follow-up action items, and tracking a director's personal task list.

## 1. Navigating to the module

In the left sidebar, open the **MOM System** group (calendar-event icon). It expands into these sub-links:

1. **Dashboard** — `/mom-system/dashboard`
2. **Meetings** — `/mom-system/meetings`
3. **Calendar** — `/mom-system/calendar`
4. **MOM** — `/mom-system/mom`
5. **Follow-ups** — `/mom-system/follow-ups`
6. **Planner** — `/mom-system/planner`

There is also a **Meeting Repository** page at `/mom-system/repository` ("Meeting Repository" — search and browse all past meetings and MOMs), but it is not currently linked from the sidebar; it must be reached by typing the URL directly.

## 2. What each page is for

- **Dashboard** — landing page. Shows stat cards (Today's Meetings, Pending MOM, Pending Actions, Delayed Tasks), a "Today's Schedule" timeline, "Upcoming Meetings" and "Pending MOM" panels, and a "Recent Action Items" table.
- **Meetings** — create and manage meeting records (see `creating-a-meeting.md`).
- **Calendar** — Month / Week / Agenda visual views of all scheduled meetings, color-coded by meeting type (Internal, External, Client, Vendor, Team, Personal).
- **MOM** — create, view, and share the actual Minutes of Meeting document for a completed meeting, including action items (see `creating-minutes-and-action-items.md`).
- **Follow-ups** — the master list of all action items across all meetings, with table and Kanban views, filtering, and status updates (see `tracking-action-items.md`).
- **Planner** — a personal/director task list ("Director Personal Planner"), separate from meeting action items, described as "Managed by Executive Assistant."
- **Meeting Repository** — read-only searchable archive of past meetings with their linked MOM summaries.

## 3. How the pieces connect

1. A **Meeting** is scheduled on the Meetings page.
2. Once a meeting takes place, it is "Processed" (marked Complete/Rejected/Hold) on the Meetings page.
3. For a **Completed** meeting that has no MOM yet, a **MOM** (Minutes of Meeting) is created from the MOM page (or via the "Create MOM" shortcut on the Dashboard's "Pending MOM" panel, which redirects to the MOM page).
4. While creating the MOM, **Action Items** can be added — each one is assigned to a person with a deadline and priority.
5. Action items created inside a MOM automatically appear in **Follow-ups**, where anyone tracking them can update status (Pending → In Progress → Done, or Delayed).
6. The **Planner** is unrelated to any specific meeting — it's a standalone personal to-do list.

## 4. Data note

The frontend pages call a REST API under `/mom-system/...` (via `momSystemApi` in `src/features/mom-system/api.ts`), backed by `MOMSystemController` / `MOMSystemService` in the backend. If that API call fails, pages fall back to built-in sample/mock data for display purposes only — real changes always go through the API.
