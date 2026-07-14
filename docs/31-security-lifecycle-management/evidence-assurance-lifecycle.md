---
title: Evidence and Assurance Lifecycle
description: How evidence is defined, collected, reviewed, reused, archived, and improved.
category: Security Lifecycle Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-lifecycle
  - isms
---

# Evidence and Assurance Lifecycle

Evidence proves that the ISMS and controls operate. Evidence should be designed into workflows instead of collected in panic before an audit.

```mermaid
flowchart LR
    A[Define Evidence Need] --> B[Generate in Workflow]
    B --> C[Store and Protect]
    C --> D[Review Quality]
    D --> E[Use for Audit / Assurance]
    E --> F[Retain or Dispose]
    F --> G[Improve Evidence Design]
    G --> A
```

## Example

For vulnerability management, evidence may include scanner coverage report, vulnerability ticket, risk acceptance record, patch change ticket, rescan result, dashboard trend, and management escalation for overdue critical findings.

## Best practices

- Define evidence source, owner, frequency, and retention.
- Prefer system-generated records over manual screenshots.
- Use evidence once and map it to multiple requirements.
- Protect evidence according to sensitivity.
- Review evidence quality before external audits.
- Archive old evidence according to retention rules.
- Feed weak evidence findings into continual improvement.

## Related chapters

- [Evidence Management Model](../19-isms-professional-toolkit/evidence-management-model.md)
- [Audit Evidence](../08-auditing/audit-evidence.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
