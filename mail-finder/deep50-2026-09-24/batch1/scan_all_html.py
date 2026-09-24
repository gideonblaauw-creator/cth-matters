#!/usr/bin/env python3
import csv, re
from pathlib import Path

CSV = Path("/home/ubuntu/.cursor/projects/workspace/uploads/teclogi-mailfinder-deep50-batch1-2026-09-24_84d5.csv")
HTML = Path(__file__).resolve().parent / "html"
EMAIL = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")

def tokens(name):
    return [p.lower() for p in re.sub(r"[^a-zA-Z\s]", " ", name).split() if len(p) > 1 and p.lower() not in {"dr", "vc"}]

rows = list(csv.DictReader(open(CSV)))
files = list(HTML.glob("*.html")) + list(HTML.glob("*.pdf"))

for r in rows:
    name = (r["Name"] or r.get("Firm") or "").strip()
    if not name:
        continue
    domain = r["Domain"].lower().strip()
    dom_root = domain.split(".")[0]
    toks = tokens(name)
    if not toks:
        continue
    hits = []
    for fp in files:
        try:
            text = fp.read_text(errors="replace")
        except Exception:
            continue
        if dom_root not in text.lower() and domain not in fp.name and domain not in text.lower():
            continue
        for em in set(EMAIL.findall(text)):
            eml = em.lower()
            if dom_root not in eml and domain.replace("www.", "") not in eml:
                continue
            if any(x in eml for x in ("info@", "hello@", "contact@", "investors@", "press@", "privacidad@", "infocolombia@", "cdmexico@", "team@", "care@")):
                continue
            idx = text.lower().find(eml)
            chunk = text.lower()[max(0, idx - 600) : idx + 600]
            if toks[0] in chunk and (len(toks) == 1 or toks[-1] in chunk):
                hits.append((eml, str(fp.name)))
    if hits:
        print(r["Monday_item_id"], name, hits[:8])
