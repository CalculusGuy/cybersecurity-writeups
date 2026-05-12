# Lab 4: SSRF via Open Redirect Chain
**Difficulty:** Practitioner
**Status:** ✅ Solved

## Vulnerability
Stock checker restricted to local URLs only.
But open redirect gadget exists at /product/nextProduct?path=
Chaining SSRF + Open Redirect bypasses the restriction.

## Payload
stockApi=/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos

## Steps
1. Confirmed direct internal IP blocked
2. Found nextProduct?path= controls redirect destination
3. Confirmed open redirect by testing path parameter
4. Chained: stockApi points to local redirect → redirect hits internal admin
5. Solved in one go

## Why It Works
SSRF check validates initial URL (local = trusted).
Doesn't validate redirect destination.
Open redirect becomes the bypass.

## Fix
Validate redirect destinations server-side.
Never use user input to construct redirect paths.
Treat redirects with same suspicion as direct URLs.
