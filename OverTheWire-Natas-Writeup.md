# OverTheWire Natas Writeup

**Platform:** OverTheWire
**Category:** Web Security
**Date:** June 2026

## OverTheWire — Natas Progress

**Category:** Web Security
**Levels Complete:** 0 → 18
**Current Level:** Natas19

| Level   | Vulnerability                  | Key Technique                         |
| ------- | ------------------------------ | ------------------------------------- |
| 0 → 1   | Information Disclosure         | Page source review                    |
| 1 → 2   | Client-Side Restriction Bypass | Developer Tools                       |
| 2 → 3   | Directory Enumeration          | Hidden `/files/` directory            |
| 3 → 4   | Sensitive Path Exposure        | `robots.txt` enumeration              |
| 4 → 5   | HTTP Header Manipulation       | Referer spoofing                      |
| 5 → 6   | Cookie Manipulation            | `loggedin=0 → 1`                      |
| 6 → 7   | Source Code Review             | Included file disclosure              |
| 7 → 8   | Local File Inclusion (LFI)     | Path traversal                        |
| 8 → 9   | Encoding Reversal              | Base64 + String Reversal + Hex        |
| 9 → 10  | OS Command Injection           | Shell metacharacters                  |
| 10 → 11 | Argument Injection             | Blacklist bypass                      |
| 11 → 12 | XOR Cookie Forgery             | Key recovery + cookie tampering       |
| 12 → 13 | File Upload Exploitation       | Hidden field manipulation + PHP shell |
| 13 → 14 | File Upload Bypass + RCE       | JPEG-PHP polyglot + command execution |
| 14 → 15 | SQL Injection                  | Authentication bypass                 |
| 15 → 16 | Blind SQL Injection            | Boolean-based password extraction     |
| 16 → 17 | Blind Command Injection        | Automated password enumeration        |
| 17 → 18 | Time-Based Blind SQL Injection | IF() + SLEEP() password extraction    |
| 18 → 19 | Broken Session Management      | Session ID brute forcing              |

**Biggest Lesson:** Every level was solved because the application trusted user-controlled input, data, or behavior that should never have been trusted.


---

## Level 0 → 1

**Goal:** Find password hidden in page source

**Work:**

* View page source

**What I learned:**
HTML comments and source code are visible to every user.

---

## Level 1 → 2

**Goal:** Bypass disabled right-click protection

**Work:**

* View page source
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
Hidden directories can often be discovered through enumeration.

---

## Level 3 → 4

**Goal:** Discover hidden location

**Work:**

* Review `robots.txt`
* Access exposed directory

**What I learned:**
`robots.txt` can unintentionally disclose sensitive paths.

---

## Level 4 → 5

**Goal:** Access protected page

**Work:**

* Modify HTTP Referer header
* Replay request

**What I learned:**
HTTP headers are completely controlled by the client.

---

## Level 5 → 6

**Goal:** Become authenticated

**Work:**

* Inspect cookies
* Change `loggedin=0` to `loggedin=1`

**What I learned:**
Authorization decisions should never rely on client-side values.

---

## Level 6 → 7

**Goal:** Recover hidden secret

**Work:**

* Review source code
* Identify included file
* Extract secret value

**What I learned:**
Source code often exposes sensitive implementation details.

---

## Level 7 → 8

**Goal:** Read sensitive server file

**Work:**

* Manipulate page parameter
* Exploit Local File Inclusion

**What I learned:**
User-controlled file paths can expose credentials and sensitive files.

---

## Level 8 → 9

**Goal:** Recover encoded secret

**Work:**

* Analyze encoding sequence
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
Unsanitized user input inside shell commands can lead to command execution.

---

## Level 10 → 11

**Goal:** Bypass command filtering

**Work:**

* Analyze blacklist restrictions
* Exploit argument injection

**What I learned:**
Blacklist-based filtering is an unreliable defense mechanism.

---

## Level 11 → 12

**Goal:** Enable password disclosure

**Work:**

* Analyze encrypted cookie
* Recover XOR key
* Forge modified cookie

**What I learned:**
Encryption without integrity validation can be manipulated.

---

## Level 12 → 13

**Goal:** Upload executable code

**Work:**

* Modify hidden filename field
* Upload PHP payload
* Execute uploaded file

**What I learned:**
Hidden form fields are fully controlled by the user.

---

## Level 13 → 14

**Goal:** Achieve Remote Code Execution

**Work:**

* Analyze image validation logic
* Create JPEG-PHP polyglot
* Bypass image-only upload restriction
* Modify hidden filename field using Developer Tools
* Upload PHP web shell
* Execute system commands
* Read Natas14 password

**What I learned:**
Validating file signatures alone does not prevent malicious uploads.

---

## Level 14 → 15

**Goal:** Bypass authentication

**Work:**

* Analyze SQL query construction
* Identify SQL Injection vulnerability
* Inject always-true condition
* Bypass login mechanism

**What I learned:**
Dynamic SQL queries built from user input are highly dangerous.

---

## Level 15 → 16

**Goal:** Extract Natas16 password

**Work:**

* Confirm Blind SQL Injection
* Test boolean conditions
* Enumerate password characters
* Automate extraction with Python
* Recover full password

**What I learned:**
Application responses can leak information even when sensitive data is never displayed.

---

## Level 16 → 17

**Goal:** Extract Natas17 password

**Work:**

* Analyze command execution logic
* Identify command substitution vulnerability
* Exploit blind command injection
* Enumerate password prefixes
* Automate extraction using Python
* Recover full password

**What I learned:**
Blind command injection can reveal secrets through subtle differences in application behavior.

---

## Level 17 → 18

**Goal:** Extract Natas18 password

**Work:**

* Analyze SQL query construction
* Identify Blind SQL Injection vulnerability
* Discover time-based side channel using `SLEEP()`
* Use `IF()` conditions to test password characters
* Automate extraction with Python
* Debug case-sensitivity issue using `BINARY`
* Recover full password

**What I learned:**
Even when applications suppress errors and query results, attackers can still extract sensitive data through timing differences. Time-based Blind SQL Injection remains one of the most effective SQLi techniques in real-world assessments.

---

## Level 18 → 19

**Goal:** Retrieve Natas19 credentials

**Work:**

* Review session management source code
* Identify predictable session IDs
* Discover session range limited to 1–640
* Enumerate active sessions
* Automate session brute forcing with Python
* Locate valid administrator session
* Retrieve Natas19 credentials

**What I learned:**
Session identifiers must be unpredictable and sufficiently large. Small or predictable session spaces allow attackers to hijack authenticated sessions through brute-force enumeration.

---

## Skills Practiced

* Source Code Review
* Directory Enumeration
* Cookie Manipulation
* HTTP Request Tampering
* Local File Inclusion (LFI)
* Encoding Reversal
* SQL Injection
* Blind SQL Injection
* Command Injection
* Blind Command Injection
* Argument Injection
* XOR Analysis
* Cookie Forgery
* File Upload Exploitation
* Remote Code Execution (RCE)
* Python Automation
* Password Enumeration
* Time-Based Blind SQL Injection
* Session Enumeration
* Session Hijacking
* Session Brute Forcing
* Authentication Bypass
* Web Exploitation Automation


---

## Current Progress

```text
Natas 0  ✓
Natas 1  ✓
Natas 2  ✓
Natas 3  ✓
Natas 4  ✓
Natas 5  ✓
Natas 6  ✓
Natas 7  ✓
Natas 8  ✓
Natas 9  ✓
Natas 10 ✓
Natas 11 ✓
Natas 12 ✓
Natas 13 ✓
Natas 14 ✓
Natas 15 ✓
Natas 16 ✓
Natas 17 ✓
Natas 18 ✓
Natas 19 Unlocked ✓
```

## Overall Takeaway

The Natas wargame demonstrates a fundamental principle of web security:

**Every successful exploit originated from misplaced trust in user-controlled input, client-side controls, or unsafe assumptions about application behavior.**

The progression from simple information disclosure to blind exploitation and automated secret extraction highlights how seemingly small security mistakes can escalate into full compromise of an application.


we need to update the git on natas. this is the last commit. update it and give me to push 
