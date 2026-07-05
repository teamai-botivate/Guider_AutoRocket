---
title: Pending Quotation – Creating and Attaching Quotations to Enquiries
module: lead_to_order
tags: [lead-to-order, quotation, pending-quotation, sales]
---

## Overview

**Lead To Order → Pending Quotation** (path `/lead-to-order/pending-quotation`) lists every enquiry currently sitting at the "Make Quotation" stage — i.e. it needs a quotation created and sent to the customer before the sale can move forward.

## Steps to create and attach a quotation

1. Open **Lead To Order → Pending Quotation**. The **Pending** tab lists enquiries awaiting a quotation, showing Lead No., Enquiry No., Company, SC Name, Source, Customer Info, Location, Customer Say, Call Date, Item Qty, Next Call Date, Created At, and Status (**Quotation Pending** or **Quotation Created/Revised** badges).
2. Click **View** on a row to inspect full enquiry details before quoting.
3. Click **Make Quotation** on the row. This navigates to **Lead To Order → Quotation** (`/lead-to-order/quotation?leadId=...&enquiryId=...`) with the lead and enquiry pre-linked. (This button is disabled — shown greyed out — if a quotation already exists for that lead.)
4. Build and save the quotation on the Quotation page (see the "Creating a Quotation" guide for the full field list). Saving there creates the quotation record tied to this lead/enquiry.
5. Once a quotation exists for the enquiry, its status changes and it can be reviewed/attached. Some flows also support directly **Attach**ing an already-created quotation to an enquiry — pick from the list of quotations for that lead, review each one's totals/items by clicking **View Details**, select the quotation to attach, add optional **Notes**, and click **Attach Quotation**. Quotations already sent to the customer are flagged **Already Sent**.
6. The **History** tab shows enquiries where a quotation has been sent — with a revision timeline per Enquiry No. (badges: **SENT**, **REV** for revisions) and a **See Copy** button to preview the quotation document.

## Notes

- "Pending" here specifically means `currentStage = MAKE_QUOTATION` and covers both first-time quotations and cases where a quotation was revised but not yet re-sent to the customer (shown as "Quotation Revised").
- Once an enquiry's quotation is sent/attached, it advances out of Pending Quotation and reappears in **Enquiry Tracking** to continue toward Order Received/Not Received.
