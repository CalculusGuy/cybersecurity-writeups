# PortSwigger SQL Injection Writeups
**Platform:** PortSwigger Web Security Academy
**Category:** SQL Injection
**Date:** April 2026

---

## Lab 1 — SQL Injection in WHERE Clause (Hidden Data)
**Method:** Modified category filter in URL
**Payload:** `'+OR+1=1--`
**What I learned:** `'` breaks out of string, `OR 1=1` makes condition always true, `--` comments out the rest — reveals all hidden/unreleased data

---

## Lab 2 — SQL Injection Login Bypass
**Method:** SQLi in username field on login page
**Payload:** `administrator'--`
**What I learned:** `'--` comments out the password check entirely — authentication bypassed with no password needed

---

## Lab 3 — UNION Attack, Determining Column Count
**Method:** Added NULLs to UNION SELECT until no error
**Payload:** `' UNION SELECT NULL,NULL,NULL--`
**Result:** 3 columns returned by original query
**What I learned:** UNION requires matching column counts — use NULL (compatible with any type) and increment until page loads without error
