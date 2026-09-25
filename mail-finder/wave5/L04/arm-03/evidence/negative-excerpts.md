# Regulatory-with-mailbox — negative evidence (Wave5 L04 Arm 03)

## Gate

**FOUND** requires `Contact_name` and a personal `person@firm` email in the **same** public regulatory HTML/PDF artifact. Form D / ADV Part 1 name-only rows do not qualify.

## Jonathan Whittle / Quona Capital

**IAPD Form ADV (CRD 277131)** — Schedule A lists the target without any email:

```
WHITTLE, JONATHON, HAROLD
I
MEMBER
...
```

Only non-mailbox web reference in ADV text: `https://medium.com/@Quona_Capital15` (firm social URL, not a personal mailbox).

**Accion Quona Inclusion Fund Form D (2019)** — related person name only; XML contains no `@` fields (see `quona-accion-formd-2019.xml`).

**EDGAR full-text:** 0 hits for `@quona.com`; 0 for `"Jonathan Whittle" AND @`.

## Keiji Matsunaga / SMBC

**EDGAR full-text:** 0 hits for exact `"Keiji Matsunaga"`. Matsunaga+SMBC boolean matches unrelated issuers (Sony 6-K, mutual fund N-PX tables), not SMBC officer contact blocks with personal email.

**SMFG SEC disclosure page** lists Form 3/4 filers for group officers; Keiji Matsunaga not among named SEC filers (role is SMBC Digital Strategy GM — not in US EDGAR officer roster with email).

## Lachy Groom / Lachy Groom (fund)

**EDGAR:** 34 Form D hits naming Lachy Groom as signer/related person; sampled primary docs (e.g. LGF Inquisitive Imagination LP 2021) show signature blocks without email fields. `@lachygroom.com` → 0 EDGAR full-text hits.

**IAPD:** 0 firm hits for “Lachy Groom”; no adviser brochure with mailbox.

## Lauren Morton / QED Investors

**IAPD Form ADV (CRD 284908)** — entire ADV PDF text contains **no** `@` character sequences (no employee or CCO email published in this regulatory package). Target name not present in ADV Part 1 schedules.

**EDGAR:** `@qedinvestors.com` → 0 full-text hits; `"Lauren Morton" AND @` → 0. Form D corpus for QED entities lists Morris/Cilluffo/Rotman et al., not Lauren Morton, and XML has no person emails.

## Lawrence G. Chua / Accial Capital

**IAPD Form ADV (CRD 305587, INACTIVE)** — no `@` in PDF text; Lawrence Chua not in Schedule A/B control persons (Miller, Fernandez, Davis, etc.).

**Accial Credit Impact Fund / Secured Accial Impact Lending Form D (2026, 2023)** — no email fields; Chua not listed.

**EDGAR:** `"Lawrence Chua" Accial` → 0; `@accialcapital.com` → 0.
