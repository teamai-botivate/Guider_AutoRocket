---
title: MIS Dashboard - Performance Scoring and Weekly Commitments
module: mis
tags: [mis, dashboard, commitment, scoring, kpi]
---

# MIS Dashboard (`/mis/dashboard`)

This is the main MIS screen, labeled **Performance Dashboard** (subtitle "MIS · Admin View") in the app. It shows every active employee's performance metrics and lets an admin capture next week's commitments.

## KPI strip (top of page)

Four summary cards, each averaged/summed across all employees currently loaded:
- **Avg Target** — average of everyone's Target %
- **Avg Actual Work** — average of everyone's Actual Work Done %
- **Total Pending** — sum of everyone's "All Pending Till Date" count
- **Avg Commitment** — average of everyone's current Commitment %

(Note: the small "+12%/+8%/-4%/+2%" trend labels shown under these cards are hardcoded in the UI, not calculated from real week-over-week data.)

## List of People table

A searchable, filterable table of all employees with columns: ID, Name, Target, Actual, Weekly Done, Weekly On Time, Total Work, Week Pending, All Pending, Planned Not Done, Not Done On Time, Commitment, Next Week ND, Next Week ND OT, Next Week Commit, Score.

- **Search name or ID...** box filters by employee name.
- **All Departments** dropdown filters by department.
- Score values are color-coded: green (score ≥ 85), amber (70–84), red (below 70) — this same threshold logic is used throughout MIS screens.
- Clicking anywhere on a row (outside the checkbox/input cells) opens that employee's **detail modal** with Total Tasks, Completed, Pending, Score, and a full Task Details table (FMS Name, Task Name, Target, Actual, Not Done, Late, Pending).

### Entering next week's commitment

1. Check the checkbox next to one or more employees (or use the header checkbox to select all filtered rows).
2. Three input columns become editable for selected rows: **Next Week ND** (Work Not Done %), **Next Week ND OT** (Work Not Done On Time %), and **Next Week Commit** (Commitment %). On mobile these appear under a "Next Week Inputs" panel when a row is expanded.
3. Click **Submit (N)** (N = number of selected employees) in the table header to send the commitments.
4. On success a toast confirms "Commitments submitted successfully!", the selection clears, and the dashboard reloads with updated figures. On failure a toast reads "Failed to submit commitments".

Behind the scenes this calls `POST /api/mis/commitments`, which validates that every selected employee belongs to the same tenant, stores a new `MISCommitment` record for each (defaulting Target to 100 and Commitment to 0 if left blank), and updates that employee's current Target/Commitment on their performance record. The week's date range is automatically computed as next Sunday–Saturday, not chosen manually by the user.

## Ranked panels (below the table)

Three side-by-side cards:
- **Top 5 Scorers** — highest-scoring employees, ranked #1–#5 with a score bar.
- **Pending Tasks by User** — the 5 employees with the most outstanding work ("this week" and "total" pending counts).
- **Lowest Scores** — lowest-scoring employees, flagged as "Needs attention".

## Department Scores

A grid at the bottom showing every department's name and average score with a colored progress bar (same green/amber/red thresholds).

## Download Report

The **Download Report** button (top-right) generates a PDF ("MIS-Dashboard-Report.pdf") containing: the full employee list (ID, Name, Department, Score, Actual/Target, Pending Tasks), a Top 5 Scorers table, a Top 5 Employees with Pending Tasks table, and a Department Scores table on a second page. Generation happens entirely client-side using the data already loaded on screen — it does not call a separate backend report endpoint.
