# Indirect Prompt Injection
**Difficulty:** Practitioner
**Objective:** Delete Carlos's account via poisoned product review

---

## Vulnerability
The LLM retrieved and processed untrusted external content (product reviews).
That content became executable instructions — classic RAG poisoning.

---

## Attack Flow
Map available functions → Verify delete_account exists → Craft 
malicious review → Victim LLM consumes review → Account deleted

---

## Steps

### 1. Function Mapping
Prompted the LLM to reveal available functions.
Confirmed delete_account capability existed.

### 2. Verify on Own Account
Tested the injection payload on own account first to confirm 
the LLM would execute it.
Confirmed self-account deletion worked.

### 3. Craft Malicious Review
Created a product review on the l33t Leather Jacket containing 
hidden instructions:
- Instructions told the LLM to call delete_account
- Written to look like normal review content

### 4. Exploitation
Carlos's session consumed the poisoned review via the LLM.
LLM treated review content as trusted instructions.
delete_account executed → Carlos deleted ✅

---

## Key Takeaway
Untrusted content retrieved by an LLM can become executable instructions.
RAG pipelines must treat all external content as untrusted input.
The LLM had no way to distinguish between legitimate instructions 
and injected ones hidden in reviews.
