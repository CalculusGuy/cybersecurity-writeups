# PortSwigger — Business Logic Vulnerabilities

Writeups for all solved Business Logic labs from PortSwigger Web Security Academy.

Each writeup follows the format: **Goal → Steps/Payloads → What I Learned** with a purple team breakdown (Attack + Detection + Fix).

---

| Category | Status |
|----------|--------|
| Path Traversal | ✅ Complete |
| Access Control | ✅ Complete |
| Authentication | ✅ Complete |
| SQL Injection + Blind SQLi | ✅ Complete |
| XSS — Apprentice + Practitioner | ✅ Complete |
| CSRF — All Practitioner (11 labs) | ✅ Complete |
| SSRF — Including open redirect chain | ✅ Complete |
| XXE — Including Expert level | ✅ Complete |
| Business Logic — 9 labs (4 Apprentice + 4 Practitioner + 1 Expert) | ✅ Complete |

---

## Key Concepts Covered

- **Numeric manipulation** — negative quantities, price tampering
- **Workflow abuse** — skipping steps, replaying requests, breaking state machines
- **Authorization flaws** — inconsistent validation, weak endpoint isolation, privilege escalation
- **Business rule failures** — coupon reuse, incomplete state tracking
- **Input handling inconsistencies** — truncation attacks, layer mismatches

---

## Purple Team Approach

Every writeup includes:
- 🔴 **Red Team** — how the attack works
- 🔵 **Blue Team** — detection strategies and SIEM rules
- 🛡️ **Fix** — secure development recommendations

*By Nilanjan Chowdhury — github.com/CalculusGuy*
