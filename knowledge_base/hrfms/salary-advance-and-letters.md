---
title: HR Salary Management, Advances, and Letters
module: hrfms
tags: [hrfms, salary, payroll, payslip, advance, loan, letters]
---

# HR Salary Management, Advances, and Letters

HRFMS includes payroll/salary operations, employee advances/loans, and HR document templates.

## Salary Management

Path: `/hr/salary-management`

The salary-management frontend uses `/hrfms/salary/*` APIs.

Main capabilities:

- Payroll overview by month and year.
- Salary hold/unhold for an employee, with optional reason.
- Generate a payslip for employee/month/year.
- Mark a payslip as paid.
- List salary employees with search and department filters.
- View an employee's monthly attendance.
- View employee loans.
- Fetch or update an employee salary structure.
- View all salary transactions with filters for search, month, year, status, employee status, page, and limit.

There is also a dynamic salary detail route: `/hr/salary-management/[employeeId]`.

## Advance / employee loan

Path: `/hr/advance`

The advance-request API uses `/hrfms/advance-request`.

Supported workflow:

1. Submit an advance request.
2. View all requests or requests by employee.
3. Open a specific request by ID.
4. Update request details.
5. Approve/reject/change status.
6. View loan history for an approved/requested advance.
7. Fetch advance dashboard stats.
8. Mark an advance complete after repayment.
9. Delete a request if appropriate.

The route `/hr/advance/loan/[advanceId]` opens loan/transaction detail for a specific advance.

Salary and advances connect: salary dashboards can show active salary holds and employee-loan counts, and the exit flow can settle employee loans.

## Letter Formatter

Path: `/hr/letter-formatter`

The letter formatter uses `/hrfms/letter-template` APIs.

Capabilities:

- List HR letter templates.
- View one template.
- Create/update/delete templates.
- Fetch field values for a template, optionally for a specific employee.
- Save template field values.
- Render a letter for a template and employee.

Use this area for reusable HR documents such as offer letters, appointment letters, experience letters, or other employee-specific letters where template fields need to be filled and rendered.

