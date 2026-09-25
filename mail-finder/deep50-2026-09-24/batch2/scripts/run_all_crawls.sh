#!/bin/bash
set -euo pipefail
ROOT="/workspace/mail-finder/deep50-2026-09-24/batch2"
SCRIPT="$ROOT/scripts/deep_crawl.py"
HTML="$ROOT/html"
JSON="$ROOT/crawl_json"
mkdir -p "$HTML" "$JSON"

python3 << 'PY'
import csv
from pathlib import Path
rows = list(csv.DictReader(Path("/workspace/mail-finder/deep50-2026-09-24/batch2/input.csv").open()))
domains = sorted({r['Domain'].strip() for r in rows if r.get('Domain')})
Path("/tmp/batch2_domains.txt").write_text("\n".join(domains))
print(len(domains))
PY

while read -r dom; do
  [[ -z "$dom" ]] && continue
  safe="${dom//./_}"
  out="$JSON/${safe}.json"
  if [[ -f "$out" ]]; then continue; fi
  echo "=== $dom ==="
  python3 "$SCRIPT" "$dom" "$HTML" > "$out" 2>"$JSON/${safe}.err" || echo "fail $dom"
done < /tmp/batch2_domains.txt

echo DONE
