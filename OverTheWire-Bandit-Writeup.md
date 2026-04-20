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

## Level 11 → 12
**Goal:** The password is stored in data.txt where all lowercase and 
uppercase letters have been rotated by 13 positions (ROT13)
**Command:**
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
**What I learned:** 
The tr command translates characters. ROT13 shifts every letter 
13 positions forward in the alphabet. Since the alphabet has 26 
letters, shifting 13 twice brings you back to the original — 
so encoding and decoding use the exact same command.

---

## Level 12 → 13
**Goal:** The password is inside data.txt which is a hex dump of a 
file that has been repeatedly compressed multiple times
**Commands:**
mkdir /tmp/bandit12_work
cd /tmp/bandit12_work
cp ~/data.txt .
xxd -r data.txt > file

# Then repeated this cycle until reaching ASCII text:
file file
mv file file.gz && gunzip file.gz
file file
mv file file.bz2 && bunzip2 file.bz2
file file
mv file file.tar && tar -xf file.tar
# ...repeated several times across gzip, bzip2, and tar formats
cat data8

**What I learned:**
This was the most complex level so far. Key lessons:
- xxd -r reverses a hex dump back to binary
- Always run "file" before assuming a file type
- Always run "ls" after every extraction to track filenames
- gunzip and bunzip2 rename files automatically based on 
  embedded original names
- Never assume a filename — verify with ls and file every time
- The 2>/dev/null trick hides error noise when needed

---

## Level 13 → 14
**Goal:** No password this time. A private SSH key is provided 
to log directly into bandit14
**Commands:**
ls
# Found: sshkey.private
chmod 600 sshkey.private
ssh -i sshkey.private bandit14@localhost
cat /etc/bandit_pass/bandit14

**What I learned:**
SSH supports key-based authentication instead of passwords.
The private key must have strict permissions (chmod 600) 
otherwise SSH refuses to use it for security reasons.
Once logged in as bandit14, the password for the next level 
is stored in /etc/bandit_pass/bandit14

---

## Level 14 → 15
**Goal:** Submit the bandit14 password to localhost on port 30000 
to receive the next password
**Commands:**
cat /etc/bandit_pass/bandit14
# Copy the password
ssh bandit15@bandit.labs.overthewire.org -p 2220
# Paste password when prompted

**What I learned:**
Each level's password is stored in /etc/bandit_pass/ and only 
readable by that level's user. Careful password copying is 
critical — hidden spaces or newlines cause login failures.
Always verify your copy before attempting SSH login.

---
