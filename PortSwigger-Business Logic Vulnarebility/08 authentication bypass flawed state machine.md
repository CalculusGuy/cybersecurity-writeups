# Lab 08 — Authentication Bypass via Flawed State Machine

**Difficulty:** Practitioner  
**Category:** Business Logic Vulnerabilities  
**Platform:** PortSwigger Web Security Academy

---

## Goal
Bypass the role selection step during login to land in an admin session by exploiting a flawed authentication state machine.

---

## Steps

1. Turn on Burp Intercept
2. Log in with `wiener:peter`
3. Forward the `POST /login` request
4. The next request is `GET /role-selector` — **DROP this request** (do not forward)
5. Turn off Burp Intercept
6. Browse to `/` — notice **Admin panel** is now visible in the navigation
7. Navigate to `/admin`
8. Delete `carlos` — lab solved

---

## What I Learned

The application's login flow was designed as a state machine:
```
POST /login → GET /role-selector → Authorized Session
```

The role-selector step was supposed to assign the user's role before granting a session. But when that step was **dropped/skipped**, the server ended up in an inconsistent state:
- Authentication: completed ✅
- Role assignment: never happened ❌

Instead of failing safely (invalidating the session), the application **defaulted to admin behavior** — the most dangerous possible failure mode.

This is directly analogous to real-world **MFA bypass attacks** — drop the MFA step, land in an authenticated session.

### 🔴 Attack
Intercept login flow. Forward `POST /login`. Drop `GET /role-selector`. Turn off intercept. Application grants admin access because role defaults to highest privilege when unassigned.

### 🔵 Blue Team Detection
- Alert on authenticated sessions where role assignment step was never completed
- Log and monitor incomplete authentication flows — sessions that skip expected steps
- SIEM rule: flag sessions where login occurred but role-selector endpoint was never hit
- Monitor for admin panel access from sessions with incomplete auth flows

### 🛡️ Fix
- Applications must **fail safely** — if any required workflow step is missing, invalidate the session and redirect to login
- Never default to elevated privileges when state is ambiguous — always default to least privilege
- Implement server-side state validation: before granting any access, confirm all required auth steps were completed
- Role assignment must be mandatory, not optional — missing role = no access, not default access
