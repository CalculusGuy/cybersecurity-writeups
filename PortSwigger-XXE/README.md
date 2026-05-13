# XXE — XML External Entity Injection

## What is XXE?
XXE exploits vulnerable XML parsers that process 
external entity references. Attackers can read local 
files, perform SSRF, and exfiltrate data through 
error messages.

## Why it's dangerous
- XML parsers process external entities by default
- Can read sensitive local files
- Can pivot to internal network via SSRF
- Works through file uploads, not just direct XML
- Even error messages can leak data

## Labs Completed

| # | Lab | Difficulty | Technique |
|---|-----|------------|-----------|
| 1 | XXE to retrieve files | Apprentice | External entity + /etc/passwd |
| 2 | XXE to perform SSRF | Apprentice | XXE + AWS metadata endpoint |
| 3 | XInclude attack | Practitioner | XInclude in form field |
| 4 | XXE via image upload | Practitioner | SVG file as XXE vector |
| 5 | Local DTD repurposing | Expert | Parameter entities + error exfiltration |

## Tools Used
- Burp Suite Community Edition
- Burp Repeater
- Mousepad (SVG payload creation)
