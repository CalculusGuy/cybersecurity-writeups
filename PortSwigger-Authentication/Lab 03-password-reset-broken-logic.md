# Lab 03 — Password Reset Broken Logic

**Difficulty:** Apprentice
**Category:** Authentication Vulnerabilities

## Problem

The password reset flow accepts a `username` (or user identifier) parameter in the reset request. But the server does not verify that the reset token belongs to that user.

## Method

1. Trigger a password reset for your own account
2. Intercept the reset form submission
3. Notice the request includes both the reset token AND a user identifier (e.g., `username=carlos`)
4. Change the user identifier to the victim's username
5. Submit the request

## Solution

- Requested a reset for my own account
- Intercepted the final "set new password" request
- Changed the `username` parameter from mine to the victim's
- The server accepted the reset token (still valid) but applied the new password to the victim's account
- Logged in as the victim

## Learning

**Reset tokens must be tied to the specific user.** If the token is validated but the user identifier isn't checked against the token, the token becomes a master key.

Related bugs to look for:
- Reset token reused across accounts
- Reset token leaked in the URL
- Reset via email change (change email → reset → access)
- Reset via predictable tokens

## Fixes

- Bind the reset token to the user at issue time (store `token → user_id` server-side)
- Ignore any client-supplied user identifier during the reset step
- Expire tokens after a short window (15-30 minutes)
- Invalidate all active sessions when password is changed
- Send a confirmation email after password reset
- 
