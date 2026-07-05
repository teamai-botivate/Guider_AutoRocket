---
title: Dispatch Planning, Approvals, and Logistics
module: order_to_dispatch
tags: [order-to-dispatch, dispatch-planning, account-approval, logistic, test-report]
---

# Dispatch Planning, Approvals, and Logistics

This covers the stages between an approved order and the goods leaving the warehouse: Check for Delivery, Dispatch Planning, Account Approval, Logistic, and Test Report.

## 1. Check for Delivery

1. Open **Order to Dispatch > Check for Delivery** (`/order2dispatch/check-delivery`). Header: "Check for Delivery — Quantity-driven stage tracking — process, cancel, or reject per item."
2. In the **Pending** tab, click **Check** on an order row (or **Process** on mobile) to open the "Check for Delivery" dialog. Click **Details** to expand PO/customer/Check-PO summary information first if needed.
3. Review the Item Details (ordered quantity, rate, amount per line).
4. Set **Stock Availability** (required) to one of:
   - **In Stock** — reveals extra fields: Production Order No., Qty Transferred, Batch Remarks.
   - **For Production Planning** — on save, you are redirected to the Production Planning orders screen.
   - **From Purchase** — opens a **Purchase Indent** popup (pre-filled with the order's items) so you can raise a purchase indent immediately.
5. Click **Save Check** to confirm, or **Cancel** to close without saving.
6. The order then appears in **Dispatch Planning**'s pending queue with its confirmed availability.

Use the **Columns** button (top right of the table) to show/hide columns such as Planned, Delay, Order Items, PO/Order Date, PO Value, Delivery dates, Availability, Submitted At/By, and Status. Filter by **Company**, **Transport**, or **Availability** using the dropdowns above the table.

## 2. Dispatch Planning

1. Open **Order to Dispatch > Dispatch Planning** (`/order2dispatch/dispatch-planning`). Header: "Dispatch Planning — Plan and schedule order dispatches."
2. Click **Plan** on a pending order row to open the "Dispatch Planning" dialog.
3. Set the **Final Delivery Date (Committed)**.
4. Review **Check for Delivery Items** (previous-stage confirmed quantities) for reference.
5. Under **Dispatch Quantities**, for each item: check its selection box, and enter a **Dispatch Qty** (capped at the item's pending quantity — order qty minus what's already been planned in earlier plans). Items can be partially planned across multiple dispatch plans.
6. Click **Create Dispatch Plan** to save (disabled until at least one item has a valid quantity), or **Cancel**.
7. A single order can have multiple dispatch plans over time (visible via the "Plan Details"/"plan(s)" badge in History).

## 3. Account Approval

1. Open **Order to Dispatch > Account Approval** (`/order2dispatch/account-approval`). Header: "Account Approval — Approve dispatch plans before logistics processing."
2. In **Pending**, click **Process** on a dispatch plan row. Expand **Details** in the dialog to review PO/customer info and the full Dispatch Plan Items list (order qty vs. quantity to dispatch, per item).
3. Set **Status** to **Approve** or **Reject**, and optionally add **Remarks**.
4. Click **Approve** (green) or **Reject** (red) to submit, or **Cancel**.
5. Only approved dispatch plans proceed to Logistic.

## 4. Logistic

1. Open **Order to Dispatch > Logistic** (`/order2dispatch/logistic`).
2. Click **Logistic** on a pending order row to open the "Logistic" dialog.
3. If the order has more than one dispatch plan, choose which one via **Select Dispatch Plan**.
4. Under **Select Items to Dispatch**, check the items to include in this shipment (each shows Order Qty, Dispatch Qty, UOM); unchecked items are skipped for this run.
5. Fill in **Transport Details**:
   - **Transporter Name** (required) — chosen from vendors of type Transport.
   - **Truck No**, **Driver Name**, **Driver Mobile No**, **Bilty No**, **Bilty Image** (file upload).
   - **Type Of Rate** — **Fix Amount**, **Per Matric Ton rate**, or **Ex Factory Transporter**; selecting Fix Amount reveals a **Fixed Amount** field, the other two reveal a **Rate Per Metric Ton** field.
6. Click **Submit Logistic (N items)** to save (button is disabled until a transporter, dispatch plan, and at least one item are selected), or **Cancel**.
7. This step creates a Dispatch record and its associated Logistic (shipment) record, which downstream stages (Test Report, Invoice, Wetman Entry, Confirm Receipt) reference.

## 5. Test Report

1. Open **Order to Dispatch > Test Report** (`/order2dispatch/test-report`).
2. Click **Test** on a pending dispatch row to open the "Test Report" dialog. Expand **Details** for PO, dispatch, and logistic context (transporter, truck, driver, bilty).
3. For each dispatch item, tick its checkbox to include it, then set:
   - **Status*** — **Approved** or **Rejected**.
   - **Report File** — optional upload (image or PDF) of the test/quality report.
4. Click **Submit Test Report (N items)** (enabled once at least one item is selected and has a status), or **Cancel**.
5. Selected items' results ("Approved"/"Rejected") then appear in the History tab's Test Result column.
