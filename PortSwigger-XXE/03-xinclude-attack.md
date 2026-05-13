# Lab 3: XInclude Attack
**Difficulty:** Practitioner
**Status:** ✅ Solved

## Vulnerability
Application embeds user input into server-side XML.
Cannot control full document so DOCTYPE injection impossible.
But XInclude directives still processed.

## Payload

    productId=<foo xmlns:xi="http://www.w3.org/2001/XInclude">
    <xi:include parse="text" href="file:///etc/passwd"/>
    </foo>&storeId=1

## Steps
1. Intercepted stock check request
2. Noticed productId=5&storeId=1 format not raw XML
3. Replaced productId value with XInclude payload
4. Server embedded it into XML and processed XInclude
5. /etc/passwd contents returned in response

## Why It Works
XInclude is an XML feature for including external content.
Even without DOCTYPE control XInclude still executes
if the parser supports it.

## Fix
Disable XInclude processing.
Sanitize user input before embedding in XML documents.
