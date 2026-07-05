---
title: Assigning a Complaint to a Technician
module: complaint_tracker
tags: [complaint-tracker, assignment, technician, dispatch]
---

## How to assign a complaint to a technician

1. In the sidebar, open **Complaint Tracker → Assign Complaint** (`/complaint-tracker/assign-complaint`). The page title is "Assign Complaint" with the subtitle "Review complaints and assign to technicians with full details".
2. The page has two tabs:
   - **Pending Assignments** — complaints that are logged but not yet assigned to a technician. Columns: Complaint ID, Company, Project, Mode of Call, Description, Date, Created At, Planned At (the internal TAT/SLA deadline for this stage), Action.
   - **Assignment History** — complaints already assigned, with columns: Complaint ID, Technician, Assigned Date, Status, Remarks, Created At, Planned At, Processed At, and a **Delay** badge ("On time" in green, or "+"/"−" with a duration in red/green showing how late/early the stage was actioned relative to its planned time).
3. On the **Pending Assignments** tab, click the **Assign** button on the row for the complaint you want to dispatch.
4. In the "Assign Complaint — <Complaint ID>" modal, under **Technician Assignment**:
   - Choose a **Technician** from the dropdown (required) — shown as name plus contact number if available.
   - Optionally add **Remarks** (assignment notes) as free text.
5. Click **Confirm Assignment** to save, or **Cancel** to back out. On success you'll see a toast: "Complaint <ID> assigned successfully".
6. Once assigned, the complaint's status changes from **Open** to **Assigned**, it moves out of the Pending tab into the technician's task list, and it appears in **Assignment History**.

### Notes
- Technicians themselves are set up elsewhere (a Technicians master list exists in the backend for creating technician records with name/contact/WhatsApp), but the day-to-day assignment flow only requires picking an existing technician from the dropdown on this screen.
- The "Planned At" / "Delay" columns reflect a configured turnaround-time (TAT) target for the assignment stage; if no TAT is configured for this stage, "Planned At" shows as "—".
