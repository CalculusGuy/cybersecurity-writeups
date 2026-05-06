# Lab 1: CSRF Vulnerability with No Defenses
**Difficulty:** Apprentice  
**Status:** ✅ Solved

## Vulnerability
No CSRF protection whatsoever. Server accepts any 
forged request as long as session cookie is present.

## Exploit
```html

    


    document.forms[0].submit();

```

## Steps
1. Intercepted email change request in Burp
2. Identified `email=` parameter with no token
3. Crafted forged HTML form
4. Tested on self first → confirmed email changed
5. Delivered to victim → solved

## Why It Works
Server only checks session cookie. No token, 
no origin validation. Browser auto-attaches 
cookie. Server can't tell forged from real.

## Fix
Implement CSRF tokens on all state-changing requests.
