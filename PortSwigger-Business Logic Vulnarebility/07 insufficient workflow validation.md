# Lab 07 — Insufficient Workflow Validation

**Difficulty:** Practitioner  
**Category:** Business Logic Vulnerabilities  
**Platform:** PortSwigger Web Security Academy

---

## Goal
Buy the "Lightweight l33t Leather Jacket" for free by replaying the order confirmation request without completing the payment step.

---

## Steps

1. Add a cheap item to the cart
2. Go through checkout normally and complete the order
3. Observe the final confirmation request in Burp HTTP history:
   ```
   GET /cart/order-confirmation?order-confirmed=true
   ```
4. Send this request to **Burp Repeater**
5. Now add the jacket to the cart (don't pay)
6. In Repeater, **replay** the confirmation request
7. The server confirms the order without verifying payment was completed
8. Jacket obtained for free — lab solved

---

## What I Learned

The order confirmation endpoint **trusted the request alone** as proof that payment had been completed. It never checked whether the payment step had actually been executed for the current cart.

This is a **workflow sequencing vulnerability** — the server assumed users would always follow the intended flow: add to cart → pay → confirm. It never validated the prerequisite (payment) before executing the consequence (order fulfillment).

Real-world equivalent: e-commerce platforms that process fulfillment based on a confirmation URL that can be replayed.

### 🔴 Attack
Complete a legitimate cheap order to capture the confirmation request. Add expensive items to the cart. Replay the confirmation request — items fulfilled without payment.

### 🔵 Blue Team Detection
- Monitor for order confirmation requests where no corresponding payment transaction exists
- Alert on repeated hits to `/cart/order-confirmation` from the same session
- Log and correlate order value vs payment amount — flag discrepancies

### 🛡️ Fix
- Every workflow step must **independently validate prerequisites** — confirmation endpoint must verify payment was completed for the current cart
- Tie confirmation tokens to specific payment transactions, not just sessions
- Implement server-side state tracking: `cart → payment_initiated → payment_confirmed → order_fulfilled`
- Never trust a single request as proof of a multi-step workflow completion
