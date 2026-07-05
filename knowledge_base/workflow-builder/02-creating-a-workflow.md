---
title: Creating a New Workflow Template
module: workflow_builder
tags: [workflow-builder, create-workflow, template, no-code]
---

# Creating a New Workflow Template

1. Go to **Workflow Builder** in the sidebar (`/workflowBuilder`). This opens the "Workflow
   Designer" list page.
2. Click **+ Create Workflow** (top right).
3. Fill in the "New Workflow Builder Design" dialog:
   - **Workflow Title*** (required) — e.g. "Leave Approval Flow".
   - **Description** — a short optional summary of what the flow does.
   - **Category** — choose from: HR, Finance, Procurement, Operations, IT, Legal, Production,
     Sales, Other. If you pick **Other**, a **Custom Category Name*** text field appears and is
     required.
4. Click **Create & Design**. You are taken straight to the canvas at
   `/workflowBuilder/designer/[id]` to start building.

New workflows are created with `module: custom` and start in **DRAFT** status — they are not
usable to launch work orders until you **publish** them (see the Publishing doc).

## Importing a workflow from a file

Instead of building from scratch, you can import a previously exported workflow:

1. On the Workflow Designer list page, click **📥 Import**.
2. Choose a `.json` file (one previously created via **Export**, see below). The file must have a
   `name` field or the import is rejected with "Invalid workflow file format (name field
   missing)."
3. The importer creates a new workflow named `<original name> (Imported)`, copying over
   description, category/module, and the steps/edges graph if present.

## Exporting a workflow

On any workflow card in the list, hover to reveal the row of icon buttons and click **📤** (Export).
This downloads a `<workflow_name>_v<version>.workflow.json` file containing the full workflow
definition (steps, edges, form schemas) — useful for backup or moving a template between
templates/environments via Import.

## Duplicating a workflow

Click the **📁** (Duplicate) icon on a workflow card to create a copy of that template so you can
modify it without touching the original.

## Deleting a workflow

Click the **🗑️** (Delete) icon on a workflow card. You'll be asked to confirm: "Are you sure you
want to delete '<name>'? This action is permanent."

## Filtering and finding workflows

On the list page you can:
- Search by name/text in the **Search templates...** box.
- Filter by **Status**: All Statuses / Draft / Published / Archived.
- Filter by **Module** (auto-populated from existing workflows' module values).
- See totals at a glance: **Total** workflow count and **Published** count, shown top-right of the
  filter bar.
