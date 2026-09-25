# Mail Finder Wave 2 — Website backfill (empty firm sites)

**Board:** 18425305222 (Teclogi Series A Mail Finder)  
**Monday Website column:** `link_mm7gdv8s` only  
**Arm:** Website backfill — map blank Website seats to investment-entity homepages (no Hunter/Apollo, no LinkedIn scrape, no pattern email guessing).  
**Input:** `input.csv` (8 seats from deep50 no-domain remainder)

## Summary counts

| MailFinder_Status | Count |
|-------------------|------:|
| EMPTY (website mapped; email still empty) | 7 |
| DOMAIN_UNRESOLVED | 1 |
| FOUND (email) | 0 |

**Stamp list:** 7 rows in `website-stamp-list.csv` (live firm sites verified 2026-09-25).  
**Excluded from stamp list:** Victoria But — no citation-grade public firm homepage (family office / principal capacity).

## Per-seat resolution

### Dennis Zaidi (13028359182)

- **Entity:** Checkmate Capital Group (from Firm string + HITL context).
- **Proposed Website:** `https://www.checkmatecapital.net/`
- **Domain:** `checkmatecapital.net`
- **Why not checkmatecap.com:** Root domain serves a parking/redirect lander; deep50 crawl documented operational site on `.net`.
- **Verify:** HTTP 200; title “Checkmate Capital | Investments | Advisory | Licensing”.
- **Email:** EMPTY (contact form only in deep50).

### Federico Storani (13080749061)

- **Entity:** Riverwood Capital (Firm + notes).
- **Proposed Website:** `https://www.riverwoodcapital.com/`
- **Verify:** Live growth-tech PE site; team section includes **Federico Storani**.
- **Email:** EMPTY (deep50: no person mailto on team pages).

### Filipe Portugal (13096680140)

- **Entity:** Canary (Brazil LatAm VC; notes + import tag).
- **Proposed Website:** `https://www.canary.com.br/` (canonical after redirect from `canary.com.br`).
- **Verify:** HTTP 200; current Canary VC marketing site.
- **Email:** EMPTY (deep50: team SPA without partner emails in HTML).

### Josep Oriol (13028393225)

- **Entity:** Okavango Capital Partners (Firm string).
- **Proposed Website:** `https://www.okavango-capital.com/`
- **Domain:** `okavango-capital.com` (hyphenated; `okavangocapital.com` does not resolve in DNS).
- **Verify:** HTTP 200; Our Team lists Josep Oriol; Brighter Future interview cites `www.okavango-capital.com`.
- **Email:** EMPTY.

### Séverine Grégoire (13100496537)

- **Entity:** ZEBOX Ventures (CMA CGM CVC).
- **Proposed Website:** `https://www.ze-box.io/ventures` (fund page; parent hub `https://www.ze-box.io/` also live).
- **Domain:** `ze-box.io` (not `zebox.io` — deep50 domain mismatch).
- **Verify:** HTTP 200 on ventures page; fund description + CMA CGM linkage.
- **Email:** EMPTY (`ventures@ze-box.io` generic only).

### Ulrich Thiem (13100496603)

- **Entity:** Porsche Ventures.
- **Proposed Website:** `https://porsche.ventures/`
- **Verify:** HTTP 200; team page lists Ulrich Thiem.
- **Email:** EMPTY (generic contact only in deep50).

### Victoria But (13028367296) — DOMAIN_UNRESOLVED

- **Firm field:** “Impact Investor I Sustainability” (descriptor, not a fund name).
- **Public identity:** Principal, **Sun East** family office / **Sun East Group Limited** (Campden FB profile; SEC Rule 14a-8 comment letter, Feb 2020).
- **No stamp:** No official public homepage for the family office investment entity.
- **Sniff-test rejections:** `victoriascr.com` (Victoria Venture Capital SCR, Spain), `victoria-fo.com` (unrelated European family office) — personal-name → unrelated corporate homepage.

### Yair Reem (13100496520)

- **Entity:** Extantia Capital (notes + climate VC desk).
- **Proposed Website:** `https://www.extantia.com/`
- **Verify:** HTTP 200; “Extantia | Industries Re-Imagined.”
- **Email:** EMPTY (imprint generic only in deep50).

## Deliverables

| File | Purpose |
|------|---------|
| `results.csv` | Full classification + proposed Domain/Website |
| `website-stamp-list.csv` | Monday manual Website stamps (`link_mm7gdv8s`) |
| `results.md` | This memo |

No `found-for-monday.csv` or `first-found-evidence.md` — no citation-grade person@firm emails discovered during website resolution.

## Live verification log (2026-09-25 UTC)

| URL | Result |
|-----|--------|
| https://www.checkmatecapital.net/ | 200 |
| https://www.riverwoodcapital.com/ | 200 (firm content; curl may 403, fetch confirms team) |
| https://www.canary.com.br/ | 200 |
| https://www.okavango-capital.com/ | 200 |
| https://www.ze-box.io/ventures | 200 |
| https://porsche.ventures/ | 200 |
| https://www.extantia.com/ | 200 |
