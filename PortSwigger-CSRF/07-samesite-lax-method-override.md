# Lab 7: SameSite Lax Bypass via Method Override
**Difficulty:** Practitioner  
**Status:** ✅ Solved

## Vulnerability
Session cookie has default SameSite=Lax restriction.
Lax allows cookies on cross-site GET top-level navigation.
Server supports _method parameter to override HTTP method.

## Payload
```
<script>
    document.location = "https://TARGET/my-account/change-email
    ?email=attacker@gmail.com&_method=POST";
</script>
```

## Steps
1. Intercepted email change POST request
2. Confirmed no CSRF token present
3. Converted to GET → endpoint rejected it
4. Added _method=POST to GET request → accepted!
5. Confirmed email changed
6. Used document.location for top-level navigation
7. Delivered to victim → solved

## Why It Works
SameSite=Lax blocks cross-site POST but allows
cross-site GET on top-level navigation.
_method=POST tricks server into treating GET as POST.
Browser sends session cookie → attack succeeds.

## Fix
Don't support method override parameters.
Use SameSite=Strict for sensitive cookies.
Implement proper CSRF tokens.
