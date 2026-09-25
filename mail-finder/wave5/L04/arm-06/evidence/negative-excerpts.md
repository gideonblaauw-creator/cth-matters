# Wave5 L04 Arm 06 — regulatory-with-mailbox negative excerpts

Method gate: **FOUND** only when `Contact_name` and personal `person@firm` appear in the **same** public regulatory HTML/PDF artifact.

## Rachel Holt — Construct Capital

**Form D — Construct Capital III Operators Fund (2025-03-31)**  
Source: https://www.sec.gov/Archives/edgar/data/2066159/000206615925000002/xslFormDX01/primary_doc.xml

```text
Last Name: Holt | First Name: Rachel
Street: 3516 Connecticut Ave NW, Floor 3, Washington, DC 20008
Relationship: Director — Managing Director of the General Partner
(no emailAddress / primaryEmail fields in relatedPerson block)
```

**Form ADV Part 1 (CRD 310594)** — Schedule A control person listing only:

```text
Holt, Rachel | MANAGER | 01/2020 | Individual control person ID 7299404
(no @construct.capital in extracted Part 1 text)
```

**EDGAR full-text:** `"Rachel Holt" AND "@"` → 0 hits.

## Roy Bahat — Bloomberg Beta

**Form D — UCode, Inc. (2016)**  
Source: https://www.sec.gov/Archives/edgar/data/1673389/000167338916000001/xslFormDX01/primary_doc.xml

```text
Related person Last Name: Bahat (no mailbox in XML)
```

**Form D — Cobalt Robotics Inc. (2019)** — Bahat listed as related person; no `@` in `primary_doc.xml`.

**EDGAR full-text:** `"Roy Bahat" AND "@"` → 0 hits; `"@bloombergbeta.com"` → 0 hits. Bloomberg Beta is not an SEC-registered adviser (IAPD firm search empty).

**Form C — Inside.com, Inc. (2021)** — regulatory crowdfunding header/issuer block; no Roy Bahat contact email in `primary_doc.xml`.

## Rafa de la Guia — Quona Capital

**Form D — Accion Quona Inclusion Fund, L.P. (2018)**  
Source: https://www.sec.gov/Archives/edgar/data/1755618/000175561818000001/xslFormDX01/primary_doc.xml

Related persons include Jonathan Whittle, Monica Brand, Livingston Parsons III — **Rafa de la Guia not listed**; **no `@quona.com` addresses** in XML.

**Form ADV Part 1 (CRD 277131)** — firm website/social links include `https://medium.com/@Quona_Capital15` (firm social handle, not a personal `person@quona.com` bound to Rafa).

**EDGAR full-text:** `"Rafa de la Guia"`, `"Rafael de la Guia"`, `"de la Guia" AND "@"` → 0 hits.

## Rodolfo Elias Dieck — Proeza Ventures

**SEC 8-K — Dila Capital Acquisition Corp (2021)** mentions Grupo Proeza / Proeza Ventures in director biography context; **no Rodolfo Elias Dieck mailbox** on page.

**XOS / NextGen 8-K (2021)** — `"Rodolfo Dieck"` appears as board member in deck excerpt; surrounding contact blocks list counsel/issuer emails (`pford@nextgenacq.com`, law-firm addresses) **not** `@proezaventures.com` for Dieck.

**EDGAR:** `"Rodolfo Elias Dieck"` → 0 hits; `"@proezaventures.com"` → 0 hits.

## Rodrigo Velasco — BBVA Spark

**BBVA parent 6-K (2024-07-31)** — organizational text references **BBVA Spark** unit; no **Rodrigo Velasco** + email block.  
Source: https://www.sec.gov/Archives/edgar/data/842180/000119312524189584/d787734d6k.htm

**EDGAR full-text:** `"Rodrigo Velasco" AND "@"` → 0 hits; `"@bbvaspark.com"` → 0 hits.
