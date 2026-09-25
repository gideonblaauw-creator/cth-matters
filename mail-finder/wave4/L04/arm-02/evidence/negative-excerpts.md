# SEC EDGAR exhibits / Form D / signature blocks — negative evidence (L04 Arm 02)

Method gate: **FOUND** requires target person’s published name and exact `person@firm` email in the **same** public filing artifact or exhibit.

---

## David García Acero — BBVA Spark (`EMPTY`)

**EDGAR full-text:** `"Garcia Acero"` → 0 hits; `"David Garcia" AND "BBVA Spark"` → 0 name-attributed filings; `@bbvaspark.com` → 0 hits (`efts_bbvaspark_domain.json`).

**BBVA parent 6-K (2024-07-31):** References BBVA Spark organizationally; contact block is corporate IR/comms only — not David García Acero:

```
comunicacion.corporativa@bbva.com
```

File: `bbva_6k_2024.htm` — no `@bbvaspark.com` and no “David García Acero” on the same artifact.

---

## Eduardo González Montes de Oca — BBVA Spark (`EMPTY`)

**EDGAR full-text:** `"Eduardo Gonzalez Montes"` → 0; `"Montes de Oca" BBVA` → 0; `@bbvaspark.com` → 0.

**Same BBVA 6-K:** `comunicacion.corporativa@bbva.com` without Eduardo González Montes de Oca (`bbva_6k_2024.htm`). No Form D / exhibit / signature block pairs Eduardo + person@bbvaspark.com.

---

## Edward Goldstein — i80 Group (`EMPTY`)

**Form D (i80 Group Specialty Finance LP, CIK 1717048, 2019-08-16):** Related person / signer **Marc Helwani**; **no `@i80group.com`** and **Edward Goldstein not named** in XML (`i80_form_d_2019.xml`).

**EDGAR full-text:** `"Edward Goldstein" AND "i80"` → 0; `"Edward Goldstein" AND "@i80group.com"` → 0. `"Edward Goldstein"` Form D hits (e.g. Pennington Alternative Income Fund) are unrelated issuers.

**Note:** `@i80group.com` appears in unrelated public-company 10-K text (Healing Co / HLCO) without Edward Goldstein co-attribution — excluded.

---

## Greg Reichow — Eclipse (`EMPTY`)

**Enovix EX-99.1 exhibit (press release, SEC filing):** Quotes Greg Reichow (Eclipse partner / Enovix director); contact emails on the same exhibit are **Enovix IR/PR** only:

```
Email: canderson@enovix.com
Email: gary@blueshirtgroup.com
```

File: `enovix_ex99-1.htm` — no `@eclipse.capital` / `@eclipse.vc` with Reichow.

**Form D (Symbio Robotics, 2018):** Lists `Reichow` as related person; **no email fields** in Form D XML (`symbio_form_d_2018.xml`).

**EDGAR full-text:** `"Greg Reichow" AND "@"` → 0; `@eclipse.capital` → 0.

---

## Iñaki García Llorente — Lendable (`EMPTY`)

**Form D (LENDABLE SPC, CIK 1816111):** 2022 and 2026 amendments reviewed — related-person blocks present; **no `@lendable.io`** addresses and **no “García Llorente” / “Llorente”** in filing XML (`lendable_form_d_2022.xml`, `lendable_form_d_2026.xml`).

**EDGAR full-text:** `"Inaki Garcia Llorente"` → 0; `@lendable.io` → 0.
