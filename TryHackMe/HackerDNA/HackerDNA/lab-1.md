# HackerDNA Lab: Hack the Login (Writeup)

## 🧑‍💻 Platform

HackerDNA
Lab Link: https://hackerdna.com/labs/hack-the-login 

##  Objective

To bypass authentication and gain access to a restricted area in order to retrieve the flag.

---

## 🔍 Recon & Initial Analysis

After launching the lab, I accessed the provided URL which displayed a login page.

At this stage, no obvious vulnerabilities were visible, so I decided to inspect the client-side code.

---

## 🧠 Enumeration

Using browser developer tools (F12), I navigated to:

Sources → script.js

Inside the JavaScript file, I discovered hardcoded credentials:

* Username: admin
* Password: (visible inside script.js)

Additionally, the flag reference was also present in the script.

---

##  Vulnerability Identified

###  Client-Side Information Disclosure

Sensitive data (credentials and flag reference) was exposed in the frontend JavaScript.

# This is a critical security flaw because:

* JavaScript is publicly accessible
* Any user can view it using browser tools
* Secrets should never be stored client-side

---

##  Exploitation

1. Extracted credentials from script.js
2. Entered them into the login form
3. Successfully authenticated

After login, the application prompted for the flag, which was already discovered during enumeration.

---

##  Result

Successfully bypassed authentication and retrieved the flag.

---

##  Key Learnings

* Never trust client-side security
* Always inspect JavaScript files during web testing
* Sensitive information must be stored securely on the server-side

---

##  Real-World Insight

This type of vulnerability can lead to:

* Account takeover
* Unauthorized access
* Data exposure

In real applications, this could be exploited by attackers to gain admin-level access.

---

## 🚀 Conclusion

This lab demonstrated a simple but impactful vulnerability caused by improper handling of sensitive data in client-side code. It reinforced the importance of thorough enumeration and understanding how web applications handle authentication.
