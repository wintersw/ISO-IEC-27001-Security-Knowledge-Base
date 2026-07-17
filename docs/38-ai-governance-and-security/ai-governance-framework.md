---
title: AI Governance Framework
description: Components of an AI governance framework including policy, committee, intake workflow, and trust principles.
category: AI Governance and Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - AI
  - governance
  - policy
  - trust-principles
---

# AI Governance Framework

An AI governance framework is a structured system for identifying, approving, and managing AI systems throughout their lifecycle. It ensures that AI risks are not a blind spot and that AI adoption follows a repeatable, auditable process instead of appearing unannounced.

## Why a framework matters

Without a governance framework, AI systems enter the organisation through ad-hoc procurement, shadow IT, or enthusiastic teams experimenting with new tools. These systems process data, make decisions, and create risk without any assessment. By the time the ISMS becomes aware of them, the exposure has already accumulated. A framework shifts AI governance from reactive discovery to proactive intake.

## Key components

### AI policy

A high-level policy that articulates the organisation's commitment to responsible AI use. It sets the tone for how AI systems will be governed, defines the scope (internal builds, purchased products, embedded AI in vendor tools), assigns high-level responsibilities, and references the trust principles the organisation will enforce. The policy should be approved at the executive or board level and communicated to all relevant personnel.

### AI governance committee

A cross-functional body empowered to make go/no-go decisions on AI initiatives. Effective committees include representatives from:

- **Legal** -- regulatory compliance, liability, data-protection law
- **Cyber-security** -- AI-specific threat assessment, security baseline enforcement
- **Technology** -- platform governance, infrastructure, integration
- **Data science / AI engineering** -- model behaviour, data quality, testing
- **Business** -- use-case justification, benefit realisation
- **Audit and risk** -- independent assurance, risk-acceptance authority

The committee should be chaired by someone with executive authority and meet at a defined cadence. Training on AI risks should be mandatory for all members.

### AI intake and approval workflow

New AI use must enter through a defined intake process before deployment. A typical workflow:

1. **Proposal** -- the business or technology team submits a proposal describing the AI system, its use case, the data it will process, and the expected benefits.
2. **Triage** -- the proposal is classified by risk tier (based on data sensitivity, decision impact, regulatory exposure).
3. **Assessment** -- high-risk proposals undergo a detailed review covering data quality, bias testing, security assessment, supplier review (if external), and regulatory compliance.
4. **Decision** -- the governance committee reviews the assessment and approves, approves with conditions, or rejects.
5. **Registration** -- approved AI systems are recorded in the AI inventory with an owner, review date, and monitoring requirements.
6. **Periodic review** -- all AI systems are reviewed on a defined cycle; changes to the system, data, or regulatory environment trigger reassessment.

### AI trust principles

The framework should define trust principles that every AI system must satisfy. At a minimum, four principles should be enforced:

- **Integrity** -- the model and its training data are protected from unauthorised modification. Data is used only for its intended purpose. Data provenance and transformations are recorded.
- **Explainability** -- the decision-making process of the AI system is documented and understandable to relevant stakeholders. The system is not an opaque black box; affected individuals can obtain meaningful explanations of decisions that affect them.
- **Fairness** -- the system does not discriminate on protected characteristics. Training data is assessed for representativeness and bias. Outcomes are monitored for disparate impact across groups.
- **Resilience** -- the system is designed and tested to resist attacks, degrade gracefully under stress, and recover from compromise. This includes both traditional infrastructure security and AI-specific robustness against adversarial inputs.

### Training and awareness

The framework is only effective if the people involved understand it. Data scientists, engineers, business sponsors, and governance committee members all need role-appropriate training on AI risks, the governance process, and their responsibilities. Training should be refreshed as the regulatory landscape and threat environment evolve.

## Using existing frameworks as a starting point

Organisations do not need to build an AI governance framework from scratch. Publicly available models can be adapted:

- The **Singapore Model AI Governance Framework** provides detailed guidance on internal governance structures, operational methodologies, and stakeholder communication. It is technology-agnostic and suitable for organisations of any size.
- **[NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework)** provides a risk-management framework organised around four functions: Map, Measure, Manage, and Govern.
- **[ISO/IEC 42001:2023](https://www.iso.org/standard/42001)** provides a certifiable AI management system standard. See [ISO/IEC 42001 and AI standards](iso-42001-and-ai-standards.md) for details.

## Typical evidence

- Approved AI policy with version control and communication records
- AI governance committee terms of reference, membership list, and meeting minutes
- AI intake and approval records for each AI system
- Trust principle verification reports (bias testing, explainability documentation, resilience testing)
- Training attendance records for governance committee members and AI practitioners

## Practical example

A financial services firm discovers that three departments have independently procured AI tools for credit decisioning, customer analytics, and fraud detection -- none of which went through any security or governance review. The firm creates an AI policy, forms a cross-functional governance committee, and establishes an intake workflow. The three existing tools are retrospectively assessed: two are approved with remediation conditions (additional bias testing, API access restrictions), and one that sends customer data to an unvetted third-party model is replaced. All future AI procurement now routes through the intake process.

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)
- [AI Governance for ISMS](../29-emerging-data-security-trends/ai-governance-for-isms.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
