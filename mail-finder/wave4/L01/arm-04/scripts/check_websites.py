#!/usr/bin/env python3
"""HTTP-check websites for arm-04 domain hygiene."""
import csv
import json
import re
import ssl
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "input.csv"

PARK_PATTERNS = [
    r"godaddy",
    r"domain is for sale",
    r"this domain",
    r"parked",
    r"sedoparking",
    r"hugedomains",
    r"buy this domain",
    r"coming soon",
    r"under construction",
    r"lander",
    r"squarespace",
    r"wix\.com",
    r"default page",
]

USER_AGENT = "MailFinder-Arm04/1.0 (+domain-hygiene; public research)"


def fetch_url(url: str, timeout: int = 20) -> dict:
    if not url.startswith("http"):
        url = "https://" + url
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*"},
        method="GET",
    )
    result = {
        "requested": url,
        "final_url": url,
        "status": None,
        "error": None,
        "parked": False,
        "title": "",
        "snippet": "",
    }
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            result["status"] = resp.status
            result["final_url"] = resp.geturl()
            body = resp.read(80000)
            try:
                text = body.decode("utf-8", errors="replace")
            except Exception:
                text = ""
            result["snippet"] = re.sub(r"\s+", " ", text[:4000])
            m = re.search(r"<title[^>]*>([^<]+)</title>", text, re.I)
            if m:
                result["title"] = m.group(1).strip()[:200]
            low = text.lower()
            for pat in PARK_PATTERNS:
                if re.search(pat, low):
                    result["parked"] = True
                    break
    except urllib.error.HTTPError as e:
        result["status"] = e.code
        result["error"] = str(e)
        try:
            body = e.read(20000)
            text = body.decode("utf-8", errors="replace")
            result["snippet"] = re.sub(r"\s+", " ", text[:2000])
        except Exception:
            pass
    except Exception as e:
        result["error"] = str(e)
        if "NXDOMAIN" in str(e) or "Name or service not known" in str(e):
            result["status"] = "NXDOMAIN"
    return result


def main():
    rows = list(csv.DictReader(INPUT.open()))
    checks = {}
    for row in rows:
        wid = row["Monday_item_id"]
        website = (row.get("Website") or "").strip()
        domain = (row.get("Domain") or "").strip()
        urls_to_try = []
        if website:
            urls_to_try.append(website)
        elif domain:
            urls_to_try.append(f"https://{domain}")
            urls_to_try.append(f"http://{domain}")
        checked = []
        primary = None
        for u in urls_to_try:
            if u in [c.get("requested") for c in checked]:
                continue
            r = fetch_url(u)
            checked.append(r)
            if primary is None and (r.get("status") == 200 or r.get("status") in (301, 302, 303, 307, 308)):
                primary = r
        checks[wid] = {
            "name": row["Name"],
            "firm": row.get("Firm") or "",
            "website": website,
            "domain": domain,
            "checks": checked,
            "primary": primary,
        }
        print(json.dumps({"id": wid, "name": row["Name"], "checks": len(checked), "status": primary.get("status") if primary else None, "final": primary.get("final_url") if primary else None, "parked": primary.get("parked") if primary else None}), flush=True)

    (ROOT / "scripts" / "http_checks.json").write_text(json.dumps(checks, indent=2))


if __name__ == "__main__":
    main()
