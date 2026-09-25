# Reddit / Hacker News / GitHub — practitioner notes (2026-09-24)

**Scope:** What practitioners **claim** works for corporate email discovery, mapped to Mail Finder protocol tags:

- **ALLOWED** — fits citation-grade public-source rules  
- **FORBIDDEN** — must not appear in Hands playbooks  
- **HITL** — allowed only with human review (no automation against ToS)

**Sample bias:** Threads skew toward **cold email / sales** and **OSINT hobbyists**; VC partners are under-represented. Success rates cited (30–70%) usually mean **any** mailbox, not **named person@firm**.

---

## Summary table

| Source | Practitioner theme | Mail Finder tag | Notes |
|--------|-------------------|-----------------|-------|
| r/coldemail — domain lists | Crawl contact/about/footer; role emails | ALLOWED (person+name only) | Generics without name → EMPTY |
| r/coldemail — Hunter/Apollo/Clay | Paid waterfall enrichment | **FORBIDDEN** as primary | May mention for context only |
| r/coldemail — pattern `info@`, `firstname@` | Guessing common patterns | **FORBIDDEN** | Conflicts with no pattern-guess rule |
| r/coldemail — LinkedIn contact info | Visible email on profile | **HITL** | No Sales Nav export / scrape |
| r/coldemail — evaboot / emailchaser | Sales Nav Chrome extensions | **FORBIDDEN** | Same as PhantomBuster class |
| r/OSINT — theHarvester | Public multi-source harvest | ALLOWED (filtered) | Disable breach/Hunter modules; attribute |
| r/OSINT — hunter.io / snov.io | Domain search APIs | **FORBIDDEN** | |
| r/OSINT — data breach dumps | Expand emails at domain | **FORBIDDEN** | |
| HN — Email Sleuth | Pattern gen + site scrape + **SMTP verify** | **FORBIDDEN** (verify + guess) | Website scrape part is ALLOWED if isolated |
| HN — Apollo-powered job finder | B2B database API | **FORBIDDEN** | |
| GitHub — theHarvester README | Search engines, cert transparency, GitHub code | ALLOWED (no API keys for Hunter) | Filter to firm-domain attribution |
| GitHub — Photon README | Fast crawler extracts emails from pages/PDFs | ALLOWED (first-party domain, polite) | `--wayback` seed is ALLOWED |

---

## Reddit

### r/coldemail — bulk websites without names

**URL:** https://www.reddit.com/r/coldemail/comments/1q1xqcz/how_to_find_email_addresses_from_list_of_websites/

**Practitioner claims:** Upload domains to Saleshandy / Anymail Finder / Hunter domain search; crawl contact pages for role emails; expect partial coverage.

**Mail Finder:**  
- **ALLOWED:** First-party crawl of contact/about for **`mailto:` co-occurring with a target name** (not implemented as bulk unsupervised stamp).  
- **FORBIDDEN:** Hunter domain search as primary; Saleshandy-style bulk enrichment.  
- **EMPTY rule:** Role-only `info@` without person → escalate to PDF/filings.

---

### r/coldemail — 1,000 company CSV enrichment

**URL:** https://www.reddit.com/r/coldemail/comments/1q31z45/i_have_a_list_of_1000_companies_with_names_and/

**Practitioner claims:** Scrape websites; Clay/Apollo/Lelmagic waterfalls; ~40–50% coverage with many generics.

**Mail Finder:**  
- **FORBIDDEN:** Apollo/Clay/LeadMagic as discovery path.  
- **ALLOWED:** “Scrape websites” reinterpreted as **Hands review** of firm pages + press PDFs with citation.

---

### r/coldemail — local business emails

**URL:** https://www.reddit.com/r/coldemail/comments/1lzz83w/getting_email_of_businesses/

**Practitioner claims:** Pattern guessing (`info@`, `ownerfirstname@`); Hunter/Apollo/Tomba; LinkedIn contact info; **evaboot** Sales Nav extraction; coldmailthem web scraper.

**Mail Finder:**  
- **FORBIDDEN:** Pattern guessing; Apollo/Hunter/Tomba; evaboot; automated web scrapers without attribution.  
- **HITL:** LinkedIn **public** contact field if user pastes URL — same as Deep50 Satgana (public post), not automated extraction.

---

### r/OSINT — emails at a company given one address

**URL:** https://www.reddit.com/r/OSINT/comments/100tn5g/email_address_accounts/

**Practitioner claims (top comments):** Phonebook.cz; **hunter.io**; **data breach dumps**; snov.io; MX toolbox; **EmailHarvester / theHarvester**.

**Mail Finder:**  
- **ALLOWED:** theHarvester-style **public** source aggregation with **manual attribution** per seat ([theHarvester README](https://raw.githubusercontent.com/laramies/theHarvester/master/README.md)).  
- **FORBIDDEN:** Breach dumps; Hunter/Snov as discovery.  
- **HITL / hygiene:** MX lookup for domain existence only — not email invention.

---

### r/coldemail — CEO email from website or LinkedIn

**URL:** https://www.reddit.com/r/coldemail/comments/1i9q743/how_to_find_ceo_name_and_email_using_company/

**Practitioner claims:** Hunter, Snov, Lusha, Kaspr — LinkedIn extraction tools.

**Mail Finder:** **FORBIDDEN** wholesale. **ALLOWED** pivot: CEO name from **annual report / IAPD / registry** → PDF/press email search.

---

## Hacker News

### Show HN: Email Sleuth (Rust CLI)

**URL:** https://news.ycombinator.com/item?id=43804665  
**Repo context:** SMTP RCPT TO verification + common pattern generation + site scrape ([discussion confirms catch-all issues](https://news.ycombinator.com/item?id=43804665)).

**Mail Finder:**  
- **FORBIDDEN:** Pattern generation; SMTP RCPT TO verification (same class as “verify spray”).  
- **ALLOWED (concept only):** Extract **published** emails from company website HTTP(S) pages — Mail Finder already does via Hands + html cache.

---

### Show HN: Dropzone (Apollo API)

**URL:** https://news.ycombinator.com/item?id=47373242

**Practitioner claims:** People search powered by **Apollo.io API** (`api_search`, `people/match`).

**Mail Finder:** **FORBIDDEN** — paid B2B database, not citation-grade public co-occurrence.

---

### Ask HN: AI agents vs Apollo for enrichment

**URL:** https://news.ycombinator.com/item?id=41340442

**Practitioner claims:** LLM trained to infer emails from name + domain; compares to Apollo accuracy.

**Mail Finder:** **FORBIDDEN** — inferred emails violate “no pattern guess / no invented emails”. LLM may **suggest search queries** only, not outputs to stamp.

---

### Show HN: Telescope company research

**URL:** https://news.ycombinator.com/item?id=39203463

**Practitioner claims:** Multi-search synthesis for company research (not email-specific).

**Mail Finder:** **ALLOWED** as inspiration for **query diversification** (press + registry + filings), not automated stamping.

---

## GitHub / tool docs

### theHarvester (laramies)

**URL:** https://github.com/laramies/theHarvester?tab=readme-ov-file  
**Raw README:** https://raw.githubusercontent.com/laramies/theHarvester/master/README.md

**Practitioner / author claims:** Aggregates emails from search engines, cert transparency, DNS datasets, code repos, etc.; optional modules for **Hunter**, Shodan, breaches.

**Mail Finder:**  
- **ALLOWED:** Passive modules without paid keys (e.g. search-engine discovery) → **candidate URLs only**; human confirms name+email on page/PDF.  
- **FORBIDDEN:** Hunter module; breach name modules; treating output as FOUND without citation.

---

### Photon (s0md3v)

**URL:** https://github.com/s0md3v/Photon/blob/master/README.md  
**Usage wiki:** https://github.com/s0md3v/Photon/wiki/Usage

**Practitioner claims:** Crawls target site; extracts **intel** (emails), files (PDF), JS endpoints; optional `--wayback` seeds from archive.org.

**Mail Finder:**  
- **ALLOWED:** Single-domain, low-depth crawl on **firm-owned domain** after hygiene pass; export PDF URLs for Hands review.  
- **FORBIDDEN:** `--cookie` for authenticated areas; high-thread aggressive crawl against bot walls; stamping extracted emails without person co-occurrence.

---

## Cross-cutting practitioner themes → protocol

1. **“Domain search tools” (Hunter/Apollo)** dominate Reddit/HN advice → Mail Finder explicitly rejects as **primary**; public filings PDFs out-yielded them in Deep50/Wave2.
2. **Website crawl** is universally recommended → Mail Finder keeps it **tertiary** after PDF/regulatory/press because VC team pages rarely expose partner mailto.
3. **SMTP verify / pattern tools** appear on HN Show HN → **FORBIDDEN**; practitioners admit catch-all false positives.
4. **LinkedIn** appears in every sales thread → **HITL only** on public artifacts (posts, visible contact), never Sales Nav / PhantomBuster / evaboot.
5. **theHarvester / Photon** align with OSINT community → **ALLOWED** as **assistive discovery** with strict attribution filter, not autonomous Monday stamps.

---

## Cited URLs (≥8)

1. https://www.reddit.com/r/coldemail/comments/1q1xqcz/how_to_find_email_addresses_from_list_of_websites/  
2. https://www.reddit.com/r/coldemail/comments/1q31z45/i_have_a_list_of_1000_companies_with_names_and/  
3. https://www.reddit.com/r/coldemail/comments/1lzz83w/getting_email_of_businesses/  
4. https://www.reddit.com/r/OSINT/comments/100tn5g/email_address_accounts/  
5. https://www.reddit.com/r/coldemail/comments/1i9q743/how_to_find_ceo_name_and_email_using_company/  
6. https://news.ycombinator.com/item?id=43804665  
7. https://news.ycombinator.com/item?id=47373242  
8. https://github.com/laramies/theHarvester?tab=readme-ov-file  
9. https://github.com/s0md3v/Photon/blob/master/README.md  
10. https://raw.githubusercontent.com/laramies/theHarvester/master/README.md  
