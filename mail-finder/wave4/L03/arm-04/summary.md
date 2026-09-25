# Wave4 L03 Arm 04 — Regulatory / securities PDF email discovery

**Batch:** 5 seats (4× P2, 1× P1 Bill Driegert)  
**Method:** Public web + PDF text (`pdftotext`) for BCSC Form 45-106F1 patterns, SEC EDGAR full-text, FINRA/IAPD (Form ADV), CNMV venture-capital prospectuses, UK Companies House statutory PDFs, and `filetype:pdf` dorks. **FOUND** only when the **same public PDF** co-attributes **display/legal name + non-generic person@seat-domain** (published spelling). Generics → EMPTY. No Hunter/Apollo, LinkedIn scrape, pattern+SMTP, or invented emails. No Monday writes.

## Scorecard

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Per seat

| Name | Domain | Outcome |
|------|--------|---------|
| Fortunato D. Costantino (firm seat) | axel-carbon.com | Named on ERIA research PDF; no mailbox on regulatory PDFs |
| Miheer Chanrai | climate.capital | Companies House PDFs; no person@climate.capital |
| Nic Gorini | spin.vc | UK accounts PDF + EDGAR; no person@spin.vc in filings |
| Nina Alastruey | demium.com | CNMV prospectus + event PDF; no person@demium.com |
| Bill Driegert | eclipse.capital | EDGAR + Eclipse Form ADV; no Driegert / no @eclipse.capital person email |

## Yield notes

- VC/CVC seats rarely publish individual mailboxes in Form D / exempt-market reports; this batch matched **wave2 filings-edgar** (0 FOUND on similar profile).
- **Near-misses (still EMPTY):** Nina Alastruey listed on SPRI event PDF with Demium role but only `info@wstartupc.com` (organizer generic, wrong domain). CNMV Demium fund PDFs use `legal@thinkbigger.vc` / auditor emails without Nina. Eclipse public pages cite `admin@eclipse.capital` (generic, HTML — out of scope for this PDF arm and excluded anyway).

## Monday stamping

`stamp-list.json` is empty. Route EMPTY seats to ReachGate; prior **L02 arm-04** firm-mailto pass was also EMPTY for the same four person seats.

## Evidence

Negative cites and downloaded regulatory PDFs under `evidence/` (no FOUND mailboxes this run).
