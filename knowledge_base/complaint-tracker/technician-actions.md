---
title: Technician Actions on Assigned Complaints
module: complaint_tracker
tags: [complaint-tracker, technician, start-work, mark-complete, field-work]
---

## How a technician works an assigned complaint

Technicians use two related screens — both require picking your name from a **Select Technician** dropdown first (there is no separate technician login; a supervisor or the technician selects their own name from the list, which also shows their Contact and WhatsApp number once selected).

### Technician Dashboard (`/complaint-tracker/technician-dashboard`)
1. Open **Complaint Tracker → Technician Dashboard**.
2. Pick your name from the **Select Technician** dropdown.
3. Four stat cards appear: **Assigned**, **In Progress**, **Completed**, **Pending Verification** — counts of your tasks in each stage.
4. Below that, the **My Tasks** table lists your tasks with columns: Complaint ID, Beneficiary, District, Nature, Priority (High/other, shown as a colored badge), and Action.
5. For any task still in **Assigned** status, click **Start Work** in the Action column — this moves the complaint to **In Progress** and shows a toast "Status updated to In Progress". For tasks already past that stage, the Action column just displays the current status as text (no button).

### My Complaint Tracker (`/complaint-tracker/technician-tracker`)
This is the more detailed, card-based view of the same assigned work, titled "My Complaint Tracker" ("Track and update your assigned complaints").
1. Select your name from **Select Technician** as above.
2. Each assigned complaint shows as a card with: Complaint ID and Beneficiary name in the header, a status badge, and detail fields (Contact, Village, District, Started date) plus the Nature of the complaint.
3. Available actions depend on current status:
   - **Assigned** → click **Start Work** to move to **In Progress**.
   - **In Progress** → click **Mark Complete** to finish the job, or **Add Remarks** to attach a note without changing status (opens a "Add Remarks — <Complaint ID>" modal with a Remarks textarea and a **Save** button).
   - Any status → click **View Details** to open a slide-out panel on the right showing Beneficiary, Contact, Village, District, Nature of Complaint, Status, Priority, and Started date.
4. Marking a task **Completed** moves it out of the technician's active list and into the **Verification** stage for a supervisor/admin to review (see "Verifying and Closing a Complaint").

### Notes on status wording
The technician-facing UI uses the button label "Mark Complete" but the underlying/tracker status after verification is pending is displayed elsewhere as "Pending Verification" — completing a task does not close it outright; it queues the item for admin verification.
