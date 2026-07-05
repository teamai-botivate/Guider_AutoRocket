---
title: Launching and Executing Work Orders
module: workflow_builder
tags: [workflow-builder, work-orders, execution, instances]
---

# Launching and Executing Work Orders

A **Work Order** is a running instance of a published workflow template — think of the template
as a blueprint and the work order as one actual "run" through it (e.g. one specific leave request
going through the Leave Approval Flow).

## 1. Launching a new work order

1. Go to **Work Orders** (`/workflowBuilder/work-orders`) — titled "Work Orders (Instances)" on
   the page.
2. Click **🚀 Launch Instance** (top right).
3. In the "Launch Workflow Instance" dialog:
   - **Select Template*** — choose from **published** workflows only. If none are published yet,
     you'll see: "No published templates available. Publish a workflow builder draft first."
   - **Subject / Instance Title*** — a descriptive name for this specific run, e.g. "Audit
     checklist - Store 05, PO #98721".
   - **Priority** — Low / Normal / High / Urgent (with icons: ⬇ Low, — Normal, ⬆ High, 🔥 Urgent).
   - **Launch Notes** — optional free-text context.
4. Click **Launch Run**. You're taken to the execution view for that instance.

You can also jump straight into launching a work order for a specific workflow by clicking that
workflow's name under the "Workflow Builder" group in the sidebar (pre-filters the Template
dropdown), or by clicking **Analytics → (workflow)** style links elsewhere in the app.

## 2. The Work Orders list

Filters available at the top: a **Template** dropdown (All Templates or a specific published
workflow) and status tabs — **All Orders / PENDING / IN_PROGRESS / COMPLETED / CANCELLED**. The
table itself is dynamic: it shows one column group per workflow step (Status / Planned / Actual /
Delay / Remarks, plus one column per custom form field captured at that step), so different
templates produce differently-shaped tables.

Row actions:
- **Execute →** (if the order isn't finished) or **View** (if completed/cancelled) — opens the
  execution page.
- **Cancel** — available for PENDING/IN_PROGRESS orders; asks "Are you sure you want to cancel
  this work order execution?"
- **Delete** — asks for confirmation, warns it deletes logs and timeline data.

Use **📊 Export Excel** to download all currently filtered work orders (with the same dynamic
per-step columns) as an `.xlsx` file.

## 3. Executing a work order (the runner view)

At `/workflowBuilder/work-orders/[id]` you get:

- A header with the instance title, status badge, order number, and template name, plus a
  **Preview Full Data** button that opens a modal with the complete step-by-step timeline
  (Planned/Actual/Delay + all submitted form data per step).
- A progress bar showing "X of Y steps completed" and percentage complete.
- A **Step Details** timeline table (Planned At / Actual / Delay / Status / Data per step).
- A left-hand **Execution Stepper** list showing every step with its status (numbered circle,
  turns ✓ when Completed or ✗ when Rejected).
- The main **current step card**, which is the actionable part:
  - If the step has a form, it renders that form (`DynamicFormRenderer`) with all configured
    fields, and a **Submit & Continue →** button.
  - If the step is a Decision/Approval-style step, instead of a submit button you get
    **✓ Yes / ✗ No** (or **✓ Approve / ✗ Reject**) buttons plus an optional Remarks/Comments box.
  - If the step has no form fields at all (a pure checkpoint step), you just get a confirmation
    message and a **Mark Completed & Continue →** button.
  - If the step has an **assigned role** and your current user role doesn't match it (and you are
    not a Super Admin), the card shows a locked state: "🔒 Waiting for <ROLE> approval — This step
    requires a <ROLE> to review and action it. Your current role (<your role>) does not have
    permission to submit this step."
- Once all steps resolve, the view shows a **🎉 Execution Complete** card with completion timestamp
  and total step count, and a **Return to Executions** button.
- If the order was cancelled, you instead see a **❌ Order Cancelled** card.

Completed steps' submitted answers also appear afterward in a **Response Parameters** section
below the current step card, grouped by step.
