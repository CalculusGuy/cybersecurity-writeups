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

---

## 🔍 Why This Vulnerability Exists

SQL Injection occurs when user-controlled input is directly inserted into a SQL query without proper validation or parameterization.

Example backend query:

```sql
SELECT * FROM users WHERE username = 'input' AND password = 'input';

If an attacker inputs:

' OR 1=1--

The query becomes:

SELECT * FROM users WHERE username = '' OR 1=1--' AND password = '';
OR 1=1 always evaluates to TRUE
-- comments out the rest of the query

This allows the attacker to bypass authentication and gain unauthorized access.    

 How to Prevent It
Use Prepared Statements (Parameterized Queries)
→ Ensures input is treated as data, not code
Avoid building queries using string concatenation
Use ORM frameworks (e.g., Django ORM, SQLAlchemy)
Apply input validation (but NOT as the only defense)
📌 Key Takeaway

SQL Injection is not just about payloads — it’s about understanding how user input interacts with backend database queries.


---

# 🧠 What this upgrade does

Before:
- “Used payload X”

After:
- Shows:
  - Backend understanding ✅  
  - Attacker mindset ✅  
  - Defense awareness ✅  
```md
## 🧠 Real-World Impact
SQL Injection can lead to full database compromise, data leakage, and in some cases remote code execution depending on database permissions.


