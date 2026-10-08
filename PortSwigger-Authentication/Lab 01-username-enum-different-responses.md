# Lab 01 — Username Enumeration via Different Responses

**Difficulty:** Apprentice
**Category:** Authentication Vulnerabilities

## Problem

The login form returns different error messages depending on whether the username exists but the password is wrong, versus the username itself being wrong.

- Wrong username → "Invalid username"
- Valid username, wrong password → "Incorrect password"

This differential reveals valid usernames.

## Method

1. Intercept a login request in Burp Suite
2. Send to Intruder
3. Load the username wordlist as the payload
4. Grep the responses for the length differential
5. Identify which usernames return a different response length

Valid usernames returned a slightly longer response length because the error message was longer ("Incorrect password" vs "Invalid username").

## Solution

- Intruder revealed `at` (or similar) as a valid username
- Sent it with a fresh password brute-force attack
- Found the valid password in the password wordlist
- Logged in and accessed the account page

## Learning

**Response differentials leak information.** Even when a developer "hides" the reason for failure, the *shape* of the response often reveals it.

Signals to look for:
- Response length
- HTTP status code
- Timing
- Error message wording

## Fixes

- Return a **single generic error message** for all login failures: "Invalid username or password"
- Ensure response length is identical regardless of failure reason
- Consider adding a small random delay to mask timing differentials
- Rate-limit failed login attempts per IP and per account
