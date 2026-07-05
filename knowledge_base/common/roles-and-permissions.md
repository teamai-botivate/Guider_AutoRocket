---
title: Understanding Roles and Permissions
module: common
tags: [roles, permissions, access-control, admin, superadmin]
---

## The roles

The platform defines four roles:
- **SUPERADMIN** — full access to everything in your organization's account, including all Profile sections (Company Profile, Create User, Permissions, System Settings, Billing, Platform Subscription) and every business module.
- **ADMIN** — broad access: can manage users, view/edit company profile, billing and subscription, configure security/notifications/permissions/system settings for other users, but some Super Admin-only areas may be hidden.
- **USER** — a regular employee account. Sees only the Profile sections relevant to themselves: **My Profile**, **Security**, **Notifications**, and **Login Sessions** (this set can be widened by an admin — see below).
- **COMPANY** — a tenant-level account type used during onboarding/company-level flows.

Your role is shown as a colored badge (e.g. next to your name on **My Profile**, and throughout the Permissions screen) — Super Admin, Admin, or User, with each rendered in a distinct color.

## What determines what you can see and do

Two separate layers control your access:

1. **Role** — sets your baseline. Admins and Super Admins automatically get broader default access than a User.
2. **Per-user menu and section permissions** — an admin can individually grant or revoke:
   - **Sidebar menu access**: which top-level navigation items (Dashboard, AI Boardroom and its sub-agents, Training, Owner Dashboard, Executive Assistance, PC, Master/Settings, Directory) and which Profile sections (My Profile, Create User, Security, Notifications, Manage Users, Permissions, System Settings) you can see at all.
   - **Section-level permissions** within each business system/module: **Read**, **Write**, and **Delete** rights (Read also covers "can see" the section; Write also covers "can approve" within it). An admin can grant or revoke access to an entire module at once, or fine-tune individual sections, and can also assign a specific section to a specific user as their designated owner ("Assigned To").

If something you expect to see is missing from your sidebar or Profile menu, it most likely means an admin has not enabled that menu item or section for your account — contact your system administrator or HR/IT admin to request access, rather than trying to find a self-service way to grant it yourself. Managing other users' permissions is done from **Profile → Permissions**, which is only available to admins.

## Checking your own access

There isn't a dedicated "my permissions" self-view; the best ways to understand your current access as a regular user are:
- The set of items actually visible in your sidebar and in your Profile menu (both are already filtered to what you're allowed to see).
- The **Role** badge and **Department** shown on your **My Profile** page.
- Asking your admin, who can see your exact Read/Write/Delete grants per module section on the Permissions screen.
