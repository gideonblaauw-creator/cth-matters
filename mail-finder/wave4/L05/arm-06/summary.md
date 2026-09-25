# Wave4 L05 Arm 06 — Impact / LP / annual-report PDFs

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`).  
**Method:** Public **impact reports**, **LP materials**, **annual reports**, and comparable **PDFs** where a named person and exact **person@firm** email must co-occur in the **same** document. Generic/role inboxes → **EMPTY**. No pattern guess, SMTP verify, Hunter/Apollo, LinkedIn scrape, or invented emails.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm / domain | Outcome |
|----------------|------|---------------|---------|
| 13096680140 | Filipe Portugal | Canary (`canary.com.br`) | EMPTY — no PDF binds Filipe + `@canary.com.br` person local-part |
| 13028367534 | Fortunato D. Costantino | Axel Carbon (`axel-carbon.com`) | EMPTY — ERIA/Digited PDFs name him; no `@axel-carbon.com` person mailbox |
| 13028371858 | Franck Nouyrigat | Electis (`electis.com`) | EMPTY — HLM sourcing PDF has other `@electis.io` staff; not Nouyrigat |
| 13100506409 | George Chalmers | Molten Ventures (`moltenventures.com`) | EMPTY — EIS IM + FY26 annual report name him; only generic `@molten.vc` contacts |
| 13028367214 | Gioberto Balinge.. | Arxus (`arxus.eu`) | EMPTY — privacy PDF only; generics, no Balinge string |

## Deliverables

- `results.csv`, `stamp-list.json`, `README.md`, `summary.md`, `evidence/` (`url-index.md`, `negative-excerpts.md`, selected PDF snapshots)

**No Monday writes** from this folder.
