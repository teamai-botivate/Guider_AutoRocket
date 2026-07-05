---
title: Outhouse Repair Dispatch, Store-In, and Payment
module: repair
tags: [repair, outhouse, machine-dispatch, store-in, vendor-payment]
---

# Outhouse Repair Dispatch, Store-In, and Payment

These screens handle the later stages of an outhouse repair after a repair indent has already been approved, a service vendor/rate has been selected, and the machine is ready to be moved through dispatch, return, and settlement.

## 1. Machine Dispatch

Path: `/maintenancepro/repair/sentmachine`

1. Open the **Machine Dispatch** page. Header subtitle: "Track machine transit to external service centers."
2. Use the search box to search by indent ID, machine, or vendor.
3. Switch between:
   - **Pending Dispatch** - approved outhouse repairs waiting to be shipped.
   - **Dispatch History** - repairs already dispatched.
4. Pending table rows show Indent No, Machine & Serial, Assigned Vendor, Approved Price, Approved On, Problem, and Actions.
5. Click **Ship Now** to open **Log Machine Dispatch**.
6. Fill in:
   - **Transporter Name** - required; selected from vendors of type Transport.
   - **Weighment / LR No.** - required.
   - **Transport Charges** - required.
   - **Proof of Dispatch** - optional upload for LR/receipt.
   - **Immediate Payment** - Cash, UPI / Digital, or To Be Billed (Postpaid).
   - **Payment Amount** - optional immediate payment amount.
7. Click **Confirm Dispatch**. This records outgoing transport details and moves the item toward Store-In.

Clicking a row opens **Dispatch & Transport Audit**, which shows machine/serial/faulty part, requester/location, task status, problem, approved vendor/rate, and transport details if already sent.

## 2. Store In Verification

Path: `/maintenancepro/repair/storein`

1. Open **Store In Verification**. Header subtitle: "Receive returned machines and verify repair quality."
2. Use the search box and switch between:
   - **Pending Store-In**
   - **Store-In History**
3. Pending rows show Indent No, Machine & Serial, Return Vendor, Dispatch Stats, Expected Date, Status, and Actions.
4. Click **Record Store-In** to open **Receive Repaired Machine**.
5. Fill in:
   - **Inspected By** - required.
   - **Return Transporter**
   - **Transportation Amount**
   - **Bill No.** - required.
   - **Type of Bill** - defaults to Service.
   - **Total Bill Amount** - required.
   - **Final Payable Amount** - optional; defaults to total bill amount if left blank.
   - **Vendor Bill** upload, if available.
   - **Inspection Result/Remarks**, if shown.
6. Click **Confirm Received & Log Bill**. The page note says the item will move to the final payment queue.

Clicking a row opens **Store-In Audit Details**, showing machine/part, indent origin, timeline, current status, problem, approved service vendor, dispatch/transit, and for history items receipt, inspection, and billing information.

## 3. Vendor Settlement

Path: `/maintenancepro/repair/payment`

1. Open **Vendor Settlement**. Header subtitle: "Finalize vendor invoices and process repair payments."
2. Use the search box and switch between:
   - **Pending Payments**
   - **Payment History**
3. Pending rows show Indent & Machine, Vendor Details, Bill Reference, Store-In Status, Due Amount, Status, and Actions.
4. Click **Pay Now** to open **Confirm Settlement**.
5. Review the Invoice Summary and Vendor Identity blocks.
6. Set:
   - **Bill Matching** - Yes - Exactly Matches, or No - Manual Overwrite.
   - **Final Status** - Cleared (Full Pay), Disputed / Partial, or Pending Authorization.
   - **Final Payment Release Amount** - required.
7. Click **Confirm & Complete Payment**. The note in the modal says this marks the repair cycle as complete.

Clicking a row opens **Settlement Details**, including asset identity, vendor details, billing summary, store-in/inspection, dispatch details, and the original issue.

