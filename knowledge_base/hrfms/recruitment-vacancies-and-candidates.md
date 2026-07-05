---
title: HR Recruitment, Job Vacancies, and Candidate Enquiries
module: hrfms
tags: [hrfms, recruitment, job-vacancy, candidate, enquiry, joining]
---

# HR Recruitment, Job Vacancies, and Candidate Enquiries

HR recruitment is built around vacancies (called HR indents in the API), candidate enquiries, and joining initiation.

## Job Vacancy

Path: `/hr/indent`

Use **HR FMS > Job Vacancy** to manage hiring requirements. The frontend uses `/hrfms/indent` APIs.

Vacancy/indent fields supported by the API include:

- **Title**
- **Gender** - Male, Female, or Any
- **Department**
- **Preference** - Fresher, Experience, or Any
- **Experience Years**
- **No. of Post**
- **Completion Date**
- **Social Site** list
- **Job Type** list
- **Budget**
- **Priority**
- **Status**

The API also has a pending-vacancy endpoint (`/hrfms/indent/get-pending`) used for vacancy queues.

## Find Enquiry / Candidate History

Path: `/hr/find-enquiry`

Use **HR FMS > Find Enquiry** to track candidates and recruitment calls. The frontend candidate API uses:

- `POST /hrfms/candidate/history` to fetch candidate history.
- `POST /hrfms/candidate/submit` to add a candidate with optional photo/resume.
- `PATCH /hrfms/candidate/:id` to update candidate details.
- `GET /hrfms/candidate/by-indent/:indentId` to filter candidates by vacancy.
- `POST /hrfms/candidate/:id/log-call` to log call status and notes.
- `PATCH /hrfms/candidate/:id/doc-verification` for document verification.

Candidate submission fields include candidate name, DOB, phone, email, previous company, experience, previous position, marital status, Aadhaar number, last salary, reason for leaving, current address, and optional linked indent.

## Candidate follow-up and joining

Candidate records support follow-up and joining preparation:

1. Save a follow-up date and notes against the candidate when another call is needed.
2. For selected candidates, initialize joining with joining date, employment type, offered CTC, monthly salary, probation months, reporting manager, work location, bank details, emergency contact, and issue flags such as email/mobile/laptop to be issued.
3. Verify documents with a document map and optional notes.
4. Mark the candidate as joined when onboarding is complete.

The separate joining API (`/hrfms/joining`) supports listing joinings, initiating a joining from a candidate, and updating joining status/documents.

