---
title: AI Lifecycle Risks and Controls
description: "Risk-to-control mapping across the AI model lifecycle stages: selection, training, deployment, and operation."
category: AI Governance and Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - AI
  - lifecycle
  - risks
  - controls
---

# AI Lifecycle Risks and Controls

AI-specific risks emerge at different stages of the model lifecycle. Understanding where each risk arises helps an organisation place the right controls at the right point in the pipeline. This page provides a consolidated reference; the underlying attack techniques are covered in detail by [Adversarial ML and Model Abuse](../29-emerging-data-security-trends/adversarial-ml-and-model-abuse.md) and [AI Threat Modeling](../29-emerging-data-security-trends/ai-threat-modeling.md).

## Lifecycle stages and associated risks

### Stage 1: Model selection

The organisation chooses or builds the machine learning model. Most organisations do not train models from scratch. They either purchase pre-trained models, use open-source models from public repositories (model zoos), or outsource training to a third party.

| Risk | Description | Attack type |
|---|---|---|
| Model poisoning | An attacker compromises a pre-trained model in a public repository, injecting a backdoor. The model behaves correctly except when the attacker's trigger is present. | Supply chain |

### Stage 2: Training, testing, and optimisation

The model is trained on datasets and iteratively refined until performance targets are met.

| Risk | Description | Attack type |
|---|---|---|
| Data poisoning | An attacker contaminates the training data so the model learns incorrect patterns. A poisoned self-driving-car model could fail to recognise stop signs. | Training |
| Training data breach | Training data stored in accessible locations (file shares, cloud buckets, development environments) is exfiltrated. AI training datasets often contain sensitive real-world data. | Traditional |

### Stage 3: Deployment

The trained model is deployed to production, typically exposed through an API.

| Risk | Description | Attack type |
|---|---|---|
| Model compromise | The attacker exploits a conventional vulnerability in the hosting infrastructure or application serving the model to gain unauthorised access. | Traditional |

### Stage 4: Operation and monitoring

The model is live and processing real inputs. This is the longest phase and where the most distinctive AI-specific attacks occur.

| Risk | Description | Attack type |
|---|---|---|
| Model evasion | The attacker crafts adversarial inputs -- small perturbations invisible to humans -- that cause the model to make incorrect predictions. An anti-malware system fails to detect a sample; a facial recognition system identifies the wrong person. | Adversarial |
| Model extraction | The attacker queries the model API repeatedly, observing inputs and outputs, and builds a functionally equivalent offline copy. The copy can be studied to find further weaknesses or stolen as intellectual property. | Adversarial |
| Data extraction (membership inference) | The attacker queries the model and infers whether specific data was used in training. In advanced cases, this can reveal sensitive information such as whether a particular person was in a medical dataset. | Adversarial |

## Control mapping

| Risk | Control |
|---|---|
| Model poisoning (supply chain) | Verify model provenance. Do not deploy models from unvetted public repositories. Require vendor security documentation including model training methodology and risk management practices. Prefer models for which threats are identified and controls are documented. Scan model files for known vulnerabilities. |
| Data poisoning | Verify the integrity of training data pipelines. Use trusted, approved data sources with hash verification. Maintain the ability to revert to a clean dataset and retrain if contamination is detected. |
| Training data breach | Apply standard data-protection controls: encryption at rest, access control on a least-privilege basis, data classification enforcement. Treat training datasets as sensitive assets in the asset inventory. |
| Model compromise | Apply standard infrastructure and application security: hardening, patching, vulnerability management, access control, logging and monitoring. The model is software running on infrastructure; platform security is a prerequisite. |
| Model evasion | Generate adversarial examples and include them in the model testing suite before deployment. Use adversarial robustness training during model development. Monitor production model accuracy for unexplained degradation. |
| Model extraction | Limit information in API responses. Do not expose raw confidence scores. Apply rate limiting and anomaly detection to model APIs. Monitor for abnormal query patterns that indicate systematic extraction attempts. |
| Data extraction (membership inference) | Sanitise model outputs to prevent disclosure of training data characteristics. Control API verbosity. Restrict API access to authorised users where feasible. Apply differential privacy techniques for models trained on sensitive data. |

## Cross-references for deeper coverage

The control mapping above summarises the main risk-control relationships. For detailed technical treatment of each attack type and its detection, see:

- [Adversarial ML and Model Abuse](../29-emerging-data-security-trends/adversarial-ml-and-model-abuse.md) -- technical depth on poisoning, evasion, and extraction attacks
- [AI Threat Modeling](../29-emerging-data-security-trends/ai-threat-modeling.md) -- structured threat modelling approach using STRIDE-like categories applied to AI systems
- [Secure AI Development Lifecycle](../29-emerging-data-security-trends/secure-ai-development-lifecycle.md) -- controls organised by development phase

## Typical evidence

- AI risk assessment records organised by lifecycle stage
- Control mapping document linking AI-specific risks to implemented controls
- Model provenance verification records for externally sourced models
- Training data integrity verification records
- Adversarial testing results for deployed models
- API monitoring dashboards with anomaly-detection thresholds

## Practical example

A team deploys an image-classification model for automated quality inspection. During the security review, the risk of model evasion is identified: an attacker could subtly modify product images to trick the system into passing defective items. The team generates adversarial examples and tests the model: the evasion success rate is unacceptably high. They apply adversarial training (retraining the model with adversarial examples in the dataset), reducing the evasion rate to below the acceptable threshold. The adversarial test suite is added to the CI/CD pipeline so every model update is retested before deployment.

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
