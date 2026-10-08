# Lab 02 — 2FA Simple Bypass

**Difficulty:** Apprentice
**Category:** Authentication Vulnerabilities

## Problem

The application has a two-factor authentication step after login. But the 2FA check can be skipped by navigating directly to a URL that only authenticated users should access.

## Method

1. Log in with valid credentials
2. The application asks for a 2FA code
3. Intercept the request flow
4. Notice that after the password step, a session is already created
5. The 2FA verification step is a separate endpoint — but the session is already "logged in"
6. Navigate directly to `/my-account` without completing 2FA

## Solution

- Logged in with the victim's credentials
- When prompted for 2FA, changed the URL directly to `/my-account`
- The page rendered the account dashboard — 2FA was skipped
- Lab solved

## Learning

**2FA is often bolted on, not built in.** If the session is fully authenticated *before* the 2FA check, the check is just a UI gate — not a security control.

Common 2FA bypass patterns:
- Direct URL access (this lab)
- Reusing the session cookie from before 2FA
- Brute-forcing the 2FA code (no rate limit)
- Response manipulation ("2fa_required": false)

## Fixes

- Do **not** issue a fully authenticated session until 2FA is verified
- Use an intermediate "pending authentication" state with limited scope
- Server-side enforce: every protected route must verify the 2FA flag was set
- Rotate session tokens after 2FA completes
- Rate-limit 2FA attempts
