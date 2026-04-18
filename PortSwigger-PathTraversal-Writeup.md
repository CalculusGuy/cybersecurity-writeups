# PortSwigger Lab: File Path Traversal - Simple Case
**Platform:** PortSwigger Web Security Academy  
**Category:** Path Traversal  
**Difficulty:** Apprentice  
**Date:** April 2026  
**Status:** ✅ Solved

---

## What is Path Traversal?
Path traversal allows an attacker to read arbitrary files 
on the server by manipulating file path parameters using 
`../` sequences to navigate up directory levels.

---

## Lab Goal
Retrieve the contents of `/etc/passwd` from the server.

---

## Tools Used
- Burp Suite Community Edition
- Burp Repeater

---

## Steps Taken

### Step 1 — Intercepted the request
Opened the lab in Burp's browser with Intercept on.
Browsed the shop and identified image requests with:
`GET /image?filename=product.jpg`

### Step 2 — Sent to Repeater
Right clicked the request → Send to Repeater

### Step 3 — Modified the filename parameter
Changed:
`filename=product.jpg`
To:
`filename=../../../etc/passwd`

### Step 4 — Sent the request
Server returned full contents of `/etc/passwd` ✅

---

## Why it worked
The application passed the filename parameter directly 
to the file system without sanitizing `../` sequences. 
This allowed navigation outside the intended directory.

---

## Defence
- Validate and sanitize all user-supplied file paths
- Use a whitelist of allowed filenames
- Resolve the absolute path and verify it starts with 
  the expected base directory

---

## Key Takeaway
Never trust user input. Always validate file paths 
server-side before passing them to the file system.
