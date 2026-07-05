---
title: Doc SubManager - Loans, Foreclosure Requests, and NOC Collection
module: doc_sub_manager
tags: [doc-submanager, loans, foreclosure, rfc, noc, settlement]
---

# Managing Loans in Doc SubManager

Loans are tracked under **Doc Submanager > Loan** in the sidebar, with three linked pages: **All Loans**, **Request Foreclosure**, and **Collect NOC**. The loan lifecycle in the UI moves a loan record through several status fields on the same record (not separate approval endpoints): active → foreclosure requested → documents collected → NOC collected → final settlement.

## 1. Create a new loan

1. Go to **Doc Submanager > Loan > All Loans** (`/doc-submanager/loan/all`).
2. Click **Add** in the page header to open the **Add New Loan** modal.
3. Fill in:
   - **Loan Name** (searchable dropdown/free text, e.g. "Home Loan")
   - **Bank Name** (searchable dropdown/free text, e.g. "HDFC Bank")
   - **Amount** (free text, e.g. "₹50,00,000")
   - **EMI** (free text, e.g. "₹45,000")
   - **Loan Start Date** and **Loan End Date**
   - **Provided Document Name** (searchable dropdown, e.g. "Agreement Copy") plus an **Attach document (PDF, image)** file picker next to it
   - **Remarks** (optional free text)
4. Click **Save Loan** (shows "Uploading…" while submitting) or **Cancel**.
5. The new loan appears in the **All Loans** table with columns: S.No, Loan Details (name + bank), Financials (amount + EMI), Duration (start/end date), Documents & Remarks, and a **Status** badge: Active, Requested for Closure, Approved for Closure, or Closed.

## 2. Request loan foreclosure (early closure)

1. Go to **Doc Submanager > Loan > Request Foreclosure** (`/doc-submanager/loan/foreclosure`), titled "Loan Foreclosure".
2. The page has **Pending** and **History** tabs.
3. On **Pending**, find the loan (not yet requested for foreclosure) and click **Action**.
4. In the **Foreclosure Action** modal, confirm the loan/bank shown, then fill in:
   - **Request Date**
   - **Requester Name**
5. Click **Save**. This sets the loan's foreclosure status to "Pending" and moves it to the **History** tab, which shows a **Foreclosure Status** badge (Pending / Approved / Rejected / Closed).

> Note: the UI's foreclosure action only records the request (sets status to "Pending"); it does not expose separate Approve/Reject buttons in this screen. The backend does provide a dedicated `PATCH /doc-submanager/loan/:id/approve-rfc` endpoint (accepting `status`: Approved/Rejected and `remarks`) for approving/rejecting the closure request, but the current front-end loan pages update status generically rather than calling that endpoint directly.

## 3. Collect NOC (No Objection Certificate)

1. Go to **Doc Submanager > Loan > Collect NOC** (`/doc-submanager/loan/noc`), titled "NOC Collection".
2. **Pending** tab lists loans where documents have been collected or foreclosure is requested, but NOC status isn't set yet. Click **Action** on a row.
3. In the **Update NOC Status** modal, confirm loan/bank, then choose **Collect NOC**: **Yes** or **No** from the dropdown.
4. Click **Save**. Loans with an NOC status set move to the **History** tab, showing the **NOC Status** badge.

> Note: the backend also exposes a dedicated `POST /doc-submanager/loan/attach-noc` (multipart) endpoint that accepts `id`, `file` (the NOC document), `settlementDate`, and `remarks` for formally attaching the NOC file — the "Collect NOC" screen in the current UI only toggles a Yes/No status field rather than uploading a file through this screen.

## 4. Collect documents for foreclosure (loan/documents route)

Although not linked in the main sidebar, the app has a **Collect All Documents** page at `/doc-submanager/loan/documents`, reachable directly by URL:
1. **Pending** tab shows loans where foreclosure is requested but document status isn't set. Click **Action**.
2. In the **Collect Documents** modal, set **Document Status** to **Collected** or **Pending**, and optionally add **Remarks**.
3. Click **Save Collection**. This feeds into the "Collect NOC" pending list once marked Collected.

## 5. Final settlement (loan/settlement route)

Also reachable directly at `/doc-submanager/loan/settlement` (not in the main sidebar):
1. **Pending** tab shows loans where NOC has been collected ("Yes") but final settlement isn't complete. Click **Action**.
2. In the **Final Settlement** modal, choose:
   - **Final Settlement**: "Yes, Settled" or "No, Pending"
   - If "No, Pending" is chosen, a **Next Date** field appears to schedule a follow-up.
3. Click **Save Settlement**. Loans marked "Yes, Settled" move to the **History** tab, showing the Settlement status and settlement date, and the loan's overall status becomes "Closed" on the All Loans page.

## Status flow summary

Active loan → **Request Foreclosure** (sets foreclosure status to Pending) → **Collect All Documents** (marks document status Collected) → **Collect NOC** (marks NOC Yes/No) → **Final Settlement** (marks settled, loan becomes Closed).
