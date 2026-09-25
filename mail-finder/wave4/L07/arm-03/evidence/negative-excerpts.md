# Wave4 L07 Arm 03 — Negative excerpts (curated public investor directories)

Method gate: **FOUND** only when an exact person name and exact `person@firm` email co-occur on the **same** public directory record without login, subscription, or paywall. Generics and cross-record joins do not qualify.

## Mercury Investor Database

- Sitemap: `mercury_investor_sitemap.xml` (295 profile URLs).
- Automated scan of all profile pages: **0** hits for `acumen.org`, `goodwell`, `proparco`, `rabobank`, `manutara`, or related `@firm` domains.
- Reference profile (method calibration): `mercury_shruti_gandhi.html` exposes `shruti@array.vc` with investor name on the same page (Mercury-class positive control; not a seat match).

## OpenVC (`openvc.app`)

- Fund pages exist for **Acumen Fund** and **Goodwell Investments** (browser pass).
- Team names may appear in UI previews, but **person emails require founder login / paid upgrade** — fails Mercury-class open-access gate.
- Automated fetch from this environment returns Cloudflare challenge (`openvc_goodwell.html`).

## Private Equity International (institution profiles)

- **Goodwell Investments** (`https___www_privateequityinternational_com_institution_profiles_goodwell_investm.html`): contacts table lists e.g. **Ms. Els Boerhof** (Managing Partner); `email` fields in `__NEXT_DATA__` are redacted (`-----------`). Public firm inbox only: `contact@goodwell.nl` (generic, not person-attributed on same block).
- **Proparco** (`https___www_privateequityinternational_com_institution_profiles_proparco_html.html`): named contacts (e.g. **Mr. Adrien Baumlin**); person emails redacted. Public generic: `proparco@proparco.fr`.
- **Rabobank** (`https___www_privateequityinternational_com_institution_profiles_rabobank_html.html`): **Ms. Lidwien Schils** listed; person email redacted. Embedded org email `raboinvestments@rabobank.com` is **Rabo Investments** entity mail, not a named Partnerships contact on the same record.
- **Acumen** profile page loads but does not expose citation-grade person `@acumen.org` without subscription.

## The GIIN (member directory)

- **Acumen** member page (`https___thegiin_org_member_acumen_.html`, 200): firm narrative and website only — **no staff roster or emails**.
- Slugs `goodwell-investments`, `proparco`, `manutara`, `rabobank` → **404**.

## Private Equity List (`privateequitylist.com`)

- **Manutara Ventures** page states investment-team emails are on **Pro plan** ($129/mo) — paid bulk directory; excluded by arm rules.
- Public generic only: `info@manutaravc.com` (FAQ JSON-LD), without named partner on same open block.

## Firm-seat note

All five `input.csv` rows are **firm-level** seats (`contact_name` blank). Even where directories name partners, no open Mercury-class record pairs that person with `person@firm` email for attribution under this arm’s gate.
