---
title: Payment Approval, Make Payment, and Tally Entry
module: payment_workflow
tags: [payment-workflow, approval, make-payment, tally-entry]
---

# Payment Approval, Make Payment, and Tally Entry

After a request is created, it moves through approval, payment execution, and Tally entry.

## Payment Approval

Path: `/payment-workflow/payment-approval`

1. Open **Payment Workflow > Payment Approval**.
2. Use the tabs:
   - **Pending** - requests waiting for approval.
   - **History** - approved, rejected, or held requests.
3. Pending rows show Unique No, Module, Purpose, Pay To, Amount, Requested By, Action, and Details.
4. Click the eye icon to open the details modal.
5. Click **Process** to open the approval modal.
6. Choose **Action**:
   - **Approve** - optional remarks, amount shown read-only.
   - **Reject** - reason required.
   - **Put on Hold** - reason required.
7. Click **Approve**, **Reject**, or **Put on Hold**.

History rows show Status, Unique No, Purpose, Pay To, Amount, Approved By, Reason, and Details.

## Make Payment

Path: `/payment-workflow/make-payment`

1. Open **Payment Workflow > Make Payment**.
2. Use the tabs:
   - **Pending** - approved payments waiting to be paid.
   - **History** - paid or later-stage payments.
3. Pending rows show Unique No, Purpose, Pay To, Amount, Approved By, Action, and Details.
4. Click **Pay Now**.
5. In **Confirm Payment**, set:
   - **Payment Mode** - Cash, Bank Transfer, UPI, or Cheque.
   - **Payment Status** - Full Payment, Partial Payment, or On Hold.
   - **Paying Now** amount if Partial Payment is selected.
   - **Payment Receipt** upload - image or PDF.
   - **Remarks**.
6. Click **Confirm Payment**.

Payment history shows Status, Unique No, Purpose, Pay To, Amount, Payment Mode, Paid By, Date, and Details.

## Tally Entry

Path: `/payment-workflow/tally-entry`

1. Open **Payment Workflow > Tally Entry**.
2. Use the tabs:
   - **Pending** - paid payments not yet marked in Tally.
   - **History** - Tally-entered payments.
3. In Pending, tick individual rows or the header checkbox to select all visible rows.
4. Click **Submit (N selected)** to mark selected payments as Tally-entered.
5. Use **Clear Selection** to reset the selected list.

Pending rows show Unique No, Purpose, Pay To, Amount, Payment Mode, Paid By, and Paid Date. History rows add the Tally Entered date.

## Details modal

The shared details modal shows:

- Payment Details: Pay To, Amount, Module, Remarks, Attachment.
- Source-specific details for freight or PO records when available.
- Request info: Requested By, Requested At, Scheduled date.
- Approval/Rejection/Hold details.
- Payment execution details, including proof link.
- Tally entry details.

