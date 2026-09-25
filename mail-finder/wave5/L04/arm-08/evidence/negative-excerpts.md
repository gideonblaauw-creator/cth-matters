# Negative regulatory audit — Wave5 L04 Arm 08

Method gate: **FOUND** requires **Contact_name** + exact non-generic **person@firm** on the **same** public regulatory HTML/PDF/filing block.

## Steven Lambe / Trinity Capital

- EFTS `"Steven Lambe"`: **0** hits.
- EFTS `Lambe` + CIK `0001786108` (Trinity Capital Inc.): **0** hits.
- Trinity SEC exhibits may list `sstanton@trincapinvestment.com` (Corporate Secretary) — different person; not Lambe.
- Seat domain `trinitycap.com` aligns with listed BDC **Trinity Capital Inc.** (`trincapinvestment.com`); no regulatory email field pairs Lambe.

## Tiago Wigman / L4 Venture Builder

- CNPJ **45.653.567/0001-03**: partners include **TIAGO WIGMAN** (Sócio-Administrador); establishment email **fiscal@praxia.com.br** (accounting provider) — not a personal `@l4` mailbox and not name-attributed to Tiago on the CNPJ record.
- CVM process **19957.012745/2022-64** / annex PDF **2810_23.pdf**: L4 VB FIP authorization text; no Wigman contact block with email.

## Will Poole / Capria Ventures

- IAPD **CAPRIA VENTURES LLC** CRD **284129** — Form ADV PDF downloaded; no `@capria.vc` person lines with Will Poole.
- Form D examples (Capria Ventures LLC; Capria Opportunities LP series): **William Poole** in `relatedPersonsList` with address only — XML schema has no email element.

## William A. Mejia / Arrebol Capital

- EDGAR full-text: **0** for Mejia + Arrebol + `@arrebol.capital` / `@arrebol.vc`.
- No IAPD registered adviser match for Arrebol Capital in SEC search API.

## Bobby Aitkenhead / IDC Ventures

- Sole EDGAR name hit: **Axela Technologies, Inc.** Form D (2021-01-20) — not IDC Ventures; Form D does not publish officer emails.
- CNMV public entity search landing pages consulted; no retrieved **sociedad gestora** record with Aitkenhead + personal email.
