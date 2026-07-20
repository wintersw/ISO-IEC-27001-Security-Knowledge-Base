# Contributing

## Editorial principles

Every page should answer four questions:

1. What is this?
2. Why does it matter?
3. How should a security team implement or operate it?
4. How can the organization demonstrate that it works?

## Requirements

Every article should:

- Explain concepts in plain language before introducing specialist terminology.
- Distinguish clearly between ISO requirements, implementation guidance, and best practice.
- Include practical examples that show how the topic is applied in real organizations.
- Identify evidence to retain so readers can demonstrate operation and control effectiveness.
- Link related clauses, controls, templates, and checklists instead of repeating content in multiple places.
- Avoid reproducing copyrighted standard text; summarize and contextualize the topic instead.
- Use vendor-neutral language unless product names are clearly presented as examples.
- Write the full term before an abbreviation on first use when practical, and add every project abbreviation to the [abbreviation list](docs/15-reference/abbreviations.md).
- Follow the [terminology governance rules](docs/15-reference/terminology-governance.md): validate terminology against the current applicable source and edition, then explain it in original plain language without copying licensed definitions, notes, examples, tables, or diagrams.
- Follow the [editorial style guide](docs/15-reference/editorial-style-guide.md) and [accessibility rules](docs/15-reference/accessibility-and-inclusive-documentation.md).
- Use primary sources for version-sensitive, legal, protocol, cryptographic, and quantitative claims; include a `## Sources` section and `reviewed_on: YYYY-MM-DD` when currency matters.
- Complete `title`, `description`, `category`, `difficulty`, `applies_to`, and `tags` front matter. Use `reviewed_on` for edition-sensitive content.

A good article should answer what the topic is, why it matters, how it is implemented, and how the organization can demonstrate that it works.

## File naming

Use lowercase hyphenated filenames. Annex A files use identifiers such as `a5-01-policies-for-information-security.md`.

## Local checks

Run `npm run validate`, `npm run validate:links`, and `npm run build` before opening a pull request. Run `npm run manifest` after adding, deleting, or renaming files.
