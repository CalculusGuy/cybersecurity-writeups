# Lab 03 — Inconsistent Security Controls

**Difficulty:** Apprentice  
**Category:** Business Logic Vulnerabilities  
**Platform:** PortSwigger Web Security Academy

---

## Goal
Access the admin panel by exploiting the fact that email domain validation is enforced during registration but NOT during email change.

---

## Steps

1. Register a new account using any email address (e.g., attacker@exploit-server.net)
2. Verify the account via the confirmation email
3. Log in to the account
4. Go to **My Account** → change email to any `@dontwannacry.com` address
   ```
   hacker@dontwannacry.com
   ```
5. The application grants admin privileges based on the new email domain
6. Navigate to `/admin`
7. Delete `carlos`

---

## What I Learned

The application correctly validated the email domain during **registration** — but completely forgot to apply the same validation when a user **changed their email** later.

This is a classic example of **inconsistent security controls** — the rule exists in one place but not everywhere it needs to be enforced.

Real-world equivalent: companies that check background checks at hiring but never for internal transfers.

### 🔴 Attack
Register normally → verify account → change email to `@dontwannacry.com` domain → gain admin access without ever having a real company email.

### 🔵 Blue Team Detection
- Alert on email domain changes to privileged domains (e.g., internal company domains)
- Log all email change events and flag changes to high-trust domains
- Review admin access grants — trigger alert when a recently-changed email gains elevated privileges

### 🛡️ Fix
- Apply the same domain validation rules at **every point** where email is accepted — registration, update, and password reset
- Re-verify email ownership after any email change before restoring privileges
- Privileged access should require re-authentication after sensitive account changes
