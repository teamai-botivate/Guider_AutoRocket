---
title: Store FMS Inventory, Store Issue, GRN, Debit Note, and Audit
module: purchase_sfms_indent
tags: [store-fms, inventory, store-issue, grn, debit-note, bill-not-received, audit]
---

# Store FMS Inventory, Store Issue, GRN, Debit Note, and Audit

The later Store FMS stages happen after PO, lifting, store check, and HOD check.

## Inventory posting

After HOD approval/closure, received material is posted into Store FMS inventory.

1. If the item already exists in inventory, its available/current quantity is increased.
2. If the item does not exist, a new inventory row is created.
3. The material becomes available for Store Issue.

Use **Store FMS > Inventory** (`/store-fms/inventory`) to view current stock.

## Store issue and issue data

Use:

- **Store Issue** (`/store-fms/store-issue`) to issue material from inventory.
- **Issue Data** (`/store-fms/issue-data`) to review issued material records.

When an issue is approved/completed, stock is deducted from inventory. If unused material is returned, returned quantity is posted back to inventory for reconciliation.

## GRN rejection and debit note

If quality/GRN checking fails:

1. The record moves to `GRN_REJECTED`.
2. A rejection reason should be captured.
3. Debit note should be marked Yes when vendor debit adjustment is required.
4. Use **Reject GRN** (`/store-fms/reject-grn`) and **Send Debit Note** (`/store-fms/send-debit-note`) for the rejection branch.

Debit note data can include debit note number, debit note copy, bill copy, goods return copy, purchaser status, and issue/actual dates.

## Bill Not Received

Use **Bill Not Received** (`/store-fms/bill-not-received`) when material has arrived but the vendor bill/invoice has not.

Typical tracked fields include:

- Bill status - Received, Not Received, or Partial.
- Bill image status.
- Vehicle number.
- Driver name and mobile number.
- Bill remarks.
- Planned and actual bill receipt dates.

Bill-not-received can run in parallel with GRN/debit-note work, but payment should stay blocked until the bill is resolved.

## Audit Data / Tally pipeline

Use **Audit Data** (`/store-fms/audit-data`) for the accounts/audit pipeline. The backend design describes five audit sub-stages:

1. **Audit Data** - initial verification of bill/PO/GST/quantity/product image.
2. **Rectify Mistake** - correction if the audit finds an error.
3. **Reaudit Data** - verification after correction.
4. **Tally Entry** - entry in accounting/Tally software.
5. **Again Audit** - final senior audit.

When all audit sub-stages are complete, the record becomes audit-complete and payment can be fully processed.

