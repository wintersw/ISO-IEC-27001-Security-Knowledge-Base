---
title: Software Supply Chain Security
description: Controls for source, dependencies, builds, provenance, artifacts, deployment, and supplier response.
category: Secure by Design
difficulty: Advanced
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
  - NIST SSDF 1.1
  - SLSA 1.2
tags:
  - secure-by-design
  - software-supply-chain
  - sbom
---

# Software Supply Chain Security

The software supply chain includes people, source repositories, third-party components, build services, package registries, artifacts, deployment systems, and update channels. A weakness in any link can make a trustworthy-looking release carry unauthorized code.

## Control the chain

- Protect source and build administration with phishing-resistant authentication, least privilege, review, protected branches, and logged emergency paths.
- Pin and verify dependencies, restrict registries, remove unused packages, monitor maintainers and ownership changes, and define response for abandoned components.
- Isolate and harden builds, use ephemeral workers, separate signing authority, and minimize network and secret access.
- Produce a software bill of materials (SBOM) in an interoperable format such as SPDX or CycloneDX, but do not confuse inventory with assurance.
- Generate verifiable provenance linking an artifact to source, builder, parameters, and dependencies; sign artifacts and verify before deployment.
- Use vulnerability-exploitability exchange (VEX) statements only with evidence and defined validity, not as blanket suppression.
- Protect update and rollback paths and rehearse revocation after signing-key, dependency, or build compromise.

Adopt maturity targets proportionate to risk. NIST's Secure Software Development Framework (SSDF) describes secure-development practices; Supply-chain Levels for Software Artifacts (SLSA) focuses on build integrity and provenance. SPDX and CycloneDX describe component data, while Sigstore provides open tooling for signing and transparency.

## Evidence

Retain repository protections, reviews, dependency policy and exceptions, SBOMs, provenance attestations, artifact verification logs, build configuration, signing access and rotation, release approvals, supplier notices, and compromise exercises.

## Practical example

A release pipeline builds from a protected commit on an isolated worker, generates an SPDX SBOM and SLSA provenance, signs the artifact through a short-lived identity, and admits it to production only after signature, provenance, policy, and vulnerability checks pass.

## Common mistakes

- generating an SBOM that is never stored, queried, or updated
- signing artifacts while leaving the build or signing identity broadly accessible
- trusting package names without verifying publisher, source, and registry
- blocking solely on a severity score without exposure, exploitability, and business context

## Sources

- [NIST SP 800-218, Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
- [SLSA specification](https://slsa.dev/spec/)
- [SPDX specification](https://spdx.dev/use/specifications/)
- [CycloneDX specification](https://cyclonedx.org/specification/overview/)
- [Sigstore documentation](https://docs.sigstore.dev/)
- [CISA Minimum Elements for an SBOM](https://www.cisa.gov/resources-tools/resources/minimum-elements-software-bill-materials-sbom)

## Related chapters

- [DevSecOps Guide](../16-implementation-guides/devsecops-guide.md)
- [Secrets Management](../07-security-domains/secrets-management.md)
- [Vulnerability Lifecycle](../31-security-lifecycle-management/vulnerability-lifecycle.md)
- [Threat Modeling](threat-modeling.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
