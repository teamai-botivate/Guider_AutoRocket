---
title: Viewing Workflow Analytics
module: workflow_builder
tags: [workflow-builder, analytics, reporting, metrics]
---

# Viewing Workflow Analytics

Each workflow template has its own analytics page at `/workflowBuilder/analytics/[id]`. Reach it
by clicking **Analytics** on a workflow card in the Workflow Designer list, or via **← Back to
templates** / **Edit Template Graph** to move between analytics and the design canvas.

## What's shown

1. **Header** — the workflow's name with "Analytics" appended, a **← Back to templates** link, and
   an **Edit Template Graph** button that jumps to the Designer canvas for that workflow.
2. **Metrics cards** (5 tiles): **Total Runs**, **Completed**, **In Progress**, **Pending**, and
   **Failed / Cancelled** — each a count of work order instances launched from this template.
3. **Completion Performance** — a donut chart showing the overall completion rate percentage
   (Completed ÷ Total Runs), with a breakdown list below showing each status's count and
   percentage share: Completed, In Progress, Pending, Failed/Cancelled.
4. **Recent Trace Activity** — an audit log / activity feed of recent actions taken across this
   workflow's work orders (step actions, state changes, and operator remarks), described in the
   UI as "Real-time audit log of step actions, state progression, and operator feedback."

If the workflow can't be found, the page shows "Workflow Not Found" with a **Return to Dashboard**
link back to the Workflow Designer list.
