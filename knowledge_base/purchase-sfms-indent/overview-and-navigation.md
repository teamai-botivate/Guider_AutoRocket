---
title: Purchase and Store FMS Overview and Navigation
module: purchase_sfms_indent
tags: [purchase, store-fms, sfms, indent, navigation, overview]
---

# Purchase and Store FMS Overview and Navigation

This module key covers two related procurement areas in the app:

1. **Purchase** - purchase requisition/indent, vendor/procurement, PO, logistics, receipt, quality, audit, and returns.
2. **Store FMS** - store indent-to-PO-to-inventory-to-payment workflow.

They are separate sidebar groups with overlapping procurement concepts. When answering a user, first identify whether they are asking about **Purchase** routes (`/purchase/...`) or **Store FMS** routes (`/store-fms/...`).

## Purchase navigation

Under **Purchase**, the sidebar includes:

| Sidebar label | Path |
| --- | --- |
| Dashboard | `/purchase/dashboard` |
| Indent | `/purchase/indent` |
| Management Approvals | `/purchase/managementApprovals` |
| Vendor Selection | `/purchase/vendorSelection` |
| Purchase Order | `/purchase/purchaseOrder` |
| Create PO | `/purchase/createPO` |
| PO History | `/purchase/poHistory` |
| Tally Entry | `/purchase/tallyEntry` |
| Advance Payment | `/purchase/advancePayment` |
| Lift Material | `/purchase/liftMaterial` |
| Receipt | `/purchase/receipt` |
| Lab Testing | `/purchase/labTesting` |
| Unload Management | `/purchase/unloadManagement` |
| Lab Report | `/purchase/labReport` |
| Mismatch | `/purchase/mismatch` |
| Purchaser Coord. | `/purchase/purchaserCoordinate` |
| Debit Note | `/purchase/debitNote` |
| Accounts Audit | `/purchase/accountsAudit` |
| Purchase Return | `/purchase/purchaseReturn` |

## Store FMS navigation

Under **Store FMS**, the sidebar includes:

| Sidebar label | Path |
| --- | --- |
| Dashboard | `/store-fms/dashboard` |
| Quotation | `/store-fms/quotation` |
| Store Issue | `/store-fms/store-issue` |
| Issue Data | `/store-fms/issue-data` |
| Inventory | `/store-fms/inventory` |
| Create Indent | `/store-fms/create-indent` |
| Department Indent Approval | `/store-fms/department-indent-approval` |
| Vendor Update | `/store-fms/vendor-update` |
| Department Approval | `/store-fms/department-approval` |
| Management Approval | `/store-fms/management-approval` |
| Pending PO Created | `/store-fms/pending-po-created` |
| Create PO | `/store-fms/create-po` |
| PO History | `/store-fms/po-history` |
| Lifting | `/store-fms/lifting` |
| Store Check | `/store-fms/store-check` |
| HOD Check | `/store-fms/hod-check` |
| Freight Payment | `/store-fms/freight-payment` |
| Make Payment | `/store-fms/make-payment` |
| Reject GRN | `/store-fms/reject-grn` |
| Send Debit Note | `/store-fms/send-debit-note` |
| Bill Not Received | `/store-fms/bill-not-received` |
| Audit Data | `/store-fms/audit-data` |

## Practical routing rule

- If the user says **SFMS**, **Store FMS**, store indent, inventory, HOD check, GRN, bill not received, or store issue, use the Store FMS docs.
- If the user says **Purchase**, purchase indent, vendor selection, PO creation, lift material, receipt, lab testing, mismatch, purchaser coordination, accounts audit, or purchase return, use the Purchase docs.
- If the question is specifically about payment after a purchase/store stage, also check the **Payment Workflow** docs because newer pages can create requests there.

