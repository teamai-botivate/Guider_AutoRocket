---
title: Creating a New Lead
module: lead_to_order
tags: [lead-to-order, leads, lead-creation, sales]
---

## Overview

The **Lead To Order** module is found in the left sidebar under **Lead To Order**. It covers the full sales pipeline: Lead → Call Tracker follow-ups → Enquiry → Quotation → Order Received/Not Received. This guide covers creating a new lead.

## Steps to create a lead

1. In the sidebar, open **Lead To Order → Leads** (path `/lead-to-order/leads`). This opens the **Lead Management** page with a **New Lead** form.
2. The form auto-generates the next lead number (shown as "Next Lead Number: LD-001", etc.) — you don't set this yourself.
3. Fill in **Basic Info**:
   - **Sales Person Name** — a searchable field pulled from your SALES-type vendor contacts. Click **Add** next to it to open the vendor form and add a new sales contact on the fly.
   - **Lead Source** (required) — choose from a dropdown (e.g. sources your company has configured). Click **Add** to create a new lead source inline.
   - **Lead Type** (optional) — dropdown with an inline **Add** option, same pattern as Lead Source.
   - **SC Name** (required) — searchable dropdown of system users (the person receiving/handling the lead).
   - **Company Name** (required) — searchable field. Selecting an existing company auto-fills phone number, person name, location, email, state, address, GST, and nature-of-business (NOB) from that vendor's record. Click **Add Vendor** to create a brand-new company/vendor if it doesn't exist yet.
4. Review the **Details** section — Phone Number, Person Name, Location, and Address. These fields become read-only (auto-filled, greyed out) once a Company is selected; they're editable only when no company is chosen yet.
5. Fill in **Contact Person Details** — Name, Designation (dropdown: Manager, Director, CEO, CFO, Proprietor), Phone Number. Click **Add Person** to add up to 3 contact persons total; use **Remove** on any contact after the first to delete it.
6. Fill in **Product Requirements** under Additional Info — for each row pick a Product from the dropdown, enter Quantity, and optionally Remarks. Click **Add Product** to add more rows, or the trash/X icon to remove a row (at least one row must remain). A product must be selected if a quantity is entered, or you'll see a validation error.
7. Optionally add **Additional Notes** in the free-text box at the bottom.
8. Click **Save Lead** to submit. On success you'll see a "Lead created successfully" toast and the form resets, ready for the next lead. Click **Reset Form** at any time to clear all fields without saving.

## What happens after saving

The new lead becomes available for follow-up in **Call Tracker**, where you log calls against it and eventually convert it into an Enquiry. See the "Call Tracker and Converting a Lead to an Enquiry" guide for the next step.

## Notes on unclear/generic areas

- The exact list of Lead Source and Lead Type option values is tenant-configured (created via the inline "Add" buttons) and not hardcoded, so specific values aren't documented here.
- "NOB" (Nature of Business) options are fixed: Manufacturing, Trading, Service, Retail — but this field is only shown/used when auto-filled from a selected vendor's record.
