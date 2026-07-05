---
title: Creating and Processing a Meeting
module: mom_system
tags: [mom-system, meetings, scheduling, create-meeting]
---

# Creating and Processing a Meeting

Meetings are the starting point of the MOM System — a Minutes of Meeting (MOM) can only be created for a meeting that has been marked "Completed."

## 1. Open the Meetings page

Go to **MOM System > Meetings** (`/mom-system/meetings`). The page header reads "Meetings" with the subtitle "Schedule, manage, and track all meetings."

Stat cards at the top show: Total, Scheduled, Completed, Pending MOM.

## 2. Start a new meeting

1. Click the **New Meeting** button (top right, blue, plus icon).
2. In the "New Meeting" dialog, fill in:
   - **Meeting Title*** — free text (e.g. "Client Discussion – MSEDCL")
   - **Meeting Type*** — one of: Internal, External, Client, Vendor, Team, Personal
   - **Priority** — High, Medium, or Low
   - **Date*** — date picker
   - **Start Time** / **End Time**
   - **Location** — free text (e.g. conference room)
   - **Google Meet Link** — optional URL
   - **Description** — free-text agenda/context
3. If a Date, Start Time, and End Time are all filled in, the dialog shows an **Availability Check** panel that flags a potential scheduling conflict if another meeting overlaps the same date/time range.
4. Add **Participants**: enter Name* (required), Company, Mobile, Email, choose a Role (Organizer, Attendee, or Optional), then click **Add Participant**. Repeat for each attendee. Added participants appear in a list below with a remove (X) control.
5. Click **Create Meeting** to save, or **Cancel** to discard.

A newly created meeting starts with status **Scheduled** and appears in the "Pending" tab of the meetings table.

## 3. Browsing and filtering meetings

The meetings table has two stage tabs: **Pending** (not yet Completed/Rejected) and **History** (Completed or Rejected). Within a stage, filter by meeting type tabs (All, Internal, External, Client, Vendor, Team, Personal), free-text search (by title or participant name), and a date filter. Each row shows Meeting, Type, Date & Time, Priority, Participants (avatars), Status, MOM status (Created / Pending / —), and a **Process** button.

## 4. Processing a meeting (marking it done)

1. Click **Process** on a meeting's row to open the "Process Meeting" dialog.
2. Choose a **Status**: Complete, Reject, or Hold.
3. Click **Update Status** to confirm, or **Cancel** to back out.
4. Completing or rejecting a meeting moves it to the History tab; putting it on Hold keeps it in Pending.

Once a meeting's status is **Completed** and it has no MOM yet, its "MOM" column shows a **Pending** badge — this is the meeting to pick when creating a MOM (see `creating-minutes-and-action-items.md`).

## 5. Viewing meeting details

Clicking a meeting (or its title, depending on context) opens a details dialog showing type/status/priority badges, date/time, location, meet link, description, the full participant list, and a "MOM Status" indicator ("MOM has been created" or "MOM not yet created").
