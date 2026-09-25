#!/usr/bin/env python3
"""Deep firm-domain crawl: mailto, regex, CF decode, JSON-LD, common paths, limited BFS."""
import json
import re
import html as html_lib
import urllib.parse
import urllib.request
from pathlib import Path
from collections import deque

UA = "MailFinder-Deep50/1.0 (Teclogi research; +https://github.com/gideonblaauw-creator/cth-matters)"
TIMEOUT = 25
MAX_PAGES = 40
MAX_DEPTH = 2

PATH_SEEDS = [
    "/", "/team", "/about", "/about-us", "/people", "/our-team", "/leadership",
    "/contact", "/contact-us", "/imprint", "/impressum", "/press", "/news",
    "/portfolio", "/investment-team", "/who-we-are", "/management", "/partners",
    "/en/team", "/en/about", "/de/team", "/de/ueber-uns", "/equipe", "/equipo",
    "/team/", "/about/", "/people/",
]

EMAIL_RE = re.compile(
    r"(?<![\w.-])([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?![\w.-])"
)
MAILTO_RE = re.compile(r"mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.+\w+)", re.I)
CFEMAIL_RE = re.compile(
    r'data-cfemail=["\']([a-f0-9]+)["\']|/cdn-cgi/l/email-protection#([a-f0-9]+)',
    re.I,
)
JSONLD_RE = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.I | re.S,
)
NEXT_DATA_RE = re.compile(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', re.S)
NUXT_RE = re.compile(r"window\.__NUXT__\s*=\s*(.+?)</script>", re.S)
PDF_RE = re.compile(r'href=["\']([^"\']+\.pdf[^"\']*)["\']', re.I)
LINK_RE = re.compile(r'href=["\']([^"\']+)["\']', re.I)


def cf_decode(hex_str: str) -> str:
    try:
        r = int(hex_str[:2], 16)
        return "".join(chr(int(hex_str[i : i + 2], 16) ^ r) for i in range(2, len(hex_str), 2))
    except Exception:
        return ""


def fetch(url: str) -> tuple[int, str, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, resp.geturl(), resp.read()
    except Exception as e:
        return 0, url, str(e).encode()


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


def extract_emails(text: str) -> set[str]:
    out = set()
    for m in EMAIL_RE.findall(text):
        if not m.endswith(".png") and not m.endswith(".jpg"):
            out.add(m.lower())
    for m in MAILTO_RE.findall(text):
        out.add(m.split("?")[0].lower())
    for g in CFEMAIL_RE.findall(text):
        hx = g[0] or g[1]
        if hx:
            dec = cf_decode(hx)
            if "@" in dec:
                out.add(dec.lower())
    for block in JSONLD_RE.findall(text):
        try:
            data = json.loads(block)
            out |= emails_from_json(data)
        except Exception:
            pass
    m = NEXT_DATA_RE.search(text)
    if m:
        try:
            out |= emails_from_json(json.loads(m.group(1)))
        except Exception:
            pass
    m = NUXT_RE.search(text)
    if m:
        raw = m.group(1).strip()
        if raw.endswith(";"):
            raw = raw[:-1]
        for em in EMAIL_RE.findall(raw):
            out.add(em.lower())
    return out


def emails_from_json(obj) -> set[str]:
    out = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("email", "contactPoint") and isinstance(v, str) and "@" in v:
                out.add(v.lower())
            out |= emails_from_json(v)
    elif isinstance(obj, list):
        for x in obj:
            out |= emails_from_json(x)
    elif isinstance(obj, str) and "@" in obj and EMAIL_RE.search(obj):
        out.add(EMAIL_RE.search(obj).group(1).lower())
    return out


def name_tokens(name: str) -> list[str]:
    n = re.sub(r"[^\w\s'-]", " ", name, flags=re.UNICODE)
    parts = [p for p in n.split() if len(p) > 2 and p.lower() not in ("and", "the", "von", "de", "del", "la")]
    return parts


def name_on_page(name: str, text: str) -> bool:
    t = html_lib.unescape(text)
    t_low = t.lower()
    parts = name_tokens(name)
    if not parts:
        return False
    if len(parts) >= 2:
        last = parts[-1].lower()
        first = parts[0].lower()
        if last in t_low and first in t_low:
            return True
        full = " ".join(p.lower() for p in parts)
        if full in t_low:
            return True
    elif parts[0].lower() in t_low:
        return True
    return False


def crawl_domain(domain: str, html_dir: Path) -> dict:
    domain = domain.strip().lower()
    base = f"https://{domain}"
    seen: set[str] = set()
    queue: deque[tuple[str, int]] = deque()
    checked: list[str] = []
    findings: list[dict] = []

    for p in PATH_SEEDS:
        queue.append((base.rstrip("/") + p if p != "/" else base + "/", 0))

    pages = 0
    while queue and pages < MAX_PAGES:
        url, depth = queue.popleft()
        if url in seen:
            continue
        seen.add(url)
        status, final_url, body = fetch(url)
        checked.append(final_url if status else url)
        if not status or status >= 400:
            continue
        pages += 1
        try:
            text = body.decode("utf-8", errors="replace")
        except Exception:
            continue
        slug = re.sub(r"[^a-zA-Z0-9._-]", "_", urllib.parse.urlparse(final_url).path or "root")[:80]
        (html_dir / f"{domain}_{slug}_{pages}.html").write_text(text[:500_000], encoding="utf-8")

        emails = extract_emails(text)
        for em in emails:
            if domain not in em.split("@")[-1]:
                continue
            if name_on_page("", text):  # placeholder — attribution per-seat done later
                pass
            findings.append({"email": em, "url": final_url})

        if depth < MAX_DEPTH:
            for href in LINK_RE.findall(text):
                nu = norm_url(final_url, href)
                if nu and same_site(domain, nu) and nu not in seen:
                    path = urllib.parse.urlparse(nu).path.lower()
                    if any(
                        x in path
                        for x in (
                            "team", "about", "people", "contact", "press", "news",
                            "leadership", "partner", "staff", "bio", "who",
                        )
                    ) or path.endswith(".pdf"):
                        queue.append((nu, depth + 1))

    # dedupe findings by email+url
    uniq = {(f["email"], f["url"]): f for f in findings}
    return {"domain": domain, "checked": checked, "findings": list(uniq.values())}


def wayback_urls(domain: str, limit: int = 8) -> list[str]:
    cdx = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&filter=statuscode:200&collapse=urlkey&limit=200"
    try:
        with urllib.request.urlopen(
            urllib.request.Request(cdx, headers={"User-Agent": UA}), timeout=30
        ) as r:
            rows = json.loads(r.read().decode())
    except Exception:
        return []
    if not rows or len(rows) < 2:
        return []
    headers = rows[0]
    out = []
    for row in rows[1:]:
        rec = dict(zip(headers, row))
        orig = rec.get("original", "")
        if any(x in orig.lower() for x in ("team", "about", "people", "contact", "leadership")):
            ts = rec.get("timestamp", "")
            out.append(f"https://web.archive.org/web/{ts}id_/{orig}")
    return out[:limit]


if __name__ == "__main__":
    import sys

    dom = sys.argv[1]
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    wb = wayback_urls(dom)
    res = crawl_domain(dom, out_dir)
    res["wayback_checked"] = []
    for wu in wb:
        st, fu, body = fetch(wu)
        res["wayback_checked"].append(wu)
        if st and st < 400:
            text = body.decode("utf-8", errors="replace")
            slug = "wb_" + re.sub(r"[^a-zA-Z0-9._-]", "_", wu[-60:])
            (out_dir / f"{dom}_{slug}.html").write_text(text[:500_000], encoding="utf-8")
            for em in extract_emails(text):
                if dom in em.split("@")[-1]:
                    res["findings"].append({"email": em, "url": wu})
    print(json.dumps(res, indent=2))
