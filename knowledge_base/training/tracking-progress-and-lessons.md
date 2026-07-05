---
title: Tracking Lesson Progress, Levels, and XP
module: training
tags: [training, progress, lessons, xp, levels, gamification]
---

# Tracking Lesson Progress, Levels, and XP

## 1. Marking a lesson or course video complete

1. Open a training from **My Training**, and select either the **Course Video** (master video) or a specific lesson in the **Course Content** panel on the right.
2. Below the video player, click **"Mark as Complete"** (in the status bar) — or use the smaller **"Mark done"** button next to that item directly in the Course Content list.
3. While saving, the button shows **"Saving..."** (status bar) or **"..."** (list button) and is disabled until the request completes.
4. Once marked, the item shows a green **"Completed"** tag with a checkmark, and it can no longer be un-marked from the UI.
5. Marking a lesson or the master video complete immediately refreshes: the circular progress ring, the "X of Y completed" lesson counter, the training card's progress bar back on the dashboard, and your overall **My Progress** stats.
6. There is no way to mark a lesson as incomplete again from this UI — completion is one-directional per the available endpoints.

## 2. "My Progress" tab

Navigate to the **My Progress** tab in the Training Portal top nav to see your personal learning summary:

1. **Level card**: shows your current numeric **Level**, total **XP**, and a progress bar toward the next level, labelled "`X` / `Y` XP to Level `N+1`". On the right of this card, your total **Courses Done** count is shown.
   - XP mechanics (server-computed): completing a course awards 100 XP each. You level up every 3 completed courses (Level = floor(completedCourses / 3) + 1). Each level requires 300 XP; `xpInCurrentLevel` is `(completedCourses % 3) * 100`.
2. **Stats grid**: four cards — **Enrolled** (total trainings you've started/been assigned), **Completed**, **In Progress**, and **Overdue** (assigned trainings past their due date that aren't yet completed).
3. **All My Trainings**: a card grid of every training you have a progress record for, each showing its status pill, mandatory badge, due date (highlighted if overdue), completed/total lesson count, and progress bar. Click any card to reopen that training's detail/player page.
4. Use the **Refresh** button (top right of the My Progress page) to reload your latest stats and progress list on demand.
5. If you have no progress yet, the page shows: "No progress yet. Open a training and complete a lesson to get started!"

## 3. Due dates, mandatory trainings, and overdue status

- A training can have a **due date**; if it's self-paced (no due date), the UI shows "Self-paced" instead.
- Trainings can be flagged **MANDATORY** by whoever created them — this shows as an orange/red "MANDATORY" badge on cards and in the progress report.
- A training becomes **OVERDUE** when its due date has passed and progress is under 100% — reflected in the status pill on cards and counted in the "Overdue" stat tile on both the My Progress page and (for admins) the Admin stats.
