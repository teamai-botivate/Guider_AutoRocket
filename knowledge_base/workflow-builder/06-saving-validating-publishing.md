---
title: Saving, Validating, and Publishing a Workflow
module: workflow_builder
tags: [workflow-builder, save, validate, publish, versioning]
---

# Saving, Validating, and Publishing a Workflow

The Designer canvas top bar (`/workflowBuilder/designer/[id]`) shows the workflow's name, its
status badge (DRAFT/PUBLISHED), current version number ("v1", "v2"...), and an "• unsaved changes"
indicator whenever you have unsaved edits. Three action buttons sit on the right: **💾 Save**,
**✓ Validate**, and **🚀 Publish**.

## 1. Save

Click **💾 Save** to persist your current canvas layout (all nodes, their positions, and
connections) to the server. While saving, the button shows "...". On success you'll briefly see a
"✓ Saved" confirmation flash; on failure, "✗ Save failed" (check the browser console for details).

Saving does **not** change the workflow's status — a Draft stays a Draft after saving.

## 2. Validate

Click **✓ Validate** to check the graph for structural problems before publishing. If you have
unsaved changes, the app auto-saves first (validation always reads from the saved database
state, not your in-memory canvas). Validation results appear as a banner directly under the top
bar, and a summary badge next to the buttons: **✓ Valid** (green) or **✗ N error(s)** (red), plus
a count of warnings (⚠) if any.

Validation rules (enforced by the backend graph validator):

**Errors** (block publishing):
- The workflow must have at least one step.
- Must have **exactly one** START node (zero or more than one is an error).
- Must have **at least one** END node.
- Every non-END step must have at least one outgoing connection ("dead end" error) —
  e.g. "Step 'Quality Check' has no outgoing edges (dead end)."
- Every DECISION step must have both a YES and a NO outgoing edge — missing either produces an
  error like "Decision step 'Approve Leave?' is missing a YES edge."

**Warnings** (do not block publishing, but worth fixing):
- Any non-START step with no incoming connection is flagged as unreachable, e.g. "Step 'Send
  Notification' has no incoming edges (unreachable)."
- An APPROVAL-type step missing an APPROVE or REJECT edge produces a warning (not an error) for
  each missing edge type.

## 3. Publish

Click **🚀 Publish**. This opens a confirmation modal ("🚀 Publish Workflow") explaining: "Creating
an immutable version snapshot. Work orders will use this version." You can optionally add
**Version Notes** describing what changed. Click **Confirm Publish** to finish.

Before publishing, the app auto-saves any unsaved canvas changes. Once published:
- The workflow's status badge changes to **PUBLISHED** and its version number increments.
- The **🚀 Publish** button disappears from the toolbar for an already-published workflow (you can
  still Save and Validate further edits, which will apply to the next version when re-published).
- Only **published** workflows are selectable when launching a new Work Order instance — draft
  workflows cannot be run.

If publish fails (e.g. the backend rejects it), an alert shows the server's error message, or a
generic "Publish failed" message.
