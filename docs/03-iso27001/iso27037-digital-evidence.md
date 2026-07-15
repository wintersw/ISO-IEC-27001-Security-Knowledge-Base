---
title: ISO/IEC 27037 Digital Evidence
description: Guidance for identifying, collecting, acquiring, and preserving digital evidence in support of ISO 27001 incident and forensic controls.
category: ISO 27000 Family
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - iso27000-family
---

# ISO/IEC 27037 Digital Evidence

ISO/IEC 27037:2012 provides guidance for the identification, collection, acquisition, and preservation of potential digital evidence. It supports incident response, forensic readiness, and internal investigations. The standard is currently published but under review; verify whether a revised edition has been released.

## Why this matters

Digital evidence is fragile. A powered-off device, a modified log, a re-imaged VM, or a cloud resource deleted without proper acquisition can destroy evidence needed for disciplinary action, legal proceedings, regulatory reporting, or insurance claims.

ISO/IEC 27037 provides guidance for preserving potential digital evidence during identification, collection, acquisition, and preservation. Later examination, analysis, interpretation, and presentation require additional procedures and may be governed by ISO/IEC 27041, ISO/IEC 27042, ISO/IEC 27043, applicable law, and the rules of the relevant forum.

## Scope and key concepts

ISO/IEC 27037 covers:

- **Identification:** Recognizing potential sources of digital evidence (endpoints, servers, cloud services, network devices, mobile devices, logs, email, messaging platforms).
- **Collection:** Gathering devices or data under controlled conditions that preserve integrity.
- **Acquisition:** Creating forensic copies (images) using validated tools and methods that do not alter the original.
- **Preservation:** Maintaining the integrity and chain of custody of evidence over time, including storage, access control, and handling records.

The standard is written primarily for traditional digital devices (servers, workstations, laptops, external storage). Cloud services and IoT systems present additional challenges that the 2012 edition does not address in detail; the cloud and IoT guidance in this page is modern project guidance, not content from the 2012 standard.

## Key principles

- **Minimize alteration:** Every action taken during evidence handling should minimize changes to the original data. Where change is unavoidable (e.g., live acquisition from a running system), document it fully.
- **Competence:** Personnel handling evidence must be trained and competent in forensic tools, procedures, and legal requirements.
- **Documentation:** Every action — who, what, when, where, why, and how — must be recorded. This forms the chain of custody.
- **Validation:** Tools and methods used for acquisition must be validated, and their use documented. Evidence analysis (examination and interpretation) is covered more directly by ISO/IEC 27042.
- **Repeatability:** A competent third party following the same documented process and using equivalent tools should obtain the same result.

## Practical implementation

1. **Define forensic readiness as part of incident management.** Identify potential evidence sources before an incident occurs. Know where logs are stored, how long they are retained, and who has access.

2. **Establish evidence-handling procedures** covering identification, collection, acquisition, storage, transfer, and disposal. Align with legal requirements in each jurisdiction where the organization operates.

3. **Acquire and validate forensic tools.** Maintain a list of approved acquisition tools. Validate tools before use and document tool versions and settings. For evidence analysis, refer to ISO/IEC 27042.

4. **Train incident responders in evidence handling.** First responders should know what not to do — powering off a running system, logging into a compromised account, or browsing files can alter evidence and break chain of custody.

5. **Document chain of custody.** Every transfer, access, or handling of evidence must be recorded: date, time, person, action, and reason. Use tamper-evident bags for physical media and access-controlled storage for digital evidence.

6. **Preserve cloud evidence.** Cloud environments present unique challenges — you cannot image a cloud server in the same way as a physical server. Plan for cloud-native acquisition: API snapshots, export of configurations, logs, and metadata from the cloud provider.

7. **Integrate with legal and HR processes.** Evidence collected for a security incident may later be used in criminal proceedings, civil litigation, regulatory investigations, or employee disciplinary actions. The same evidential standards should apply regardless of the initial purpose.

## Relationship to ISO/IEC 27001 controls

Digital-evidence handling most directly supports A.5.28 and can provide supporting evidence for other Annex A controls:

- **A.5.24 (Incident management):** Evidence handling is a core incident response capability.
- **A.5.25 (Assessment of information security events):** Proper evidence collection supports event triage and root cause analysis.
- **A.5.28 (Collection of evidence):** This control explicitly requires procedures for the identification, collection, acquisition, and preservation of evidence.
- **A.5.33 (Protection of records):** Evidence records must be protected from loss, destruction, falsification, and unauthorized access.
- **A.5.10 (Acceptable use, indirect relationship):** Acceptable-use rules can notify users about authorized monitoring and handling of organizational assets, subject to applicable law and policy.

## Practical example

A SaaS platform detects unusual API activity suggesting a data exfiltration attempt. Under its approved response and evidence-handling procedure, the incident team isolates affected systems while preserving identified volatile data, takes provider-supported snapshots, exports relevant SIEM and web-application-firewall logs before retention limits expire, records integrity information where appropriate, and documents every transfer and action. Qualified investigators later use the preserved material to identify the compromised API key, assess the apparent exfiltration path, and help determine the affected data. Legal and privacy specialists separately decide whether notification or referral thresholds are met. Following the documented process improves reliability and traceability but does not guarantee admissibility or freedom from challenge.

## Evidence to retain

- evidence-handling procedure
- chain-of-custody forms (completed)
- forensic acquisition logs (tool, version, hash values, timestamp)
- tool validation records
- evidence storage access logs
- disposal authorisation records

## Common mistakes

- Powering off a compromised system before capturing volatile data (memory, running processes, network connections).
- Using non-forensic tools or methods that write to the source disk, altering original evidence.
- Failing to document every action — an undocumented action creates a gap in chain of custody that can weaken or challenge the reliability of evidence in legal or disciplinary proceedings.
- Storing evidence without access controls or integrity verification (hash comparison).
- Treating cloud evidence the same as on-premise — cloud-native snapshots and API exports are not equivalent to disk images.
- Holding evidence indefinitely — define retention periods aligned with legal requirements and incident closure, then securely dispose.

## Related controls, clauses, templates, and checklists

- [ISO/IEC 27035 Incident Management](iso27035-incident-management.md)
- [Incident Response](../07-security-domains/incident-response.md)
- [ISO/IEC 27000 Family Detailed Guide](iso27000-family-detailed.md)

Project indexes: [clauses](clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
