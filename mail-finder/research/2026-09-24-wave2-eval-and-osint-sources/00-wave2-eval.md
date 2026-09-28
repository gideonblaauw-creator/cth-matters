# Wave2 + Deep50 post-run evaluation (2026-09-24)

**Program:** Teclogi Series A — citation-grade `person@firm` discovery  
**Goal:** 50 FOUND (Monday `email_mm7ffmz4`)  
**Stamped before Wave2:** 26  
**Stamped after Wave2:** 27 (+1)  
**Gap to goal:** 23  

Sources: attached `WAVE2-CLOSEOUT-FACTS.md`, `Mail-Finder-Yield-Lessons-deep50-2026-09-24.md`, and repo artifacts under `mail-finder/deep50-2026-09-24/`.

---

## Executive summary

Deep50 (~50 seats, method-focused Hands) produced roughly **~10 FOUNDs (~6% seat yield)** by leaning on **regulatory PDFs, issuer press/footers, curated investor directories, and firm team `mailto:`** — not bulk HTML grinding.

Wave2 (five parallel arms, composer-2.5 Fast) added **one** citation-grade email: **Fernando Casado** (`fernando.casado@inclimo.com`) from an **Inclimo regulatory/DFI-class PDF** in the deferred high-yield arm. The other four arms improved **domain/website hygiene** and closed many EMPTY seats but did not convert to FOUND at citation grade.

**Net:** Public-source stack is directionally correct; **yield is limited by seat mix** (many VC sites hide personal mailboxes) and **under-weighting of PDF/regulatory search** relative to site crawl + EDGAR full-text + Wayback in Wave2.

---

## Yield table — Deep50 (same calendar day, pre-Wave2)

| Wave / batch | Seats (approx.) | FOUND | Yield | Primary methods that converted |
|--------------|----------------:|------:|------:|--------------------------------|
| Morning + hardwave + pagesource (prior) | (rolled into 26 pre-Wave2) | 16 | — | Mixed early arms (not re-audited here) |
| Deep50 P1 | 22 | 2 | 9% | SEC EDGAR exhibit signature; ethics/DocuSign PDF |
| Deep50 batch1 | ~25 | 1 | ~4% | Impact-finance PDF (LatAm) |
| Deep50 batch2 | ~25 | 1 | ~4% | Press HTML `mailto:` + name anchor |
| Deep50 batch3 | ~35 | 4 | ~11% | BCSC 45-106F1 PDF; Mercury directory; Citi press footnote; public LinkedIn post (HITL) |
| **Deep50 subtotal (repo CSVs)** | **~107 person-seats touched** | **8 logged in CSVs** | **~7–8% on logged batches** | Facts doc cites **~10 FOUND** including team mailto / partners not in every CSV export |

**Deep50 FOUND patterns (high confidence):**

| Person | Firm | Email (as published) | Evidence class |
|--------|------|----------------------|----------------|
| Marc Helwani | i80 Group | `healing@i80group.com` | SEC EDGAR exhibit / signature block |
| Fernando Cortes McAllister | Fundación Bolívar Davivienda | `fcortes@fundacionbd.org` | DocuSign / ethics PDF |
| Daniel Izzo | Vox Capital | `daniel@voxcapital.com.br` | Impact-finance PDF |
| Florian Heinemann | Project A | `florian.heinemann@project-a.com` | Press `mailto:` |
| Quin Garcia | AutoTech VC | `qg@autotechvc.com` | BCSC Form 45-106F1 PDF |
| Shruti Gandhi | Array Ventures | `shruti@array.vc` | Mercury investor DB (name+email same page) |
| Vibhor Rastogi | Citi Ventures | `vibhor.rastorgi@citi.com` | Issuer press footnote (published spelling) |
| Shahnaz Khan | Satgana | `shahnaz@satgana.com` | Public LinkedIn post (**HITL** — not scrape) |

---

## Yield table — Wave2 (parallel arms)

| Arm | Agent / PR | Email FOUND | Seat outcomes | Non-email value |
|-----|------------|------------:|---------------|-----------------|
| Website backfill | bc-c0a3688 / #18 | **0** | 7 sites mapped | 3 Monday Website corrections (parked/wrong entity) |
| Domain cleanup | bc-a7b01a0a / #19 | **0** | 15 domains resolved | 10 Website corrections; Victoria But **DOMAIN_UNRESOLVED** |
| **Deferred high-yield** | bc-b27eba43 / **#20** | **1** | Fernando Casado FOUND; Nic Gorini HOLD; Elvia/Miheer EMPTY | **Inclimo DFI/regulatory PDF** |
| Filings / EDGAR | bc-24fd438d / #21 | **0** | 24 EMPTY | Near-miss generics / wrong-person; Fernando Lelo **DOMAIN_UNRESOLVED** (`rumbo.vc`) |
| Wayback CDX | bc-30e6aa56 / #22 | **0** | 18 EMPTY | HOLD Maite Fibla + Jason Sydow (LinkedIn-only) |

**Wave2 sole FOUND (citation-grade):**

- **Fernando Casado** — `fernando.casado@inclimo.com` — regulatory/DFI PDF (Inclimo). Confirms Deep50 lesson: **LatAm/EU impact & development-finance disclosures** beat live team HTML for this seat mix.

---

## What worked

1. **Regulatory and quasi-regulatory PDFs** with signer blocks (BCSC 45-106F1, SEC exhibits, CNMV-style filings, DFI impact docs).
2. **Firm-published press / perspectives** where the author name and mailbox co-occur (footnotes, `mailto:` in article HTML).
3. **Curated public directories** where the page binds investor name + contact email (Mercury investor DB — not paid enrichment APIs).
4. **Domain hygiene before crawl** — Wave2 #19 corrected 10 wrong/parked Website stamps; prevents wasted crawl budget (no FOUND, but reduces false EMPTY).
5. **Deferred URL tickets** — Wave2 #20 converted when a pre-identified high-yield PDF was executed as a short Hands pass.

---

## What did not work (this pass)

1. **Bulk EDGAR / Form D arm (Wave2 #21)** — 0/24 FOUND. Form D Item 2 is address + phone, not issuer contact email ([SEC Form D PDF](https://www.sec.gov/files/formd.pdf)). Value is **officer names + related persons** → redirect to **exhibits, IAPD brochures, 13F letters**, not Form D body alone.
2. **Wayback-only arm (Wave2 #22)** — 0/18 FOUND. Many historical team pages never had `mailto:`; CDX finds snapshots but not citation-grade name+email if the live era used contact forms only.
3. **Live team/about HTML grind** — Confirmed identity on bios without personal mailbox (Lightrock, Eclipse, Lendable LatAm, etc. in P1 notes). Generics (`info@`, `investments@`) correctly stamped EMPTY.
4. **403 / bot walls / JS-heavy SPAs** — One Wayback attempt then escalate (per Deep50 lessons); do not deepen HTML pass.

---

## Inconclusive / process outcomes (not FOUND)

| Outcome | Meaning | Next action |
|---------|---------|-------------|
| **HOLD (LinkedIn-only)** | Public post or profile mentions firm but no citable email on allowed source | Human review; no Sales Nav / scrape |
| **DOMAIN_UNRESOLVED** | Cannot tie person to firm domain (`rumbo.vc`, Victoria But) | Alias search + OpenCorporates/registry, then re-queue PDF arm |
| **Website correction without email** | Fixed Monday `link_mm7gdv8s` | Re-run **one** team/press/PDF arm on corrected domain |
| **Near-miss generic** | Mailbox found without person co-occurrence | Do not stamp; escalate PDF/press |

---

## Success-rate interpretation (avoid false precision)

- **Method yield ≠ seat yield.** A single BCSC PDF arm can yield 1 FOUND per 5–10 targeted fund-manager seats; a blind EDGAR text sweep can yield 0/24.
- **Sample bias:** Deep50 and Wave2 seats skew toward **global VC/CVC/impact** with **minimal public mailto culture**; LatAm foundation/DFI and US registered-adviser paths over-index in FOUNDs.
- **Parallelism:** 3–5 Hands arms is appropriate; Wave2 proved **hygiene + deferred PDF** arms complement but do not replace **PDF/regulatory-first** queues.

---

## Recommended next 3–5 method arms (toward goal 50)

Priority order for the **next Hands wave** (no Monday writes from this doc):

1. **Regulatory PDF queue (LatAm + EU + Canadian)**  
   - Targets: CNMV gestora “Atención al cliente” tabs, BCSC/SEDAR+ document viewer PDFs, CNMV/ECSPR-style fund docs, IAPD **Form ADV Part 2B supplements** (supervised persons).  
   - Query pattern: `"<full name>" "<fund legal name>" filetype:pdf` plus jurisdiction site operators (`site:bcsc.bc.ca`, `site:cnmv.es`, `site:adviserinfo.sec.gov`).

2. **Impact / LP / annual report PDF arm**  
   - DFI, development bank, “impact report”, “SFDR”, “PRI”, “annual report” PDFs where signatories list emails (Wave2 Inclimo + Deep50 Vox/United Way class).

3. **Press + podcast + conference show-notes**  
   - `"<name>" "<firm>" email`, `mailto:` on industry media; verify name anchor text (Deep50 Project A pattern).

4. **Curated directory sweep (allowed only)**  
   - Mercury investor DB profile pages; IFC/development finance disclosure pages; academic/government investor lists — **attribution filter:** same-page name + email only.

5. **Hygiene-gated re-crawl**  
   - For EMPTY seats with corrected Website from Wave2 #18/#19: **one** Photon/theHarvester-class **first-party domain** pass (see `01b-reddit-hn-github-notes.md`) → if no person `mailto`, **do not** third pass HTML; return to arms 1–2.

**Deprioritize for next wave:** Form D-only EDGAR, wide Wayback without prior signal of historical mailto, generic mailbox deepening.

---

## Status vocabulary (unchanged)

`FOUND` | `EMPTY` | `UNCERTAIN` (do not stamp) | `DOMAIN_UNRESOLVED`

**Hard rules retained:** No Hunter/Apollo primary; no LinkedIn scrape/Sales Nav/PhantomBuster; no pattern guessing or SMTP verify; no invented emails; stamp **published** local-part spelling only.
