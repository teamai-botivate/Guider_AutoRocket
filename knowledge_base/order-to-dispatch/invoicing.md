---
title: Invoicing, Wetman Entry, and Confirming Receipt
module: order_to_dispatch
tags: [order-to-dispatch, invoice, wetman-entry, confirm-receipt]
---

# Invoicing, Wetman Entry, and Confirming Receipt

This covers billing the customer for a dispatch, recording weighment slips, and confirming the customer received the material.

## 1. Create an Invoice

1. Open **Order to Dispatch > Invoice** (`/order2dispatch/invoice`).
2. In the **Pending** tab, click **Invoice** (or the **Eye** icon) on a dispatch row to open the "Make Invoice" dialog. Expand **Details** to see PO, party, GST, address, transport, dispatch date, delivery dates, and logistic info (transporter, truck, driver, bilty).
3. In **Product Lines**, tick the items to bill (all are selected by default) and enter/confirm the **Rate (₹)** for each — the **Total (₹)** per line and a **Grand Total (Selected)** update live.
4. Fill in the invoice fields:
   - **Invoice Number*** — pre-filled as `INV-<PO number>` but editable.
   - **Invoice Date**.
   - **Vehicle Number**.
   - **Bilty Number** — pre-filled from the logistic record's bilty number if present.
   - **Bill Amount**.
5. Click **Submit Invoice** (enabled once Invoice Number is set and at least one item is selected), or **Cancel**.
6. The record then shows in **History** with Bill No, Invoice Date, Invoice Amount, Vehicle No, and Bilty No columns.

## 2. Wetman Entry (weighment recording)

1. Open **Order to Dispatch > Wetman Entry** (`/order2dispatch/wetman-entry`).
2. Click **Wetman** on a pending dispatch row (or **Handle Wetman Entry** on mobile) to open the "Wetman Entry" dialog.
3. Read-only **PO Number** and **Contact** are shown for reference.
4. For each dispatch item, enter:
   - **Actual Qty Loaded in Truck**.
   - **Actual Qty Per Weighment Slip**.
5. Upload up to three weighment slip photos: **Image of Slip 1**, **Image of Slip 2**, **Image of Slip 3**.
6. Add optional **Remarks**.
7. Click **Submit Wetman Entry** to save, or **Cancel**.

## 3. Confirm Receipt

1. Open **Order to Dispatch > Confirm Receipt** (`/order2dispatch/confirm-receipt`) — this is the module's actual material-receipt-confirmation screen (the older `/order2dispatch/material-receipt` URL automatically redirects here).
2. In **Pending**, click the row action to open the "Confirm Receipt" dialog for a dispatch/invoice.
3. Fill in:
   - **Receipt Date**.
   - **Remarks**.
   - **Receipt Proof Image** — optional file upload.
4. Submit to confirm the material reached the customer. The record moves to **History** showing Receipt Date, Confirmed Qty, Confirmation Remarks, Submitted By, and a **CONFIRMED** stage-status badge.

Each of these three tables uses **Pending/History** tabs, a search box, and (for Invoice and Test Report) a **Columns** picker to customize visible fields such as Planned/Delay timers, Dispatch Qty, Transporter, Truck No, and Submitted By/At.
