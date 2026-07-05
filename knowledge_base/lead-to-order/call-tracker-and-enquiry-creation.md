---
title: Call Tracker – Logging Calls and Converting a Lead into an Enquiry
module: lead_to_order
tags: [lead-to-order, call-tracker, enquiry, follow-up, sales]
---

## Overview

After a lead is created, it appears in **Lead To Order → Call Tracker** (path `/lead-to-order/call-tracker`) waiting for a follow-up call. This is where a lead's interest is recorded and — if positive — turned into a formal **Enquiry**, which is the trigger for quotation work.

## Steps to log a call and process a lead

1. Open **Lead To Order → Call Tracker**. The page has two tabs: **Pending** (leads/follow-ups awaiting a call) and **History** (calls already logged).
2. On the **Pending** tab, use the **Company**, **Person**, **Phone**, and **Date** filters (Today / Overdue / Upcoming) or the search box to find the lead you need to call. Each row shows the Lead No., company, contact person, and a "Planned At" / "Delay" indicator (On time or +Xd Xh Xm late).
3. Click **View** on a row to open the **Follow-up Details** dialog — this shows contact info, lead source, location, prior call history timeline, and current product requirements. From here you can also click **Edit Products** to add/change the product/quantity list attached to the lead before logging the call.
4. Click **Call Now →** on a row to open the **Log Call** dialog. Fill in:
   - **Contact Name** and **Contact Number** (pre-filled from the lead, editable).
   - **Status** (required) — choose one of:
     - **Enquiry Received** (`YES`) — customer is interested; this converts/creates an Enquiry.
     - **Expected** (`EXPECTED`) — still following up; schedules another call.
     - **Not Interested** (`NOT_INTERESTED`) — closes out this lead as uninterested.
5. If Status = **Enquiry Received**: fill in Enquiry Date, Approach (Incoming/Outgoing, required), and confirm/adjust the **Product Requirements** list (Select Product, Quantity, Spc/Remarks) using **Add Product** / trash icon to manage rows.
6. If Status = **Expected**: fill in **Next Action** (required, free text, e.g. "Call back for confirmation"), **Next Call Date** (required) and **Next Call Time** (optional) to schedule the follow-up.
7. Enter **Customer Says** (required) — free-text notes on what the customer said during the call.
8. Click **Save Call Log**. This records the call in history and, if the status was "Enquiry Received," creates/advances the corresponding **Enquiry** record (visible next in **Enquiry Tracking**).
9. The **History** tab shows all past calls with columns for company, customer say, status, call date/time, created/processed timestamps, and a Delay badge comparing actual processing time to the planned TAT. Rows here can be **Edit**ed (e.g. correcting Customer Say, next call date/time) via inline edit/save/cancel controls.

## Notes

- "Delay"/TAT badges throughout Call Tracker and Enquiry Tracking compare the actual call/processing time against a system-planned target time; "On time" (green) vs "+Xd Xh Xm" (red, late).
- The Call Tracker's product list on a lead can also be edited outside of logging a call, via the **View → Edit Products** action in the Follow-up Details dialog, and every product/quantity edit is tracked in a "Product Change History" timeline (labelled Initial Add / Via Call / Manual Edit).
