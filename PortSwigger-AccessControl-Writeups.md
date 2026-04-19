# PortSwigger Access Control Labs Writeups
**Platform:** PortSwigger Web Security Academy  
**Category:** Access Control  
**Date:** April 2026

---

## Lab 1 — Unprotected Admin Functionality
**Method:** Checked robots.txt  
**Command:** `/robots.txt` → found `/administrator-panel`  
**What I learned:** robots.txt reveals hidden pages

---

## Lab 2 — Unprotected Admin with Unpredictable URL
**Method:** Viewed page source, searched for "admin"  
**Found:** `/admin-tjt9tw` hidden in JavaScript  
**What I learned:** Sensitive URLs leak in client-side code

---

## Lab 3 — User Role Controlled by Cookie
**Method:** Burp Suite — changed `Admin=false` to `Admin=true`  
**What I learned:** Never trust client-side cookies for access control

---

## Lab 4 — User ID with Unpredictable GUIDs
**Method:** Found carlos GUID in blog post URL  
**What I learned:** GUIDs exposed publicly can be harvested

---

## Lab 5 — Password Disclosure via Account Page
**Method:** Changed `?id=wiener` to `?id=administrator`  
**Found:** Admin password in masked input field in page source  
**What I learned:** Never prefill passwords in HTML — they're readable
