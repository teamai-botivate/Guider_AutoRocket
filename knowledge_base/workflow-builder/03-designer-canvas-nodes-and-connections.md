---
title: Using the Designer Canvas - Nodes and Connections
module: workflow_builder
tags: [workflow-builder, canvas, nodes, react-flow, drag-and-drop]
---

# Using the Designer Canvas

The Designer canvas (`/workflowBuilder/designer/[id]`) is a drag-and-drop visual editor built on
`@xyflow/react`. Layout: a **Step Types** palette on the left, the canvas in the middle, and a
configuration panel on the right (Properties Panel when a step is selected, or a "Configure a
Step" placeholder plus workflow info when nothing is selected).

## 1. Step types you can add

Drag any of these from the left **Step Types** palette onto the canvas:

| Step type | Palette label | Hint shown | Behavior |
|---|---|---|---|
| START | Start | Entry point | Auto-created; only one allowed per workflow. Cannot be deleted. |
| FORM | Form Step | Custom fields | A step that collects data via a configurable form. |
| DECISION | Decision | YES / NO branch | A diamond-shaped branch node with two required outgoing paths, **YES** and **NO**. |
| NOTIFICATION | Notification | Send alert | Sends an automated alert. |
| END | End | Terminal node | Marks flow completion. Can have multiple END nodes; each can be individually removed via its cut (✂) icon. |

Every new workflow starts with a **Start** node already on the canvas. Dragging a second Start
node onto the canvas is blocked with the message: "A workflow can only have one Start node."

> Note: form field data on a FORM step can also produce **APPROVE/REJECT** branching if the step
> is treated as an approval step downstream — see the Decision Routing doc for how that mapping
> works via the Decision node's condition config.

## 2. Adding a node

1. In the left **Step Types** panel, click-and-drag a step type card onto the canvas.
2. Drop it where you want it positioned. It's added with an auto-generated ID and immediately
   selected, opening the **Properties Panel** on the right so you can name/configure it right away.

## 3. Connecting nodes

Each node exposes connection handles (small dots on its edges):
- **START**: one output handle (bottom).
- **FORM / NOTIFICATION**: one input handle (top) and one output handle (bottom).
- **DECISION**: one input handle (top), plus two labeled output handles — **YES** (right, green)
  and **NO** (left, red).
- **END**: one input handle (top) only.

To connect two nodes, click and drag from a source node's output handle to a target node's input
handle. The connection is drawn as a smooth step line and automatically colored/labeled based on
which handle it came from:

| Source handle | Edge type | Line color | Label |
|---|---|---|---|
| (default output) | ALWAYS | gray | (none) |
| `yes` (Decision) | YES | green, dashed | "Yes" |
| `no` (Decision) | NO | red, dashed | "No" |
| `approve` | APPROVE | green | "✓ Approve" |
| `reject` | REJECT | red | "✗ Reject" |
| `failure` | FAILURE | red | "Failure" |

## 4. Selecting, editing, and deleting

- **Click a node** to select it and open its Properties Panel.
- **Click a connection (edge)** to select it; a **✂ Remove Connection** button appears in the
  top-right floating panel.
- **Delete/Backspace key**: with a node or edge selected (and you're not typing in a text field),
  pressing Delete or Backspace removes it. Edges are deleted before nodes if both are somehow
  selected. The START node is protected and cannot be deleted this way.
- **Hover delete button**: FORM, NOTIFICATION (and other non-Start/End) nodes show a small red
  **×** button in the top-right corner on hover — click it, confirm the browser prompt ("Delete
  this node and all its connections?"), and it's removed.
- **END node removal**: hover an END node to reveal a red **✂** (scissors) button; clicking it
  confirms "Remove the END node and all its connections?" before deleting.
- A floating hint at the bottom of the canvas reminds you: "Press Delete or Backspace to remove
  selected node/connection" whenever something is selected.

## 5. Canvas controls

Top-right floating panel and standard React Flow controls provide:
- **↕ Auto Layout** — automatically re-arranges all nodes into a single vertical column (Start
  first, End last, 140px vertical spacing), useful to tidy up a messy canvas.
- Standard zoom/pan controls (bottom-left) and a **MiniMap** (bottom-right) showing an overview of
  the whole graph, color-coded by step type (Start=green, End=red, Form=blue,
  Notification=cyan, Decision=amber).
- Background dot grid for visual alignment; canvas supports free positioning (no snap-to-grid).

If the canvas has no nodes yet (a brand-new or emptied workflow), it shows a placeholder: "Empty
Designer Canvas — Drag elements like Start, Form Step, Notification etc. from the left palette
onto this area."
