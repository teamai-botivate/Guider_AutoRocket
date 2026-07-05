---
title: Managing Your Profile, Sessions and Notifications
module: common
tags: [profile, account-settings, notifications, sessions, avatar]
---

## Getting to your profile

Click your name/avatar in the top navigation bar to open the **Account Center**, which lives at `/profile/{yourUserId}/...`. It has its own left-hand navigation (on mobile, a horizontal scrollable tab bar) with sections such as **My Profile**, **Company Profile** (admins), **Create User** (admins), **Security**, **Notifications**, **Permissions** (admins), **System Settings** (admins), **Login Sessions**, **Account Billing** and **Platform Subscription** (admins). Which sections you see depends on your role and on menu access your admin has granted you — regular users typically see at least **My Profile**, **Security**, **Notifications**, and **Login Sessions**.

## Updating your profile (My Profile)

On the **My Profile** page (`/profile/{yourId}/my-profile`):
1. Click **Update Profile** to enter edit mode.
2. Editable fields include **Full Name**, **Username**, **Email Address**, **Phone Number**, and **Department** (choose from a dropdown of your organization's departments).
3. To change your photo, click the camera icon over your avatar, pick a JPG/PNG/WebP image under 5 MB — it shows a local preview immediately and marks itself "pending" until you save.
4. Click **Save Changes** to persist the edits (and upload the pending photo, if any) or **Cancel** to discard.

The page also shows read-only info: **Employee ID**, **Role**, **Reporting Person**, **HOD Name**, **Weekend Off**, account status (Active/Inactive), email verification status, a profile-completion percentage, and your assigned department(s).

## Login Sessions

**Profile → Login Sessions** (`/profile/{yourId}/sessions`) lists every device currently signed in to your account: device name, OS, IP address, and last-sync time, with the device you're using right now marked **Current**. Click **Log Out** next to any other session to remotely sign that device out. A **Login Activity** table below shows recent sign-in/sign-out/password-change/2FA events with device and IP.

The same session table and activity log also appear at the bottom of the **Security** page.

## Notifications

There are two distinct things called "notifications" in the product:

1. **The notification bell in the top navbar** — this is the real, live notification center. It shows a red badge with your unread count, and clicking it opens a dropdown panel listing notifications (e.g. password-set or forgot-password events) with a timestamp ("5m ago", etc.). From the panel you can:
   - Click a notification to mark it as read.
   - Click the **X** that appears on hover to dismiss/delete a notification.
   - Click **Mark all read** (shown when you have unread notifasctions) to clear the unread badge.
   New notifications also arrive in real time via a live connection while you have the app open — you don't need to refresh the page.

2. **Profile → Notifications** (`/profile/{yourId}/notifications`) — a preferences screen with toggle switches for **Email Notifications**, **SMS Notifications**, **Push Notifications**, and **In-App Alerts**, plus a **Save Preferences** / **Save Changes** button and a **Reset** button. Use this page to indicate which channels you'd generally like to be notified through.

Note: at the time of writing, the channel toggles on the Profile → Notifications preferences page are not yet wired to a live backend setting — treat them as your stated preference rather than a guaranteed on/off switch for each channel; the top-navbar notification bell is the reliable, functioning notification feed.
