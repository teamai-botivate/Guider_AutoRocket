---
title: Quality Control (Lab Test) Approval
module: production_planning
tags: [lab-test, quality-control, qc, audit, approval, rework]
---

# Quality Control (Lab Test) Approval

Every job card that has actual production recorded automatically gets a QC record. This page is
where a Quality Auditor passes or fails that batch before it's treated as usable Finished Goods.

## Where

**Production Planning → Quality Control (Lab Test)** (`/production-planning/lab-test-1`). Page
heading: "Quality Control (Lab Test)"; subtitle: "Completed job cards awaiting quality approval
before inventory update."

## 1. Review QC records

1. Stats cards: **Total Audits**, **Approved**, **Rejected**, **Pending**.
2. Card title: "Lab Test Registry". Two tabs: **Pending** (result = Pending) and **History**
   (any other result).
3. Table columns: Edit, Test No, Job Card, Prod No, Product, Produced, Rejected, Auditor, QC
   Status, Remarks, and Planned At (pending) / Delay (history).
4. QC Status badge colors: Pass (green), Fail (red), Hold (yellow), Rework (orange), Pending
   (blue).

## 2. Edit/update a QC record directly (basic form)

1. Click the pencil icon (Pending tab) to open "Update QC Record", or the eye icon (History tab)
   for a read-only "View QC Record".
2. Editable fields: **Test Date**, **Quality Auditor** (free text), **QC Decision** (dropdown:
   Pending / Pass / Fail / Hold), **Remarks / Findings** (free text, placeholder example: "E.g.
   Dimensions verified, viscosity approved...").
3. Click **Save** to store the update, or **Close**/**Cancel** to dismiss.

## 3. Quality Auditor Approval (formal audit dialog)

Note: the code defines a more structured "Quality Auditor Approval" dialog (fields: Product &
Batch, Quality Auditor, Inspection Findings/Observations, and an Approve/Reject toggle) intended
for the formal pass/fail decision, distinct from the basic edit dialog above:

1. **Quality Auditor \*** — required, name of the person doing the audit.
2. **Inspection Findings / Observations \*** — required multi-line text (placeholder example:
   "E.g. Color checked ✓, Viscosity verified ✓, Dimensions within tolerance...").
3. **Approval Decision \*** — two large toggle buttons: **Approve** (green, check icon) or
   **Reject** (red, X icon).
4. Submit button label changes based on decision: **Approve & Complete** (green) or **Reject &
   Send to Rework** (red).
5. On submit:
   - If **Approve**: remarks default to "Quality standard approved by <auditor>" (if you left
     findings blank) and a success toast reads "Approved by <auditor>! Added to Finished Goods
     Inventory."
   - If **Reject**: remarks default to "QC Rejected by <auditor>" and a toast reads "Rejected by
     <auditor>! Sent to Rework station."

## Notes

- The "Added to Finished Goods Inventory" / "Sent to Rework station" language shown in the toast
  is descriptive messaging only — the actual FG stock increment already happened earlier, at the
  Actual Production step (see `actual-production-and-stock-update.md`). The Lab Test step does not
  itself call any separate inventory-adjustment API; it only updates the lab test record's result
  and remarks.
