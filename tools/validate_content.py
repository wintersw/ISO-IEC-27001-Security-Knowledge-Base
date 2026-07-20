#!/usr/bin/env python3
"""Fail fast on structural errors in the Markdown knowledge base."""

from __future__ import annotations

import re
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
H1_RE = re.compile(r"^# (.+)$", re.MULTILINE)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
FORBIDDEN = (
    "example.invalid",
    "newly uploaded pdf",
    "chat-planned architecture",
    "the owner defines its trigger and scope, uses authoritative sources",
    "intent documents are insufficient on their own; retain scoped operating records",
    "a risk owner adapts this scenario to a real service",
    "/final?null=",
)
ALLOWED_CATEGORIES = {
    "AI Governance and Security", "Annex A", "Auditing", "Best Practices",
    "BSI / ISMS Enhancement", "Checklists", "Continual Improvement",
    "Cybersecurity Governance", "Data Security Governance", "Emerging Data Security Trends",
    "End-to-End Case Studies", "Ethics and Framework Relationships", "Examples", "FAQ",
    "Fundamentals", "Getting Started", "Governance, Risk, and Compliance", "Guided Labs",
    "Implementation", "Incident and Data Breach Management", "ISMS", "ISMS Documentation Templates",
    "ISMS Professional Toolkit", "ISO 27000 Family", "ISO/IEC 27001", "IT Governance and ITSM",
    "Labs", "Mappings", "PDF Source Integration", "Privacy Engineering and Data Protection",
    "Reference", "Risk Management", "Secure by Design", "Security Domains",
    "Security Lifecycle Management", "Source Research and Mapping", "Templates",
    "Worked Risk Scenarios", "Zero Trust and Data-Centric Security",
}


def front_matter(path: Path, text: str) -> dict:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML front matter")
    data = yaml.safe_load(text[4:end])
    if not isinstance(data, dict):
        raise ValueError("front matter is not a mapping")
    return data


def local_target(path: Path, raw: str) -> Path | None:
    target = raw.strip().split(maxsplit=1)[0].strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    target = unquote(target.split("#", 1)[0].split("?", 1)[0])
    resolved = (path.parent / target).resolve()
    if resolved.is_dir():
        resolved = resolved / "index.md"
    return resolved


def main() -> int:
    errors: list[str] = []
    titles: dict[str, list[Path]] = defaultdict(list)
    paths = sorted(DOCS.rglob("*.md"))
    page_count = 0

    for path in paths:
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8-sig")
        page_count += 1
        try:
            meta = front_matter(path, text)
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f"{rel}: {exc}")
            continue

        title = meta.get("title")
        description = meta.get("description")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{rel}: missing string title")
        else:
            titles[title.strip()].append(path)
        if not isinstance(description, str) or not description.strip():
            errors.append(f"{rel}: missing string description")
        category = meta.get("category")
        if not isinstance(category, str) or not category.strip():
            errors.append(f"{rel}: missing string category")
        elif category not in ALLOWED_CATEGORIES:
            errors.append(f"{rel}: unknown category {category!r}")
        difficulty = meta.get("difficulty")
        if difficulty not in {"Beginner", "Intermediate", "Advanced"}:
            errors.append(f"{rel}: difficulty must be Beginner, Intermediate, or Advanced")
        tags = meta.get("tags")
        if not isinstance(tags, list) or not tags or not all(isinstance(t, str) and t.strip() for t in tags):
            errors.append(f"{rel}: missing non-empty tags list")
        applies_to = meta.get("applies_to")
        if not isinstance(applies_to, list) or not applies_to or not all(
            isinstance(value, str) and value.strip() for value in applies_to
        ):
            errors.append(f"{rel}: missing non-empty applies_to list")

        reviewed_on = meta.get("reviewed_on")
        if reviewed_on is not None:
            if isinstance(reviewed_on, date):
                reviewed_date = reviewed_on
            elif isinstance(reviewed_on, str):
                try:
                    reviewed_date = date.fromisoformat(reviewed_on)
                except ValueError:
                    reviewed_date = None
            else:
                reviewed_date = None
            if reviewed_date is None:
                errors.append(f"{rel}: reviewed_on must be an ISO date (YYYY-MM-DD)")
            elif reviewed_date > date.today():
                errors.append(f"{rel}: reviewed_on cannot be in the future")

        is_mapping = rel.parts[:2] == ("docs", "17-mappings") and path.name != "index.md"
        is_reference_register = rel.as_posix() in {
            "docs/15-reference/references.md",
            "docs/30-source-research-and-mapping/external-reference-register.md",
        }
        if (is_mapping or is_reference_register) and reviewed_on is None:
            errors.append(f"{rel}: edition-sensitive page requires reviewed_on")
        if is_mapping and "\n## Sources\n" not in text:
            errors.append(f"{rel}: mapping page requires a Sources section")

        prose = FENCE_RE.sub("", text)
        headings = H1_RE.findall(prose)
        if len(headings) != 1:
            errors.append(f"{rel}: expected one H1, found {len(headings)}")
        elif isinstance(title, str) and headings[0].strip() != title.strip():
            errors.append(f"{rel}: H1 does not match title")

        lowered = text.lower()
        for marker in FORBIDDEN:
            if marker in lowered:
                errors.append(f"{rel}: forbidden stale marker {marker!r}")

        for raw in LINK_RE.findall(prose):
            target = local_target(path, raw)
            if target is not None and not target.exists():
                errors.append(f"{rel}: broken local link {raw!r}")

    for title, occurrences in sorted(titles.items()):
        if len(occurrences) > 1:
            joined = ", ".join(str(p.relative_to(ROOT)) for p in occurrences)
            errors.append(f"duplicate title {title!r}: {joined}")

    annex = (DOCS / "06-annex-a" / "index.md").read_text(encoding="utf-8-sig")
    control_links = re.findall(r"\]\((?:organizational|people|physical|technological)/a(?:5|6|7|8)-[^)]+\.md\)", annex)
    if len(control_links) != 93:
        errors.append(f"docs/06-annex-a/index.md: expected 93 control links, found {len(control_links)}")

    for name in ("README.md", "CONTRIBUTING.md", "CHANGELOG.md"):
        root_doc = ROOT / name
        if not root_doc.exists():
            continue
        root_text = root_doc.read_text(encoding="utf-8-sig")
        root_prose = FENCE_RE.sub("", root_text)
        for raw in LINK_RE.findall(root_prose):
            target = local_target(root_doc, raw)
            if target is not None and not target.exists():
                errors.append(f"{name}: broken local link {raw!r}")

    manifest_path = ROOT / "MANIFEST.md"
    if not manifest_path.exists():
        errors.append("MANIFEST.md: missing file manifest")
    else:
        listed = set(re.findall(r"`([^`]+)`", manifest_path.read_text(encoding="utf-8-sig")))
        try:
            result = subprocess.run(
                ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
            )
            expected = {line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()}
            missing = sorted(expected - listed)
            stale = sorted(listed - expected)
            for item in missing:
                errors.append(f"MANIFEST.md: missing entry for {item} (run npm run manifest)")
            for item in stale:
                errors.append(f"MANIFEST.md: stale entry for {item} (run npm run manifest)")
        except (subprocess.CalledProcessError, FileNotFoundError) as exc:
            errors.append(f"MANIFEST.md: could not enumerate repository files: {exc}")

    config_path = ROOT / "docusaurus.config.js"
    if not config_path.exists():
        errors.append("docusaurus.config.js: missing Docusaurus configuration")
    else:
        config = config_path.read_text(encoding="utf-8")
        if "example.invalid" in config:
            errors.append("docusaurus.config.js: placeholder site URL remains")
        for required in ("sitemap.xml", "onBrokenAnchors: 'throw'"):
            if required not in config:
                errors.append(f"docusaurus.config.js: missing required search/index integrity setting {required!r}")

    package_path = ROOT / "package.json"
    if not package_path.exists() or '"@docusaurus/plugin-sitemap"' not in package_path.read_text(encoding="utf-8"):
        errors.append("package.json: official @docusaurus/plugin-sitemap dependency is required")

    if errors:
        print(f"Content validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Content validation passed: {page_count} pages, {len(titles)} unique titles, "
        "93 Annex A links, controlled metadata, sources, and manifest."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
