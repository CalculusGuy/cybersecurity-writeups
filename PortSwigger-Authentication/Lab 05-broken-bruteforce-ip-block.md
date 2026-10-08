# Lab 05 — Broken Brute-Force Protection, IP Block

**Difficulty:** Practitioner
**Category:** Authentication Vulnerabilities

## Problem

The login form has brute-force protection: after a few failed attempts, your IP gets blocked. The block is designed to stop password brute-forcing.

But the block can be bypassed by **interleaving valid logins** to reset the failure counter.

## Method

1. Try a few wrong passwords for the victim → your IP gets blocked
2. Notice: if you log in with **valid** credentials (the ones the lab gives you), the counter resets
3. Even better: the counter only tracks failures since the last success
4. So alternate:
   - 2 failed attempts (wrong password for victim)
   - 1 successful login (your own valid credentials)
   - Repeat
5. Never trigger the counter threshold

## Solution

1. Setup Burp Intruder with a wordlist that interleaves:
   - Attempt 1: `carlos:password1` (wrong)
   - Attempt 2: `carlos:password2` (wrong)
   - Attempt 3: `wiener:peter` (valid — resets counter)
   - Repeat with next two password attempts
2. Ran the attack
3. Found the victim's password before ever triggering the block
4. Logged in as `carlos` — lab solved

Alternative bypass (also valid): spoof the `X-Forwarded-For` header on each request to appear as a different IP.

## Learning

**Brute-force protections are often per-session or per-counter, not per-account or per-IP-globally.** Attackers will always find the reset condition.

Common bypasses:
- Interleaving valid logins (this lab)
- Rotating IPs (via proxies or `X-Forwarded-For` spoofing)
- Credential stuffing (using leaked password lists — no brute-force signature)
- Distributed attacks (thousands of IPs, one attempt each)

## Fixes

- Rate-limit **per account**, not just per IP or session
- Use exponential backoff after failures
- After N failures, lock the account and require email/SMS verification to unlock
- Detect credential stuffing via breached password checks (HIBP API)
- Do not trust client-supplied IP headers unless you're behind a trusted proxy
- Alert on distributed failure patterns (many IPs, same target account)
