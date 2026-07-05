---
title: MIS History and Commitments, and KPI/KRA Reference
module: mis
tags: [mis, history, commitment, kpi, kra, designation]
---

# History & Commitments (`/mis/history_commitment`)

Labeled **History & Commitments** (subtitle "MIS · Historical View"). This page has two tabs.

## History tab (default)

Shows current employee performance data (the same underlying data as the Dashboard's employee list) as a historical reference table.

- KPI strip: Total Employees, Avg Score, Avg Target %, Avg Commitment %
- Filters: **Search by Name**, **Filter by Department**
- Table columns: Employee, Department, Target %, Actual %, Wk Done, On Time, Total %, Wk Pending, All Pending, Commitment, Score
- Empty state: "No employees found"

## Commitment History tab

Shows every commitment ever submitted from the Dashboard's "Submit" action (one row per `MISCommitment` record).

- KPI strip: Total Records, Avg Target %, Avg Commitment %
- Filters: **Start Date** / **End Date** (filters by the commitment's week-start date), **Employee** dropdown (built from employees who appear in the commitment history), **Target Range** dropdown (All Targets, 80–90%, 85–95%, 90–100%, 95–100% — these are approximate ±5 bands around the selected value, not exact ranges)
- An "ACTIVE" badge appears when any filter is set; **Clear All** resets them
- Table columns: Emp ID, Name, Department, Target, Week Start, Week End, Not Done %, Not Done OT %, Commitment, Submitted (date + time), Action
- **Action column**: a trash-can icon deletes that commitment record. Clicking it prompts a browser confirmation ("Are you sure you want to delete this record?") before calling `DELETE /api/mis/commitments/:id`. Deletion only removes the historical commitment row — it does not undo any target/commitment values already applied to the employee's performance record.
- Empty state: "No commitment records found"

---

# KPI & KRA (`/mis/kpi_kra`)

Labeled **KPI & KRA Dashboard** ("Performance metrics and role information"). This is a reference/lookup page, not a data table — it describes what is expected of each job role (designation) and where to learn more.

## Designation selector

A dropdown in the header switches between designations: **CRM, PURCHASE, HR, EA, SALES Coordination, AUDITOR, ACCOUNTANT**. Selecting one reloads the cards below for that role.

## Cards shown per designation

- **Role Details** — the "Actual Role" description text
- **Task Overview** — the daily task count for that role
- **Performance Scoring** — two links that open in a new tab: **How Scoring Works** and **How To Score Better** (these point to external videos/resources configured per designation)
- **Team Communication** — the list of people/roles that designation is expected to coordinate with
- **Communication Process** — free-text guidance on "How to Communicate" plus the **Key Person** to contact
- **Systems and Resources** — a table (cards on mobile) of the systems relevant to that role, each with a System Name, Task Name, Description, and three link buttons: **System** (the tool itself), **Dashboard** (its data view), **Training** (a training video)

All of this content comes from the `MISKpiKra` table, one row per designation, fetched via `GET /api/mis/kpi-kra`. This is the only MIS endpoint that is not tenant-scoped in the current code — it returns the same reference data regardless of which tenant is logged in.
