# Wave4 L04 Arm 07 — SEC EDGAR exhibits / Form D / signature blocks

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`).  
**Method:** Public **SEC EDGAR** filings and exhibits, including **Form D** and **signature blocks**; disambiguate by firm/target name. **FOUND** only when the seat person’s published name and an exact **person@firm** email appear in the **same** public filing artifact (preserve local-part spelling). Generic mailboxes → **EMPTY**. No pattern guess, SMTP verify, Hunter/Apollo, LinkedIn scrape, or invented emails.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm / domain | Outcome |
|----------------|------|---------------|---------|
| 13028365646 | Ana Lucía Rodhas Alcántara | Hyatt (`hyatt.com`) | EMPTY — 0 EDGAR name hits; Hyatt Exhibit 14.1 has other `@hyatt.com` names only |
| 13028359995 | Andrii Hordiichuk | BioSingularity (`biosingularity.world`) | EMPTY — 0 EDGAR / Form D for name or domain |
| 13028358627 | Andrés Méndez | Colaborativo (`colaborativo.io`) | EMPTY — domain absent; unrelated “colaborativo” token in other issuers |
| 13100509887 | Andrés Saborido | Wayra / Telefónica (`telefonica.com`) | EMPTY — 0 Saborido; Wayra in 20-F appendix; generics `amv@` / `ir@` only |
| 13028336707 | Andrés Salazar González | Bavaria (`bavaria.co`) | EMPTY — 0 target name; Salazar+Bavaria hits are other individuals |

## Deliverables

- `results.csv`, `stamp-list.json`, `README.md`, `summary.md`, `evidence/` (`edgar_search.json`, `url-index.md`, `negative-excerpts.md`, selected filing snapshots)

**No Monday writes** from this folder.
