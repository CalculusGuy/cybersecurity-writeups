# Lab 05 — Inconsistent Handling of Exceptional Input

**Difficulty:** Practitioner  
**Category:** Business Logic Vulnerabilities  
**Platform:** PortSwigger Web Security Academy

---

## Goal
Gain admin access by exploiting a discrepancy between the email length used for verification and the email length stored in the database.

---

## Steps

1. Investigate `/admin` — access denied, requires `@dontwannacry.com` email
2. Register a new account with a crafted oversized email:
   ```
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa@dontwannacry.com
   ```
   Total length: > 255 characters, ending in `@dontwannacry.com`
3. The verification email is sent to the **full address** — receive it via exploit server
4. Verify the account
5. Log in — check **My Account**
6. The stored email is truncated to 255 characters — ends in `@dontwannacry.com`
7. Application grants admin access based on stored (truncated) email
8. Navigate to `/admin` → delete `carlos`

---

## What I Learned

The application sent the verification email to the **full** address, but **stored only the first 255 characters** in the database. Because the crafted email was designed so that the 255-char truncation still ends with `@dontwannacry.com`, the system treated the account as a trusted employee.

This is a **layer inconsistency attack** — the email transport layer and the storage layer handled the same input differently.

Real-world impact: this exact class of bug has appeared in production identity systems where database field limits differ from validation layer assumptions.

### 🔴 Attack
Craft an email longer than the database field limit (255 chars) that ends with the trusted domain. The verification layer processes the full address, but the storage layer truncates it — resulting in a stored email that appears to belong to the trusted domain.

### 🔵 Blue Team Detection
- Alert on registration attempts with email addresses longer than 100 characters
- Log all truncation events in the database layer
- Monitor for newly registered accounts that immediately gain admin-level privileges

### 🛡️ Fix
- Enforce maximum email length at the **input validation layer** before storage
- Truncate (or reject) input BEFORE sending verification, not after
- Ensure the email stored matches exactly the email verified — no post-verification transformation
- Apply consistent length limits across all layers: API, application, and database
