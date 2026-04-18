# OverTheWire Bandit Writeup
**Platform:** OverTheWire
**Category:** Linux Fundamentals  
**Date:** April 16, 2026

---

## Level 0 → 1
**Goal:** Find password in readme file  
**Command:** `cat readme`  
**What I learned:** Basic file reading in Linux

---

## Level 1 → 2
**Goal:** Read file named `-`  
**Command:** `cat ./-`  
**What I learned:** ./ prefix to handle dashed filenames

---

## Level 2 → 3
**Goal:** Read file with spaces in name  
**Command:** `cat -- "--spaces in this filename--"`  
**What I learned:** Using -- to handle dashes, quotes for spaces

---

## Level 3 → 4
**Goal:** Find hidden file in directory  
**Command:** `cd inhere && cat ...Hiding-From-You`  
**What I learned:** ls -la reveals hidden files

---

## Level 4 → 5
**Goal:** Find human-readable file  
**Command:** `file ./*` then `cat ./-file07`  
**What I learned:** file command identifies file types

---

## Level 5 → 6
**Goal:** Find file with specific size  
**Command:** `find . -type f -size 1033c ! -executable`  
**What I learned:** : find command with size and permission filters

## Level 6 → 7
**Goal:** Find file owned by specific user and group, 33 bytes  
**Command:** `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`  
**What I learned:** find with user/group filters, 2>/dev/null hides errors

---

## Level 7 → 8
**Goal:** Find password next to word "millionth"  
**Command:** `grep "millionth" data.txt`  
**What I learned:** grep searches for words inside files

---

## Level 8 → 9
**Goal:** Find line that appears only once  
**Command:** `sort data.txt | uniq -u`  
**What I learned:** Piping commands, sort + uniq combination

---

## Level 9 → 10
**Goal:** Find human-readable string preceded by = signs  
**Command:** `strings data.txt | grep "=="`  
**What I learned:** strings extracts readable text from binary files

---

## Level 10 → 11
**Goal:** Decode base64 encoded file  
**Command:** `base64 -d data.txt`  
**What I learned:** Base64 encoding and decoding
