---
title: Material Return, Management Approval, and Credit Note
module: order_to_dispatch
tags: [order-to-dispatch, material-return, credit-note, department-approval]
---

# Material Return, Management Approval, and Credit Note

If a customer reports an issue with delivered material (damage, quality issue, wrong material, short life, etc.), it is handled through this four-step return flow: Material Return → Management Approval → Credit Note → Return of Material.

## 1. File a Material Return (from an invoice)

1. Open **Order to Dispatch > Material Return** (`/order2dispatch/material-return`). Header: "Material Return — Track and manage returned materials from parties," with the form titled "Material Return From Party Form."
2. Enter the **Invoice / Bill Number** the return relates to (an autocomplete dropdown suggests matching invoice/bilty numbers as you type), then click **Lookup**.
3. Once the invoice loads, a product table appears showing each item's Total Qty, Already Returned, Available quantity, and D.O Number. Click **Process** on the item to return (disabled if Available Qty is 0).
4. In the "Material Return Process" dialog, review the invoice/party/product summary, then fill in:
   - **Return Qty** (capped at the item's available quantity).
   - **Reason** — choose **Damage**, **Quality Issue**, **Wrong Material**, **Short Life**, or **Other**.
   - Upload a **Debit Note** image/file and a reason-specific image (labeled e.g. "Damage Image").
   - Optional **Remarks**.
5. Submit — a **Return No.** is generated and a success toast confirms it. The return then awaits Management Approval.

## 2. Management Approval (Department Approval)

1. Open **Order to Dispatch > Management Approval** (`/order2dispatch/department-approval`). Header: "Management Approval — Review material returns and approve or reject them."
2. In **Pending**, click **Process** on a return row (or the **Eye** icon to just view). The dialog shows the full trail: Order & Invoice Details, Party Details, Dispatch Details, Logistic Details, Material Receipt Details, and the Return Items table (order/dispatch/invoice/return quantities, rate, reason, remarks, and a link to the debit note).
3. Set **Status** to **Approve** or **Reject**, add optional **Remarks**.
4. Click **Approve** or **Reject** to submit, or **Cancel**.
5. Status labels shown in the list: **Pending Management Approval**, **Management Approved**, **Management Rejected**.

## 3. Credit Note

1. Open **Order to Dispatch > Credit Note** (`/order2dispatch/credit-note`). Header: "Credit Note — Create credit notes for approved material returns."
2. Only returns already Management-approved appear here, labeled **Pending Credit Note** until processed.
3. Click **Process** on a pending row to open the dialog (shows the same full return trail as Management Approval, plus any existing credit note info).
4. Fill in:
   - **Credit Note Date*** (required).
   - **Credit Note No.*** (required).
   - **Credit Note Copy*** (required file upload — image or PDF).
5. Click **Submit Credit Note** (all three fields are mandatory), or **Cancel**.
6. Once saved, status becomes **Credit Note Created**, and the credit note copy can be viewed later via a "View copy" link.

## 4. Return of Material (physical return logistics)

1. Open **Order to Dispatch > Return of Material** (`/order2dispatch/return-of-material`). Header: "Return of Material — Track returned material movement after credit note."
2. Only returns with a completed credit note appear here, labeled **Pending Return of Material**.
3. Click **Process** on a row to open the dialog (shows the same order/invoice/party/dispatch/logistic/receipt/return-items trail plus credit note details).
4. Fill in the physical return shipment details:
   - **Return No.** (read-only, shown as "Generated on material return" until set).
   - **Transporter Name*** (required).
   - **Transporter Mobile*** (required).
   - **Vehicle No.*** (required).
   - **Received Delivery Date*** (required).
   - **Remarks** (optional).
5. Click **Submit Return** — all four starred fields must be filled or a validation error toast appears ("Transporter, mobile, vehicle, and received date are required").
6. Once submitted, status becomes **Material Returned**, completing the return cycle. The record's History view shows Returned Qty, Final Return Status, Remarks, and who processed it.

## Notes

- Every screen in this flow uses the same **Pending/History** tab layout with search and Company/Transport filters, and each row can be expanded (chevron icon) to preview the full return trail inline without opening the dialog.
- The party for a return is derived from the original order's linked Customer or Vendor record; if the order used a Customer record, contact/mobile/email/GST fields display as "—" since those are only tracked on Vendor-type records.
