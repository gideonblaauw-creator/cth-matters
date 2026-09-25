# L10 Arm 07 — negative audit excerpts

Method pass: public **CNPJ** (Brazil), **IAPD** Form ADV, **BCSC** search, **SEC EDGAR/EFTS**, **DocuSign** co-mentions in filings, **ethics/compliance PDFs**.

## Gate

**FOUND** requires a **named target person** and exact **person@firm** on the **same public page/PDF**. Generics (`proparco@`, `info@`, `complaints@`, `acumen-america@`, department inboxes) → **EMPTY**.

Input seats have **blank `contact_name`** — no Monday-specified individual to attribute; regulatory scans still run at firm level.

---

### Proparco (`proparco.fr`)

- **IAPD / Form ADV:** No Proparco-branded US adviser match with employee emails in brochure text.
- **SEC EFTS:** `"Proparco"` → 266 filing hits (Azure Power, Sabesp, etc.); `"@proparco.fr"` → **0** full-text hits. Signature blocks name officers (e.g. Philippe Bassery) with **address/fax only**, no `@proparco.fr` in examined exhibits.
- **Ethics PDF:** `ethics-charter-afd.pdf` — **no** email addresses in extracted text.
- **ICM policy PDF:** Only `complaints@icm-complaintsmechanism.org` (third-party ICM desk, not a named Proparco officer).
- **CNPJ:** Public lookup for French entity RCS 310792205 / formatted CNPJ rejected as invalid on BrasilAPI/publica.cnpj.ws (no Brazilian registration surfaced on these endpoints).

### Rabobank Partnerships (`rabobank.com`)

- **EFTS:** `"@rabobank.com"` → 170 hits; `"Rabobank" + code of conduct` → 1516 hits — typical **department** mailboxes (e.g. `Bedrijven.uhr@rabobank.nl`) without a named Partnerships contact on the same block.
- **IAPD:** Firm name search returned no Rabobank Partnerships adviser with Part 2 employee emails.
- **DocuSign + Rabobank (EFTS):** Large hit volume; filings reference **PDF/email execution** clauses, not person@rabobank.com contact tables for a named seat target.
- **BCSC:** Portal search executed; no Goodwell/Manutara-class 45-106F1 name+email block tied to this seat.

### Acumen (`acumen.org`)

- **IAPD CRD 174380 (Acumen Fund, Inc. ERA):** Form ADV PDF — phone/fax/website; **Chief Compliance Officer email field blank**; no `@acumen.org` person mailboxes in Items 1–11 extracted text.
- **IAPD CRD 285564 (Acumen Capital Partners LLC, active):** Form ADV — **no** extracted email addresses.
- **EFTS:** `"@acumen.org"` → **0** hits.
- **Excluded:** `acumen-america@acumen.org` on Acumen America contact page (generic investment desk, no named person on same block).

### Goodwell Investments (`goodwell.nl`)

- **IAPD:** `"Goodwell Investments"` API search does not map to a Goodwell.nl adviser (CRD 318378 resolves to unrelated **Bedinghaus Financial Group**).
- **Form ADV 318378 PDF:** 23 pages, **zero** email strings in text extraction.
- **EFTS `"Goodwell"` + `@`:** 122 hits are **unrelated** issuers (Goodwell Fitness Network, etc.), not goodwell.nl staff.
- **Site:** Responsible tax policy cites **info@goodwell.nl** only (generic).

### Manutara Ventures (`manutaravc.com`)

- **EFTS:** `"Manutara"`, `"manutaravc"`, `"Manutara Ventures"` → **0** hits. No SEC Form D located for Manutara Ventures (Cristian Olea name hits tie to **other** issuers, e.g. Buildlovers Inc.).
- **First-party about:** **info@manutaravc.com** only (generic); team names listed without personal mailboxes on same page.
- **DocuSign + Manutara (EFTS):** **0** hits.
