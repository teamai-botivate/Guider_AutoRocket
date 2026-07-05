---
title: Doc SubManager - Subscriptions, Approval, Payment, and Renewal
module: doc_sub_manager
tags: [doc-submanager, subscriptions, approval, payment, renewal]
---

# Managing Subscriptions in Doc SubManager

Subscriptions (recurring payments/services like Netflix, software licenses, etc.) move through four stages in Doc SubManager: **Create → Approve → Pay → Renew**. All screens are under **Doc Submanager > Resource Manager** in the sidebar.

## 1. Create a subscription request

1. Go to **Doc Submanager > Resource Manager > All Subscriptions** (`/doc-submanager/subscription/all`).
2. Click **Add** in the page header to open the **Add Subscription** modal.
3. Fill in:
   - **Company Name** (searchable dropdown, add-new supported)
   - **Subscriber Name** (free text)
   - **Subscription Name** (searchable dropdown, e.g. "Netflix Premium")
   - **Price** (free text, e.g. "$19.99")
   - **Frequency** (dropdown: Monthly / Quarterly / Half-Yearly / Yearly)
   - **Purpose** (free text explaining why the subscription is needed)
4. Click **Save Subscription**. The new request is created with a pending status and appears in **All Subscriptions** and in the approval queue.
5. **All Subscriptions** table shows: S.No, Requested date, Planned (approval due date/time), Company, Subscriber, Subscription, Price, Frequency, Purpose, Start Date, End Date, and a **Status** badge (Pending / Approved / Rejected / Paid).

## 2. Approve or reject a subscription request

1. Go to **Doc Submanager > Resource Manager > Sub Approval** (`/doc-submanager/subscription/approval`), titled "Subscription Approvals".
2. **Pending** tab lists new requests awaiting approval. Click **Approve** in the Action column for a row.
3. In the **Subscription Action** modal, review the Serial No, Requested On date, Company, and Subscription name, then:
   - Choose **Action Status**: **Approve** or **Reject**
   - Enter **Remarks**
4. Click **Save**. Approved/rejected requests move to the **History** tab, showing Approval No, Type (initial approval vs. renewal), Approved On date, Delay (on-time or delay label), Status, and Remarks.
5. Approving a subscription (status becomes "Approved") makes it eligible for payment.

## 3. Pay a subscription

1. Go to **Doc Submanager > Resource Manager > Sub Payment** (`/doc-submanager/subscription/payment`), titled "Subscription Payments".
2. **Pending** tab lists approved subscriptions awaiting payment. Click **Pay** in the Action column for a row.
3. In the **Process Payment** modal, review Sub No, Company, Subscription, and Price/Frequency, then fill in:
   - **Start Date** and **End Date** (the new subscription period being paid for)
   - **Payment Method** (dropdown: Credit Card / Bank Transfer / UPI)
   - **Upload Receipt** (attach the payment receipt file)
4. Click **Save** (shows "Saving…" while uploading). Paid subscriptions move to the **History** tab, showing Payment Date, Approved On, Planned, Start/End Date, Method, Delay, and a **View** link to the uploaded receipt (clicking a history row also opens the receipt).

## 4. Renew a subscription

1. Go to **Doc Submanager > Resource Manager > Renewals > Sub Renewal** (`/doc-submanager/subscription/renewal`), titled "Subscription Renewals".
2. **Pending** tab shows subscriptions nearing/at their end date. Click **Action** (with a refresh icon) on a row.
3. In the **Process Renewal** modal, review Sub No, Company, Subscriber, Price, and Current End Date. The modal explains: *"This will create a renewal request with Pending status. It will appear in Subscription Approvals for approval, and after approval it will appear in Subscription Payments."*
4. Click **Send for Approval** to submit, or **Cancel** to close.
5. The renewal then must go through **Sub Approval** (status "Renewal Approved" or rejected) and then **Sub Payment**, same as a new subscription. Completed renewals appear in the **Sub Renewal > History** tab, showing Renewal No and Renewal Sub status (Approved/Rejected).

## Status flow summary

Create (Pending) → **Sub Approval** (Approve/Reject) → **Sub Payment** (Pay, upload receipt, set new Start/End Date) → subscription becomes "Paid" and active until End Date → **Sub Renewal** (Send for Approval) restarts the cycle via approval and payment again.

## Notes on fields captured

Based on backend request examples: creating a subscription sends `companyName`, `subscriberName`, `subscriptionName`, `price`, `frequency`, `purpose`. Approving sends `status` (`Approved`/`Rejected`/`Renewal Approved`) and `remarks` to `PATCH /doc-submanager/subscription/:id/approve`. Paying sends `file` (receipt), `subscriptionId`, `startDate`, `endDate`, `paymentMethod`, `needsRenewal` to `POST /doc-submanager/subscription/pay`.
