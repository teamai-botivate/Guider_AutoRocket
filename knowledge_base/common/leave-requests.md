---
title: Applying for Leave (Employee Self-Service)
module: common
tags: [leave, hr, self-service, time-off, approval]
---

## Where to apply

Go to **HR → Leave** (`/hr/leave`), which opens the **Leave Management** page ("Time Off"). This same screen doubles as your personal leave history and, for admins/HR, an approval queue — what you can do on it depends on your role.

## Applying for leave

1. Click **Apply Leave** (visible if you have an employee record, or if you're a Super Admin).
2. In the **Apply for Leave** form, fill in:
   - **Employee** — pre-filled with your own name (admins can pick a different employee to apply on their behalf).
   - **Department** — defaults to your department; choose from the dropdown if it needs changing.
   - **From Date** and **To Date** — pick your leave date range (cannot be in the past).
   - **Select Days** — once a date range is chosen, each day in the range appears as a checkbox row. For each day you can:
     - Uncheck it to exclude that day from the request.
     - Mark it **Full Day** or **Half Day**.
     - If Half Day, choose **1st Half** or **2nd Half**.
     A running total of requested days is shown.
   - **Reason for Leave** — free-text explanation (required).
   - **HOD / Manager** — select your reporting manager from the dropdown (required).
   - **Substitute** — name of the colleague covering your work while you're away (required).
3. Click **Submit Application**. On success you'll see an "Application Submitted!" confirmation with the total number of days, and the request is sent to HR/your manager for review.

## Tracking your requests

The Leave Management page has two tabs:
- **Pending** — leave requests awaiting a decision, with a count badge.
- **Processed** — requests that have already been approved, partially approved, rejected, or cancelled, with a count badge.

Each row shows the date range, number of days, and a color-coded status pill: **PENDING**, **APPROVED**, **PARTIAL** (some days in a multi-day request were approved and others rejected), **REJECTED**, or **CANCELLED**. Click **View** on any row to open a read-only detail view showing the day-by-day breakdown (if applicable), your stated reason, who submitted it and when, who approved/rejected it and when, and any HR remarks (especially important on rejections, since HR is required to provide a rejection reason).

## Notes

- Regular employees only ever see their own leave requests on this page; users with ADMIN or SUPERADMIN roles instead see every employee's requests, plus approve/reject controls, bulk-selection actions, and search — that manager/HR-side approval workflow is out of scope for this self-service doc.
- The small bell/globe icons in the Leave Management page header are cosmetic in the current build and not the place to check your actual notifications — use the notification bell in the main top navigation bar instead (see "Profile, Sessions and Notifications").
