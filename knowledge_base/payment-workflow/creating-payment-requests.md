---
title: Creating Payment Workflow Requests
module: payment_workflow
tags: [payment-workflow, request-form, freight-payment, vendor-payment]
---

# Creating Payment Workflow Requests

Payment requests can be created manually from the Request Form or pre-filled from freight/vendor payment helper pages.

## Manual request form

Path: `/payment-workflow/request-form`

1. Open **Payment Workflow > Request Form**.
2. Fill **Submit New Request**:
   - **Purpose*** - what the payment is for.
   - **Pay To*** - vendor/payee name.
   - **Amount***.
   - **Scheduled Date** - optional.
   - **FMS Name** - optional source module, such as Purchase, SFMS PO, SFMS Freight, Outhouse Repair, Petrol Expense, Doc Subscription, or Manual.
   - **Unique No.** - optional reference such as a PO number; disabled until an FMS/source module is selected.
   - **Remarks** - optional.
3. Click **Submit Request**.
4. The request appears in **All Requests** with Status, Unique No, Purpose, Pay To, Amount, Requested By, and Date.

Manual requests default into the approval queue with `REQUESTED` status.

## Vendor Payment helper

Path: `/payment-workflow/vendor-payment`

Use this page to raise vendor payment requests from existing Store/Purchase data.

1. Choose a tab:
   - **Store** - received Store FMS rows.
   - **Purchase** - purchase orders.
2. Review source columns such as PO number, vendor, bill number/status, total amount, received quantity, PO date, and delivery date.
3. Click **Request Payment** on a row.
4. The dialog is pre-filled with source information. Confirm/edit:
   - **Pay To**
   - **Amount**
   - **Purpose** - defaults to "Vendor Payment"
   - **Scheduled Date**
   - **Remarks**
5. Click **Submit Request**.

Store rows create `SFMS_PO` requests. Purchase rows create `PURCHASE_PO` requests.

## Freight Payment helper

Path: `/payment-workflow/freight-payment`

Use this page to raise transporter/freight payment requests from logistics sources.

1. Choose a tab:
   - **Store** - Store FMS freight data.
   - **Purchase** - Purchase logistics arrangement history.
   - **Order** - Order-to-Dispatch logistics history.
2. Review transporter, PO/order/logistic numbers, bill/vehicle/bilty fields, rate type, and amount.
3. Click **Request Payment**.
4. Confirm/edit:
   - **Pay To** - transporter/payee.
   - **Amount**
   - **Purpose** - defaults to "Freight Payment"
   - **Scheduled Date**
   - **Remarks**
5. Click **Submit Request**.

Store and Order freight requests use `SFMS_FREIGHT`; Purchase freight rows currently create payment requests from Purchase logistics data.

