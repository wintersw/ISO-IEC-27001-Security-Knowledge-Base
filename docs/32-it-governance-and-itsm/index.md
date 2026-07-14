---
title: IT Governance and ITSM
description: IT governance and IT service management concepts for ISMS professionals.
category: IT Governance and ITSM
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - isms
---

# IT Governance and ITSM

IT governance and IT service management are essential to a practical ISMS. ISO/IEC 27001 defines the management system for information security, but many security controls are operated through IT governance and ITSM processes such as incident management, change enablement, configuration management, service continuity, supplier management, request fulfillment, and service reporting.

## Why this chapter was added

The existing project included references to ITIL, ISO/IEC 20000, and COBIT. What was missing was a practical explanation of **how IT governance and ITSM support the ISMS day to day**.

## Working distinction

| Concept | Main question |
|---|---|
| IT governance | Are IT and digital services directed, controlled, and monitored to support business objectives and risk appetite? |
| ITSM | Are IT services designed, delivered, supported, and improved in a reliable and controlled way? |
| ISMS | Are information security risks managed through a suitable, adequate, and effective management system? |

## How they connect

```mermaid
flowchart TD
    A[Business Objectives] --> B[IT Governance]
    B --> C[ITSM Operating Processes]
    C --> D[Security Controls]
    D --> E[ISMS Evidence and Assurance]
    E --> F[Management Review]
    F --> B
```

## Example

A production change is managed through ITSM change enablement. The ISMS uses that same change record as evidence for operational control, secure development, security testing, approval, rollback planning, and auditability. One workflow supports both service reliability and security assurance.

## Related chapters

- [ITIL, ISO/IEC 20000 and ISMS](../21-ethics-and-framework-relationships/itil-iso20000-and-isms.md)
- [COBIT and ISMS](../21-ethics-and-framework-relationships/cobit-and-isms.md)
- [Framework Relationship Map](../21-ethics-and-framework-relationships/framework-relationship-map.md)
- [ISMS Process Architecture](../24-pdf-source-integration/isms-process-architecture.md)
