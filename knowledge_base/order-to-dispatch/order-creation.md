---
title: Creating and Checking Orders
module: order_to_dispatch
tags: [order-to-dispatch, order-creation, check-po, purchase-order]
---

# Creating and Checking Orders

This covers entering a new customer purchase order and the internal "Check PO" verification step that follows it.

## 1. Create a new order

1. Go to **Order to Dispatch > Order** (`/order2dispatch/order`). This page is titled "Orders Management."
2. Click **Add New Order** (top right, blue button). A "Create New Order" form opens in a modal.
3. Fill in **Section 1: Order Details**:
   - **PO Number** (required) — e.g. "PO-2024-001".
   - **PO Date**.
   - **PO Value (₹)**.
   - **Customer** — pick from the dropdown of sales-type vendors/customers, or click the **+** button next to it to add a new customer on the fly.
   - **Sales Person** — pick from the same vendor list, or add a new one via the **+** button.
   - **Payment Term** — pick an existing term or click **+** to add a new one (opens an "Add Payment Term" mini-dialog with a text field and **Add**/**Cancel** buttons).
   - **Customer Requested Delivery Date**.
   - **Transport Type** — choose **FOR**, **Ex Factory**, or **Ex Factory But paid by Us**.
   - When a customer is selected, a summary panel shows their Contact Person, Mobile Number, GST Number, Email, and Address for confirmation.
4. Fill in **Section 2: Order Items**:
   - Click **Add Item** to open the "Add Order Items" panel.
   - Select a **Product** (only finished-goods products appear in the list), or click the **+** next to it to create a new product.
   - **UOM** auto-fills from the product; enter **Quantity** (required) and optionally a **Price per Unit (₹)** (defaults to the product's base price if set) and a **Remark**.
   - Click **Add Item** to add it to the order, or **Done** to close the item panel. Repeat for each line item.
   - Each added item is listed with its quantity, price, and computed total; you can remove any item with the trash icon.
   - An **Items Total** banner shows the running total against the entered PO Value for a quick sanity check.
5. Click **Create Order** (bottom right) to save, or **Cancel** to discard. The button shows "Creating..." while submitting and is disabled until at least one item is added.
6. On success, the new order appears in the **All Orders** table on the Order page, showing Total Orders and Total Value stat cards at the top. Use the **Export** button (top right) to export the order list.

## 2. Check PO (internal PO verification)

This is a separate downstream stage where PO details are reviewed and quantities confirmed before the order proceeds.

1. Open **Check PO** (this stage is generally reached from the pipeline; it uses Pending/History tabs like other stages, titled "Check PO — Review purchase orders and confirm quantities").
2. In the **Pending** tab, find the order and click **Process** on its row (or expand the row with the chevron to preview PO, customer, and item details first).
3. In the **Check PO** dialog:
   - Review the read-only PO Number, PO Date, Requested Delivery, Transport, Order Date, PO Value, Total Amount, and Current Status.
   - Review Customer Details and the Item Details table (ordered quantity, rate, amount for each line).
   - Set **Check Status** to **Approve** or **Reject**.
   - Add optional **Remarks**.
4. Click **Approve PO** (green) or **Reject PO** (red) — the button label and color follow the selected status. Click **Cancel** to close without saving.
5. Once approved, the order becomes eligible for the next stage, **Check for Delivery** (see `dispatch-and-logistics.md`).

## Notes

- Every order retains its original PO Number and gets an internal Order No once created.
- The order source can be "Manual" or "Lead Order" (`LEAD_TO_ORDER`) — orders created from the Lead-to-Order module are tagged with a violet "Lead Order" badge in later stage tables and carry through the same PO-driven origin.
