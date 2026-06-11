Natas 0 → 1
Goal

Find the password for the next level.

Steps

Viewed page source:

<!-- password hidden here -->

Found the password inside an HTML comment.

What I learned
HTML comments are visible to anyone.
"Hidden" source code is not secure.
Always inspect page source before doing anything complicated.
Real-world takeaway

Developers sometimes leave secrets, API keys, or debug notes in comments.

Natas 1 → 2
Goal

Find the next password.

Steps

Right-click was disabled.

Used:

Ctrl + U

or Developer Tools.

Viewed the source and found the password.

What I learned
JavaScript restrictions only affect honest users.
Browser controls can always be bypassed.
Real-world takeaway

Client-side controls are never security controls.

Natas 2 → 3
Goal

Find the next password.

Steps

Viewed page source.

Found:

<img src="files/pixel.png">

Visited:

/files/

Directory listing was enabled.

Found a file containing the password.

What I learned
Web servers sometimes expose entire directories.
Source code often reveals hidden paths.
Real-world takeaway

Directory enumeration is one of the first things attackers perform.

Natas 3 → 4
Goal

Find the next password.

Steps

Checked:

/robots.txt

Found:

Disallow: /s3cr3t/

Visited:

/s3cr3t/

Found the password.

What I learned
robots.txt is public.
It often leaks sensitive directories.
Real-world takeaway

Search engine instructions should never contain sensitive paths.

Natas 4 → 5
Goal

Access the protected page.

Steps

Page checked the HTTP Referer header.

Intercepted request using DevTools.

Modified:

Referer: expected-page

Server accepted the request and displayed the password.

What I learned
Referer headers are fully controlled by users.
HTTP headers should never be trusted.
Real-world takeaway

Many older applications rely on spoofable headers for access control.

Natas 5 → 6
Goal

Become logged in.

Steps

Checked browser cookies.

Found:

loggedin=0

Changed it to:

loggedin=1

Refreshed page.

Password appeared.

What I learned
Cookies are client-side data.
Users can modify them freely.
Real-world takeaway

Authorization must always be enforced on the server.

Natas 6 → 7
Goal

Find the secret value.

Steps

Viewed source code.

Found:

include "includes/secret.inc";

Opened:

/includes/secret.inc

Recovered the secret.

Submitted it to obtain the password.

What I learned
Source code disclosure is dangerous.
Included files may be directly accessible.
Real-world takeaway

Never store secrets inside publicly reachable files.

Natas 7 → 8
Goal

Find the next password.

Steps

Observed:

?page=home

Modified parameter to read local files.

Used Local File Inclusion to access:

/etc/natas_webpass/natas8

Retrieved the password.

What I learned
File inclusion functions are dangerous.
User-controlled paths create severe risks.
Real-world takeaway

LFI vulnerabilities can expose configuration files, credentials, and source code.

Natas 8 → 9
Goal

Recover the secret.

Steps

Source code showed:

bin2hex(strrev(base64_encode($secret)))

Reversed the operations:

Hex decode
Reverse string
Base64 decode

Recovered the original secret.

What I learned
Encoding is reversible.
Obfuscation is not encryption.
Real-world takeaway

Sensitive data must be encrypted, not merely encoded.

Natas 9 → 10
Goal

Retrieve the next password.

Steps

Source code contained:

passthru("grep -i $key dictionary.txt");

Injected additional shell syntax.

Application executed unintended commands.

Used this to read:

/etc/natas_webpass/natas10
What I learned
User input inside shell commands is extremely dangerous.
Command injection leads directly to server compromise.
Real-world takeaway

One command injection vulnerability can become full Remote Code Execution.

Natas 10 → 11
Goal

Bypass command filtering.

Steps

Characters like:

; | &

were blocked.

Instead of executing another command, manipulated grep arguments.

Used argument injection to access sensitive data.

Retrieved the password.

What I learned
Blacklists fail.
Applications must validate inputs properly.
Real-world takeaway

Attackers often bypass filters without needing blocked characters.

Natas 11 → 12
Goal

Enable password display.

Steps

Cookie contained:

{
  "showpassword":"no",
  "bgcolor":"#ffffff"
}

Cookie was XOR-encrypted.

Recovered XOR key.

Changed:

"showpassword":"yes"

Re-encrypted cookie.

Loaded modified cookie.

Password appeared.

What I learned
Encryption without integrity checks is insecure.
XOR is weak when implemented incorrectly.
Real-world takeaway

Authenticated encryption is essential when storing client-side data.

Natas 12 → 13
Goal

Upload executable code.

Steps

Application accepted uploads but trusted:

$_POST["filename"]

Used DevTools to modify:

random.jpg

to:

shell.php

Uploaded PHP payload.

Executed uploaded file.

Read:

/etc/natas_webpass/natas13
What I learned
Hidden form fields are user-controlled.
File uploads require strict validation.
Real-world takeaway

Unrestricted file upload vulnerabilities frequently lead to Remote Code Execution.

Natas Progress
Level	Vulnerability
0	Source Disclosure
1	Client-side Restriction Bypass
2	Directory Enumeration
3	robots.txt Information Disclosure
4	Referer Spoofing
5	Cookie Manipulation
6	Source Code Disclosure
7	Local File Inclusion
8	Encoding Reversal
9	Command Injection
10	Argument Injection
11	XOR Cookie Forgery
12	Unrestricted File Upload
