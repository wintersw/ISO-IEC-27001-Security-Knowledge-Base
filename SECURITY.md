# Security Policy

## Reporting a vulnerability

Do not publish exploit details, credentials, personal data, or a working proof of concept in a public issue. Report a repository, website, build-pipeline, or dependency vulnerability through [GitHub private vulnerability reporting](https://github.com/wintersw/ISO-IEC-27001-Security-Knowledge-Base/security/advisories/new). Include the affected component, reproducible impact, and a safe way to validate the report.

Documentation corrections that do not expose a vulnerability can use a normal issue or pull request.

## Supported version

The `main` branch and the currently published GitHub Pages site are supported. Historical commits and third-party forks are not maintained by this project.

## Dependency policy

Continuous integration fails on high or critical npm advisories. Moderate findings are reviewed for reachability and available non-breaking remediation. Development-server dependencies are not shipped as executable server software in the static GitHub Pages output, but they remain part of the contributor threat model and must be updated when upstream packages provide a compatible fix.

Do not apply `npm audit fix --force` without reviewing the proposed major-version changes, site behavior, and generated lockfile. Run `npm audit --audit-level=high`, the content and link validators, and a production build after dependency changes.
