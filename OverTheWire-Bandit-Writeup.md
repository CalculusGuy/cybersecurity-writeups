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

## Level 15 → 16
**Goal:** Submit the current level's password to port 30001 
on localhost using SSL/TLS encryption
**Command:**
openssl s_client -connect localhost:30001
# Then paste the bandit15 password when connected

**What I learned:**
openssl s_client is used to connect to SSL/TLS encrypted ports.
After the handshake completes and you see "read R BLOCK", 
the server is waiting for input. Regular nc won't work here 
because the port requires encrypted communication.

---

## Level 16 → 17
**Goal:** Find which port in range 31000-32000 speaks SSL 
and gives credentials instead of echoing back
**Commands:**
nmap -p 31000-32000 localhost
# Found open ports: 31046, 31518, 31691, 31790, 31960
nmap -p 31046,31518,31691,31790,31960 --script ssl-enum-ciphers localhost
# Found SSL ports: 31518, 31691, 31790
openssl s_client -connect localhost:31790 -ign_eof
# Pasted bandit16 password → received RSA private key

mkdir /tmp/mykey
nano /tmp/mykey/sshkey.private
# Pasted the RSA private key
chmod 600 /tmp/mykey/sshkey.private
ssh -i /tmp/mykey/sshkey.private -p 2220 bandit17@bandit.labs.overthewire.org

**What I learned:**
- nmap can scan port ranges and detect SSL with --script ssl-enum-ciphers
- Some ports echo back (useless), only one gives real credentials
- The -ign_eof flag prevents OpenSSL from closing on KEYUPDATE messages
- Sometimes the server returns an SSH private key instead of a password
- Private key files must be chmod 600 or SSH refuses to use them
- /tmp directories get wiped periodically — use long names

---

## Level 17 → 18
**Goal:** Two files exist — passwords.old and passwords.new. 
Find the one changed line in passwords.new
**Command:**
diff passwords.old passwords.new
# Line marked with > is the new bandit18 password

**What I learned:**
diff compares two files line by line.
< means the line exists in the first file (old)
> means the line exists in the second file (new)
This is the changed line — which is the password.

---

## Level 18 → 19
**Goal:** .bashrc kicks you out with "Byebye!" immediately on login
**Command:**
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat ~/readme"

**What I learned:**
You can pass a command directly to SSH without opening an 
interactive shell. This bypasses .bashrc entirely because 
the command runs before the shell fully initializes.
The readme file contained the bandit19 password.

---

## Level 19 → 20
**Goal:** Use the setuid binary in the home directory to 
read the next password
**Commands:**
./bandit20-do
# Shows usage instructions
./bandit20-do cat /etc/bandit_pass/bandit20

**What I learned:**
Setuid binaries run as their owner (bandit20) regardless 
of who executes them. This means we can read files owned 
by bandit20 even though we are logged in as bandit19.
This is a classic privilege escalation concept in Linux.

---

