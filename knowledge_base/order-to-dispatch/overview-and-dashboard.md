---
title: Order-to-Dispatch Overview and Dashboard
module: order_to_dispatch
tags: [order-to-dispatch, dashboard, pipeline, overview]
---

# Order-to-Dispatch: Overview and Dashboard

The **Order-to-Dispatch** module manages the full lifecycle of a customer purchase order — from order entry through delivery checks, dispatch planning, approvals, logistics, invoicing, and material returns. It is a system-level module (not tenant business-domain-only) found under **Order to Dispatch** in the left sidebar.

## 1. Navigating the module

1. In the left sidebar, open the **Order to Dispatch** section. Its sub-links, in order, are:
   - Dashboard (`/order2dispatch/dashboard`)
   - Order (`/order2dispatch/order`)
   - Check for Delivery (`/order2dispatch/check-delivery`)
   - Dispatch Planning (`/order2dispatch/dispatch-planning`)
   - Account Approval (`/order2dispatch/account-approval`)
   - Logistic (`/order2dispatch/logistic`)
   - Test Report (`/order2dispatch/test-report`)
   - Invoice (`/order2dispatch/invoice`)
   - Confirm Receipt (`/order2dispatch/confirm-receipt`)
   - Material Return (`/order2dispatch/material-return`)
   - Management Approval (`/order2dispatch/department-approval`)
   - Credit Note (`/order2dispatch/credit-note`)
   - Return of Material (`/order2dispatch/return-of-material`)

## 2. Reading the Dashboard

1. Open **Order to Dispatch > Dashboard**. The header reads "Order to Dispatch — Real-time pipeline overview · all 12 stages."
2. Click **Refresh** (top right) at any time to reload the latest numbers.
3. The **KPI row** shows six tiles: Total Orders, Dispatched, Invoiced, Receipts Done, Credit Notes, and Pending Actions (the sum of all pending counts across stages). Clicking most tiles jumps to the related stage page.
4. If any stage has pending work, a **Needs Attention** section appears above the pipeline map, listing each bottleneck stage with its pending count — click a card to jump straight to that stage's pending queue.
5. The **Pipeline Status** panel shows all 12 stages as numbered circles (1–12): Check Delivery, Dispatch Plan, Account Approval, Dept Approval, Logistic, Test Report, Invoice, Mgmt Approval, Confirm Receipt, Material Return, Credit Note, Return. Circles are colored amber (pending work exists), green (clear), or gray (no data). Click any circle to navigate to that stage.
6. Below that, **Top Customers** and **Top Products** panels rank by order value and quantity ordered, respectively.
7. The **Order Value Funnel** chart shows the drop-off in count/amount from Total Orders → Dispatched → Invoiced → Receipts Done → Credit Notes.

## 3. The end-to-end pipeline (stage order)

An order moves through these stages in sequence (some stages can run per line-item, allowing partial progress):

1. **Order** — order/PO is created (see `order-creation.md`).
2. **Check PO** — internal verification/approval of PO quantities (reachable from Order records; see `order-creation.md`).
3. **Check for Delivery** — confirm stock availability and delivery feasibility (see `dispatch-and-logistics.md`).
4. **Dispatch Planning** — plan which items/quantities to dispatch and commit a final delivery date.
5. **Account Approval** — finance reviews and approves/rejects the dispatch plan.
6. **Logistic** — record transporter, vehicle, and driver details, and select items to load.
7. **Test Report** — record quality/test approval or rejection per dispatched item.
8. **Invoice** — generate the invoice / bill for dispatched items (see `invoicing.md`).
9. **Confirm Receipt** ("Mgmt Approval" stage 8 on the pipeline map / stage 9 "Confirm Receipt") — confirm the customer/party received the material.
10. **Material Return** — if a customer reports a problem, look up the invoice and file a return request per item (see `material-return-and-credit-note.md`).
11. **Management Approval** (Department Approval) — management reviews and approves/rejects the return.
12. **Credit Note** — finance issues a credit note for the approved return.
13. **Return of Material** — logs the physical return shipment back from the customer once the credit note exists.

Each stage screen in this module follows the same **Pending / History** tab pattern: the **Pending** tab lists records awaiting action at that stage, and **History** shows everything already processed with full audit details (submitted at, submitted by, remarks). Records typically expose a magnifying-glass **Eye** icon (view details) and a colored action button (e.g. **Process**, **Check**, **Plan**, **Logistic**, **Invoice**) to open the processing dialog.
