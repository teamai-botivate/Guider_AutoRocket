---
title: Admin Training Management, Progress Reports, and Video Groups
module: training
tags: [training, admin, superadmin, progress-report, video-groups]
---

# Admin Training Management, Progress Reports, and Video Groups

An **Admin** tab appears in the Training Portal's top navigation only for users whose role is **ADMIN** or **SUPERADMIN**. A role badge (e.g. "SUPERADMIN") is shown in the header for these users.

## 1. Admin dashboard stats

At the top of the Admin tab, four stat cards summarize the tenant's training activity:

1. **Total Trainings** — count of all trainings.
2. **Active Learners** — users currently engaged with training.
3. **Avg Completion** — average completion percentage across learners.
4. **Overdue** — count of overdue assignments.

## 2. Progress Report (SuperAdmin only)

1. SuperAdmins see a tab switcher with **Progress Report** and **Video Groups**. Regular Admins only see the stat cards and a message: "Progress report is only available to Super Admins."
2. The **Progress Report** tab shows a **"User Progress Report"** table ("All users' training progress for this organisation") with columns: **Employee** (name, employee ID, email), **Department**, **Training** (title, with MANDATORY/OVERDUE tags), **Category**, **Progress** (bar + percentage), **Lessons** (completed/total), and **Completed** (completion date, or "Due <date>" if not yet complete, or "—").
3. Click **Refresh** (top right) to reload both the stats and the report table.
4. If no data exists yet, the table area shows "No progress data yet."

## 3. Video Groups (SuperAdmin only)

Video Groups let a SuperAdmin bundle specific training videos and assign that bundle to specific users.

1. Switch to the **Video Groups** tab.
2. Click **"+ New Group"** to reveal the create form: enter a **Group name** (e.g. "Onboarding, Sales Training") and an optional **Description**, then click **"Create Group"**.
3. Existing groups are listed as cards showing videos count and assigned-users count, each with **Edit** and a delete (trash icon) button. Deleting prompts a confirmation ("Delete this video group? This cannot be undone.").
4. Clicking **Edit** on a group opens two additional panels side-by-side:
   - **Training Videos**: a searchable, checkbox list of all trainings ("Search videos...", "Select all" toggle). Check/uncheck videos to add/remove them from the group, then click **"Save Videos"** to commit (the button is disabled/dimmed with "No changes" text when nothing is dirty; when dirty it shows a `+N / −N` delta).
   - **Assign Users**: a searchable, checkbox list of all tenant users ("Search users...", "Select all" toggle) with avatar initials. Check/uncheck users, then click **"Save Users"** to commit assignments.
5. Click **Close** (was "Edit") on the group card to exit edit mode.

## 4. Creating/editing trainings and lessons (API-level; no dedicated admin form UI found)

The frontend service layer (`trainingApi`) supports full CRUD for trainings and lessons — create, update, delete a training, and add/update/delete individual lessons — matching backend endpoints:
- `POST /training`, `PATCH /training/:id`, `DELETE /training/:id`
- `POST /training/:id/lessons`, `PATCH /training/:id/lessons/:lessonId`, `DELETE /training/:id/lessons/:lessonId`

Training fields include: title, category, description, duration, trainer, due date, mandatory (yes/no), thumbnail (index or custom image URL), video URL (YouTube link — the backend auto-normalizes `youtu.be` links, `watch?v=` links, or pasted `<iframe>` embed code into a clean `youtube.com/embed/...` URL), and target role.

Note: no dedicated "Create Training" or "Edit Training" form/button was found rendered in the current Training Portal page — the admin-facing UI observed in code only exposes the **Progress Report** and **Video Groups** management screens. Training/lesson creation may happen through another admin surface (e.g. a system-builder/back-office screen) not covered by this file; if a user asks to create a new training course video from within the Training Portal itself, describe the mechanism (the API supports it) but note the create/edit form was not located in this module's page code.

## 5. Suggested trainings and training series (platform-level)

- **Suggested by Admin**: SuperAdmins can mark trainings as "suggested" for users (via `GET /training/suggested`), which surfaces them in a dedicated section on the learner's My Training dashboard with a "SUGGESTED" badge.
- **Training Series / Platform Video Groups**: a platform-level grouping feature (`GET /training/platform-groups`) that organizes trainings into named series with ordered "chapters" (internally called "seasons," relabeled "Chapter N" in the UI), visible to all authenticated users as playlist-style cards on the My Training dashboard.
