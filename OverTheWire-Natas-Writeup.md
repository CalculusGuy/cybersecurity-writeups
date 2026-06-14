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
