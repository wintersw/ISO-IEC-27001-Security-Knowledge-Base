---
title: Data Security Risk Scenarios
description: Reusable data security risk scenarios for risk assessments and threat modeling.
category: Data Security Governance
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-scenarios
  - data-security
---

# Data Security Risk Scenarios

Use these scenarios when updating the risk register or performing project risk assessments.

## Scenario library

| Scenario | Example impact |
|---|---|
| unauthorized bulk export | confidentiality breach, fraud, regulatory exposure |
| over-permissive data lake access | unauthorized analytics or disclosure |
| sensitive data in logs | unintended retention and exposure |
| production data in test | broad access to sensitive data |
| API data leakage | third-party or public exposure |
| model training data leakage | privacy and IP exposure |
| re-identification of anonymized data | privacy harm |
| ransomware encrypts critical data | availability loss |
| backup data exfiltration | long-tail breach impact |
| weak deletion process | retention violation |
| data poisoning | analytics, AI, or decision integrity failure |
| supplier misuse | legal and customer trust impact |

## Risk scenario format

> Threat actor or error causes unauthorized access, alteration, disclosure, loss, or misuse of a classified data asset, leading to business, legal, privacy, safety, or trust impact.


## Typical evidence

- approved policy, standard, procedure, or architecture record
- risk assessment or design review
- owner and role assignment
- implementation plan
- operating records
- monitoring records
- exception or waiver decisions
- test results
- audit records
- management review decisions

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)
