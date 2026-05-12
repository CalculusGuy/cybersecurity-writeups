# Lab 1: Basic SSRF Against Localhost
**Difficulty:** Apprentice
**Status:** ✅ Solved

## Vulnerability
Server fetches user-controlled URL without validation.
Pointing it to localhost gives access to internal admin panel.

## Payload
stockApi=http://localhost/admin/delete?username=carlos

## Steps
1. Intercepted stock check request in Burp
2. Changed stockApi to http://localhost/admin
3. Admin panel returned in response
4. Changed to /admin/delete?username=carlos
5. Carlos deleted → solved

## Why It Works
Request comes FROM the server itself.
Internal systems trust localhost unconditionally.

## Fix
Whitelist allowed URLs. Never trust user-controlled URLs.
