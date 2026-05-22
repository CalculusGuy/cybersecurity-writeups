# Lab 06 — Weak Isolation on Dual-Use Endpoint

**Difficulty:** Practitioner  
**Category:** Business Logic Vulnerabilities  
**Platform:** PortSwigger Web Security Academy

---

## Goal
Access the admin panel by exploiting a password reset endpoint that performs both self-service and admin-level password changes on the same endpoint — without properly enforcing authorization.

---

## Steps

1. Log in as `wiener` (normal user)
2. Go to **My Account** → change password
3. Intercept the `POST /my-account/change-password` request in Burp Suite
4. Observe the original request body:
   ```
   username=wiener&current-password=peter&new-password-1=test&new-password-2=test
   ```
5. Modify the request — **remove** `current-password` parameter and **change username** to `administrator`:
   ```
   username=administrator&new-password-1=hacked&new-password-2=hacked
   ```
6. Forward the request — admin password changed successfully
7. Log in as `administrator` with new password
8. Navigate to `/admin` → delete `carlos`

---

## What I Learned

The endpoint handled both regular password changes (requiring `current-password`) and admin-level resets (not requiring it) on the **same endpoint**. When `current-password` was removed, the application didn't reject the request — it silently fell through to the admin code path.

**The authorization check depended entirely on user-controlled input** — the presence or absence of a parameter the attacker could simply remove.

### 🔴 Attack
Send the change-password request to Burp Repeater. Remove `current-password`, change `username` to `administrator`. The server processes it without any authorization check.

### 🔵 Blue Team Detection
- Alert on password change requests missing expected parameters (e.g., `current-password`)
- Log all admin account password change events with source IP and session details
- SIEM rule: flag any password change for privileged accounts not initiated through an admin-specific authenticated flow

### 🛡️ Fix
- **Never use the same endpoint** for self-service and admin operations
- Enforce `current-password` validation server-side regardless of what parameters are present
- Authorization must be based on the **authenticated session**, never on user-supplied parameters like `username`
- Implement separate, properly access-controlled endpoints for admin operations
