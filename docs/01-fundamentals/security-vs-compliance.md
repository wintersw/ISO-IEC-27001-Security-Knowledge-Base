---
title: Security vs Compliance
description: Explains the relationship and difference between real security and compliance evidence.
category: Fundamentals
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - fundamentals
---

# Security vs Compliance

Security reduces risk. Compliance demonstrates that defined obligations have been met. They overlap, but they are not the same.

## Compliance without security

A process may produce audit evidence but still fail to reduce meaningful risk. Example: annual access reviews that approve all access without checking whether it is still needed.

## Security without compliance

A team may implement strong technical controls but fail certification because responsibilities, risk decisions, documentation, and evidence are not controlled.

## Best practice

Use compliance to make security repeatable and provable. Use security risk to make compliance meaningful.

## Evidence

- risk-based control selection
- operating evidence
- audit trails
- effectiveness metrics
- corrective actions

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Security vs Compliance** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A company undergoes ISO 27001 surveillance audit and passes with zero nonconformities. Three months later, a misconfigured S3 bucket exposes customer data — the bucket was outside the vulnerability scanning scope, and access reviews had been approving all accounts without challenge. The audit evidence was complete and accurate, but the underlying security controls were ineffective. Compliance confirmed that processes existed and evidence was retained; it did not guarantee that risk was reduced. The corrective action expands scanning scope and redesigns access reviews to require challenge of unnecessary privileges — making both security and compliance stronger.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
