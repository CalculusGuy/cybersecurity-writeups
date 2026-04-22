# OWASP Top 10 — Study Notes

**Date:** April 2026  
**Status:** ✅ Completed

---

## What is OWASP?
Open Web Application Security Project — a non-profit foundation 
that publishes free security resources. The OWASP Top 10 is a 
list of the 10 most critical web application security risks, 
updated every few years based on real world data.

---

## A01 — Broken Access Control
Users doing things they shouldn't be allowed to do.

**Real example from my labs:**
Changed `?id=wiener` to `?id=administrator` in PortSwigger 
Access Control lab — accessed admin panel without authorization.

---

## A02 — Cryptographic Failures
Sensitive data exposed due to weak or missing encryption.

**Real example from my labs:**
picoCTF RSA challenges — small exponent attack and multi-prime 
RSA factoring exploited weak cryptographic implementations.

---

## A03 — Injection
Untrusted data sent to an interpreter as part of a command.

**Real example from my labs:**
SQL Injection on PortSwigger — manipulating queries using 
`' OR 1=1--` to bypass authentication and extract data.

---

## A04 — Insecure Design
Flaws in architecture and design itself — not just bad code.
Cannot be fixed by patching alone — requires rebuilding.

**Key lesson:** You can patch bad code. You cannot patch bad design.

---

## A05 — Security Misconfiguration
Default passwords, unnecessary features enabled, directory 
listing exposed, verbose error messages.

**Real example from my work:**
Google Dorking with `intitle:"index of" "config.php"` found 
a real server exposing database.php, auth.php and config.php 
publicly — textbook A05 misconfiguration.

---

## A06 — Vulnerable and Outdated Components
Using libraries or frameworks with known vulnerabilities.

**Real world example:**
Log4Shell (2021) — a tiny Java logging library used by millions 
of applications. One string input caused remote code execution.
Affected Apple, Amazon, Tesla and government systems worldwide.

---

## A07 — Identification and Authentication Failures
Weak login mechanisms, no brute force protection, bad session 
management.

**Real example from my labs:**
PortSwigger Authentication labs — username enumeration via 
different server responses, brute forcing passwords with 
Burp Suite Intruder.

---

## A08 — Software and Data Integrity Failures
Trusting updates or data pipelines without verification.
Supply chain attacks live here.

**Real world example:**
SolarWinds attack — malicious code injected into a software 
update that was trusted and installed by thousands of companies 
including US government agencies.

---

## A09 — Security Logging and Monitoring Failures
No logs means attackers stay hidden. Most breaches go 
undetected for 200+ days because of missing or ignored logs.

**Key lesson:** If you cannot detect an attack, you cannot 
respond to it. Logging is not optional — it is defense.

---

## A10 — Server Side Request Forgery (SSRF)
Tricking a server into making HTTP requests on the attacker's 
behalf — reaching internal systems that should never be public.

**How it works:**
Attacker sends: `https://site.com/fetch?url=http://169.254.169.254/`
Server fetches AWS metadata containing credentials internally.
Attacker gets cloud credentials without ever touching the server.

**Real world example:**
Capital One 2019 — SSRF used to steal 100 million customer 
records from AWS metadata server.

---

## My OWASP Coverage So Far

| # | Vulnerability | Status |
|---|--------------|--------|
| A01 | Broken Access Control | ✅ PortSwigger labs |
| A02 | Cryptographic Failures | ✅ picoCTF RSA challenges |
| A03 | Injection | ✅ PortSwigger SQLi labs |
| A04 | Insecure Design | 📖 Theory only |
| A05 | Security Misconfiguration | ✅ Google Dorking real server |
| A06 | Vulnerable Components | 📖 Theory — Log4Shell |
| A07 | Auth Failures | ✅ PortSwigger Auth labs |
| A08 | Data Integrity Failures | 📖 Theory — SolarWinds |
| A09 | Logging Failures | 📖 Theory only |
| A10 | SSRF | 📖 Theory — PortSwigger next |

---

## Key Takeaway
6 out of 10 OWASP vulnerabilities covered through real !
hands-on labs and real world OSINT findings — not just theory.
