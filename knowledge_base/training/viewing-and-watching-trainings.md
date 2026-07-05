---
title: Viewing and Watching Training Videos
module: training
tags: [training, videos, dashboard, my-training, lessons]
---

# Viewing and Watching Training Videos

The Training module lives at **Training Portal** (`/training` in the app). It has an in-page top navigation bar with tabs: **My Training**, **My Progress**, and (for Admin/SuperAdmin users only) **Admin**.

## 1. Browsing your assigned trainings ("My Training")

1. Open the **Training Portal**. You land on the **My Training** tab by default. The page subtitle reads "Click any course card to start the course automatically."
2. If you have any courses in progress, a **"CONTINUE WHERE YOU LEFT OFF"** strip appears at the top showing each in-progress course with its percent complete — click a card to jump back in.
3. If a SuperAdmin has recommended courses to you, a **"Suggested by Admin"** section appears with a **SUGGESTED** badge on each card.
4. If the platform has grouped courses into a multi-part series, a **"Training Series"** section appears showing playlist-style cards (with a "+N" badge for additional chapters). Click a series card to open a modal listing its chapters (labelled e.g. "Chapter 1", "Chapter 2" — the app converts internal "season" labels to "Chapter" for display); click any chapter to open that training's detail page (only chapters actually assigned to you are clickable — others show "Not assigned to you").
5. Below that is the main course grid/list. Each training card shows: category badge (HR, Sales, Tech, Safety, Compliance), a **MANDATORY** badge if required, a status pill (**NOT STARTED**, **IN PROGRESS**, **OVERDUE**, or **COMPLETED**), the title, number of lessons, duration, a progress bar, and a call-to-action button that reads **"Start Learning"**, **"Continue Learning"**, or **"Course Completed"** depending on your progress.
6. Use the **search box** ("Search trainings...") to filter by title or trainer name, the **category pill filters** (dynamically built from your assigned trainings, e.g. All / HR / Sales / Tech...) to filter by category, and the **status dropdown** (All, Completed, In Progress, Not Started, Mandatory) to filter by status.
7. Toggle between **grid** and **list** card layouts using the two icon buttons next to the filters.
8. Click any training card to open its detail/player page.

## 2. Watching a course (detail page)

1. Clicking a card opens the training detail view with a **"Back to Training Dashboard"** link at the top.
2. Opening a training automatically calls the start/enroll endpoint in the background, so simply opening a course marks it as started (creates a 0%+ progress record) — there is no separate "Enroll" button.
3. The main video player (large embedded YouTube iframe) sits at the top of the left/center column. Videos are stored as YouTube links and embedded via `youtube.com/embed/...`.
4. Below the player, a status bar shows either **"Course Video"** (the master/intro video) or **"Active Lesson"** (a specific lesson), with the item's title and either a **"Completed"** indicator or a **"Mark as Complete"** button.
5. On the right-hand side:
   - A **Course Progress** card shows a circular progress ring with the percent complete and "X of Y completed" lesson count.
   - A **Course Content** panel ("Click a video below to start playing") lists the master/course video (if any) at the top, followed by each lesson in order ("Lesson 1", "Lesson 2", ...). Click any row to switch the player to that video. Each row shows a small thumbnail, duration badge, and either a green **Completed** tag or a **Mark done** button.
6. Below the player, an **"About this Course"** card shows the description (or a fallback auto-generated blurb naming the trainer), plus a stats grid: Trainer, Duration, Lessons, Due Date (or "Self-paced" if no due date is set).
7. When every lesson (and master video, if present) is marked complete, progress reaches 100% and a green **"Course Completed! Certificate Earned"** banner appears, noting you can re-watch any lesson at any time.

## Notes on what triggers progress

- Progress is tracked per lesson/master video, not by video-watch-time — completion happens only when the user explicitly clicks **Mark as Complete** / **Mark done**, not automatically when a video finishes playing.
- The training's overall `progress` percentage and `completedAt` timestamp are computed server-side from completed lesson count vs. total lesson count.
