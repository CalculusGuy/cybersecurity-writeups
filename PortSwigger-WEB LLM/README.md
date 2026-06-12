# 🤖 Web LLM Attacks — PortSwigger Labs

**Status:** 8/8 Solved ✅ | Apprentice ✅ | Practitioner ✅ | Expert ✅
**SECTION COMPLETE**

---

## What Are Web LLM Attacks?

Large Language Models integrated into web applications introduce a new class of 
vulnerabilities. Unlike traditional web attacks, LLM vulnerabilities arise from:

- **Excessive agency** — LLMs granted too much access to backend systems
- **Insecure output handling** — LLM responses rendered without sanitization
- **Prompt injection** — Untrusted input manipulating LLM behavior
- **AI agent exploitation** — Chaining LLM actions to trigger secondary vulnerabilities
- **Agent jailbreaking** — Instruction overrides hijacking an agent's task

---

## Labs Completed

| # | Lab | Difficulty | Key Technique |
|---|-----|-----------|---------------|
| 1 | Exploiting LLM APIs with Excessive Agency | Apprentice | API enumeration → debug_sql abuse |
| 2 | Exploiting Vulnerabilities in LLM APIs | Practitioner | OS command injection via LLM API |
| 3 | Indirect Prompt Injection | Practitioner | RAG poisoning via product review |
| 4 | Exploiting Insecure Output Handling in LLMs | Expert | XSS + indirect prompt injection chained |
| 5 | Exploiting AI Agents to Trigger Secondary Vulnerabilities | Practitioner | SSRF + AI agent + indirect prompt injection |
| 6 | Exploiting AI Agents to Perform Destructive Actions | Apprentice | Fake vuln report → CSRF executed by AI scanner |
| 7 | Exploiting AI Agents to Exfiltrate Sensitive Information | Apprentice | "Ignore previous instructions" jailbreak → API key leaked |
| 8 | Bypassing AI Scanner Defenses to Exfiltrate Sensitive Information | Practitioner | Reframed request bypasses redaction defense |

---

## Key Takeaways

- LLMs can be weaponized through their own tool access — no traditional injection needed
- Untrusted content (reviews, documents, comments) consumed by an LLM becomes an attack surface
- LLM output rendered in browser without encoding = XSS vector
- AI agents with network access amplify SSRF and internal service attacks
- AI agents can be jailbroken via "ignore previous instructions" — even when autonomous
- Soft defenses (e.g. redaction instructions) can be bypassed through prompt reframing
- Always treat LLM input/output boundaries as trust boundaries

---

## Tools Used

- Burp Suite
- PortSwigger Web Security Academy

---

## Related Medium Article

> [I Didn't Hack the App. I Hacked the AI.](https://medium.com/@nilanjan.calculus/i-didnt-hack-the-app-i-hacked-the-ai-web-llm-is-breached-79d7aa57c471)
