---
title: Planning and Updating Job Cards
module: production_planning
tags: [job-card, planning, supervisor, shift, material-check]
---

# Planning and Updating Job Cards

A Job Card is the machine-level production record created automatically when you click **Start
Production** on the Full Kitting page. This page is where you fill in the operational planning
details (supervisor, shift, date) before production runs.

## Where

**Production Planning → Job Cards** (`/production-planning/job-cards`). Page heading: "Job
Cards"; subtitle "Track machine-level production jobs with operator assignment."

## 1. Review job cards

1. KPI cards: **Total**, **Planning**, **Completed**, **Rejected** (counts by status).
2. Two tabs: **Pending** (status = Planning or Running) and **History** (status = Completed or
   Rejected).
3. Table columns: Action, Job Card No, Prod No, Product, Supervisor, Shift, Date, Planned,
   Produced, Rejected, Status, and Planned At (pending) / Delay (history).
4. Search box filters by job card no, production no, product name, or party name.

## 2. Update a pending job card

1. In the **Pending** tab, click **Update** on a row (pencil icon).
2. The "Update Job Card — <Job Card No>" dialog opens. At the top, if a BOM exists for the
   product, a **Raw Material Availability (BOM Check)** panel automatically re-verifies whether
   enough raw material is available for the current produced quantity — showing Per Unit,
   Required, Available, Shortage, and a ✓ OK / ✗ Short status per material. If no BOM exists you
   see an amber notice; if the check fails to reach the server you see a red error notice.
3. Editable/read-only fields in the form:
   - Production No, Order No, Product, Party Name — read-only (pulled from the order).
   - **Supervisor** — free text, editable.
   - **Shift** — dropdown: Morning / Evening / Night.
   - **Date** — date picker.
   - Produced Qty — read-only.
   - Status — shown as a fixed "Planning" badge (this update action always sets status to
     `Planning`).
   - **Remarks** — optional free text.
4. Click **Update**. The button is disabled (with an explanatory tooltip) if the BOM check found
   insufficient raw materials, or if a separate material-sufficiency check is still loading or
   found a shortage — you must resolve the shortage (e.g. reduce quantity or purchase material)
   before you can save.
5. On success: toast "Job Card <No> planned successfully."

## 3. View a completed/rejected job card

1. In the **History** tab, click **View** (eye icon) — opens a read-only "View Production" dialog
   showing the same production details for reference (no editing).

## Notes

- Job cards are not created manually from this page — they originate from **Full Kitting →
  Start Production**. This page only lets you plan/update details on an already-created job card.
- The status values used across the UI are `Planning`, `Running`, `Completed`, `Rejected` (the
  backend's raw default status on creation is `Open`, but the Full Kitting "Start Production"
  action explicitly sets it to `Running`).
