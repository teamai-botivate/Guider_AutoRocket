---
title: Store FMS Indent to Payment Flow
module: purchase_sfms_indent
tags: [store-fms, sfms, indent, po, inventory, grn, debit-note, audit, payment]
---

# Store FMS Indent to Payment Flow

Store FMS follows a long indent-to-payment workflow. The backend design doc `indent.md` describes this operational sequence:

1. Indent
2. Department Approval
3. Vendor Rates
4. Department Re-Approval
5. Management Approval
6. Purchase Order
7. Lifting
8. Store Check-In
9. HOD Check and Closure
10. Inventory Posting
11. Store Issue from Inventory
12. Material Return to Inventory
13. GRN Quality Check
14. Debit Note if GRN is rejected
15. Bill Not Received tracking
16. Audit Data / Tally Entry pipeline
17. Payment processed

## Core Store FMS stages

| Stage | Route | What happens |
| --- | --- | --- |
| Create Indent | `/store-fms/create-indent` | Requester creates a store indent |
| Department Indent Approval | `/store-fms/department-indent-approval` | Department approves/rejects initial indent |
| Vendor Update | `/store-fms/vendor-update` | Procurement records vendor/rate information |
| Department Approval | `/store-fms/department-approval` | Department re-approves after vendor/rate update |
| Management Approval | `/store-fms/management-approval` | Management approves the indent |
| Pending PO Created / Create PO | `/store-fms/pending-po-created`, `/store-fms/create-po` | Purchase order is prepared |
| PO History | `/store-fms/po-history` | PO records/history |
| Lifting | `/store-fms/lifting` | Material lifting/transport begins |
| Store Check | `/store-fms/store-check` | Store confirms received material |
| HOD Check | `/store-fms/hod-check` | HOD closes/approves received material |
| Inventory | `/store-fms/inventory` | Approved material becomes inventory |
| Store Issue / Issue Data | `/store-fms/store-issue`, `/store-fms/issue-data` | Inventory is issued to departments/users |
| Reject GRN | `/store-fms/reject-grn` | Quality/GRN rejection handling |
| Send Debit Note | `/store-fms/send-debit-note` | Debit note is sent for rejected goods |
| Bill Not Received | `/store-fms/bill-not-received` | Tracks cases where material came but bill did not |
| Audit Data | `/store-fms/audit-data` | Accounts/audit/Tally pipeline |
| Freight Payment / Make Payment | `/store-fms/freight-payment`, `/store-fms/make-payment` | Freight/payment processing |

## Status flow

Common statuses from the backend Store FMS design:

`DRAFT -> DEPT_APPROVED -> RATE_FINALIZED -> DEPT_REAPPROVED -> MGMT_APPROVED -> PO_CREATED -> LIFTING_IN_PROGRESS -> STORE_CHECKED_IN -> HOD_APPROVED_CLOSED -> INVENTORY_POSTED -> STORE_ISSUE_CREATED -> STOCK_ISSUED -> STOCK_RETURNED -> GRN_ACCEPTED -> AUDIT_IN_PROGRESS -> AUDIT_COMPLETE -> PAYMENT_PROCESSED`

Important branches:

- `REJECTED_BY_DEPT` - initial department rejection.
- `REJECTED_BY_MGMT` - management rejection.
- `GRN_REJECTED` - failed quality check; should trigger debit note.
- `DEBIT_NOTE_ISSUED` - debit note branch after rejection.
- `BILL_NOT_RECEIVED` - parallel bill-follow-up state while invoice is missing.

## Creating and approving Store FMS indents

The Store FMS create-indent API uses:

- `GET /sfms/indents/pending`
- `POST /sfms/indents`
- `PATCH /sfms/indents/:id/approve`
- `GET /sfms/indents?status=...`
- `PATCH /sfms/indents/:id/mgmt-approve`

Every stage should keep the same indent identity and tenant isolation. When troubleshooting missing records, check both the route/stage and the current status.

## Inventory and payment gates

Inventory is posted only after HOD approval/closure. Payment should not be treated as complete until the bill is received, GRN is accepted or rejection/debit-note is resolved, audit/Tally stages are complete, and final payment is processed.

