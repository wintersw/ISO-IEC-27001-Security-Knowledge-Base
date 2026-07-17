---
title: AI Security and Data Risk
description: Data security risks introduced by AI systems and AI-enabled workflows.
category: Emerging Data Security Trends
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - AI
  - data-risk
---

# AI Security and Data Risk
AI systems depend on data and create new risks around collection, training, inference, outputs, prompts, embeddings, and automation.

## Risk categories

- sensitive data in prompts
- training data leakage
- model memorization
- model inversion or membership inference
- data poisoning
- prompt injection
- insecure output handling
- supply-chain compromise
- excessive agency or tool access
- opaque decision logic
- unauthorized model use
- insecure vector stores

## Control themes

- AI asset inventory
- dataset approval
- model/data lineage
- prompt and output controls
- human oversight
- red teaming
- logging and monitoring
- supplier and model provider review
- incident playbooks for AI systems

## Current external references

NIST AI RMF 1.0 provides a risk management framework for AI risks to individuals, organizations, and society. OWASP's large language model (LLM) Top 10 identifies application-level risks such as prompt injection, insecure output handling, training data poisoning, model denial of service, supply-chain vulnerabilities, and sensitive information disclosure.

## Typical evidence

- AI asset inventory including models, prompts, and vector stores
- dataset approval and model/data lineage records
- prompt injection and output-handling test results
- provider reviews referencing NIST AI RMF or OWASP LLM Top 10 risks
- AI-specific incident playbooks and monitoring logs

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A customer-service assistant built on an LLM is tested against the OWASP LLM Top 10 before launch. Red-teaming shows a crafted support message can prompt-inject the model into revealing other customers' order details pulled from the vector store. The team scopes retrieval to the authenticated customer's records, adds output filtering, and logs the finding as a risk-register entry with a retest before go-live.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
