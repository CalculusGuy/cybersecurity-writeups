# PortSwigger — Business Logic Vulnerabilities

Writeups for all solved Business Logic labs from PortSwigger Web Security Academy.

Each writeup follows the format: **Goal → Steps/Payloads → What I Learned** with a purple team breakdown (Attack + Detection + Fix).

---

## Labs Solved

| # | Lab | Difficulty | Status |
|---|-----|------------|--------|
| 01 | Excessive trust in client-side controls | Apprentice | ✅ Solved |
| 02 | High-level logic vulnerability | Apprentice | ✅ Solved |
| 03 | Inconsistent security controls | Apprentice | ✅ Solved |
| 04 | Flawed enforcement of business rules | Apprentice | ✅ Solved |
| 05 | Inconsistent handling of exceptional input | Practitioner | ✅ Solved |
| 06 | Weak isolation on dual-use endpoint | Practitioner | ✅ Solved |
| 07 | Insufficient workflow validation | Practitioner | ✅ Solved |
| 08 | Authentication bypass via flawed state machine | Practitioner | ✅ Solved |

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
