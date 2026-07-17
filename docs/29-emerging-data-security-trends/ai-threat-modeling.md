---
title: AI Threat Modeling
description: Threat modeling for models, datasets, prompts, agents, APIs, and outputs.
category: Emerging Data Security Trends
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - AI
  - threat-modeling
---

# AI Threat Modeling
AI threat modeling extends application threat modeling to data, models, prompts, plugins, agents, and model outputs.

## Assets to model

- training data
- validation data
- prompts
- embeddings
- vector databases
- model weights
- application programming interface (API) keys
- tools and plugins
- output channels
- evaluation results
- user feedback

## Threats

- prompt injection
- data poisoning
- model extraction
- sensitive data disclosure
- tool misuse
- insecure output handling
- unauthorized access
- denial of wallet or resource exhaustion
- dependency compromise
- unsafe autonomous action

## Typical evidence

- threat model documents covering models, prompts, tools, and output channels
- asset lists including training data, embeddings, and API keys
- identified threats mapped to mitigations and owners
- threat model updates after architecture or provider changes
- test results verifying the highest-risk threats are mitigated

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

Threat modeling an AI agent that can create calendar events and send email, the team identifies "unsafe autonomous action" as the top threat: a prompt-injected instruction hidden in a received email could make the agent forward confidential messages. Mitigations — requiring human confirmation for send actions and stripping instructions from untrusted content — are recorded in the threat model and verified with injection test cases.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
