---
title: Workflow Builder - Overview and Navigation
module: workflow_builder
tags: [workflow-builder, navigation, no-code, overview]
---

# Workflow Builder Overview

Workflow Builder lets you design a custom, no-code, multi-step process (a "workflow template"),
then launch and track real running instances of it ("work orders"). It uses a drag-and-drop
visual canvas to connect steps together.

## 1. Where to find it

In the left sidebar, look for the **Workflow Builder** section. It has two main areas:

- **Workflow Builder** (list/dashboard) — at `/workflowBuilder` — where you create and manage
  workflow *templates*.
- **Work Orders** — at `/workflowBuilder/work-orders` — where you launch and track running
  *instances* of a published template. The sidebar also lists each published workflow by name
  under the Workflow Builder menu group, and clicking one jumps straight to its filtered Work
  Orders list.

If a template has pending work order approvals waiting on you, a live count badge appears next
to "Workflow Builder" / "Work Orders" in the sidebar.

## 2. The three screens

1. **Workflow Designer (list)** — `/workflowBuilder`. Shows all workflow templates as cards, with
   search, a Status filter (Draft / Published / Archived), and a Module filter. Header actions:
   **📥 Import** (upload a `.json` workflow file) and **+ Create Workflow**.
2. **Designer canvas** — `/workflowBuilder/designer/[id]`. The visual drag-and-drop builder for a
   single template. This is where you add steps, connect them, and configure each step's
   properties and form fields.
3. **Work Orders** — `/workflowBuilder/work-orders`. Lists running/completed instances launched
   from published templates, with an execution view per instance at
   `/workflowBuilder/work-orders/[id]`.
4. **Analytics** — `/workflowBuilder/analytics/[id]`. Per-template stats: counts of work orders by
   status and a recent activity/history log.

## 3. Note on access control

Every screen checks your permissions for the `workflow_builder` module (`workflows` or
`work_orders` sections). If you don't have `see` or `read` access (and are not a super admin),
you'll see an **Access Restricted** message instead of the page content — contact your
administrator to request access.

## 4. A note on duplicate routes (technical detail, not user-facing)

The codebase contains two nearly identical route trees: `/workflow-builder/...` (older, under the
"system" screens) and `/workflowBuilder/...` (current). All sidebar navigation and in-app links
point to `/workflowBuilder/...` — that is the version end users actually navigate to and the one
described throughout this knowledge base.
