---
title: Doc SubManager - Master Data (Companies, Document Types, Categories)
module: doc_sub_manager
tags: [doc-submanager, master-data, setup]
---

# Master Data in Doc SubManager

Master Data is a small supporting reference list used to power the searchable dropdowns (Company Name, Document Type, Category) elsewhere in Doc SubManager — for example when adding a Document.

## View and add master records

1. Go to **Doc Submanager > Master Data** (`/doc-submanager/master`), titled "Master Data" with the description "Centralized management for core document and company records".
2. The table lists existing records with columns: **Company Name**, **Document Type**, **Category**.
3. Click **Add Record** in the page header to open the **Add Master Record** modal.
4. Fill in:
   - **Company Name** (searchable dropdown, add-new supported)
   - **Document Type** (searchable dropdown, add-new supported)
   - **Category** (searchable dropdown)
5. Click **Save Record** to add it, or **Cancel** to close without saving.

## How Master Data is used

When a new Document is created (see the Documents guide) with a company/type/category combination that doesn't already exist in Master Data, the system automatically adds it as a new Master Data record — so most of the time this list grows on its own as new documents are entered. Manually adding a record here is mainly useful to pre-populate the dropdown options before anyone creates the related documents.
