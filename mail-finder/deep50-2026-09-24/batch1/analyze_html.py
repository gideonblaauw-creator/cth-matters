#!/usr/bin/env python3
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "html"
CSV = Path("/home/ubuntu/.cursor/projects/workspace/uploads/teclogi-mailfinder-deep50-batch1-2026-09-24_84d5.csv")

rows = list(csv.DictReader(open(CSV)))
EMAIL = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")

def tokens(name):
    return [p.lower() for p in re.sub(r"[^a-zA-Z\s]", " ", name).split() if len(p) > 1 and p.lower() not in {"dr"}]

for r in rows:
    name = r["Name"] or r.get("Firm", "")
    domain = r["Domain"].lower()
    toks = tokens(name)
    if not toks:
        continue
    hits = []
    for fp in HTML.glob("*.html"):
        text = fp.read_text(errors="replace").lower()
        if domain.replace("www.", "") not in text and domain not in fp.name:
            continue
        for em in set(EMAIL.findall(text)):
            eml = em.lower()
            if domain.split(".")[0] not in eml and domain not in eml:
                continue
            idx = text.find(eml)
            chunk = text[max(0, idx - 500) : idx + 500]
            if toks[0] in chunk and (len(toks) == 1 or toks[-1] in chunk):
                hits.append((eml, fp.name))
    if hits:
        print(r["Monday_item_id"], name, domain, hits[:5])
