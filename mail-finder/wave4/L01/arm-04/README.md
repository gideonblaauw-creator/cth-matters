# Mail Finder — Wave4 Loop L01 Arm 04

**Focus:** Domain hygiene + Website backfill (Potential Investors only).

## Input

`input.csv` — columns: Monday_item_id, Name, Contact_name, Firm, Kind, Priority, Status, Website, Domain, LinkedIn.

## Method (this arm)

1. **Blank Website:** resolve live investment-entity homepage via public web search (firm + contact).
2. **Filled Website:** HTTP-check for NXDOMAIN, parking, wrong entity, or redirect to a different firm domain.
3. **Propose** corrected `https://…` when blank/wrong/parked; sniff-test noisy inferences before proposing.
4. **Opportunistic email:** first-party team/people page with **name + person@firm mailto** co-occurrence → `FOUND`. Generics (`info@`, `hello@`, `team@`, etc.) are not FOUND.
5. Name/domain may seed search only — never invent emails, pattern+SMTP, Hunter/Apollo, or LinkedIn scrape.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat status, websites, notes, checked URLs |
| `website-corrections.json` | Monday Website patch list (wrong/blank/parked only) |
| `stamp-list.json` | FOUND emails for workbench Monday stamp |
| `summary.md` | Scorecard |
| `evidence/` | Excerpts for any FOUND (empty this run) |

## Scripts (audit trail)

- `scripts/check_websites.py` — HTTP fetch + parking heuristics
- `scripts/scan_team_emails.py` — mailto + name proximity scan
- `scripts/generate_deliverables.py` — writes deliverables from adjudicated outcomes
