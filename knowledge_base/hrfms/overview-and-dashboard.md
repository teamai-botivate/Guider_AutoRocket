---
title: HRFMS Overview and Dashboard
module: hrfms
tags: [hrfms, hr, dashboard, navigation, workforce]
---

# HRFMS Overview and Dashboard

HRFMS is the HR operations module for workforce, hiring, attendance, leave, salary, advances, onboarding, exit, and letters.

## Main navigation

Under **HR FMS**, the sidebar includes:

| Sidebar label | Path | Purpose |
| --- | --- | --- |
| Dashboard | `/hr/dashboard` | HR summary for workforce, recruitment, joining, salary, leave, and advances |
| Employee | `/hr/employee` | Employee master list and employee records |
| Job Vacancy | `/hr/indent` | Hiring/vacancy indent creation and tracking |
| Find Enquiry | `/hr/find-enquiry` | Candidate enquiry/history and recruitment follow-up |
| After Joining | `/hr/after-joining` | Onboarding and joining-related work |
| After Leaving | `/hr/after-leaving` | Resignation, exit checklist, loan settlement, account deactivation |
| Attendance | `/hr/attendance` | Daily/monthly attendance, shifts, claims, approvals |
| Salary Management | `/hr/salary-management` | Payroll overview, salary structures, payslips, transactions |
| Leave Management | `/hr/leave` | HRFMS leave requests and approvals |
| Leave Management | `/checklist&deligation/leave-management` | Separate Checklist & Delegation leave-management screen |
| Advance | `/hr/advance` | Employee advance/loan requests and approval workflow |
| Letter Formatter | `/hr/letter-formatter` | HR letter templates, field values, rendered letters |

The codebase also contains HR pages/features for company calendar, reports, payroll, my attendance, my salary, my profile, social site, gate pass, and MIS report, but the core visible HRFMS sidebar items are the ones above.

## HR Dashboard

Open **HR FMS > Dashboard** (`/hr/dashboard`). The dashboard heading is **HR Dashboard** with the subtitle "Workforce, hiring pipeline, and leave overview."

The top KPI cards include:

- Active Employees
- Open Vacancies
- Total Applications
- Pending Joining
- Total Salary
- Salary Hold
- Employee Loan

Several cards open richer drill-down panels when clicked, such as employee movement, open vacancies, applications, pending joining, salary employee list, salary holds, and employee-loan requests.

Main dashboard sections include:

- **Recruitment Pipeline** - application breakdown by position/designation.
- **Hiring vs Attrition** - last six months hired vs left trend.
- Department/designation distribution charts.
- Leave type distribution.
- Open vacancies list.
- Recent candidate applications.
- Recent joinings.
- Salary summary by department.
- Advance summary for salary holds and loans.

The dashboard is fed by the HR dashboard v3 API and mixes hiring, employee, salary, leave, and advance data into one executive HR view.

