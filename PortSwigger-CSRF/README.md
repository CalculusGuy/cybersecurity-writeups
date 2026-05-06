# CSRF — Cross-Site Request Forgery

## What is CSRF?
CSRF tricks a victim's browser into making requests to a site where they're already logged in — without their knowledge. The server sees a legitimate session cookie and executes the action.

## Three conditions needed:
1. A relevant action exists (change email, transfer funds etc.)
2. Cookie-based session handling — no other identity verification
3. No unpredictable request parameters

## Labs Completed

| # | Lab | Difficulty | Technique |
|---|-----|------------|-----------|
| 1 | CSRF with no defenses | Apprentice | Basic forged form |
| 2 | Token validation depends on request method | Practitioner | POST→GET bypass |
| 3 | Token validation depends on token being present | Practitioner | Delete token entirely |
| 4 | Token not tied to user session | Practitioner | Cross-account token swap |
| 5 | Token tied to non-session cookie | Practitioner | CRLF + cookie injection |
| 6 | Token duplicated in cookie | Practitioner | Double-submit bypass |
| 7 | SameSite Lax bypass via method override | Practitioner | _method=POST override |

## Tools Used
- Burp Suite Community Edition
- PortSwigger Exploit Server
