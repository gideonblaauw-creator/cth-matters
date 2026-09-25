#!/usr/bin/env python3
"""Wave2 Wayback CDX arm — parse historical team/about pages for name+mailto."""
from __future__ import annotations

import csv
import json
import re
import time
import urllib.parse
import urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_DIR = ROOT / "html"
INPUT = ROOT / "input.csv"

UA = "Mozilla/5.0 (compatible; TeclogiMailFinder-Wave2Wayback/1.0; +research)"
PATH_KEYWORDS = ("team", "about", "people", "leadership", "contact", "our-team", "equipe", "equipo")

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")

GENERIC_LOCAL = re.compile(
    r"^(info|contact|hello|support|sales|team|careers|jobs|press|media|"
    r"investors?|invest|ir|privacy|legal|admin|office|enquiries|inquiry|"
    r"partnerships?|marketing|hr|recruitment|feedback|webmaster|post|mail|"
    r"impact|pitchdeck|comms|ventures|hol[aá]|info\.|general|service|"
    r"infocolombia|speed|investors|info\.rbvc|info\.ramesohl)$",
    re.I,
)


def fetch(url: str, timeout: int = 45) -> tuple[int | None, bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read(), r.headers.get("Content-Type", "")
    except Exception as e:
        return None, b"", str(e)


def decode_cfemail(hex_str: str) -> str:
    try:
        r = int(hex_str[:2], 16)
        return "".join(chr(int(hex_str[i : i + 2], 16) ^ r) for i in range(2, len(hex_str), 2))
    except Exception:
        return ""


def is_generic_email(email: str) -> bool:
    local = email.split("@")[0].lower()
    if GENERIC_LOCAL.match(local):
        return True
    if local.startswith("info") and len(local) <= 12:
        return True
    return False


def name_tokens(full_name: str) -> list[str]:
    if not full_name or full_name.strip() in ("CrossBoundary", "Rabobank Partnerships"):
        return []
    # strip firm suffixes in name field
    n = re.sub(r"\s+", " ", full_name.strip())
    parts = [p for p in re.split(r"[\s,.]+", n) if len(p) > 2 and p.lower() not in ("de", "del", "la", "le", "von", "van", "di")]
    return [p.lower() for p in parts]


def path_is_promising(url: str) -> bool:
    u = url.lower()
    return any(k in u for k in PATH_KEYWORDS)


def cdx_query(domain: str, limit: int = 80) -> list[dict]:
    """CDX for domain; keep rows whose original URL matches team/about paths."""
    q = urllib.parse.urlencode(
        {
            "url": f"{domain}/*",
            "output": "json",
            "filter": "statuscode:200",
            "collapse": "urlkey",
            "limit": str(limit),
        }
    )
    url = f"https://web.archive.org/cdx/search/cdx?{q}"
    st, body, _ = fetch(url, timeout=60)
    if st != 200:
        return []
    try:
        data = json.loads(body.decode())
    except Exception:
        return []
    if not data:
        return []
    header, *rows = data
    out = []
    for row in rows:
        rec = dict(zip(header, row))
        orig = rec.get("original", "")
        if path_is_promising(orig):
            out.append(rec)
    return out


def extract_emails(html: str) -> set[str]:
    emails: set[str] = set()
    for m in re.finditer(r'href\s*=\s*["\']mailto:([^"\'?>\s]+)', html, re.I):
        emails.add(unescape(urllib.parse.unquote(m.group(1).strip())))
    for m in re.finditer(r'data-cfemail=["\']([0-9a-fA-F]+)["\']', html):
        dec = decode_cfemail(m.group(1))
        if dec and "@" in dec:
            emails.add(dec)
    for m in EMAIL_RE.findall(html):
        if not m.lower().endswith((".png", ".jpg", ".gif", ".webp", ".css", ".js")):
            emails.add(m)
    return {e.strip().lower() for e in emails if "@" in e}


def name_near_email(html: str, name: str, email: str, window: int = 2500) -> bool:
    tokens = name_tokens(name)
    if not tokens:
        return False
    html_l = html.lower()
    email_l = email.lower()
    idx = 0
    while True:
        pos = html_l.find(email_l, idx)
        if pos < 0:
            break
        chunk = html_l[max(0, pos - window) : pos + window]
        if all(t in chunk for t in tokens[:2]):  # first + last (or two main tokens)
            return True
        if len(tokens) == 1 and tokens[0] in chunk:
            return True
        idx = pos + 1
    return False


def mailto_anchor_names(html: str, email: str) -> list[str]:
    """Anchor text for mailto links matching email."""
    names = []
    pat = re.compile(
        rf'<a[^>]+href\s*=\s*["\']mailto:{re.escape(email)}[^"\']*["\'][^>]*>(.*?)</a>',
        re.I | re.S,
    )
    for m in pat.finditer(html):
        text = re.sub(r"<[^>]+>", " ", m.group(1))
        text = unescape(re.sub(r"\s+", " ", text)).strip()
        if text:
            names.append(text)
    return names


def name_matches_anchor(name: str, anchor: str) -> bool:
    tokens = name_tokens(name)
    if not tokens:
        return False
    a = anchor.lower()
    return all(t in a for t in tokens[: min(2, len(tokens))])


def analyze_snapshot(html: str, name: str, domain: str) -> dict | None:
    """Return best FOUND candidate or None."""
    if len(html) < 500:
        return None
    emails = extract_emails(html)
    firm_emails = [e for e in emails if domain.lower() in e.split("@")[-1] or e.split("@")[-1].endswith(domain.lower())]
    # also allow subdomains of domain root
    dom_root = domain.lower().split(".")[-2] + "." + domain.lower().split(".")[-1] if "." in domain else domain.lower()
    firm_emails = [e for e in emails if dom_root in e.split("@")[-1]]

    for email in sorted(firm_emails):
        if is_generic_email(email):
            continue
        anchors = mailto_anchor_names(html, email)
        for anc in anchors:
            if name_matches_anchor(name, anc):
                return {"email": email, "reason": f"mailto anchor '{anc}' co-tagged with address"}
        if name_near_email(html, name, email):
            return {"email": email, "reason": "name tokens co-occur within HTML window of email"}
    return None


def wayback_snapshot_url(timestamp: str, original: str) -> str:
    return f"https://web.archive.org/web/{timestamp}id_/{original}"


def process_seat(row: dict) -> dict:
    mid = row["Monday_item_id"]
    name = row.get("Name", "").strip()
    firm = row.get("Firm", "").strip()
    domain = row.get("Domain", "").strip().lower().replace("https://", "").replace("http://", "").strip("/")
    priority = row.get("Priority", "P2")
    prior_checked = row.get("Checked_URLs", "") or row.get("prior_notes", "")

    cdx_urls = []
    checked: list[str] = [
        f"https://web.archive.org/cdx/search/cdx?url={urllib.parse.quote(domain + '/*')}&output=json&filter=statuscode:200"
    ]
    snapshots_tried: list[str] = []

    cdx_rows = cdx_query(domain, limit=120)
    # prefer newest timestamps first
    cdx_rows.sort(key=lambda r: r.get("timestamp", ""), reverse=True)

    found = None
    source_url = ""
    notes_parts = []
    saved_html = ""

    for rec in cdx_rows[:25]:
        orig = rec.get("original", "")
        ts = rec.get("timestamp", "")
        if not orig or not ts:
            continue
        snap = wayback_snapshot_url(ts, orig)
        snapshots_tried.append(snap)
        st, body, ct = fetch(snap)
        if st != 200 or not body:
            continue
        try:
            html = body.decode("utf-8", errors="replace")
        except Exception:
            html = body.decode("latin-1", errors="replace")

        if len(html) < 800 and "loading" in html.lower()[:2000]:
            notes_parts.append(f"truncated/shell at {snap}")
            continue

        slug = re.sub(r"[^a-zA-Z0-9._-]+", "_", f"{domain}_{ts}_{orig}")[:120]
        saved_html = slug + ".html"
        (HTML_DIR / saved_html).write_text(html[:2_000_000], encoding="utf-8", errors="replace")

        hit = analyze_snapshot(html, name, domain)
        if hit:
            found = hit
            source_url = snap
            break

        # only generics on this snapshot?
        emails = extract_emails(html)
        dom_root = domain.split(".")[-2] + "." + domain.split(".")[-1] if domain.count(".") >= 1 else domain
        firm_em = [e for e in emails if dom_root in e.split("@")[-1]]
        if firm_em and all(is_generic_email(e) for e in firm_em):
            notes_parts.append(f"generics only on {orig} ({ts}): {', '.join(sorted(firm_em)[:5])}")
            # per method: if snapshot yields only generics, mark EMPTY and stop for this path exploration
            # but continue other CDX URLs until we've checked promising paths

    if not snapshots_tried and cdx_rows:
        notes_parts.append("CDX had rows but no successful snapshot fetch")
    elif not cdx_rows:
        notes_parts.append("CDX returned no 200 snapshots for team/about/contact paths")

    checked.extend(snapshots_tried[:12])

    if found:
        status = "FOUND"
        conf = "HIGH"
        email = found["email"]
        etype = "work"
        notes = found["reason"] + f"; Wayback CDX on {domain}."
        method = "wayback_cdx"
    elif name and "linkedin" in (row.get("prior_notes") or "").lower() and "only" in (row.get("prior_notes") or "").lower():
        status = "HOLD"
        conf = "HIGH"
        email = etype = ""
        notes = (row.get("prior_notes") or "")[:400]
        if not notes:
            notes = "LinkedIn-primary; no Wayback name+person email."
        notes += " Wayback CDX: no person mailto on archived team/about paths."
        method = "wayback_cdx"
    else:
        status = "EMPTY"
        conf = "HIGH"
        email = etype = ""
        source_url = ""
        uniq_notes = "; ".join(dict.fromkeys(notes_parts)) if notes_parts else (row.get("prior_notes") or "")[:350]
        notes = (uniq_notes + " Wayback CDX arm: no citation-grade name+person@ on archived paths.").strip()
        method = "wayback_cdx"

    return {
        "Monday_item_id": mid,
        "Name": name,
        "Firm": firm,
        "Domain": domain,
        "Priority": priority,
        "Email": email,
        "Email_type": etype,
        "Confidence": conf,
        "Source_URL": source_url,
        "Checked_URLs": " | ".join(checked[:15]),
        "Status": status,
        "Notes": notes[:900],
        "Method": method,
        "_saved": saved_html,
    }


def main():
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    seats = []
    with INPUT.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            seats.append(row)

    results = []
    for i, row in enumerate(seats):
        print(f"[{i+1}/{len(seats)}] {row.get('Name')} @ {row.get('Domain')}", flush=True)
        results.append(process_seat(row))
        time.sleep(0.4)

    header = [
        "Monday_item_id",
        "Name",
        "Firm",
        "Domain",
        "Priority",
        "Email",
        "Email_type",
        "Confidence",
        "Source_URL",
        "Checked_URLs",
        "Status",
        "Notes",
        "Method",
    ]
    out_rows = [{k: r[k] for k in header} for r in results]

    with (ROOT / "results.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        w.writerows(out_rows)

    found = [r for r in out_rows if r["Status"] == "FOUND"]
    with (ROOT / "found-for-monday.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        w.writerows(found)

    # machine-readable log for finalize
    (ROOT / "run_log.json").write_text(json.dumps(results, indent=2), encoding="utf-8")

    counts = {}
    for r in out_rows:
        counts[r["Status"]] = counts.get(r["Status"], 0) + 1
    print("DONE", counts)


if __name__ == "__main__":
    main()
