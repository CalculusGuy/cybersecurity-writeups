# Lab 04 — Flawed Enforcement of Business Rules

**Difficulty:** Apprentice  
**Category:** Business Logic Vulnerabilities  
**Platform:** PortSwigger Web Security Academy

---

## Goal
Buy the "Lightweight l33t Leather Jacket" at a heavily discounted price by exploiting a flaw in coupon reuse logic.

---

## Steps

1. Sign up for the newsletter to get coupon: `NEWCUST5`
2. Find the second coupon in the page: `SIGNUP30`
3. Add the jacket to the cart
4. Apply coupons in alternating order repeatedly:
   ```
   NEWCUST5 → SIGNUP30 → NEWCUST5 → SIGNUP30 → ...
   ```
5. The application only blocks **consecutive** reuse of the same coupon
6. Alternate until the jacket price drops within your store credit
7. Complete checkout

---

## What I Learned

The application prevented applying the same coupon twice **in a row** — but it didn't track the full transaction history. By alternating between two coupons, both could be applied unlimited times.

This is a **business rule enforcement failure** — the rule ("no coupon reuse") was partially implemented but not thoroughly enough.

### 🔴 Attack
Alternate `NEWCUST5` and `SIGNUP30` repeatedly. Each swap resets the "last used" check, allowing infinite discount stacking.

### 🔵 Blue Team Detection
- Alert on orders where the same coupon appears more than once in transaction history
- Monitor for abnormally high discount percentages applied to a single order
- Flag orders where final price is reduced by more than X% via coupons

### 🛡️ Fix
- Track coupon usage against the **full order history**, not just the last applied coupon
- Enforce "each coupon can only be used once per order" at the database level
- Implement a coupon usage table that records all coupons used per session/order
