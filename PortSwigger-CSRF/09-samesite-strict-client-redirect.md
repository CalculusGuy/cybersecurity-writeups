# Lab 9: SameSite Strict Bypass via Client-Side Redirect
**Difficulty:** Practitioner  
**Status:** ✅ Solved

## Vulnerability
SameSite=Strict blocks cross-site requests.
But a client-side redirect gadget exists on the target site.
postId parameter used to dynamically construct redirect path.
Endpoint accepts GET requests for email change.

## Payload
```
<script>
    document.location = "https://TARGET/post/comment/confirmation
    ?postId=1/../../my-account/change-email
    ?email=attacker@gmail.com%26submit=1";
</script>
```

## Steps
1. Found commentConfirmationRedirect.js handles redirect using postId
2. Tested path traversal: postId=1/../../my-account → redirected to account page
3. Confirmed email change endpoint accepts GET requests
4. Chained path traversal + GET email change into one payload
5. document.location triggers top-level navigation → session cookie included
6. Delivered to victim → solved

## Why It Works
SameSite=Strict only blocks CROSS-SITE requests.
document.location navigates to target site first.
Redirect happens same-site → cookie included.
Server follows the redirected path with session.

## Fix
Validate redirect destinations server-side.
Never use user input to construct redirect paths.
