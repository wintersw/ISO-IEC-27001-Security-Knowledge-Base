---
title: AI Regulatory Landscape
description: Overview of the EU AI Act risk-based framework and its implications for ISMS governance.
category: AI Governance and Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - AI
  - regulation
  - EU-AI-Act
---

# AI Regulatory Landscape

Regulation is the primary driver for formal AI governance in many organisations. The most consequential regulation globally is the European Union's [Artificial Intelligence Act (Regulation (EU) 2024/1689)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en), which establishes a risk-based compliance framework with extraterritorial reach. Understanding this regulation, and how it interacts with the ISMS, allows an organisation to prepare before compliance deadlines arrive.

## The EU AI Act: risk-based tiers

The Act classifies AI systems into four risk levels and applies requirements accordingly:

### Unacceptable risk (prohibited)

AI practices that are banned outright. Examples include: real-time remote biometric identification in publicly accessible spaces (with narrow law-enforcement exceptions), social scoring that leads to detrimental or disproportionate treatment (applying to both public and private actors), AI systems that manipulate individuals through subliminal techniques, systems that exploit vulnerabilities related to age, disability, or social or economic situation, and emotion recognition in workplaces and educational institutions (with narrow medical and safety exceptions).

### High risk

The bulk of the regulation's obligations. An AI system is high risk if it is a safety component of a product already subject to third-party conformity assessment (machinery, medical devices, toys) or if it is listed in the Act's Annex III. Annex III domains include: critical infrastructure, education and vocational training, employment and worker management, access to essential private and public services, law enforcement, migration and border control, and administration of justice.

High-risk AI systems must meet obligations covering: risk management system, data quality and governance, technical documentation and record-keeping, transparency and provision of information to users, human oversight, accuracy, robustness and cybersecurity, and post-market monitoring. Providers must undergo a conformity assessment and register the system in an EU database before placing it on the market.

### Limited risk

Systems that interact directly with people or generate content are subject to transparency obligations: users must be informed they are interacting with an AI system (chatbots), and AI-generated or manipulated content such as deepfakes must be disclosed as such.

### Minimal risk

The vast majority of AI systems (spam filters, recommendation engines, inventory-optimisation tools) fall here. No mandatory obligations apply, though codes of conduct are encouraged.

## Extraterritorial scope

Like the GDPR, the EU AI Act applies beyond EU borders. It covers:

- Providers placing AI systems on the EU market or putting them into service in the EU
- Deployers (users) of AI systems located in the EU
- Providers and deployers in third countries where the output of the AI system is used in the EU

An organisation outside the EU that sells an AI-powered product to EU customers, or whose AI system's outputs affect individuals in the EU, can be in scope.

## Phased application

The Act entered into force on 1 August 2024. Key compliance deadlines are staggered: provisions on prohibited practices apply earliest, followed by obligations for general-purpose AI models, and finally the full high-risk system obligations and penalties regime. Organisations should verify the current timeline against the published regulation text and the European Commission's [AI Act implementation overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai).

## Preparing for compliance

An organisation that already operates an ISO/IEC 27001 ISMS has a structural advantage. Steps to prepare:

1. **Inventory AI systems** -- identify every AI system the organisation builds, buys, or uses, including those embedded in vendor products.
2. **Classify by risk tier** -- determine which systems fall into high-risk, limited-risk, or minimal-risk categories under the Act.
3. **Gap assessment** -- compare current practices against the Act's requirements for each tier. High-risk obligations in particular are substantial.
4. **Integrate into ISMS** -- treat AI Act requirements as compliance obligations in the context assessment (clause 4) and link them to specific controls and documented information.
5. **Plan for conformity assessment** -- if the organisation places high-risk AI systems on the market, establish the conformity assessment process and prepare the technical documentation.

## Other jurisdictions

Several other countries and regions are developing or have enacted AI regulations. The United States has taken a sectoral approach through executive orders and agency-specific guidance. China has enacted regulations on algorithmic recommendation, deep synthesis, and generative AI. Singapore publishes voluntary model governance frameworks. The ISMS should treat the applicable regulatory landscape as part of clause 4 context and interested-party analysis.

## Typical evidence

- AI system inventory with regulatory tier classification
- EU AI Act gap assessment report
- Mapping of regulatory obligations to ISMS controls
- Conformity assessment documentation (for high-risk system providers)
- Register of applicable AI regulations by jurisdiction

## Practical example

A software company selling an AI-powered CV screening tool to EU customers classifies it as high risk (employment and worker management). The company uses its existing ISMS document-control and risk-assessment processes as a foundation, then adds the Act's specific requirements: a detailed risk management system for the AI component, data quality checks against training data bias, technical documentation following the Act's prescribed structure, and a conformity assessment record. The existing internal audit programme is extended to cover AI Act compliance.

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
