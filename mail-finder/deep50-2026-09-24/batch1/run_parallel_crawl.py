#!/usr/bin/env python3
import csv, json, concurrent.futures
from pathlib import Path
from deep_crawl import crawl_domain

CSV = Path("/home/ubuntu/.cursor/projects/workspace/uploads/teclogi-mailfinder-deep50-batch1-2026-09-24_84d5.csv")
OUT = Path(__file__).resolve().parent / "crawl_results.json"

rows = list(csv.DictReader(open(CSV)))

def job(row):
    name = row["Name"] or row.get("Firm", "")
    domain = row["Domain"]
    data = crawl_domain(domain, name)
    data["monday_id"] = row["Monday_item_id"]
    return data

results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    for data in ex.map(job, rows):
        results.append(data)
        print(data["monday_id"], data["domain"], len(data["attributions"]), "attr", file=__import__("sys").stderr)

OUT.write_text(json.dumps(results, indent=2))
print(f"Wrote {OUT}")
