---
title: MIS Module Overview and Navigation
module: mis
tags: [mis, navigation, overview, performance]
---

# MIS (Management Information System)

The MIS module is a manager/admin-facing reporting area that tracks employee task performance, weekly commitments, and departmental scores. It sits under the **MIS** section in the left sidebar (grouped separately from the business-domain modules), with six sub-pages:

| Sidebar label | Path | Purpose |
| --- | --- | --- |
| Dashboard | `/mis/dashboard` | Main admin performance dashboard — table of every employee's metrics, top/bottom scorers, department scores, and the weekly commitment entry form |
| Department | `/mis/department` | Task-level breakdown filterable by employee/department/date range |
| History Commitment | `/mis/history_commitment` | Two-tab historical view: employee performance history and past commitment submissions |
| Today Tasks | `/mis/today_tasks` | List of tasks due today across the company |
| Pending Tasks | `/mis/pending_tasks` | List of overdue/incomplete tasks |
| KPI & KRA | `/mis/kpi_kra` | Reference page describing each designation's role, scoring method, and systems used |

All MIS data is scored per employee, not self-reported by the viewer — an MIS/admin user reviews everyone's numbers from these screens. There is no separate personal MIS page for individual employees inside this module (a "My Dashboard" personal snapshot with score/rank/attendance exists as a different widget elsewhere in the app, fed by a related `my-dashboard` API, but it is not one of the six MIS pages above).

## How the metrics are generated

Every active user in a tenant gets an `MISPerformance` record. Scores and percentages (Target, Actual Work Done, Weekly Work Done, Weekly Work Done On Time, Total Work, Week Pending, All Pending Till Date, Planned Work Not Done, Planned Work Not Done On Time, Commitment, Score) are snapshot values maintained on that record — they are not computed live from the task/checklist tables in front of the user. If a new user has no record yet, the system creates one with Score = 0 and Target = 0 so they still appear in the employee list.

## Typical workflow

1. Open **MIS → Dashboard** to see everyone's current scores and pending work at a glance.
2. Use the search box and department dropdown to narrow the "List of People" table to specific staff.
3. Click a row to open that employee's detail modal for a task-by-task breakdown.
4. Select one or more employees (checkboxes) to enter next week's commitment numbers inline, then click **Submit**.
5. Use **Download Report** to export the current dashboard view (all employees, top scorers, most-pending employees, department scores) as a PDF.
6. Check **Today Tasks** / **Pending Tasks** for the operational task lists behind those scores, and **Department** for a task-level view grouped by department.
7. Use **History Commitment** to audit what commitments were made in the past and delete incorrect entries.
8. Refer to **KPI & KRA** to look up what a given role/designation is expected to do and how its score is calculated.

See the other files in this folder for details on each screen.

## Note on source-of-truth conflict

The backend's `mis.md` design doc describes `GET /api/mis/dashboard` as accepting `name`/`departmentId` query filters and returning `topScorers`/`lowestScorers` arrays directly from the server, and describes score calculation as a live weighted formula. The actual shipped code does neither: filtering and top/bottom-scorer sorting happen entirely client-side in the Dashboard component after fetching the full employee list, and `MISPerformance.score` is a stored field with no visible calculation formula in the service layer (it is presumably set by an external process/worker not present in the `services/mis` or `controllers/mis` code reviewed). Treat `mis.md`'s "Business Logic & Aggregations" section as aspirational, not descriptive of current behavior.
