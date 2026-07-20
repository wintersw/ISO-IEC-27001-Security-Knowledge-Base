#!/usr/bin/env python3
"""Regenerate MANIFEST.md from the set of Git-tracked files.

Keeps the file manifest in sync with the repository so `npm run validate`
can detect drift. Run via `npm run manifest`.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST.md"


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    files = sorted({line.strip() for line in result.stdout.splitlines() if line.strip()})
    return files


def render(files: list[str]) -> str:
    lines = ["# File Manifest", ""]
    lines.extend(f"- `{path}`" for path in files)
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    try:
        files = tracked_files()
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"Failed to list tracked files: {exc}")
        return 1
    MANIFEST.write_text(render(files), encoding="utf-8")
    print(f"Wrote {MANIFEST.relative_to(ROOT)} with {len(files)} entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
