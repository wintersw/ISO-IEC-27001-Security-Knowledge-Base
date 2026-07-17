---
title: ISO/IEC 42001 and AI Standards
description: How ISO/IEC 42001:2023 (AI management system) and related AI standards integrate with ISO/IEC 27001.
category: AI Governance and Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - AI
  - ISO-42001
  - ISO-23894
  - standards
---

# ISO/IEC 42001 and AI Standards

[ISO/IEC 42001:2023](https://www.iso.org/standard/42001) is the international standard for an Artificial Intelligence Management System (AIMS). Published in December 2023, it provides a certifiable framework for governing AI systems -- analogous to how ISO/IEC 27001 governs information security. Several complementary standards support AI risk management and governance.

## ISO/IEC 42001:2023 -- AI Management System

ISO/IEC 42001 specifies requirements for establishing, implementing, maintaining, and continually improving an AI management system. It follows the same harmonised structure (Annex SL) as ISO/IEC 27001, which means the clause structure is identical: context of the organisation (clause 4), leadership (clause 5), planning (clause 6), support (clause 7), operation (clause 8), performance evaluation (clause 9), and improvement (clause 10).

Because of this shared structure, an organisation that already operates an ISO/IEC 27001 ISMS has a significant head start. Many management system elements -- document control, internal audit, management review, corrective action -- can serve both systems with minimal duplication. Joint or integrated audits are practical.

## Integration with ISO/IEC 27001

Areas where the two management systems naturally overlap:

| Domain | ISO/IEC 27001 | ISO/IEC 42001 |
|---|---|---|
| Asset management | Information assets | AI systems, models, datasets |
| Risk assessment | Information security risks | AI-specific risks (bias, drift, adversarial robustness) |
| Supplier management | Third-party security | AI model and data providers |
| Incident management | Security incidents | AI-specific incidents (model compromise, data poisoning, unintended outputs) |
| Competence | Security competence | AI governance and AI-security competence |
| Monitoring | Security metrics and KPIs | AI system performance, drift, fairness metrics |

## Other relevant ISO/IEC AI standards

- **[ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html)** -- Guidance on AI risk management. Complements ISO/IEC 42001 by providing detailed risk-management methodology for AI systems. Useful as a reference when designing the organisation's AI risk assessment approach.
- **[ISO/IEC 22989:2022](https://www.iso.org/standard/74296.html)** -- AI terminology and concepts. Establishes a common vocabulary.
- **ISO/IEC 23053:2022** -- Framework for AI systems using machine learning. Describes the ML lifecycle and system components.
- **ISO/IEC 38507:2022** -- Governance implications of AI for organisations. Guidance for governing bodies on AI oversight responsibilities.

## NIST AI RMF as a complementary resource

The United States [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) (AI RMF 1.0, January 2023) is not an ISO standard but is widely referenced internationally. It organises AI risk management around four functions:

- **Map** -- understand the AI system's context, purpose, and risk factors
- **Measure** -- assess the system for trustworthiness characteristics including validity, reliability, safety, security, resilience, accountability, transparency, explainability, interpretability, privacy, and fairness
- **Manage** -- allocate risk resources, treat identified risks, and maximise benefits
- **Govern** -- cultivate a culture of risk management throughout the AI lifecycle

The NIST AI RMF is non-mandatory and can be used alongside ISO/IEC 42001. Many organisations use the NIST framework for internal governance while certifying against ISO/IEC 42001 for external assurance.

## Typical evidence

- Scope statement showing ISMS-AIMS overlap or integration
- Combined or aligned risk assessment methodology covering both information security and AI risks
- Joint or coordinated internal audit programme
- Management review records addressing AI governance
- Mapping of ISO/IEC 42001 controls to ISMS controls where overlap exists

## Practical example

An organisation already certified to ISO/IEC 27001 decides to extend to ISO/IEC 42001. The existing context analysis is updated to include AI-related interested parties and obligations. The risk assessment methodology is extended with AI-specific risk categories (bias, drift, adversarial robustness). The internal audit programme adds AI governance audit lines. Document control, management review, and corrective action processes are reused with AI-specific content added. A combined certification audit covers both standards, reducing audit overhead.

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)
- [ISO/IEC 27000 Family Detailed](../03-iso27001/iso27000-family-detailed.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
