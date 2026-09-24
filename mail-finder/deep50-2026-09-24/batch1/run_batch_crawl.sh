#!/bin/bash
set -e
cd "$(dirname "$0")"
CSV="/home/ubuntu/.cursor/projects/workspace/uploads/teclogi-mailfinder-deep50-batch1-2026-09-24_84d5.csv"
OUT="crawl_raw.jsonl"
: > "$OUT"
tail -n +2 "$CSV" | while IFS= read -r line; do
  id=$(echo "$line" | cut -d, -f1)
  name=$(echo "$line" | cut -d, -f2)
  domain=$(echo "$line" | rev | cut -d, -f1 | rev)
  echo "=== $id $name @ $domain ===" >&2
  python3 deep_crawl.py "$domain" "$name" >> "$OUT" 2>/dev/null || echo "{\"domain\":\"$domain\",\"error\":\"crawl_failed\"}" >> "$OUT"
done
