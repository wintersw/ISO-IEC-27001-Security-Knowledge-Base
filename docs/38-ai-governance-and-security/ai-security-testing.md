---
title: AI Security Testing
description: Extending penetration testing to AI systems using MITRE ATLAS and adversarial robustness testing techniques.
category: AI Governance and Security
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - AI
  - security-testing
  - red-teaming
  - ATLAS
---

# AI Security Testing

Traditional penetration testing finds vulnerabilities in the platform and application layers. AI security testing extends this to the model layer, testing for adversarial robustness, model extraction resistance, and training data privacy. The field is maturing rapidly, but several frameworks and tools are already available.

## MITRE ATLAS

[MITRE ATLAS](https://atlas.mitre.org/) (Adversarial Threat Landscape for Artificial-Intelligence Systems) is a knowledge base of adversary tactics, techniques, and case studies for machine learning systems. Modelled on the widely used MITRE ATT&CK framework, it maps real-world AI attacks to a structured taxonomy that security practitioners already understand.

ATLAS organises AI attacks into tactics such as: Reconnaissance, Resource Development, Initial Access, ML Model Access, Execution, Persistence, Defence Evasion, Discovery, Collection, ML Attack Staging, Exfiltration, and Impact. Each tactic contains specific techniques with descriptions, mitigations, and references to public incidents.

The ATLAS case studies page documents known attacks on production AI systems and is a valuable resource for security teams building AI threat models or designing test scenarios.

## AI security testing approaches

### Standard security testing of the platform

Before testing the model, test the platform. This is the same discipline as any penetration test: infrastructure scanning, application vulnerability assessment, access control review, configuration audit. The model runs on infrastructure; if the infrastructure is compromised, the model is compromised. This is a prerequisite, not a substitute for AI-specific testing.

### Adversarial robustness testing

Test the model's resistance to inputs designed to cause misclassification or incorrect outputs. Adversarial testing includes:

- **Evasion testing** -- craft inputs that are imperceptibly different from legitimate inputs but cause the model to produce incorrect results. Example: adding noise to a malware sample so an AI-based anti-malware system classifies it as benign.
- **Poisoning testing** -- evaluate whether a model trained on partially poisoned data exhibits the expected backdoor behaviour.
- **Extraction testing** -- attempt to reconstruct the model's functionality through systematic API queries. Assess whether the API responses leak enough information to enable a copy.
- **Inference testing** -- test whether querying the model can reveal characteristics of its training data, including whether specific data points were used in training.

### Red team / blue team model

A structured adversarial testing approach adapted from traditional security operations:

- **AI red team**: Internal or external specialists who simulate adversarial attacks against AI systems. The red team attempts evasion, extraction, poisoning, and inference attacks against production or pre-production models. Their goal is to find weaknesses before real attackers do.
- **AI blue team**: Internal security personnel who monitor AI systems for signs of attack, respond to incidents, and verify that controls are effective. Blue teams should understand the attack techniques the red team uses and maintain detection and response capabilities.

Red and blue team exercises should be conducted periodically and after significant model changes. Findings should be tracked in the risk register with assigned remediation owners and retest dates.

## Testing tooling characteristics

When selecting AI security testing tools, look for:

- **Model-agnostic** -- works across different model architectures and frameworks rather than being tied to one type
- **Technology-agnostic** -- can test models hosted on cloud, on-premise, or hybrid infrastructure
- **Automatable** -- provides command-line or API interfaces so tests can be scripted and integrated into CI/CD pipelines

Examples of publicly available AI security testing tools include Counterfit (Microsoft) for automated adversarial attack simulation and the Adversarial Robustness Toolbox (ART) for evaluating and defending models against evasion, poisoning, extraction, and inference attacks. Both are open-source and designed for integration into existing security testing toolkits.

## Integrating into the ISMS

AI security testing results should feed into the organisation's risk management process:

- Findings are recorded as risks in the risk register with severity, likelihood, and treatment decisions
- Testing is scheduled as part of the internal audit programme or security assurance calendar
- Test results are reviewed during management review as part of the AI governance reporting
- Corrective actions for failed tests follow the organisation's corrective action process (clause 10)
- Retesting confirms remediation effectiveness

## Typical evidence

- AI security testing methodology document referencing MITRE ATLAS or equivalent framework
- Adversarial test results for each AI system with identified weaknesses and remediation status
- Red team exercise reports with findings, severity ratings, and recommended controls
- Blue team monitoring procedures and detection rules for AI-specific attack patterns
- Risk register entries linked to AI security testing findings

## Practical example

An organisation deploys a customer-facing chatbot powered by a large language model. Before launch, an AI red team exercises the system against ATLAS-aligned scenarios: prompt injection (attempting to override system instructions), jailbreaking (attempting to bypass content restrictions), and data extraction (attempting to elicit training data or other customers' information). The red team finds that the model can be prompted to reveal system prompt contents and occasionally fabricates plausible but false information about the organisation's policies. Mitigations are applied -- input filtering, output monitoring, and a human-in-the-loop review for sensitive topics -- and the system is retested before go-live.

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)
- [AI Threat Modeling](../29-emerging-data-security-trends/ai-threat-modeling.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
