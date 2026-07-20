---
title: Container and Cloud-Native Security
description: Securing containers, Kubernetes, and infrastructure as code under ISO 27001.
category: Security Domains
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Container and Cloud-Native Security

Cloud-native applications are built from containers, orchestrated by platforms such as Kubernetes (K8s), and provisioned through infrastructure as code (IaC). This model changes where controls live: security is defined in images, manifests, and pipelines rather than in long-lived servers. The ISMS still applies — the evidence just moves into code and registries.

## The container supply chain

Security spans the whole path from source to running workload:

1. **Base images** — use minimal, trusted, and regularly updated images.
2. **Build** — scan images for vulnerabilities and generate a software bill of materials (SBOM).
3. **Registry** — sign images and restrict who can push and pull.
4. **Admission** — allow only signed, scanned images to run; block privileged or misconfigured workloads.
5. **Runtime** — monitor container behavior and enforce least privilege.

## Kubernetes security essentials

- **Role-based access control (RBAC).** Grant least privilege to users and service accounts.
- **Network policies.** Default-deny pod-to-pod traffic and allow only required flows.
- **Secrets management.** Store secrets outside manifests, integrate with a [key management](key-management.md) service, and avoid plaintext in Git.
- **Pod security.** Restrict privileged containers, host mounts, and root execution.
- **Isolation.** Use namespaces and, where needed, separate clusters for differing trust levels.

## Infrastructure as code

IaC (for example, Terraform, CloudFormation, or Kubernetes manifests) defines infrastructure in version-controlled files:

- Scan IaC for misconfigurations before deployment (policy as code).
- Require peer review and prevent direct changes to production ("no click-ops").
- Keep state files and provisioning credentials protected.
- Treat drift between declared and actual state as a control failure.

## Core capabilities

- image vulnerability scanning and SBOM generation
- image signing and admission control
- Kubernetes RBAC and network policy
- secrets management integration
- runtime detection for containers
- IaC and policy-as-code scanning in the pipeline

## Evidence

- image scan and signing results
- admission-control policy and denied-deployment logs
- Kubernetes RBAC and network-policy definitions
- IaC scan reports and pull-request reviews
- runtime alerts and investigations

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Relevant Annex A controls include A.8.9 (configuration management), A.8.8 (technical vulnerability management), A.8.25–A.8.29 (secure development and testing), A.8.31 (separation of environments), and A.8.15/A.8.16 (logging and monitoring).
- **Implementation guidance:** Shift controls left into pipelines: scan images and IaC on every build, enforce signed-image admission, and manage cluster access with RBAC. Record the [shared-responsibility](cloud-security.md) split with the cloud provider.
- **Best practice:** Make the pipeline the control point. If an insecure image cannot be built or admitted, the control is preventive and self-evidencing rather than dependent on manual review. See the [DevSecOps guide](../16-implementation-guides/devsecops-guide.md).

## Practical example

A SaaS team builds images from a hardened base, fails the pipeline on critical vulnerabilities, signs passing images, and configures the cluster to admit only signed images. Terraform changes require review and pass a policy scan that blocks public storage buckets. Runtime monitoring alerts on containers that spawn unexpected shells.

## Related chapters

- [Cloud Security](cloud-security.md)
- [Application Security](application-security.md)
- [DevSecOps Guide](../16-implementation-guides/devsecops-guide.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
