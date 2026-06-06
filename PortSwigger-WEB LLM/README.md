# 🤖 Web LLM Attacks — PortSwigger Labs

**Status:** 5/8 Solved | Apprentice ✅ | Practitioner ✅ | Expert ✅

---

## What Are Web LLM Attacks?

Large Language Models integrated into web applications introduce a new class of 
vulnerabilities. Unlike traditional web attacks, LLM vulnerabilities arise from:

- **Excessive agency** — LLMs granted too much access to backend systems
- **Insecure output handling** — LLM responses rendered without sanitization
- **Prompt injection** — Untrusted input manipulating LLM behavior
- **AI agent exploitation** — Chaining LLM actions to trigger secondary vulnerabilities

---

## Labs Completed

| # | Lab | Difficulty | Key Technique |
|---|-----|-----------|---------------|
| 1 | Exploiting LLM APIs with Excessive Agency | Apprentice | API enumeration → debug_sql abuse |
| 2 | Exploiting Vulnerabilities in LLM APIs | Practitioner | OS command injection via LLM API |
| 3 | Indirect Prompt Injection | Practitioner | RAG poisoning via product review |
| 4 | Exploiting Insecure Output Handling in LLMs | Expert | XSS + indirect prompt injection chained |
| 5 | Exploiting AI Agents to Trigger Secondary Vulnerabilities | Practitioner | SSRF + AI agent + indirect prompt injection |

---

## Key Takeaways

- LLMs can be weaponized through their own tool access — no traditional injection needed
- Untrusted content (reviews, documents) consumed by an LLM becomes an attack surface
- LLM output rendered in browser without encoding = XSS vector
- AI agents with network access amplify SSRF and internal service attacks
- Always treat LLM input/output boundaries as trust boundaries

---

## Tools Used

- Burp Suite
- PortSwigger Web Security Academy

---

## Related Medium Article

> [Web LLM Attacks — From API Abuse to Agent Exploitation](#) *(link after publish)*
