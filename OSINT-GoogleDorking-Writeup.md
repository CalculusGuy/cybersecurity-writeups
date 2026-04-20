# OSINT — Google Dorking Writeup
**Category:** OSINT (Open Source Intelligence)
**Date:** April 2026
**Status:** ✅ Completed

---

## What is Google Dorking?
Google Dorking is the technique of using advanced Google search 
operators to find specific information that is publicly exposed 
on the internet but not easily discoverable through normal searches.
It is one of the first techniques used during the reconnaissance 
phase of any penetration test.

---

## Key Operators Used

| Operator | Purpose | Example |
|----------|---------|---------|
| site: | Search within a specific website | site:github.com passwords |
| filetype: | Find specific file types | filetype:pdf confidential |
| intitle: | Find pages with specific title | intitle:"index of" |
| inurl: | Find specific words in URLs | inurl:admin login |
| "quotes" | Exact phrase match | "internal use only" |

---

## Dork 1 — Finding Exposed Password Files on GitHub
**Query:**
site:github.com "password" filetype:txt

**What I found:**
SecLists — a famous cybersecurity wordlist repository containing
default credentials, common passwords and cracked hashes used 
by professional pentesters worldwide.

**What this means:**
Developers accidentally commit sensitive files to public GitHub 
repositories all the time. This dork finds them instantly.

**Real world impact:**
Attackers use this to find accidentally leaked API keys, 
credentials and tokens in public repositories.

---

## Dork 2 — Finding Exposed Config Files
**Query:**
intitle:"index of" "config.php"

**What I found:**
A real web server with directory listing enabled, exposing:
- database.php
- auth.php
- mail.php
- session.php
- config.php

**What this means:**
Directory listing misconfiguration allows anyone to see what 
files exist on the server. Even without reading the files, 
an attacker learns the entire tech stack — in this case 
Laravel PHP framework.

**Real world impact:**
This is a reportable finding in any pentest. Even partial 
exposure reveals technology stack and potential attack surface.

**Defence:**
Disable directory listing in web server configuration.
Never expose config directories publicly.

---

## Dork 3 — Finding Exposed Backup Folders
**Query:**
intitle:"index of" "backup"

**What I found:**
A Faculty of Security Studies university website running Moodle
with a misconfigured server exposing backup directories.

**What this means:**
Backup folders often contain old source code, credentials and 
database dumps. This is one of the highest value findings 
in real pentests.

**Real world impact:**
Exposed backups can contain plaintext passwords, old API keys
and entire database dumps from previous versions.

**Defence:**
Never store backups in publicly accessible directories.
Restrict access to backup folders at server level.

---

## Key Takeaways

1. Google indexes everything — including things that should 
   never be public
2. Misconfigured servers are extremely common even in 
   security-focused organizations
3. OSINT requires zero interaction with target systems — 
   making it completely passive and legal
4. Always practice responsible disclosure if you find 
   real vulnerabilities
5. This is exactly what threat intelligence companies 
   like CloudSEK do at scale

---

## Tools Used
- Google Search with advanced operators
- Browser only — no special tools required

---

## What's Next
- Shodan — Google for internet connected devices
- theHarvester — automated OSINT tool
- WHOIS and DNS enumeration
