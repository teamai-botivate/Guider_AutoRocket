---
title: Decision Nodes and Conditional Routing
module: workflow_builder
tags: [workflow-builder, decision-node, conditions, branching, routing]
---

# Decision Nodes and Conditional Routing

A **Decision** step lets your workflow branch into two paths based on a value entered earlier in
the flow. It's shown on the canvas as an amber diamond with two labeled output handles: **YES**
(right, green) and **NO** (left, red).

## 1. Basic setup

1. Drag a **Decision** node from the palette onto the canvas.
2. Connect the preceding step's output into the Decision node's top (input) handle.
3. Draw two separate outgoing connections from the Decision node: one from the **YES** handle to
   whichever step should run if the condition is true, and one from the **NO** handle to whichever
   step should run otherwise.
4. Both a YES and a NO edge are required — the Validate step (see the Publishing doc) will flag a
   Decision node missing either one as an error.

## 2. Auto-routing based on a form field (Decision Condition config)

Click the Decision node to open its Properties Panel, then scroll to the **◆ Decision Condition**
section (Properties tab). This lets you automatically route YES/NO based on what was submitted in
the *immediately preceding connected step's* form:

- If no step is connected before the Decision node, you'll see: "Connect a Form step before this
  Decision node to configure auto-routing."
- If the connected step has no form fields yet, you'll see: "Parent step '<name>' has no form
  fields. Add fields first."
- Otherwise:
  1. Choose **Evaluate field** — pick which of the parent step's form fields to check.
  2. For each outgoing route already drawn from this Decision node (e.g. YES, NO), a
     **Value → Route mapping** box appears. If the evaluated field is a Dropdown/Multi-select/
     Radio type, you check off which option value(s) should trigger that route. For free-text
     fields, you type comma-separated values (e.g. "yes, approved, true").
  3. If there is more than one outgoing route, you can set a **Default route (if no match)** —
     which path to take if the submitted value doesn't match any configured rule.

This mechanism also supports **APPROVE/REJECT** style routing if the preceding connections use
those edge types instead of YES/NO — the same value-to-route mapping UI applies.

## 3. How this plays out during execution

When a work order reaches a Decision step during execution, the person executing it is shown
**✓ Yes** and **✗ No** buttons (or **✓ Approve** / **✗ Reject** if the step is configured as an
approval-style gate) instead of a form to fill in. Clicking one submits that choice as the routing
action, and the work order advances along the matching edge.
