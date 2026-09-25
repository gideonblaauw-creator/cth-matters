# Wave5 L03 Arm 07 — Impact / DocuSign / ethics PDFs

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`)  
**Method:** Public first-party and issuer/fund impact, ethics, LP, and regulatory fund documents (PDF or HTML). **FOUND** only when the exact `Contact_name` and a personal `person@firm` email co-occur in the **same** qualifying artifact. Role/generic inboxes → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guess, SMTP verify, invented emails, or Monday writes.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Contact_name | Firm | Outcome |
|----------------|--------------|------|---------|
| 13100496520 | Yair Reem | Extantia Capital | EMPTY — Lobbyregister + KPMG annual PDF name Reem without personal @extantia.com on same doc |
| 13132406232 | Aaron Holiday | 645 Ventures | EMPTY — Form ADV / Form D name Holiday; no aholidayiii@645ventures.com on same fund artifact |
| 13132429817 | Adeyemi Ajao | Base10 Partners | EMPTY — Purpose impact HTML + Bentley Advancement PDF name Ajao without ade@base10.vc |
| 13132423003 | Blake Modersitzki | Pelion VP | EMPTY — no qualifying fund/LP PDF with Modersitzki + blake@pelionvp.com |
| 13132426966 | Brad Svrluga | Primary VP | EMPTY — Form ADV names Svrluga; no brad@primary.vc on same PDF |

## Artifacts

- `results.csv`, `stamp-list.json` (empty), `CLOSEOUT.md`, `evidence/` (`url-index.md`, `negative-excerpts.md`, lobbyregister excerpt)
