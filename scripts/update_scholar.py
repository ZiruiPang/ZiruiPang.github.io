#!/usr/bin/env python3
"""Fetch Google Scholar metrics for the sidebar and write _data/scholar.json.

If Google blocks the request or the page markup changes, the existing JSON is
kept untouched so the site never loses its last known numbers.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

SCHOLAR_ID = "L9GRttsAAAAJ"
OUTPUT = Path(__file__).resolve().parent.parent / "_data" / "scholar.json"
PROFILE_URL = (
    f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en&cstart=0&pagesize=100"
)
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def log(message: str) -> None:
    print(message, file=sys.stderr)


def fetch_html(url: str) -> str | None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset, errors="replace")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        log(f"warning: fetch failed: {exc}")
        return None


def strip_tags(html: str) -> str:
    return unescape(re.sub(r"<[^>]+>", "", html)).strip()


def parse_int(text: str) -> int | None:
    digits = re.sub(r"[^\d]", "", text)
    return int(digits) if digits else None


def looks_blocked(html: str) -> bool:
    lower = html.lower()
    if "unusual traffic" in lower or "captcha" in lower:
        return True
    return "gsc_rsb_std" not in lower and "gsc_a_at" not in lower


def parse_metrics(html: str) -> dict[str, int] | None:
    table = re.search(
        r'<table[^>]*id="gsc_rsb_st"[^>]*>(.*?)</table>',
        html,
        re.DOTALL | re.IGNORECASE,
    )
    if not table:
        return None

    metrics: dict[str, int] = {}
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", table.group(1), re.DOTALL | re.IGNORECASE):
        cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.DOTALL | re.IGNORECASE)
        if len(cells) < 2:
            continue
        label = strip_tags(cells[0]).lower()
        value = parse_int(strip_tags(cells[1]))
        since = parse_int(strip_tags(cells[2])) if len(cells) > 2 else None
        if value is None:
            continue
        if "citation" in label:
            metrics["citations"] = value
            if since is not None:
                metrics["citations_since_2021"] = since
        elif "h-index" in label:
            metrics["h_index"] = value
        elif "i10" in label:
            metrics["i10_index"] = value

    if not {"citations", "h_index", "i10_index"}.issubset(metrics):
        return None
    if metrics["citations"] == 0 and metrics["h_index"] == 0:
        return None
    return metrics


def parse_year_graph(html: str) -> list[dict[str, int]]:
    years = [
        int(match)
        for match in re.findall(r'gsc_g_t[^>]*>\s*(\d{4})', html, re.IGNORECASE)
    ]
    counts = [
        parse_int(strip_tags(match))
        for match in re.findall(
            r'class=["\']gsc_g_al["\'][^>]*>([^<]*)<',
            html,
            re.IGNORECASE,
        )
    ]
    return [
        {"year": year, "citations": counts[index]}
        for index, year in enumerate(years)
        if index < len(counts) and counts[index] is not None
    ]


def parse_papers(html: str) -> list[dict[str, int | str]]:
    papers: list[dict[str, int | str]] = []
    for row in re.finditer(
        r'<tr class="gsc_a_tr"[^>]*>(.*?)</tr>',
        html,
        re.DOTALL | re.IGNORECASE,
    ):
        chunk = row.group(1)
        title_match = re.search(
            r'class="gsc_a_at"[^>]*>(.*?)</a>',
            chunk,
            re.DOTALL | re.IGNORECASE,
        )
        if not title_match:
            continue
        citations_match = re.search(
            r'class="gsc_a_ac[^"]*"[^>]*>(.*?)</a>',
            chunk,
            re.DOTALL | re.IGNORECASE,
        )
        year_match = re.search(
            r'class="gsc_a_y"[^>]*><span[^>]*>(\d{4})</span>',
            chunk,
            re.IGNORECASE,
        )
        id_match = re.search(r"citation_for_view=([A-Za-z0-9_:-]+)", chunk)

        entry: dict[str, int | str] = {
            "id": id_match.group(1) if id_match else "",
            "title": strip_tags(title_match.group(1)),
            "citations": (
                parse_int(strip_tags(citations_match.group(1)))
                if citations_match
                else 0
            )
            or 0,
        }
        if year_match:
            entry["year"] = int(year_match.group(1))
        papers.append(entry)
    return papers


def build_payload(html: str) -> dict | None:
    if looks_blocked(html):
        log("warning: Google Scholar page looks blocked")
        return None

    metrics = parse_metrics(html)
    papers = parse_papers(html)
    if not metrics or not papers:
        log("warning: could not parse metrics or publications")
        return None

    payload: dict = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "scholar_id": SCHOLAR_ID,
        **metrics,
        "year_graph": parse_year_graph(html),
        "papers": papers,
    }
    payload.setdefault("citations_since_2021", payload["citations"])
    return payload


def main() -> int:
    html = fetch_html(PROFILE_URL)
    if not html:
        log("warning: keeping existing scholar.json")
        return 0

    payload = build_payload(html)
    if not payload:
        log("warning: keeping existing scholar.json")
        return 0

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    log(f"updated {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
