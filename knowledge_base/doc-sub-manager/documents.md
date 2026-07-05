---
title: Doc SubManager - Managing Documents and Renewals
module: doc_sub_manager
tags: [doc-submanager, documents, renewal, upload, share]
---

# Managing Documents in Doc SubManager

Doc SubManager stores company/personal/director documents in a central repository and tracks their renewal dates. Navigate via the left sidebar: **Doc Submanager > Resource Manager**.

## 1. Add a new document

1. Go to **Doc Submanager > Resource Manager > All Documents** (`/doc-submanager/document/all`). This page is titled "Documents Repository".
2. Click the **Add** button in the page header to open the **New Document Entry** modal.
3. For each document entry, fill in:
   - **Document Name** (free text, e.g. "Agreement")
   - **Document Type** (searchable dropdown; type a new value and use "add new" to create an option that doesn't exist yet)
   - **Category** (searchable dropdown, e.g. Personal / Company / Director; same add-new behavior)
   - The name field label changes based on category — it shows **Company Name** for Company, **Person Name** for Personal, **Director Name** for Director category
   - **Renewal Needed** checkbox — if checked, a renewal date field appears and becomes required
   - **Upload File** — attach the document file (choose file)
4. Click **Add Another Document (n/10)** to add up to 10 documents in the same batch before saving.
5. Click **Save Documents** to submit. Each entry uploads its file (via presigned URL) and creates a document record; if the company/type/category combination is new, it is also added to Master Data automatically.
6. Click **Cancel** to close without saving.

## 2. View, edit, download, delete documents

On the **Documents Repository** page:
- Use the category filter tabs (**All / Personal / Company / Director**) above the table to narrow the list.
- Use the search box in the page header to search the table.
- Table columns: checkbox select, Actions, S.No, Document Name, Type, Category, Owner, Renewal (Yes/No badge), Renewal Date, File.
- Click the **Edit** (pencil) icon in the Actions column to edit a document's details.
- Click the **Trash** icon to delete a document.
- Click **View** under the File column to download/open the attached file.
- Click the **⋯ (more)** icon to reveal **Email** and **WhatsApp** share options for that single document.

## 3. Share documents (Email / WhatsApp)

1. From **All Documents**, either:
   - Open the ⋯ menu on a row and choose **Email** or **WhatsApp**, or
   - Select one or more documents via the row checkboxes, then click the **Share** button that appears next to the "N Selected" badge (batch share defaults to email).
2. The **Share Document** modal opens, showing the document name.
   - For Email: fill **Recipient Name**, **Email Address**, **Subject**, **Message**.
   - For WhatsApp: fill **WhatsApp Number** (prefixed with +91).
3. Click **Share Now** to send. Click **Cancel** to close without sharing.
4. All shares are logged and visible under **Doc Submanager > Resource Manager > Doc Shared** (`/doc-submanager/document/shared`), titled "Share History" — showing Share No, Date & Time, Serial No, Document Name, File, Via (Email/WhatsApp), Recipient, Contact.

## 4. Renew a document

1. Go to **Doc Submanager > Resource Manager > Renewals > Doc Renewal** (`/doc-submanager/document/renewal`), titled "Document Renewals".
2. The page has two tabs: **Pending** and **History**.
3. On the **Pending** tab, find the document and click the **Renewal** button (with a refresh icon) in its Action column. This opens the **Process Renewal** modal, showing the document's current name, serial number, company, and current renewal date/file.
4. Toggle **Again Renewal?** on if this document will need another renewal cycle after this one. When toggled on, two additional fields appear:
   - **Next Renewal Date**
   - **New Document File** (upload the newly renewed document)
5. Click **Save Record** to submit (button shows "Uploading…" while in progress), or **Cancel** to close.
6. Completed renewals move to the **History** tab, showing Renewal No, Serial No, Document Name, Company, Old Expiry, New Expiry, Renewed On, and a link to View the file.

## Notes on fields captured

Based on the backend request examples, creating a document sends: `file`, `companyName`, `documentType`, `category`, `documentName`, `needsRenewal`, `currentExpiryDate`, `nextRenewalDate`, `status`. Renewing a document sends: `file`, `documentId`, `newExpiryDate`, `needsRenewal`.
