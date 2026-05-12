# SSRF — Server-Side Request Forgery

## What is SSRF?
SSRF tricks a server into making requests on your behalf — 
to internal systems, admin panels, cloud metadata endpoints, 
and private networks that are normally unreachable from outside.

## Why it's dangerous
- Internal systems trust the server — not your browser
- Internal services often have zero authentication
- The server becomes your proxy into the network

## Labs Completed

| # | Lab | Difficulty | Technique |
|---|-----|------------|-----------|
| 1 | Basic SSRF against localhost | Apprentice | localhost admin access |
| 2 | Basic SSRF against internal network | Apprentice | Internal IP scanning |
| 3 | SSRF with blacklist bypass | Practitioner | 127.1 + double URL encoding |
| 4 | SSRF via open redirect | Practitioner | SSRF + Open Redirect chain |

## Tools Used
- Burp Suite Community Edition
- Burp Intruder (IP range scanning)
- Burp Repeater
