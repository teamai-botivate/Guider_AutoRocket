---
title: HR Attendance and Leave Management
module: hrfms
tags: [hrfms, attendance, leave, shifts, claims, approvals]
---

# HR Attendance and Leave Management

HRFMS has separate areas for attendance tracking and HR leave requests.

## Attendance

Path: `/hr/attendance`

The attendance APIs live under `/hrfms/attendance`.

Core attendance actions:

1. Fetch employees for attendance from `/hrfms/attendance/employees`.
2. Fetch company shifts from `/hrfms/attendance/shifts`.
3. Fetch daily attendance for a date from `/hrfms/attendance/daily?date=YYYY-MM-DD`.
4. Create/update an attendance record with employee, date, shift, check-in, check-out, status, and notes.
5. Fetch an employee's monthly records from `/hrfms/attendance/monthly`.
6. Fetch monthly summary from `/hrfms/attendance/monthly-summary`.
7. Fetch holidays for the year from Checklist & Delegation settings (`/checklist-delegation/settings/holidays`).

Attendance claims are also handled here:

- Submit a claim.
- Admin-submit a claim for an employee.
- View my claims.
- View all claims filtered by status or claim type.
- Approve or reject a claim with review notes.
- Edit a previous approval/rejection review.

## Leave Management

Path: `/hr/leave`

The HR leave API lives under `/hrfms/leave`.

Submitting a leave request requires employee, HOD, substitute, date range, day-by-day leave entries, and reason. Leave day entries support full day or half day, and half days can be first half or second half.

Typical leave workflow:

1. Create a request with employee name/id, department, HOD name/id, substitute, from/to dates, leave-days list, and reason.
2. HR/admin views all leave requests or pending approvals.
3. HR updates the request status with optional remarks.
4. HR can also apply per-day decisions on the leave-days list, approving or rejecting individual days.
5. Requests can be fetched by employee for employee-specific history.

Note: the sidebar also links to `/checklist&deligation/leave-management`, which is a separate Checklist & Delegation leave-management page, not the same code path as `/hr/leave`.

