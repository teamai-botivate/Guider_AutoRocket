---
title: Enquiry Tracking – Managing and Processing Sales Enquiries
module: lead_to_order
tags: [lead-to-order, enquiry, enquiry-tracking, sales, quotation]
---

## Overview

**Lead To Order → Enquiry Tracking** (path `/lead-to-order/enquiry-tracking`) is the central screen for tracking every enquiry from creation through quotation to final order outcome. Enquiries here are created automatically from Call Tracker when a call is logged as "Enquiry Received," or manually.

## Viewing and filtering enquiries

1. Open **Lead To Order → Enquiry Tracking**. Two tabs are shown: **Pending** and **History**.
2. On **Pending**, use the Company / Customer filters and the **Status** dropdown to narrow the list: *Quotation Revised*, *New Quotation Pending*, *Quotation Pending*, *Quotation Sent*.
3. On **History**, the Status filter shows outcomes: *Order Received*, *Order Not Received*, *On Hold*.
4. Each row shows Lead No., Enquiry No., customer, company, SC Name, source, location, items/quantities, and (on Pending) the linked quotation number and value if one exists.
5. Click **View** on any row to open the full **Enquiry Details** dialog, which includes customer info, processing status, item list (editable while no quotation has been sent yet, via **Edit Products**), sent-quotation summary (once a quotation has actually been shared with the customer), notes, product change history, and a full chronological **Processing History** timeline (lead created → calls → quotation created/sent/revised → order outcome).
6. Click **See Copy** (where shown) to preview the attached quotation in the **Quotation Copy** popup without leaving the page.

## Creating an enquiry manually

1. From the Enquiry Tracking page, use the **New Enquiry** creation flow (dialog) if you need to add an enquiry directly rather than via Call Tracker.
2. Fill in **Contact Name** (required), **Mobile Number** (required), optional **Company Name** (dropdown of vendors), and **Enquiry Status** (Enquiry Received / Expected / Not Interested).
3. Add **Products & Quantity** rows with **Add Product**, selecting a product and entering quantity for each; remove rows with the trash icon.
4. Click **Create Enquiry** to save.

## Processing an enquiry (moving it forward)

1. On the **Pending** tab, click **Process** on an enquiry that has status `PENDING`. This opens the **Process Enquiry** dialog.
2. Choose the **Current Stage**:
   - **Order Expected** — still negotiating/awaiting decision; requires a **Next Call Date** (and optional time) to schedule follow-up.
   - **Negotiation** — same as Order Expected (also requires next call date/time).
   - **Order Received** — customer confirmed the order. Requires **PO Number**, optional PO Date, PO Value, Requested Delivery date, Transport Type (FOR / Ex Factory / Ex Factory But Paid by Us), and a **Final Order Items** list (product, PO Qty, Rate) pre-populated from the quotation/lead items — edit quantities/rates/remarks as needed to match the actual PO.
   - **Order Not Received** — mark the enquiry closed without an order; requires a reason in "Reason for not receiving order."
   - **On Hold** — neither confirmed nor cancelled.
3. Enter **Customer Says** (required) describing the call/decision.
4. Click **Complete Processing** to save. Selecting **Order Received** automatically creates a corresponding order in the **Order 2 Dispatch** module using the PO details and final item list entered here — no separate manual order-creation step is needed.

## After processing

- Enquiries marked **Order Received** move into the **Order Received** view (see "Order Outcomes" guide) and also appear in Order 2 Dispatch.
- Enquiries marked **Order Not Received** move into the **Order Not Received** view.
- Enquiries still needing a quotation appear in **Pending Quotation** (see that guide) until a quotation is created and attached.
