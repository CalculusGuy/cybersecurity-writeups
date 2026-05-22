# Lab 01 — Excessive Trust in Client-Side Controls

**Difficulty:** Apprentice  
**Category:** Business Logic Vulnerabilities  
**Platform:** PortSwigger Web Security Academy

---

## Goal
Buy the "Lightweight l33t Leather Jacket" for less than its actual price by manipulating client-side data sent to the server.

---

## Steps

1. Add the jacket to the cart normally
2. Intercept the `POST /cart` request in Burp Suite
3. Observe the `price` parameter in the request body
4. Modify the price value to `1` (or any low number)
5. Forward the modified request
6. Complete checkout — jacket purchased at manipulated price

**Key Request:**
```
POST /cart
productId=1&redir=PRODUCT&quantity=1&price=1
```

---

## What I Learned

The application trusted the price value sent from the client (browser) instead of looking it up server-side from the database.

This is a fundamental mistake — **any value visible in a request can be modified by an attacker.**

### 🔴 Attack
Intercept the cart POST request and modify the `price` parameter to an arbitrary low value using Burp Suite.

### 🔵 Blue Team Detection
- Log and alert on price mismatches between the product catalog and incoming cart requests
- Monitor for unusual price values in POST /cart requests (e.g., price < $1 for premium items)
- SIEM rule: flag any cart submission where submitted price ≠ server-side catalog price

### 🛡️ Fix
- **Never accept price from the client.** Always fetch price from the server-side database using the productId
- Validate all sensitive numeric parameters server-side before processing
- Treat all client-supplied input as untrusted
