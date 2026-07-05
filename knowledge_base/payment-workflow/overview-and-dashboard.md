---
title: Payment Workflow Overview and Dashboard
module: payment_workflow
tags: [payment-workflow, payments, dashboard, approval, tally]
---

# Payment Workflow Overview and Dashboard

Payment Workflow centralizes payment requests from multiple business modules and moves them through approval, payment execution, and Tally entry.

## Navigation

Under **Payment Workflow**, the sidebar includes:

| Sidebar label | Path | Purpose |
| --- | --- | --- |
| Dashboard | `/payment-workflow/dashboard` | Payment KPIs, cash-flow trends, module breakdown, aging, subscription payments |
| Freight Payment | `/payment-workflow/freight-payment` | Create freight payment requests from Store, Purchase, or Order logistics data |
| Vendor Payment | `/payment-workflow/vendor-payment` | Create vendor payment requests from Store received items or Purchase Orders |
| Request Form | `/payment-workflow/request-form` | Manually submit a payment request |
| Payment Approval | `/payment-workflow/payment-approval` | Approve, reject, or hold requested payments |
| Make Payment | `/payment-workflow/make-payment` | Execute approved payments |
| Tally Entry | `/payment-workflow/tally-entry` | Mark paid items as entered in Tally |

## Status lifecycle

Payment request statuses are:

| Status | Meaning |
| --- | --- |
| `REQUESTED` | Request submitted and waiting for approval |
| `APPROVED` | Approved and waiting for payment execution |
| `REJECTED` | Rejected by approver |
| `ON_HOLD` | Put on hold with a reason |
| `PAID` | Payment executed, waiting for Tally entry |
| `TALLY_ENTERED` | Payment completed and marked in Tally |

## Source modules

Requests can be tagged with these source modules:

- `SFMS_PO` - Store PO
- `SFMS_FREIGHT` - Freight
- `SFMS_DEBIT_NOTE` - Debit Note
- `PURCHASE_PO` - Purchase PO
- `OUTHOUSE_REPAIR` - Repair
- `PETROL_EXPENSE` - Petrol Expense
- `DOC_SUBSCRIPTION` - Doc Subscription
- `MANUAL` - Manual

## Dashboard

Open **Payment Workflow > Dashboard** (`/payment-workflow/dashboard`). The page heading is **Payment Dashboard** with the subtitle "Real-time payment workflow overview."

Dashboard sections include:

- KPI cards for pending, approved, paid-this-month, on-hold, and Tally-pending metrics.
- **Cash Flow Trends (30 days)** - requested, approved, and paid amounts.
- **Module Breakdown** - payment amount by source module.
- **Subscription Payments** - Doc Submanager subscription payment requests with pending/approved/paid/total-paid summaries and inline Pay Now for approved subscriptions.
- **Payment Aging** - pending/held requests by age bucket.
- **Aging Amount** - amount overdue by age bucket.

The **Sync Historical Data** button runs the one-time backend backfill endpoint to import historical module payments into the workflow.

