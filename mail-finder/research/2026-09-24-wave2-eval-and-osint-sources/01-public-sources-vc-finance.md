# Public sources catalogue — VC / PE / CVC / impact / LatAm finance

**Purpose:** Improve Mail Finder’s **allowed** public-source stack for citation-grade `person@firm`.  
**Not in scope:** Paid enrichment APIs, LinkedIn automation, pattern guessing, SMTP verification, breach dumps.

Each entry includes **why it works**, **limits**, and **example query patterns** (legal public search / registry navigation only).

---

## 1. US SEC — EDGAR (exhibits & registrations, not Form D body alone)

| Source | URL | Why it works | Limits | Example patterns |
|--------|-----|--------------|--------|------------------|
| EDGAR full-text search | https://www.sec.gov/edgar/search/ | Exhibits, merger docs, credit agreements often contain **signature blocks** with email ([Deep50 i80 exhibit](https://www.sec.gov/Archives/edgar/data/1441082/000147793222007571/hlco_ex1018.htm)) | Form D **does not** collect issuer email ([Form D PDF Item 2](https://www.sec.gov/files/formd.pdf)) | `"<person name>" "<fund name>"` in EDGAR; filter **EX-10**, **EX-99** attachments |
| Form D (context only) | https://www.sec.gov/edgar/search/#/dateRange=custom&category=form-cat1&entityName= | Names **executive officers, directors, promoters, control persons** for VC funds ([sample Form D XML](https://www.sec.gov/Archives/edgar/data/1902507/000190250722000001/xslFormDX01/primary_doc.xml?stream=top)) | Phone/address only in Item 2; use names to pivot to IAPD/brochures | Entity search → fund LP/GP legal name → officer list |
| 13F / institutional holdings | EDGAR 13F-HR | Identifies managers; occasional cover letters | Rarely personal email | Manager name → IAPD / firm site press |

---

## 2. IAPD / Form ADV (investment advisers & ERAs)

| Source | URL | Why it works | Limits | Example patterns |
|--------|-----|--------------|--------|------------------|
| IAPD firm search | https://adviserinfo.sec.gov/ | **Part 2A brochure** must include contact email on cover ([Form ADV Part 2 spec](https://www.sec.gov/about/forms/formadv-part2.pdf)) | Often **general** firm inbox, not each partner | Firm legal name → Brochure PDF → search `@` |
| Part 2B brochure supplements | IAPD brochure library | **Supervised persons** disclosure (names + roles); some filings include direct lines/emails in supplements ([SEC ADV amendments rule discussion](https://www.sec.gov/files/rules/final/2010/ia-3060.pdf)) | Not every GP files 2B with email | Download latest Part 2B PDF → full-text person name |
| IARD registration guide | https://www.sec.gov/about/divisions-offices/division-investment-management/electronic-filing-investment-advisers-iard/electronic-filing-investment-advisers-iard-how-register-sec-investment-adviser-how-file-reports-sec | Confirms public brochure filing duty | — | Cross-check exempt reporting advisers (venture sub-advisers) |

---

## 3. Canada — BCSC / SEDAR+ (exempt distributions & fund docs)

| Source | URL | Why it works | Limits | Example patterns |
|--------|-----|--------------|--------|------------------|
| BCSC document viewer | https://www.bcsc.bc.ca/documents/ | **Form 45-106F1** PDFs can bind GP manager name + email + signature ([Deep50 AutoTech doc](https://www.bcsc.bc.ca/documents/view/J7B1B6G7K7I5K7XBP6P2K7S8Y7M0)) | Not all schedules public on web; SEDAR+ migration gaps ([SEDAR+ FAQ](https://systems.securities-administrators.ca/onlinehelp/faqs/report-of-exempt-distribution-filings-45-106f1/)) | BCSC search → `"Report of Exempt Distribution"` + fund name |
| Form 45-106F1 template | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/139_2023_Form%2045-106F1 | Shows purchaser/contact fields in regulatory schema | Purchaser PII often redacted in published copies | Use **issuer-side** signatory blocks, not purchaser tables |
| SEDAR+ issuer profiles | https://www.sedarplus.ca/ | Prospectus, annual MD&A, material change reports for Canadian issuers & some funds | Login for some filings; respect terms | Issuer name → management information circular |

---

## 4. EU / Spain — CNMV (gestoras, SCR, ELTIF-style)

| Source | URL | Why it works | Limits | Example patterns |
|--------|-----|--------------|--------|------------------|
| CNMV gestora registry | https://www.cnmv.es/portal/consultas/entregiic?lang=es | **Atención al cliente** view can list **named department head + email** ([example gestora tab](https://www.cnmv.es/portal/consultas/iic/sgiic?lang=eu&nif=A42939678&vista=16)) | Often **client service** email, not partner; still useful for small SCR | Search gestora legal name → vista=Atención al cliente |
| CNMV IIC registers | https://www.cnmv.es/portal/menu/registros-oficiales-iic?lang=es | Official register of fund managers / AIFs | Person email usually on gestora page, not fund page | NIF / registry number from fund factsheet → gestora |

---

## 5. LatAm — securities & corporate registries

| Source | URL | Why it works | Limits | Example patterns |
|--------|-----|--------------|--------|------------------|
| Brazil CNPJ (Receita / public consult) | https://www.gov.br/receitafederal/ | Legal entity name, cadastral status for **fund vehicles & gestoras** | Email rarely in CNPJ card; use for **entity resolution** | CNPJ or razão social → confirm fund GP spelling |
| CVM (Brazil) | https://www.gov.br/cvm/ | Fund registers, advisers, disclosure PDFs | Portuguese-only; PDF-heavy | `"<gestora>" CVM filetype:pdf` |
| Colombia / Mexico / Chile supervisors | SFC, CNBV, CMF portals | Issuer & fund filings, ethics codes (Deep50 Colombia ethics PDF class) | Inconsistent email publication | `"código de ética" "<foundation or fund>" filetype:pdf` |
| **DFI / development finance PDFs** | IDB, IFC, Proparco, DEG public docs | Signatory pages for impact funds (**Wave2 Inclimo** class) | Ad hoc indexing | `"<person>" "<fund>" inversión impacto filetype:pdf` |

---

## 6. OpenCorporates & national company registers

| Source | URL | Why it works | Limits | Example patterns |
|--------|-----|--------------|--------|------------------|
| OpenCorporates web + API | https://opencorporates.com/ ; API ref: https://api.opencorporates.com/documentation/API-Reference | **Officer search** ties person ↔ company number ([officer search docs](https://knowledge.opencorporates.com/knowledge-base/searching-for-an-officer/)) | **No email** in core officer record; use for **DOMAIN_UNRESOLVED** | `GET .../officers/search?q=<name>&jurisdiction_code=<code>` |
| Terms | https://opencorporates.com/terms-of-use-2/ | API keys for programmatic use; personal vs commercial rules | Rate limits | Manual web UI acceptable for Hands |

---

## 7. Firm-published web (first-party only)

| Source | Where | Why it works | Limits | Example patterns |
|--------|-------|--------------|--------|------------------|
| Team / partners pages | `https://<domain>/team`, `/people`, `/partners` | Real `mailto:` in HTML/JSON-LD | Modern VC sites often **form-only** | View-source / cached HTML; stop after generics |
| Press / newsroom | `/news`, `/perspectives`, `/blog` | Author byline + footnote email ([Citi Ventures pattern](https://www.citi.com/ventures/perspectives/opinion/agents-as-a-service-evolution.html)) | Corporate CMS may hide mailto | `site:<domain> "<name>"` |
| Press kits & media PDFs | `/press`, `/media` | Contact tables with named IR/press | May be generic | PDF download → full-text name |

---

## 8. Curated public directories (not paid finders)

| Source | URL | Why it works | Limits | Example patterns |
|--------|-----|--------------|--------|------------------|
| Mercury Investor Database | https://mercury.com/investor-database | Many profiles expose **Contact Email** on same page as name ([example profile structure](https://mercury.com/investor-database/aileen-lee)) | Coverage ~hundreds not thousands; some profiles email-free | Browse by stage/geo → open profile → verify person match |
| Mercury blog (scope) | https://mercury.com/blog/investor-db | Explains DB intent & filters | — | — |
| IFC / MDB project disclosures | https://disclosures.ifc.org/ | Project docs with responsible officers | Project finance bias | Officer name in disclosure PDF |
| University / accelerator cohort lists | Program sites | Cohort PDFs with mentor email | Stale | `"<program>" mentors filetype:pdf` |

**Forbidden for Mail Finder:** Third-party **bulk scrape APIs** of Mercury (e.g. marketplace scrapers) — use **human Hands on public profile pages** only.

---

## 9. Wayback Machine / CDX (historical first-party)

| Source | URL | Why it works | Limits | Example patterns |
|--------|-----|--------------|--------|------------------|
| CDX API | https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md | Finds dated `/team` captures when live site lost mailto ([IA tutorial](https://archive.org/developers/tutorial-compare-snapshot-wayback.html)) | Wave2: **0/18** when history never had mailto | `https://web.archive.org/cdx/search/cdx?url=<domain>/team*&output=json&filter=statuscode:200` |
| Wayback overview | http://archive.org/help/wayback_api.php | — | Rate limits; attribution still required | Compare two snapshots for `mailto:` diff |

---

## 10. DNS / WHOIS (hygiene only)

| Use | Allowed | Forbidden |
|-----|---------|-----------|
| Confirm **registrant org** matches fund | WHOIS/RDAP for domain sanity | Inventing `first.last@` from WHOIS privacy |
| Find **alternate corporate domains** | NS/MX hints for parked vs live | SMTP probe / catch-all spray |
| Wave2 domain cleanup (#19) | 15 domains resolved, 10 Website fixes | — |

---

## 11. Legal search engine patterns (PDF-first)

Use on **public indexes** (Google/Bing/DuckDuckGo web search — no auth bypass):

```
"<First Last>" "<Fund Brand>" filetype:pdf
site:bcsc.bc.ca "<Fund legal name>"
site:sec.gov "<person name>" "@"
site:cnmv.es "<gestora>" correo electrónico
site:<firm-domain> filetype:pdf team
"<Fund>" "Form 45-106F1"
"<Fund>" "brochure supplement" filetype:pdf
```

Always require **name + email co-occurrence** in the same citation fragment (sentence, signature block, or mailto anchor).

---

## 12. ALLOWED vs FORBIDDEN (public-source stack)

| Category | ALLOWED | FORBIDDEN |
|----------|---------|-----------|
| Registries & filings | SEC EDGAR exhibits, IAPD PDFs, BCSC/SEDAR+, CNMV, CNPJ/CVM, OpenCorporates for identity | Credential stuffing portals; bypassing paywalls |
| Firm pages | Team mailto, press footnotes, LP reports | Scraping LinkedIn/Sales Nav; PhantomBuster |
| Directories | Mercury public profiles, IFC, academic/podcast show notes | Hunter/Apollo/ContactOut as **primary** |
| OSINT tools | theHarvester/Photon on **firm domain** with attribution filter | Breach dumps; paste-site PII |
| Verification | Human read of published source | SMTP RCPT TO / pattern guess + verify |

See also: `01b-reddit-hn-github-notes.md` for practitioner sentiment and tool tagging.

---

## Primary references (cited)

1. https://www.sec.gov/files/formd.pdf  
2. https://www.sec.gov/about/forms/formadv-part2.pdf  
3. https://www.bcsc.bc.ca/documents/view/J7B1B6G7K7I5K7XBP6P2K7S8Y7M0  
4. https://systems.securities-administrators.ca/onlinehelp/faqs/report-of-exempt-distribution-filings-45-106f1/  
5. https://www.cnmv.es/portal/consultas/entregiic?lang=es  
6. https://mercury.com/investor-database  
7. https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md  
8. https://api.opencorporates.com/documentation/API-Reference  
9. https://raw.githubusercontent.com/laramies/theHarvester/master/README.md  
10. https://github.com/s0md3v/Photon/blob/master/README.md  
