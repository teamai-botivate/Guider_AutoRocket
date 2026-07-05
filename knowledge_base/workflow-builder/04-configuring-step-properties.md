---
title: Configuring Step Properties and Form Fields
module: workflow_builder
tags: [workflow-builder, properties-panel, form-fields, step-configuration]
---

# Configuring Step Properties and Form Fields

Clicking any node on the Designer canvas opens the **Properties Panel** on the right. Its header
shows the step's name and its type (e.g. "FORM Step"). For non-Start steps, two tabs appear:
**Properties** and **Form Fields** (the latter shows a badge with the current field count).

## 1. Properties tab

Fields available (Start nodes only get "Step Name"; all other step types get the full set):

- **Step Name*** — required text field, e.g. "Quality Control Inspection".
- **Description** — free text describing what happens in this step.
- **Department** — a dropdown populated from your organization's departments
  (`/settings/user-departments`). Selecting a department resets the Assigned Users field.
- **Assigned Users** — a multi-select dropdown of users belonging to the selected department
  (disabled with placeholder "Select a department first" until a department is chosen). Includes
  a "Select All" checkbox and shows a live count badge of how many are selected.
- **Timing Configuration** — an "Estimated Duration" number field plus a **Unit** dropdown
  (Minutes / Hours / Days). This value is used elsewhere (Work Order execution view) to compute
  each step's planned/expected time and flag delays.
- **Decision Condition** (DECISION steps only) — see the dedicated Decision Routing doc.
- **Delete Step** button at the bottom (labeled "✂ Remove End Node" for END steps, "🗑 Delete
  Step" otherwise) — asks for confirmation before removing.

## 2. Form Fields tab

Only shown for non-Start steps. This is where you build the custom data-entry form users fill out
when they reach this step during execution. Click **Form Fields** tab, then use the **Add Field**
row of buttons to add a field of any of these types:

| Field type | Icon |
|---|---|
| Text | 📝 |
| Number | 🔢 |
| Textarea | 📄 |
| Dropdown (select) | 🔽 |
| Multi-select | ☑️ |
| Checkbox | ✅ |
| Date | 📅 |
| Time | 🕐 |
| Rating | ⭐ |
| File Upload | 📎 |
| Email | 📧 |
| Phone | 📞 |

Each added field appears as a collapsible row; click it to expand and configure:

- **Label*** — the field's display name (auto-generates a slugified **Field Key** the first time
  you type, e.g. "Employee Name" → `employee_name`). You can manually override the Field Key.
- **Auto-fill (Linked Field)** — if other fields on the same form pull from a master data source
  (see Data Source below), you can link this field to auto-fill from one of those linked records'
  attributes ("Field to Pull").
- **Data Source** (Dropdown/Multi-select fields only) — choose where the options come from:
  - Static Options (Manual)
  - 👥 HR Employees
  - 🏢 Vendors Module
  - 📦 Products Module
  - 🏬 Inventory Module
  - 👥 Staff / Users
  - 🏛️ Departments
  - 🏪 Warehouses
  - 📋 Workflow Records (Custom) — pulls from a prior workflow's work order records; requires
    entering a **Source Workflow ID**.
  - When a non-static source is chosen, a **Display Fields (Label)** selector lets you pick which
    fields from that data source appear in the dropdown label.
- **Options** (Static data source only) — a textarea, one option per line.
- **Placeholder** — hint text shown in the empty field (not available for checkbox/file/date/
  time/rating fields).
- **Rating Settings** (Rating fields only) — choose Max Rating of **5 Stars** or **10 Stars**, with
  a live preview.
- **File Upload Settings** (File fields only):
  - Single File vs Multiple Files toggle.
  - Max File Size (MB) — free entry or quick-pick buttons: 1 / 5 / 10 / 25 / 50 MB.
  - Allowed File Types — checkboxes for Image, PDF, Document, Spreadsheet, Presentation, Video,
    Audio, Archive (each maps to specific file extensions).
- **Validation Rules** (Text/Phone/Email/Textarea fields) — Max Length (all of these), plus Min
  Length specifically for Phone fields.
- **Required field** checkbox.
- **Conditional Visibility** — make this field only appear when another Dropdown field (with
  static options, appearing earlier in the form) equals a specific value. Configure "Depends on
  dropdown" then "Show when value is". Until a trigger value is picked, the field stays hidden.

Use the **↑ / ↓** arrows on a field's header row to reorder fields, and **×** to remove a field.
If no fields have been added yet, the panel shows: "No fields yet — add one above."
