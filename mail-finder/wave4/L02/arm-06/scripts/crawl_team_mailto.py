#!/usr/bin/env python3
"""Wave4 L02 Arm06: firm-domain team/people pages — name + mailto co-occurrence only."""
from __future__ import annotations

import json
import re
import html as html_lib
import urllib.parse
import urllib.request
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = "MailFinder-Wave4-L02-Arm06/1.0 (Teclogi public research)"
TIMEOUT = 25
MAX_PAGES = 35
MAX_DEPTH = 2

PATH_SEEDS = [
    "/",
    "/team",
    "/team/",
    "/people",
    "/people/",
    "/about",
    "/about-us",
    "/our-team",
    "/leadership",
    "/contact",
    "/contact-us",
    "/who-we-are",
    "/management",
    "/partners",
    "/en/team",
    "/en/about",
]

MAILTO_RE = re.compile(
    r'<a[^>]*href=["\']mailto:([^"\'?]+)[^"\']*["\'][^>]*>(.*?)</a>',
    re.I | re.S,
)
MAILTO_HREF_RE = re.compile(r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', re.I)
LINK_RE = re.compile(r'href=["\']([^"\']+)["\']', re.I)

GENERIC_LOCAL = {
    "info",
    "contact",
    "hello",
    "hi",
    "support",
    "admin",
    "office",
    "team",
    "mail",
    "enquiries",
    "inquiries",
    "press",
    "media",
    "careers",
    "jobs",
    "hr",
    "legal",
    "privacy",
    "dpo",
    "sales",
    "marketing",
    "noreply",
    "no-reply",
}


def fetch(url: str) -> tuple[int, str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            raw = resp.read()
            try:
                text = raw.decode("utf-8", errors="replace")
            except Exception:
                text = raw.decode("latin-1", errors="replace")
            return resp.status, resp.geturl(), text
    except Exception as e:
        return 0, url, f"<!-- fetch error: {e} -->"


def norm_url(base: str, link: str) -> str | None:
    if not link or link.startswith(("mailto:", "tel:", "javascript:", "#")):
        return None
    u = urllib.parse.urljoin(base, link)
    p = urllib.parse.urlparse(u)
    if p.scheme not in ("http", "https"):
        return None
    return urllib.parse.urlunparse((p.scheme, p.netloc, p.path or "/", p.params, p.query, ""))


def same_site(domain: str, url: str) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower().removeprefix("www.")
    dom = domain.lower().removeprefix("www.")
    return host == dom or host.endswith("." + dom)


def strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    return html_lib.unescape(re.sub(r"\s+", " ", s)).strip()


def is_generic(email: str) -> bool:
    local = email.split("@")[0].lower()
    if local in GENERIC_LOCAL:
        return True
    for g in GENERIC_LOCAL:
        if local.startswith(g + ".") or local.endswith("." + g):
            return True
    return False


def name_tokens(full_name: str) -> list[str]:
    parts = [p for p in re.split(r"[\s,.-]+", full_name.strip()) if len(p) > 1]
    return [p.lower() for p in parts]


def name_on_page(full_name: str, page_text: str) -> bool:
    low = page_text.lower()
    tokens = name_tokens(full_name)
    if not tokens:
        return False
    if full_name.lower() in low:
        return True
    # require first + last token both present
    if len(tokens) >= 2:
        return tokens[0] in low and tokens[-1] in low
    return tokens[0] in low


def anchor_names_person(anchor_text: str, full_name: str) -> bool:
    t = strip_tags(anchor_text).lower()
    tokens = name_tokens(full_name)
    if full_name.lower() in t:
        return True
    if len(tokens) >= 2 and tokens[0] in t and tokens[-1] in t:
        return True
    return False


def email_domain_ok(email: str, firm_domain: str) -> bool:
    dom = email.split("@")[-1].lower().removeprefix("www.")
    fd = firm_domain.lower().removeprefix("www.")
    return dom == fd or dom.endswith("." + fd)


def crawl_domain(base_url: str, firm_domain: str, contact_name: str) -> dict:
    seeds = set()
    parsed = urllib.parse.urlparse(base_url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    for path in PATH_SEEDS:
        seeds.add(urllib.parse.urljoin(origin + "/", path.lstrip("/")))

    visited: set[str] = set()
    queue: deque[tuple[str, int]] = deque((u, 0) for u in sorted(seeds))
    pages: list[dict] = []
    hits: list[dict] = []
    checked: list[str] = []

    while queue and len(visited) < MAX_PAGES:
        url, depth = queue.popleft()
        if url in visited:
            continue
        visited.add(url)
        status, final_url, html = fetch(url)
        checked.append(final_url if status else url)
        fname = (
            firm_domain.replace(".", "_")
            + "_"
            + re.sub(r"[^a-zA-Z0-9]+", "_", urllib.parse.urlparse(final_url).path or "root")
            + ".html"
        )
        ev_path = ROOT / "evidence" / fname
        ev_path.write_text(html[:500_000], encoding="utf-8")

        mailtos: list[dict] = []
        page_plain = strip_tags(html)
        for m in MAILTO_RE.finditer(html):
            email = urllib.parse.unquote(m.group(1).split("?")[0]).lower().strip()
            anchor = m.group(2)
            mailtos.append(
                {
                    "email": email,
                    "anchor_text": strip_tags(anchor)[:200],
                    "generic": is_generic(email),
                    "firm_domain": email_domain_ok(email, firm_domain),
                }
            )
            if (
                email_domain_ok(email, firm_domain)
                and not is_generic(email)
                and name_on_page(contact_name, page_plain)
                and (anchor_names_person(anchor, contact_name) or name_on_page(contact_name, strip_tags(anchor)))
            ):
                hits.append(
                    {
                        "email": email,
                        "url": final_url,
                        "anchor_text": strip_tags(anchor),
                        "snippet": html[max(0, m.start() - 120) : m.end() + 120],
                    }
                )

        # also: mailto in HTML with name in nearby context (same block ~500 chars)
        for m in MAILTO_HREF_RE.finditer(html):
            email = m.group(1).lower()
            if not email_domain_ok(email, firm_domain) or is_generic(email):
                continue
            start = max(0, m.start() - 800)
            chunk = strip_tags(html[start : m.end() + 200])
            if name_on_page(contact_name, chunk):
                if not any(h["email"] == email and h["url"] == final_url for h in hits):
                    hits.append(
                        {
                            "email": email,
                            "url": final_url,
                            "anchor_text": "",
                            "snippet": html[max(0, m.start() - 120) : m.end() + 120],
                            "context": chunk[:400],
                        }
                    )

        pages.append({"url": final_url, "status": status, "mailtos": mailtos, "name_present": name_on_page(contact_name, page_plain)})

        if depth < MAX_DEPTH and status:
            for link in LINK_RE.findall(html):
                nu = norm_url(final_url, link)
                if nu and same_site(firm_domain, nu) and nu not in visited:
                    if any(
                        seg in nu.lower()
                        for seg in (
                            "team",
                            "people",
                            "about",
                            "leadership",
                            "contact",
                            "staff",
                            "partner",
                            "who-we",
                            "management",
                        )
                    ):
                        queue.append((nu, depth + 1))

    return {
        "base_url": base_url,
        "firm_domain": firm_domain,
        "contact_name": contact_name,
        "checked_urls": checked,
        "pages": pages,
        "hits": hits,
    }


def main() -> None:
    seats = [
        ("13028372793", "Stefanie Hauer", "https://nature-re.com", "nature-re.com"),
        ("13028360224", "William Prescott", "https://redribbon.co", "redribbon.co"),
        ("13028385021", "Jeff Stoike", "https://blueactionaccelerator.com", "blueactionaccelerator.com"),
        ("13028367829", "Mikayla Hart", "https://congruencecapital.com", "congruencecapital.com"),
    ]
    out = []
    for mid, name, web, dom in seats:
        print(f"Crawling {dom} for {name}...")
        out.append({"monday_id": mid, **crawl_domain(web, dom, name)})
    (ROOT / "evidence" / "crawl_report.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("Done.", ROOT / "evidence" / "crawl_report.json")


if __name__ == "__main__":
    main()
