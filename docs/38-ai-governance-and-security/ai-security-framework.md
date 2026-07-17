---
title: AI Security Framework
description: "Building an AI security capability: regulatory mapping, security baseline, inventory, risk assessments, awareness, and assurance integration."
category: AI Governance and Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - AI
  - security-framework
  - baseline
---

# AI Security Framework

Securing AI systems requires extending the existing information security capability with AI-specific controls. An AI security framework provides a structured approach to identifying, assessing, and mitigating the unique risks that AI systems introduce.

## Key components

### Map the regulatory environment

Different jurisdictions impose different obligations on AI systems. The organisation must understand which regulations apply to its AI systems based on where they are developed, deployed, and where their outputs are used. This determines the mandatory minimum controls and the documentation required for compliance. See [AI Regulatory Landscape](ai-regulatory-landscape.md).

### Define an AI security baseline

A security baseline provides the minimum controls that must be applied to every AI system, regardless of its risk level. The baseline operates at two layers:

- **Platform layer** -- standard infrastructure security: hardening of cloud or on-premise hosting, encryption of data at rest and in transit, access control, logging and monitoring, vulnerability management, patching. This is the same discipline applied to any production system and should follow existing security standards.
- **AI-specific layer** -- controls unique to AI systems: training data integrity, model provenance verification, adversarial robustness testing, prompt and output controls, API throttling, anomaly detection for model queries, confidence-score restrictions, data sanitisation in model outputs, and model rollback capability.

The baseline should be documented, approved, and maintained as the threat landscape evolves.

### Maintain an AI system inventory

You cannot secure what you do not know exists. The inventory should capture for each AI system:

- System name and description
- Business unit and owner
- Use case and decisions the system influences
- Technology stack and model provider
- Data types used for training and in production
- Whether personal or confidential data is involved
- Customers served (internal, external, jurisdiction)
- API exposure level
- Risk classification (under the EU AI Act and the organisation's own criteria)
- Last review date and next review due

The inventory should be maintained as a living document and reviewed periodically. Discovery of unregistered AI systems should trigger the governance intake workflow.

### Conduct AI technical risk assessments

Each AI system in the inventory should undergo a technical risk assessment proportional to its risk classification. The assessment should cover: training data quality and provenance, model supply chain (pre-trained models, third-party libraries), adversarial robustness (evasion, poisoning, extraction), data privacy (memorisation, membership inference), and operational resilience (drift detection, rollback procedures).

An AI-specific risk assessment methodology should be defined and integrated with the organisation's overall risk management process. See [AI Lifecycle Risks and Controls](ai-lifecycle-risks-and-controls.md) for a detailed mapping.

### Build an AI security awareness programme

The biggest single risk factor for AI security is lack of awareness. Security professionals who treat AI systems as standard applications will miss AI-specific vulnerabilities. Data scientists who are unaware of adversarial threats may train models without defensive considerations.

An effective programme includes: awareness briefings for security teams on adversarial machine learning and model-specific attacks, training for data science and engineering teams on secure model development practices, and executive briefings that translate AI security risks into business-impact language.

### Extend security assurance to AI

Existing security assurance processes -- penetration testing, code review, architecture review, supplier due diligence, change management -- should be extended to cover AI-specific concerns:

- **Penetration testing**: Include AI-specific attack techniques (adversarial samples, model extraction, membership inference). See [AI Security Testing](ai-security-testing.md).
- **Architecture review**: Include the AI pipeline -- data sources, training infrastructure, model serving, monitoring and drift detection.
- **Supplier review**: Assess AI model and data providers' security practices, model provenance, and incident response capability.
- **Change management**: Treat model retraining, data-source changes, and hyper-parameter tuning as changes requiring review.

## Typical evidence

- Approved AI security baseline document
- AI system inventory with current entries and review dates
- AI-specific risk assessment records
- AI security awareness training attendance and materials
- Security assurance records that include AI-specific test results
- Updated penetration testing methodology covering AI attack techniques

## Practical example

A company creates its first AI security baseline by extending its existing cloud-security standard. The platform layer references the same encryption, access-control, and monitoring requirements used for all production services. The AI-specific layer adds: training data must be from approved sources with hash verification, all model APIs must apply rate limiting and monitor for abnormal query patterns, models handling personal data must be tested for membership inference before deployment, and every AI system must have a documented rollback procedure. The baseline becomes a mandatory requirement in the AI system intake process.

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)
- [Secure AI Development Lifecycle](../29-emerging-data-security-trends/secure-ai-development-lifecycle.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
