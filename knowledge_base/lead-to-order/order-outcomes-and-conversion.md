---
title: Converting an Enquiry to an Order (Order Received / Not Received)
module: lead_to_order
tags: [lead-to-order, order-conversion, order-received, order-not-received, order2dispatch]
---

## Overview

The final stage of the Lead-to-Order pipeline is recording whether an enquiry resulted in an actual order. This is done from **Enquiry Tracking** via the **Process** action, and the outcome is then browsable on dedicated **Order Received** / **Order Not Received** pages.

## Converting an enquiry into an order (the actual "conversion" step)

1. Go to **Lead To Order → Enquiry Tracking**, find the enquiry (Pending tab), and click **Process**.
2. In the **Process Enquiry** dialog, set **Current Stage** to **Order Received**.
3. Fill in the order-confirmation fields:
   - **PO Number** (required)
   - **PO Date** (optional)
   - **PO Value** (optional — a suggested total is shown based on item totals)
   - **Requested Delivery** date (optional)
   - **Transport Type** — FOR / Ex Factory / Ex Factory But paid by Us
   - **Final Order Items** — one row per product carried over from the quotation/lead, each with editable **PO Qty**, **Rate**, and **Remarks** to reflect exactly what was ordered (may differ slightly from the quotation).
4. Enter **Customer Says** (required) with any final notes.
5. Click **Complete Processing**.

Submitting this form does two things automatically:
- Marks the enquiry's order status as **Order Received** (`ordersReceivedStatus = YES`).
- **Creates a new order in the Order 2 Dispatch module** (an `O2DOrder` record, numbered like `DO-<FY>-###`, with `source = LEAD_TO_ORDER`) using the PO details and final item list you just entered — there is no separate manual step to push the order into Order 2 Dispatch.

## Marking an enquiry as not converted

1. From the same **Process Enquiry** dialog, choose **Order Not Received** as the Current Stage.
2. Enter the **Reason for not receiving order** (required) in the Customer Says field.
3. Click **Complete Processing**. The enquiry's order status becomes `ordersReceivedStatus = NO` and it is closed out (no order is created).

An **On Hold** stage is also available for enquiries that are neither confirmed nor cancelled yet.

## Reviewing outcomes

- **Lead To Order → Order Received** view: lists every enquiry where an order was received, showing Enquiry No., Customer, Company, Quotation No., Quotation Value, and Closed On date. **View** opens full enquiry details; **See Copy** opens the attached quotation document.
- **Lead To Order → Order Not Received** view: lists closed-without-order enquiries, with the same columns plus a **Reason** column (from Customer Says).
- Both views support search by enquiry number, customer name, or mobile number.

## Notes

- These two review pages (Order Received / Order Not Received) are reachable at `/lead-to-order/order-received` and `/lead-to-order/order-not-received`; they were not found as top-level sidebar links in the main navigation — they are most likely reached via links/filters from Enquiry Tracking's History tab (Order Status = "Order Received"/"Order Not Received") or bookmarked directly, since the sidebar's "Lead To Order" group otherwise lists Dashboard, Leads, Call Tracker, Pending Quotation, Quotation, and Enquiry Tracking only.
