# OverTheWire Natas Writeup

**Platform:** OverTheWire
**Category:** Web Security
**Date:** June 2026

---

## Level 0 → 1

**Goal:** Find password hidden in page source

**Work:**

* View Page Source

**What I learned:**
HTML comments are visible to everyone.

---

## Level 1 → 2

**Goal:** Bypass disabled right-click protection

**Work:**

* View Page Source
* Open Developer Tools

**What I learned:**
Client-side restrictions are not security controls.

---

## Level 2 → 3

**Goal:** Find hidden password file

**Work:**

* Inspect source code
* Discover `/files/`
* Browse directory listing

**What I learned:**
Hidden directories can often be enumerated directly.

---

## Level 3 → 4

**Goal:** Discover hidden location

**Work:**

* Check `/robots.txt`
* Visit exposed directory

**What I learned:**
robots.txt can reveal sensitive paths.

---

## Level 4 → 5

**Goal:** Access protected page

**Work:**

* Modify HTTP Referer header
* Reload request

**What I learned:**
HTTP headers are controlled by the client.

---

## Level 5 → 6

**Goal:** Become authenticated

**Work:**

* Inspect cookies
* Change `loggedin=0` → `loggedin=1`

**What I learned:**
Authorization should never depend on client-side values.

---

## Level 6 → 7

**Goal:** Recover hidden secret

**Work:**

* Review source code
* Locate included file
* Retrieve secret value

**What I learned:**
Source code review often exposes sensitive information.

---

## Level 7 → 8

**Goal:** Read sensitive server file

**Work:**

* Manipulate page parameter
* Exploit Local File Inclusion

**What I learned:**
User-controlled file paths can expose credentials.

---

## Level 8 → 9

**Goal:** Recover encoded secret

**Work:**

* Analyze encoding logic
* Reverse transformations

**What I learned:**
Encoding is not encryption.

---

## Level 9 → 10

**Goal:** Retrieve protected data

**Work:**

* Analyze source code
* Exploit command injection

**What I learned:**
Unsanitized input inside shell commands is dangerous.

---

## Level 10 → 11

**Goal:** Bypass command filtering

**Work:**

* Analyze blacklist restrictions
* Manipulate command arguments

**What I learned:**
Blacklist filtering is not reliable security.

---

## Level 11 → 12

**Goal:** Enable password display

**Work:**

* Analyze encrypted cookie
* Recover XOR key
* Forge modified cookie

**What I learned:**
Encryption without integrity checks is weak.

---

## Level 12 → 13

**Goal:** Upload executable code

**Work:**

* Modify hidden filename field
* Upload PHP payload
* Execute uploaded file

**What I learned:**
Hidden form fields are fully user-controlled.

---

## Levels 0–12 Summary

**Key Skills Learned:**

* Source Code Review
* Directory Enumeration
* Cookie Manipulation
* HTTP Request Tampering
* Local File Inclusion (LFI)
* Encoding Reversal
* Command Injection
* Argument Injection
* XOR Analysis
* Cookie Forgery
* File Upload Exploitation

**Biggest Lesson:**
Every level was solved because the application trusted something it should not have trusted.
