#!/usr/bin/env python3
"""Check unique external documentation links with retries and GET fallback."""

from __future__ import annotations

import concurrent.futures
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r'https?://[^\s)>"`]+')
USER_AGENT = "ISO-27001-KB-link-check/1.0 (+https://github.com/wintersw/ISO-IEC-27001-Security-Knowledge-Base)"
ALLOW_BLOCKED = {
    "csrc.nist.gov": {403, 404},
    "www.bsi.bund.de": {400, 403, 404},
    "www.cisa.gov": {403},
    "www.iec.ch": {403},
}
TIMEOUT = 20


def urls() -> list[str]:
    found: set[str] = set()
    for path in [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]:
        text = path.read_text(encoding="utf-8-sig")
        found.update(match.rstrip(".,;:") for match in URL_RE.findall(text))
    return sorted(found)


def request(url: str, method: str) -> tuple[int, str]:
    headers = {"User-Agent": USER_AGENT, "Accept": "text/html,application/pdf,*/*"}
    if method == "GET":
        headers["Range"] = "bytes=0-1023"
    req = urllib.request.Request(url, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
        return response.status, response.geturl()


def check(url: str) -> tuple[str, str]:
    last = "unknown error"
    last_status: int | None = None
    for attempt in range(3):
        for method in ("HEAD", "GET"):
            try:
                status, final_url = request(url, method)
                if status < 400:
                    return "OK", f"{status}\t{url}\t{final_url}"
                last = f"HTTP {status}"
                last_status = status
            except urllib.error.HTTPError as exc:
                last = f"HTTP {exc.code}"
                last_status = exc.code
                if exc.code not in {400, 403, 405, 429, 500, 502, 503, 504}:
                    break
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                last = str(exc)
        if attempt < 2:
            time.sleep(1 + attempt)
    host = urllib.parse.urlparse(url).hostname or ""
    if last_status in ALLOW_BLOCKED.get(host, set()):
        return "WARN", f"publisher returned bot-blocking HTTP {last_status}\t{url}"
    return "FAIL", f"{last}\t{url}"


def main() -> int:
    targets = urls()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, targets))
    failures = [message for status, message in results if status == "FAIL"]
    warnings = [message for status, message in results if status == "WARN"]
    for message in warnings:
        print(f"WARN\t{message}")
    if failures:
        print(f"External-link validation failed: {len(failures)} of {len(targets)} links")
        for message in failures:
            print(f"FAIL\t{message}")
        return 1
    print(f"External-link validation passed: {len(targets)} links ({len(warnings)} allowlisted warning(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
