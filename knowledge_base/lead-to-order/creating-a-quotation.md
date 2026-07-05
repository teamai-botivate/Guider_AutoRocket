---
title: Creating, Revising, and Viewing Quotations
module: lead_to_order
tags: [lead-to-order, quotation, sales, pricing]
---

## Overview

**Lead To Order → Quotation** (path `/lead-to-order/quotation`) is the **Quotation Management** page. It has three top-level tabs: **Generator** (create new), **Revise** (edit/re-quote an existing one), and **History** (view/search past quotations).

## Creating a new quotation (Generator tab)

1. Open **Lead To Order → Quotation**, ensure the **Generator** tab is selected. Within it, switch between **Edit Quotation** and **Live Preview** sub-tabs to see the document take shape as you fill fields.
2. **Consignor Details (Your Company)** — Company Name, Address, GSTIN, State Code, Mobile/Phone. Your profile logo (if set) appears alongside.
3. **Lead** (required) — select the lead this quotation is for (auto-fills from URL if you arrived via "Make Quotation" on Pending Quotation). **Vendor (Company)** auto-locks to the lead's vendor once a lead is chosen; it can be picked independently only if no lead is selected. **Quotation Made By** (required) — pick from system users.
4. **Subject / Reference** and **Valid Until (Expiry Date)** — optional.
5. **Billing Address** (Address Line 1/2, State, Pincode) and **Shipping Address** — check **SAME AS BILLING** to reuse the billing address, or uncheck to enter a separate shipping address.
6. **Consignee Additional Details** — Consignee Mobile, Consignee GSTIN (GSTIN is locked/disabled once a Lead is selected).
7. **Our Bank Details (for Payment)** (required) — Bank Name, A/C Number, IFSC Code, Branch.
8. **Terms & Conditions** — click **Add Term** to add a line, or the trash icon to remove one.
9. **Remarks / Customer Notes** — optional free text.
10. **Items / Services** table — for each row select a Product, Quantity, Rate (₹), Discount (₹), optional Spc/Remarks, and GST % (18/12/5/28/0). Click **Add Item** for more rows; use the trash icon to remove a row (at least one must remain). The table footer auto-calculates Total Discount, Taxable Value, and Total Amount (Incl. GST).
11. Click **Generate Quotation** to save. Use **Cancel** to clear the form without saving.

## Revising an existing quotation (Revise tab)

1. Click the **Revise** tab. You'll see a list of quotations grouped by base quotation number (e.g. `QT-001`), each showing how many revisions exist; only quotations linked to enquiries that have **not** yet received an order are eligible.
2. Expand a group to see each revision (marked **Latest** / **Original**), then click one to select it for revision — this pre-fills the entire form (header, addresses, bank, terms, items) from that quotation and locks the Lead/Vendor fields.
3. Edit whatever needs to change (prices, items, terms, etc.) using the same form described above.
4. Click **Submit Revised Quotation** to save the new revision (it will be numbered as a suffix of the base number, e.g. `QT-001-01`). Click **← Back to quotation list** to pick a different quotation, or **Cancel** to discard changes.

## Viewing quotation history

1. Click the **History** tab to see all quotations in a table: Quot. No, Enquiry, Vendor, Subject, Shared By, Valid Until, Value (excl./incl. tax), Date, Remarks.
2. Click **View** on a row to see full quotation details (consignor, addresses, items, terms, remarks) in a read-only dialog.
3. Click **See Copy** to open a formatted preview of the quotation document as it would appear when shared with the customer.

## Notes

- A quotation is not counted as "sent" to the customer merely by being created — the system tracks a separate "sent/attached" event (visible as **Quotation Sent** vs **Quotation Created**/**Quotation Revised** badges elsewhere in the module), which happens via the Pending Quotation attach flow or the enquiry processing flow.
