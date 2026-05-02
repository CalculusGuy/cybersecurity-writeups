# XSS (Cross-Site Scripting) — Complete Writeup
**Platform:** PortSwigger Web Security Academy  
**Date:** May 2026  
**Level Reached:** Practitioner  
**Tools Used:** Burp Suite, Browser DevTools  

---

## What is XSS?

Cross-site scripting is a client-side injection vulnerability where an attacker 
injects malicious JavaScript into a web application. The browser executes it 
instead of displaying it as text.

Three types:
- **Reflected XSS** — payload fires once via URL, only for the attacker
- **Stored XSS** — payload saved in database, fires for every user who visits
- **DOM-based XSS** — browser itself executes the payload, no server involved

---

## Labs Solved

### Lab 1 — Reflected XSS into HTML context, nothing encoded
**Difficulty:** Apprentice  
**Payload:**
```html
alert(1)
```
**What happened:**  
Search box reflected input directly into HTML response with zero sanitization. 
Browser saw script tags, executed them. Alert fired.

**Lesson:** Always test the simplest payload first. Baseline with no defenses.

---

### Lab 2 — Stored XSS into HTML context, nothing encoded
**Difficulty:** Apprentice  
**Payload:**
```html
alert(1)
```
Injected into name, email, and comment fields.

**What happened:**  
Payload stored in database. Every user visiting the page triggers execution.

**Lesson:** Stored XSS is significantly more dangerous than reflected — 
one injection affects every visitor, not just the attacker.

---

### Lab 3 — Reflected XSS into attribute with angle brackets HTML-encoded
**Difficulty:** Apprentice  
**Payload:**
?search=%22%3E%3Csvg%20onload%3Dalert(1)%3E
URL decoded: `"><svg onload=alert(1)>`

**What happened:**  
Angle brackets were being HTML-encoded, neutralizing `<script>` tags.  
Input was inside an HTML attribute — so I:
- Used `"` to close the attribute
- Used `>` to close the HTML tag
- Injected SVG element with onload event handler

**Lesson:** Always identify your injection context. Breaking out of an 
attribute requires different technique than breaking out of HTML body.

---

### Lab 4 — Reflected XSS into HTML context, most tags and attributes blocked
**Difficulty:** Apprentice  
**Payload:**
```html
<img src=1 onerror=alert(1)>
```
**What happened:**  
Script tags explicitly blocked. Used broken image tag instead — browser 
tries to load src=1, fails, fires onerror event handler.

**Lesson:** When script tags are blocked, event handlers are your friend. 
`onerror`, `onmouseover`, `onload` — all valid execution vectors.

---

### Lab 5 — Reflected XSS into attribute with angle brackets HTML-encoded
**Difficulty:** Apprentice  
**Payload:**
?returnPath=javascript:alert(document.cookie)
**What happened:**  
Injected into an href attribute via javascript: protocol.  
Extracted document.cookie — not just a proof of concept anymore.  
In a real attack this is session hijacking.

**Lesson:** `javascript:` protocol in href attributes is a powerful vector. 
`document.cookie` extraction = game over for the victim's session.

---

### Lab 6 — Stored XSS into anchor href attribute with double quotes HTML-encoded
**Difficulty:** Apprentice  
**Payload:**
```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/#" 
onload="this.src+='<img src=x onerror=print()>'">
</iframe>
```
**What happened:**  
Multi-stage chained execution:
1. Injected iframe pointing to same domain
2. Waited for iframe to load
3. Dynamically injected second payload inside iframe via onload
4. Two execution contexts, one attack chain

**Lesson:** XSS payloads can chain. Real-world exploits are rarely 
single-stage — learn to think in execution chains.

---

### Lab 7 — Reflected XSS into attribute with angle brackets HTML-encoded (Burp)
**Difficulty:** Apprentice  
**Payload:**
" onmouseover="alert(1)
**Tool:** Burp Suite Repeater  

**What happened:**  
Switched from browser to Burp Suite. Intercepted the GET request, 
modified the search parameter directly in Repeater.  
Response showed payload reflected into input field value attribute.  
`onmouseover` fires on hover — confirmed in response before touching browser.

**Lesson:** Burp Suite Repeater lets you confirm injection in the response 
before ever triggering it in the browser. Faster, cleaner, more controlled.

---

### Lab 8 — Reflected XSS into href attribute with double quotes HTML-encoded
**Difficulty:** Apprentice  
**Payload:**
javascript:alert(1)
**What happened:**  
Injected javascript: protocol into anchor href.  
Click triggers execution. Clean and direct.

---

### Lab 9 — Reflected XSS into a JavaScript string with angle brackets HTML-encoded
**Difficulty:** Apprentice  
**Payload:**
'-alert(1)//
**Tool:** Burp Suite Repeater  

**What happened:**  
Input was inside a JavaScript string — completely different context from HTML.  
- `'` closed the existing string
- `-alert(1)` executed the function  
- `//` commented out everything after, preventing syntax errors

**Lesson:** JavaScript string context requires breaking out of the string 
first. The `//` comment is critical — without it the remaining code 
causes a syntax error and execution fails.

---

### Lab 10 — XSS into HTML context with most tags and attributes blocked (SELECT)
**Difficulty:** Practitioner ⭐  
**Payload:**
/product?productId=1&storeId="></select><img%20src=1%20onerror=alert(1)>
**What happened:**  
Input was inside a SELECT element — a completely different HTML context.  
Multi-layer escape required:
1. `"` — closed the value attribute
2. `></select>` — escaped the SELECT element entirely
3. `<img src=1 onerror=alert(1)>` — injected fresh execution context

**Lesson:** Always identify the full HTML context of your injection point. 
SELECT elements require escaping both the attribute AND the element itself 
before injecting. This is why context analysis is the most important skill 
in XSS.

---

## Key Techniques Learned

| Technique | Payload Pattern | When to Use |
|-----------|----------------|-------------|
| Basic script injection | `<script>alert(1)</script>` | No sanitization |
| Event handler injection | `<img src=1 onerror=alert(1)>` | Script tags blocked |
| Attribute escape | `"><svg onload=alert(1)>` | Input inside HTML attribute |
| JavaScript string escape | `'-alert(1)//` | Input inside JS string |
| Protocol injection | `javascript:alert(1)` | Input inside href |
| Element escape | `"></select><img...>` | Input inside form elements |
| Chained execution | iframe + onload injection | Multi-stage attacks |

---

## XSS vs Prompt Injection — The Connection

Both attacks exploit the same core weakness:

**Systems that process untrusted input without understanding context.**

- In XSS: browser treats injected text as executable code
- In Prompt Injection: AI treats injected text as legitimate instructions

The technique is identical — find the boundary between data and instruction, 
break through it. Web security knowledge is the perfect foundation for AI 
security. The surface changes. The mindset stays the same.

---

## Tools Used
- **Burp Suite Community Edition** — request interception, Repeater
- **Browser DevTools** — response inspection
- **PortSwigger Web Security Academy** — lab environment

---

## Resources
- [PortSwigger XSS Learning Path](https://portswigger.net/web-security/cross-site-scripting)
- [PortSwigger XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)
- [Medium Article — Full Writeup](https://medium.com/@nilanjan.calculus/from-prompt-injection-to-xss-my-first-night-attacking-ai-and-web-systems-8255a6ecc45f)

---

*Written by Nilanjan Chowdhury*
