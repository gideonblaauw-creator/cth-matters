#!/usr/bin/env python3
"""Deep domain crawl helper for Mail Finder batch3."""
import re
import json
import base64
import urllib.parse
import urllib.request
from html import unescape
from bs4 import BeautifulSoup

UA = "Mozilla/5.0 (compatible; TeclogiMailFinder/1.0; +research)"

EMAIL_RE = re.compile(
    r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
)


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            ct = r.headers.get("Content-Type", "")
            body = r.read()
            return r.status, ct, body
    except Exception as e:
        return None, str(e), b""


def decode_cfemail(hex_str):
    try:
        r = int(hex_str[:2], 16)
        return "".join(chr(int(hex_str[i : i + 2], 16) ^ r) for i in range(2, len(hex_str), 2))
    except Exception:
        return ""


def extract_from_html(html, base_url=""):
    emails = set()
    mailtos = set()
    cf = set()
    json_ld = []
    next_data = None

    soup = BeautifulSoup(html, "lxml")
    for a in soup.find_all("a", href=True):
        h = a["href"]
        if h.lower().startswith("mailto:"):
            m = h.split("mailto:", 1)[1].split("?")[0]
            mailtos.add(unescape(urllib.parse.unquote(m)))

    for el in soup.find_all(attrs={"data-cfemail": True}):
        cf.add(decode_cfemail(el["data-cfemail"]))

    text = soup.get_text(" ", strip=False)
    for m in EMAIL_RE.findall(html):
        if not m.endswith((".png", ".jpg", ".gif", ".webp")):
            emails.add(m)
    for m in EMAIL_RE.findall(text):
        emails.add(m)

    for script in soup.find_all("script", type="application/ld+json"):
        try:
            json_ld.append(json.loads(script.string or ""))
        except Exception:
            pass

    nd = soup.find("script", id="__NEXT_DATA__")
    if nd and nd.string:
        try:
            next_data = json.loads(nd.string)
        except Exception:
            pass

    return {
        "mailtos": sorted(mailtos),
        "cfemail": sorted(x for x in cf if x),
        "regex_emails": sorted(emails),
        "json_ld": json_ld,
        "has_next": next_data is not None,
    }


def wayback_cdx(domain, limit=15):
    url = (
        "https://web.archive.org/cdx/search/cdx?"
        + urllib.parse.urlencode(
            {
                "url": f"{domain}/*",
                "output": "json",
                "filter": "statuscode:200",
                "collapse": "urlkey",
                "limit": str(limit),
            }
        )
    )
    st, _, body = fetch(url)
    if st != 200:
        return []
    try:
        data = json.loads(body.decode())
        if not data:
            return []
        header, *rows = data
        out = []
        for row in rows:
            rec = dict(zip(header, row))
            if any(
                x in rec.get("original", "").lower()
                for x in ("/team", "/people", "/about", "/contact", "/leadership", "/staff")
            ):
                out.append(rec)
        return out
    except Exception:
        return []


def crawl_paths(domain):
    paths = [
        "/",
        "/team",
        "/about",
        "/about-us",
        "/people",
        "/contact",
        "/leadership",
        "/our-team",
        "/team/",
        "/about/",
        "/contact-us",
        "/imprint",
        "/impressum",
    ]
    results = []
    for p in paths:
        for scheme in ("https", "http"):
            url = f"{scheme}://{domain}{p}"
            st, ct, body = fetch(url)
            if st == 200 and b"html" in (ct or "").lower() or (body[:15].lower().find(b"<!doctype") >= 0 or body[:5].lower().find(b"<html") >= 0):
                ext = extract_from_html(body.decode("utf-8", errors="replace"), url)
                results.append({"url": url, "status": st, **ext})
                break
            elif st:
                results.append({"url": url, "status": st, "error": ct})
    return results


if __name__ == "__main__":
    import sys

    domain = sys.argv[1]
    print(json.dumps({"domain": domain, "crawl": crawl_paths(domain), "wayback": wayback_cdx(domain)}, indent=2))
