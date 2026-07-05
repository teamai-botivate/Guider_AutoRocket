---
title: Raising a New Complaint
module: complaint_tracker
tags: [complaint-tracker, new-complaint, intake, create-complaint]
---

## How to raise a new complaint

1. In the left sidebar, open **Complaint Tracker**, then click **New Complaint** (`/complaint-tracker/new-complaint`). This page is titled "Complaint Management" and lists all complaints logged so far, with a search bar to filter by company, technician, or beneficiary name.
2. Click the **New Complaint** button in the top-right corner. A form opens showing an auto-generated serial number (e.g. shown next to "New Complaint —" in the modal title).
3. Fill in the fields:
   - **Company Name** (required) — chosen from a dropdown of existing companies.
   - **Mode of Call** — free text, e.g. "Phone" or "WhatsApp".
   - **Project Name** — free text.
   - **Complaint Date** — date picker.
   - **Description** (optional, labeled "Description" but maps to the complaint's nature-of-complaint field) — a short free-text explanation of the issue.
   - A note under the title clarifies: "Beneficiary and product details can be filled in the Assign section" — so at intake you only need the basic company/call/date/description details; beneficiary, village, district, product, technician name, etc. are added later when the complaint is assigned.
4. Click **Submit Complaint** to save it, or **Cancel** to discard.
5. The new complaint appears in the table with columns: ID, Company, Mode of Call, Project, Description, Date, Created At, Status, Action. A newly created complaint starts in **Open** status (shown as a blue "Open" badge).
6. To edit a complaint later, click the **Edit** button on its row — this opens an "Edit Complaint" modal with the same fields (Company Name, Mode of Call, Project Name, Complaint Date, Description) and a **Save Changes** button.
7. Use the filter boxes above the table ("Search company…", "Search technician…", "Search beneficiary…") plus **Apply**/**Clear** buttons to narrow the list.

### Underlying status values
A complaint moves through these statuses as it's processed (shown as colored badges throughout the module): **Open** → **Assigned** → **In Progress** → **Verification** (pending manager verification) → **Closed**. This document only covers reaching the "Open" state; see the other Complaint Tracker articles for assignment, technician work, and verification/closing.

### Notes on unclear/generic UI text
- The "Description" field's placeholder text ("Briefly describe the nature of the complaint…") maps internally to a "nature of complaint" field, but the visible label a user sees is just "Description".
- The new-complaint form is intentionally minimal; the richer intake fields visible in raw API examples (vendor, beneficiary name, contact number, village/block/district, product/make/rating, insurance type, technician name, etc.) are not present on this screen — they get filled in later via the Assign Complaint screen, per the in-app note.
