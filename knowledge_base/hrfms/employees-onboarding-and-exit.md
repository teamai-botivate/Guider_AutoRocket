---
title: HR Employees, Onboarding, and Exit Process
module: hrfms
tags: [hrfms, employee, onboarding, after-joining, after-leaving, exit]
---

# HR Employees, Onboarding, and Exit Process

Employee records are the HRFMS master data for staff. They connect to onboarding, salary, attendance, leave, advances, and exit processing.

## Employee master

Path: `/hr/employee`

The employee API uses `/hrfms/employee` and supports:

- List employees.
- View one employee.
- Create an employee with optional photo and resume files.
- Update an employee with optional photo/resume replacement.
- Delete an employee.
- Fetch employee stats.
- Fetch leaving employees.

Employee fields accepted by the API include name, phone, email, designation, department, joining date, status, manager name, blood group, work location, applying-for/vacancy references, candidate enquiry number, bank account, IFSC code, and separation fields such as last working day, termination date, separation type, and leaving reason.

## After Joining / onboarding

The employee API exposes onboarding-specific endpoints:

- `GET /hrfms/employee/onboarding` - employees in onboarding.
- `PATCH /hrfms/employee/:id/onboarding` - update onboarding state.
- `GET /hrfms/employee/joined-without-account` - joined employees without a user account.
- `GET /hrfms/employee/checklist-config` and `PATCH /hrfms/employee/checklist-config` - configure onboarding checklist items.

Onboarding fields include standard toggles such as offer letter issued, ID card issued, induction done, plus an onboarding checklist and custom checklist items.

## After Leaving / exit workflow

Path: `/hr/after-leaving`

The After Leaving flow manages resignation and exit clearance.

1. Fetch active employees from `/hrfms/employee`.
2. Record a resignation with employee, resignation date, last working day, and leaving reason.
3. Track leaving employees from `/hrfms/employee/leaving`.
4. Process exit details such as status, exit checklist, advance-payment taken/amount/settled, and experience-letter issued.
5. Deactivate the linked user account when needed.
6. Settle active loans from the employee's loan list using the advance-request loan-settlement endpoint.

Leaving employee records show department, status, resignation/termination/last-working-day dates, separation type, leaving reason, exit checklist, advance settlement flags, experience-letter flag, linked user-account status, and active loans.

