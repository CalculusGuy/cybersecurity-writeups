# Lab 04 — Username Enumeration via Subtly Different Responses

**Difficulty:** Practitioner
**Category:** Authentication Vulnerabilities

## Problem

This lab is subtler than the Apprentice version. The error message is **the same** ("Invalid username or password"), but the server behaves slightly differently depending on whether the username is valid.

The difference: **a single character** in the response body. Or a slightly different response length. Or a small timing difference.

## Method

1. Intercept a login request in Burp Suite
2. Send to Intruder
3. Load the username wordlist
4. Add a **Grep — Extract** rule for the trailing character of the error message
5. Also add **Grep — Match** for the error string
6. Compare lengths
7. One username will stand out — either by length, by a specific trailing character, or by subtle timing

In my run, the valid username was **`987654321`** — the response length was 189 vs ~200 for invalid ones (the response body was slightly shorter).

## Solution

1. Enumerated valid username: `987654321`
2. Brute-forced the password with the password wordlist against that user
3. Found the valid password
4. Logged in and accessed `/my-account`

## Learning

**Differentials are everywhere — you just have to look.** The moment a developer adds *any* conditional logic around the response (a trim, a different redirect, a longer error string), you have an oracle.

Signals that almost never lie:
- Response length
- Trailing character differences
- HTTP headers (Set-Cookie, Location)
- Small timing differences
- Content-Length header even when body looks identical

## Fixes

- Always return the **exact same response body** for all invalid login attempts
- Do not branch logic on whether the username exists server-side
- Constant-time comparison for authentication checks
- Server-side delay before response (e.g., 200-500ms) to mask timing
- Log failures but never expose the reason to the client
