#!/usr/bin/env python3
"""Fail fast on structural errors in the Markdown knowledge base."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
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
)


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
        if path.parent.name == "includes":
            continue
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

    config_path = ROOT / "docusaurus.config.js"
    if not config_path.exists():
        errors.append("docusaurus.config.js: missing Docusaurus configuration")
    else:
        config = config_path.read_text(encoding="utf-8")
        if "example.invalid" in config:
            errors.append("docusaurus.config.js: placeholder site URL remains")

    if errors:
        print(f"Content validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    include_count = len(paths) - page_count
    print(
        f"Content validation passed: {page_count} pages, {include_count} include file(s), "
        f"{len(titles)} unique titles, 93 Annex A links."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
