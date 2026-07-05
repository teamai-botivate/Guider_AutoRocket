---
title: Creating Minutes of Meeting (MOM) and Adding Action Items
module: mom_system
tags: [mom-system, mom, minutes-of-meeting, action-items, assign-tasks]
---

# Creating Minutes of Meeting (MOM) and Adding Action Items

A MOM (Minutes of Meeting) captures the summary, decisions, and follow-up action items for a meeting that has already happened. MOMs can only be created for meetings whose status is **Completed** and that don't already have a MOM.

## 1. Open the MOM page

Go to **MOM System > MOM** (`/mom-system/mom`). The header reads "Minutes of Meeting" with subtitle "Create, manage and share meeting minutes." Stat cards show Total MOMs, Draft, Finalized, Shared.

You can also jump in from the **Dashboard**'s "Pending MOM" panel by clicking **Create MOM** next to a listed meeting — this opens a small dialog that then directs you to use the MOM page for the actual creation.

## 2. Create a MOM — step by step

Click **Create MOM** (top right, blue, plus icon) to open the "Create Minutes of Meeting" dialog. It is organized into three numbered sections:

### Step 1 — Meeting Info
- **Select Meeting*** — a dropdown listing only completed meetings that don't yet have a MOM. Choosing one shows a summary strip with the meeting's date, time, type badge, and participant count.

### Step 2 — Meeting Summary
Four repeatable list fields, each starting with one blank row. For each, type text and use **Add Discussion** / **Add Decisions** / **Add Risks** / **Add Next** (button labels are "Add " + first word of the field label) to add more rows, or the X icon to remove a row:
- **Discussion Points**
- **Decisions Made**
- **Risks / Issues**
- **Next Steps**

### Step 3 — Action Items (assigning follow-up tasks)
1. Fill in the inline row: **Task description*** , **Assigned to*** (free-text name), **Deadline** (date picker), **Priority** (High / Medium / Low).
2. Click **Add Action Item** to add it to the table above. Repeat for each action item needed.
3. Each added action item appears in a table with Task, Assigned To, Deadline, Priority, and a delete (trash) icon to remove it before saving.

Note: Assignment is done by typing the assignee's name as free text (not a user picker), and every action item defaults to a **Pending** status when the MOM is saved.

## 3. Saving the MOM

At the bottom of the dialog:
- **Cancel** — discard without saving.
- **Save Draft** — saves the MOM with status **Draft**.
- **Finalize & Share** — saves the MOM with status **Shared**.

After saving, the source meeting is marked as having a MOM created, and the new MOM appears in the MOM list / stat counts.

## 4. Viewing and sharing a MOM

On the MOM list, each card shows the meeting title, date, meeting-type and MOM-status badges, attendee avatars, action item/decision/next-step counts, and a discussion-point preview. Two buttons per card:
- **View** — opens a read-only dialog with full attendee list, all four summary sections, and a table of action items (Task, Assigned, Deadline, Status).
- **Share** — marked as a share action (emerald-colored button) for distributing the MOM.

Inside the View dialog there is also a **Share MOM** button and a **Close** button.

## 5. Filtering the MOM list

Tabs: All, Draft, Finalized, Shared (with counts). A search box filters by meeting title or attendee name.
