---
title: MIS Department View, Today Tasks, and Pending Tasks
module: mis
tags: [mis, department, tasks, pending, filters]
---

# Department (`/mis/department`)

Labeled **Department Performance** (subtitle "MIS · Department View"). This is a task-level report — each row is one task occurrence tied to an employee, rather than one row per employee.

## Filters card

- **Filter by Name** — dropdown of employee names (built from tasks currently loaded)
- **Filter by Department** — dropdown of departments
- **Start Date** / **End Date** — restricts to tasks whose due date falls in range
- **Clear All** button resets all four filters; an "ACTIVE" badge appears next to "Filters" when any filter is set
- A status pill at the top right of the page shows how many tasks currently match ("N task(s) found")

## KPI strip

Five cards computed from the filtered task list: **FMS Names** (distinct FMS/department groupings involved), **Employees** (distinct employees involved), **Pending Tasks** (sum of each involved employee's all-time pending count), **Overall Score** (average of each task's employee's Total Work %), **Delay Score** (100 minus the average On-Time %, i.e. higher = more delay).

## Department Tasks table

Columns: Employee ID, FMS, Task, Employee, Target, Total Achv., % Work Done, % On Time, Pending. Each row pulls its metrics from that task's assigned employee's performance record (not from the task occurrence itself). When no tasks match the filters, the table shows "No tasks found — Try adjusting your filters to see more results."

---

# Today Tasks (`/mis/today_tasks`)

Labeled **Today's Tasks** (subtitle "MIS · Today's View"). Lists every task occurrence scheduled for today, company-wide.

- Search box: "Search tasks, people, FMS…"
- **All Persons** / **All FMS Names** dropdowns to narrow the list
- **Clear All** button appears once any filter is active
- KPI strip: Total Persons, FMS Names, Unique Tasks, Today's Total Tasks
- Table columns: Employee ID, Name, FMS Name, Task Name, Today Tasks (a count badge, colored green when > 0)
- Empty state: "No Tasks Found — Try adjusting your filters or search query"

---

# Pending Tasks (`/mis/pending_tasks`)

Labeled **Pending Tasks** (subtitle "MIS · Pending View"). Lists task occurrences that are not yet completed and due on or before today.

- Same search/person/FMS filter pattern as Today Tasks
- KPI strip: Total Persons, FMS Names, Unique Tasks, **Total Pending** (shown in red when > 0)
- An **overdue callout banner** ("N task(s) is/are overdue") appears above the table whenever any listed task's due date has already passed
- Table columns: Employee ID, Name, FMS Name, Task Name, Due Date (with an "Overdue" or "Due soon" tag when applicable), Pending (count badge)
- Empty state: "No Pending Tasks Found — Try adjusting your filters or search query"

Both Today Tasks and Pending Tasks are read-only lists — there is no action button to complete or reassign a task from these MIS screens; task completion happens in the underlying checklist/delegation module.
