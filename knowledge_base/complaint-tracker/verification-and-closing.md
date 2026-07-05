---
title: Verifying, Closing, and Reopening a Complaint
module: complaint_tracker
tags: [complaint-tracker, verification, document-verification, closing, reopen, approved]
---

## How a complaint gets verified and closed

Once a technician marks their work **Completed**, the complaint enters a two-stage sign-off before it's fully closed: manager **Verification**, then **Document Verification**.

### Step 1 — Manager Verification (`/complaint-tracker/verification`)
1. Open **Complaint Tracker → Verification**. The page is titled "Verification" ("Verify completed tasks and complaints").
2. The **Pending Verification** tab lists completed jobs awaiting sign-off, with columns: Complaint ID, Beneficiary, Technician, Completed Date, Remarks, Created At, Planned At, Delay, Actions.
3. For each row you can:
   - Click **Approve** to accept the work. This closes the complaint (status becomes **Closed**) and records the actual close date/time.
   - Click **Reject** to send it back. This opens a "Reject — <Complaint ID>" modal with an optional **Rejection Remarks** textarea and a **Reject** button. Rejecting sends the complaint back to **In Progress** so the technician can redo the work — it does not delete or discard the original job.
4. The **Verified Tasks** tab shows the history of everything already approved or rejected, with columns including Verified By, Verified Date, and a Status badge ("Approved" or "Rejected").

### Step 2 — Document Verification (`/complaint-tracker/document-verification`)
1. Open **Complaint Tracker → Document Verification** ("Verify and archive documents for closed complaints before final approval").
2. Three summary cards show: **Pending Doc Verification**, **Documents Verified**, **Total Reviewed** counts.
3. The **Pending Verification** tab (note: same tab label as the previous screen, but this is a distinct queue) lists complaints that are already **Closed** and awaiting document sign-off, with columns: Complaint ID, Beneficiary, District, Technician, Closed Date, Work Notes, Created At, Planned At, Delay, Action.
4. Click **Verify Documents** on a row to open a "Confirm Document Verification" dialog summarizing Beneficiary, District, Closed date, and Technician, then click **Confirm Verification** to finalize (or **Cancel**).
5. Once confirmed, the item moves to the **Verified Documents** tab, shown with a "Doc Verified" status badge — this is the final archival state of the complaint.

### Approved Complaints view (`/complaint-tracker/approved`)
This screen ("Approved Complaints" — "View all approved and closed complaints") is a read-oriented list of everything that has reached **Closed** status, with a search box (search by ID, beneficiary name, or district) and summary cards for **Total Approved**, **This Month**, and **Avg. Approval Time** (this last stat is not currently computed and always shows "—").
- Each row shows a **Closed** status badge and a **Reopen** action. Clicking **Reopen** prompts "Confirm reopen?" with **Yes**/**Cancel** — confirming sends the complaint back to **Assigned** status (clearing its close date) so it re-enters the assignment/tracking workflow from that point.

### Checking complaint history/status generally
- **Tracker** (`/complaint-tracker/tracker`) is the general-purpose in-progress tracking screen: its **Pending Tasks** tab shows all complaints currently Assigned or In Progress (with an Update action to move status forward — e.g. Assigned → In Progress → Completed — and an optional remarks field), and items already at "Pending Verification" show as "Awaiting Verification" instead of an Update button. Its **History** tab shows everything that has completed that stage, with Created At/Processed At/Planned At timestamps and a Delay indicator.
- **Report** (`/complaint-tracker/report`) provides date-range-filterable analytics: overview stats, a district-by-district breakdown (Total/Resolved/Pending/Resolution %), technician performance (Assigned/Completed/Completion %), a trend view, and a **CSV export** button for the district and technician tables.
- The main **Dashboard** (`/complaint-tracker`, the "Dashboard" nav item) shows overall stat cards, a searchable/status-filterable complaints table, and a by-region breakdown — the fastest place to check the current status of any specific complaint or scan overall load.

### Status lifecycle summary
Open → Assigned → In Progress → (Completed by technician) → Pending Verification → (Manager Approves) → Closed → (Document Verification confirmed) → archived/"Doc Verified". A manager **Reject** at the Verification step sends it back to In Progress; a **Reopen** from the Approved list sends a Closed complaint back to Assigned.
