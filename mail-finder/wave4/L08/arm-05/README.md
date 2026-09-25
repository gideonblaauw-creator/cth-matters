# Mail Finder — Wave4 / L08 / Arm 05

**Focus:** **Wayback CDX** on first-party `/team`, `/about`, or `/people` for promising EMPTY seats that already have a firm **Website** (no domain backfill in this arm).

**Write path:** `mail-finder/wave4/L08/arm-05/` only. **No Monday API writes.**

## Input

- `input.csv` — 5 seats (Monday export).

## Method (per seat)

1. Require non-blank firm **Website** (all five seats qualify).
2. Choose **one** path among `/team`, `/about`, `/people` using live homepage hints (single path only).
3. Run **one** CDX query: `https://web.archive.org/cdx/search/cdx?url={domain}{path}*&output=json&filter=statuscode:200&limit=15`.
4. For captures returned on that path, fetch archived HTML (same path only) and search for **exact target name** and **person@firm** `mailto:` or plaintext email on the **same page region**.
5. **FOUND** only with citation-grade co-occurrence; CDX metadata alone is not evidence.
6. Generics (`info@`, `infocolombia@`, office inboxes without the target name) → **EMPTY**.

## Prohibited

Pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator scraping, broad Wayback domain crawls, authenticated sources, Monday writes, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Every seed row once; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND rows only |
| `summary.md` | Scorecard |
| `evidence/` | CDX run log, URL index, negative excerpts |

## Regenerate CDX pass

```bash
python3 mail-finder/wave4/L08/arm-05/run_wayback_cdx.py
```

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l08-arm05-959e`
