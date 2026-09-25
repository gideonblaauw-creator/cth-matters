# Wave5 L04 Arm-05 — Regulatory with mailbox (scorecard)

**Method:** Public regulatory filings / registries / adviser disclosures containing mailboxes. **FOUND** requires target `Contact_name` and personal `person@firm` email in the **same** artifact.

| Monday_item_id | Contact | Firm | Status | Email | Citation |
|----------------|---------|------|--------|-------|----------|
| 13132419019 | Mo Barhoush | Bicycle Capital | EMPTY | — | Form D name-only (Barhoush not in filing) |
| 13132422879 | Nabeel Hyatt | Spark Capital | EMPTY | — | IAPD ADV + Wayfair DRS: no Hyatt mailbox |
| 13132422922 | Nichole Wischoff | Wischoff Ventures | EMPTY | — | Form D signatures without email |
| 13132412695 | Paula Giraldo | 30N Ventures | EMPTY | — | No SEC/CMF artifact with Giraldo + @30n.vc |
| 13132412712 | Pepe Bolaños | COMETA | EMPTY | — | Cometa IV Form D: Bolanos, no email |

## Totals

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Notes

- **Bicycle / Barhoush:** Form D for Bicycle I, L.P. confirms fund vehicle; partner not disclosed and no emails in XML.
- **Spark / Hyatt:** Closest regulatory mailbox is `alex@sparkcapital.com` tied to Alex Finkelstein in Wayfair DRS — not promoted to Hyatt.
- **Wischoff:** Multiple Form D vehicles name Nichole Wischoff; standard Form D name/address-only pattern (W2 lesson).
- **30N / Giraldo:** No Form D hit for Emerging Founders I; CMF private-fund manager index has no 30N Ventures match with contact email.
- **Cometa / Bolaños:** SEC Form D uses legal name Jose Luis Bolanos Flores; still no email block.

Evidence: `evidence/negative-excerpts.md`, `evidence/url-index.md`, Form D snapshots under `evidence/`.
