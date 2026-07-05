---
title: Work Order System (Project / Vendor Work Orders)
module: maintenance
tags: [work-order, quotation, approval, vendor, payment, warranty, project-tracking]
---

The **Work Order System** (routes under `/work-order/...`) is a *separate* feature from Maintenance Pro's machine maintenance tasks — despite the similar name, it is not about equipment upkeep. It manages outsourced/vendor **project work orders** (e.g., a renovation or contracted project) through a fixed pipeline: Quotation → Approval → Issue → Tracking → Payment → Warranty → Completed. Do not confuse this with the maintenance "work orders" (machine tasks) described in the Maintenance Pro completion/approval guide.

## Creating a work order

1. Go to **Work Order System > Create Work Order** (`/work-order/create`).
2. Fill in the required fields: **Priority** (Low/Medium/High), **Project Name**, **WO Type** (pick from existing types, or click **Add Type** to create a new one inline), **Party Name** (vendor — pick from existing vendors, or click **Add Party** to go to Settings > Vendors), **Department**, **Site Location**, **Currency**, **Total Work Value**, **Start Date**, **End Date**, and **Payment Terms**.
3. Define one or more **Project Stages** — each needs a Stage name, a Duration number, and a Duration Unit (Days/Weeks/Months). Use **Add Stage** to add more, or the trash icon to remove one (at least one stage is required).
4. Optionally attach a **Document** and add an internal **Remark**.
5. Click **Save Work Order** to create it (or **Reset** to clear the form). On success you'll see a toast "Work order created" with the new work order number, and you're redirected to the Quotation stage list.

## The stage pipeline

Each stage has its own page reachable from the Work Order System navigation, and every stage page has a **Pending** tab and a **History** tab:

1. **Quotation** (`/work-order/quotation`) — "Quotation Entry": enter up to three vendor quotations (vendor name, rate, payment terms, remarks, optional warranty/guarantee terms) for the same work order. Click **Process** on a row to open it, fill in quotations, then click **Submit For Approval** (requires at least one vendor quotation with a rate filled in).
2. **Approval** (`/work-order/approval`) — "Quotation Approval": compare the three quotations side by side and select which vendor to approve. Click **Approve & Issue** (requires a vendor to be selected) to move the order to Issued.
3. **Issue** (`/work-order/issue`) — "Work Order Issue": record any issue note, then click **Issue & Start Tracking** to move it into Tracking.
4. **Tracking** (`/work-order/tracking`) — "Work Tracking": mark each project stage as completed and enter its amount (an amount is required before a stage can be marked completed). Once all stages are completed, click **Send To Payment**.
5. **Payment** (`/work-order/payment`) — "Payment Process": record payment status; if marking payment as **Paid**, Bank Name, Account Number, IFSC Code, and a Payment Receipt upload are all required. Click **Save Warranty Details** to proceed to the Warranty stage.
6. **Warranty** (`/work-order/warranty`) — "Warranty / Guarantee": view warranty/guarantee/service commitment details for work orders that have completed payment. This tab is labeled "Active Warranties" instead of "Pending."
7. **Completed** (`/work-order/completed`) — "Completed Work Orders": read-only review of finished project work orders.

## Dashboard and lists

- **Work Order System > Dashboard** (`/work-order/dashboard`) gives an overview of all work orders.
- On any stage's Pending/History table, use the **Columns** button to toggle which columns are visible (e.g., Planned/Delay, WO Number, Priority, Project Name, WO Type, Party, Department, Site Location, Currency, Work Value, Stages Total, Start/End Date, Timeline, Payment Terms, Remark, Attachment) — your column choices are remembered per browser.
- Click **View** (History tab) or **Process** (Pending tab) on any row to open its detail modal, which also shows a visual status pipeline (Created → Quotation → Approval → Issued → Tracking → Payment → Warranty → Completed) highlighting the current stage.

## Key validation rules to know

- A work order cannot move to Approval without at least one vendor quotation that has both a vendor name and a rate.
- A work order cannot move to Issued without an approved vendor selected.
- All project stages must be marked completed (each with an amount) before the order can move to Payment.
- Marking payment as "Paid" requires bank name, account number, IFSC, and a receipt upload.
