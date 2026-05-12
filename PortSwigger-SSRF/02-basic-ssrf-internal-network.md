# Lab 2: Basic SSRF Against Internal Network
**Difficulty:** Apprentice
**Status:** ✅ Solved

## Vulnerability
Server can reach internal network 192.168.0.X.
No restriction on which IPs stockApi can request.

## Payload
stockApi=http://192.168.0.156:8080/admin/delete?username=carlos

## Steps
1. Intercepted stock check request in Burp
2. Sent to Intruder
3. Set payload position on last octet: 192.168.0.§1§:8080/admin
4. Numbers payload 1-255
5. Sorted by status — found 200 response at .156
6. Sent delete request → solved

## Why It Works
Server can reach internal network. Browser cannot.
Server becomes internal network reconnaissance tool.

## Fix
Block server-side requests to private IP ranges.
Implement network-level controls alongside application controls.
