---
title: Logging In and Resetting Your Password
module: common
tags: [login, authentication, password-reset, otp, two-factor-auth]
---

## Logging in

1. Go to the login page (`/login`).
2. Enter your **Mobile Number** (e.g. `+91 9XXXXXXXXX`).
3. Enter your **Password** (at least 8 characters). Use the eye icon inside the password field to show/hide what you typed.
4. Optionally check **Remember me**.
5. Click **Sign in**.

If your account also supports signing in with an Employee ID instead of a mobile number, the platform has that capability built in, but the current login screen only exposes the Mobile Number field — use whichever identifier your organization has told you to log in with.

### What happens next
- If your password was set by an admin and has never been changed, you'll be redirected to a **Set Your New Password** screen and required to choose a new password before continuing.
- If your account is still awaiting approval, you'll see an "Account Pending Verification" notice on the login screen telling you to wait for AutoRocket approval or contact `support@autorocket.in`.
- If your account has two-factor authentication (2FA) enabled, after entering your mobile number and password you'll be prompted for a **6-digit code** from your authenticator app (Google Authenticator or Authy) on a "Two-Factor Auth" screen. Enter the code and click **Verify**.
- Otherwise, you're taken straight to your dashboard.

## Resetting a forgotten password

Go to the login page and click **Forgot password?** (or navigate to `/forgot-password`). This is a mobile-number + OTP flow, not an email-link flow:

1. **Enter your registered mobile number** and click **Send OTP**. The system sends a one-time code to your organization admin's email (not to you directly) — this is by design, since the admin needs to relay it to you or verify the request.
2. **Enter the 6-digit OTP** shown on the "Check Admin Email" screen. The masked admin email address the OTP was sent to is displayed for confirmation. If you don't receive it, use **Resend OTP** (disabled for 30 seconds after each send).
3. Once the OTP is verified, you'll land on **Reset Password**: enter a **New Password** and **Confirm Password** (minimum 8 characters, both must match).
4. On success you'll see a confirmation screen and can click **Back to Login** to sign in with your new password.

## Setting a new password when required (first login / temporary password)

If you log in with a temporary password issued by an admin, you're redirected to a dedicated **Set Your New Password** page instead of the dashboard:
1. Enter a **New Password** (minimum 8 characters — you cannot reuse the temporary password).
2. Enter the same value in **Confirm Password**.
3. Click **Set Password & Continue**. You'll then be redirected back to the login page to sign in with the new password.

## Changing your password while logged in

Go to **Profile → Security** (`/profile/{yourId}/security`):
1. Under **Password Update**, fill in **Current Password**, **New Password**, and **Confirm New Password** (minimum 8 characters).
2. Click **Update Password**.

The same Security page also lets you enable/disable **Two-Factor Authentication** (scan a QR code with an authenticator app, then confirm with a 6-digit code) and review **Active Sessions** and **Login Activity** (see "Profile, Sessions and Notifications" doc for details).

Note: the notification-settings and channel toggles described elsewhere are separate from security; password and 2FA changes always go through the Security tab.
