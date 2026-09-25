#!/usr/bin/env python3
import csv, json, concurrent.futures
from pathlib import Path
from deep_crawl import crawl_domain

ROOT = Path(__file__).resolve().parent
CSV = Path("/home/ubuntu/.cursor/projects/workspace/uploads/teclogi-mailfinder-deep50-batch1-2026-09-24_84d5.csv")
rows = list(csv.DictReader(open(CSV)))

def work(row):
    domain = row["Domain"].strip()
    out = ROOT / f"crawl_{domain.replace('.', '_')}.json"
    if out.exists():
        return domain, "skip"
    name = row["Name"] or row.get("Firm", "")
    data = crawl_domain(domain, name)
    out.write_text(json.dumps(data, indent=2))
    return domain, f"attr={len(data.get('attributions',[]))}"

tasks = [r for r in rows if not (ROOT / f"crawl_{r['Domain'].replace('.', '_')}.json").exists()]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    for dom, status in ex.map(work, tasks):
        print(dom, status, flush=True)
