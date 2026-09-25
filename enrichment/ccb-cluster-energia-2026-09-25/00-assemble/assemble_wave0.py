#!/usr/bin/env python3
"""Wave 0 — union micro-hand enrich CSVs, email gap, Resend stage, Mail Finder pilot cut."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WAVE = ROOT.parent

OUT_UNION = ROOT / "union.csv"
OUT_BLANK = ROOT / "email_blank.csv"
OUT_RESEND = ROOT / "resend_stage.csv"
OUT_PILOT = ROOT / "mailfinder_pilot_candidates.csv"
OUT_REPORT = ROOT / "REPORT.md"

ROLE_LOCAL = re.compile(
    r"^(info|contacto|contact|ventas|comercial|administracion|admin|contabilidad|"
    r"notificaciones|servicio|servicioalcliente|servicio_al_cliente|gerencia|"
    r"proyectos|contactenos|coordinacion|reportes|impuestos|facturacion|"
    r"soporte|recepcion|atencion|clientes|marketing|rrhh|recursos|legal|"
    r"promesaesp|ins)([._-]|$)",
    re.I,
)
ROLE_EXACT = {
    "info",
    "contacto",
    "ventas",
    "comercial",
    "administracion",
    "contabilidad",
    "gerencia",
}

SANTANDER_CITY_HINTS = (
    "bucaramanga",
    "giron",
    "girón",
    "floridablanca",
    "piedecuesta",
    "barbosa",
    "san gil",
    "sangil",
    "socorro",
    "málaga",
    "malaga",
    "lebríja",
    "lebrija",
    "santander",
)

METHOD_RANK = {"mailto": 0, "contact_page": 1, "homepage": 2}


def nit_join_key(nit: str | None) -> str:
    if not nit:
        return ""
    nit = str(nit).strip()
    base = nit.split("-", 1)[0] if "-" in nit else nit
    return re.sub(r"\D", "", base)


def clean_email(val: str | None) -> str:
    if not val:
        return ""
    v = str(val).strip()
    if not v or v.lower() in {"no provisto", "n/a", "na", "none", "null"}:
        return ""
    if "@" not in v:
        return ""
    return v


def classify_email(email: str, *, from_rep_legal: bool = False) -> str:
    if not email:
        return ""
    if from_rep_legal:
        return "PERSON"
    local = email.split("@", 1)[0].lower()
    local = local.split("+", 1)[0]
    if local in ROLE_EXACT or ROLE_LOCAL.search(local):
        return "ROLE"
    if re.match(r"^[a-z]+\.[a-z]+", local) and not any(
        x in local for x in ("servicio", "ventas", "info", "contact")
    ):
        return "PERSON"
    if re.match(r"^[a-z]{2,}\d*@?", local) and "." in local:
        parts = local.replace("_", ".").split(".")
        if len(parts) >= 2 and all(p.isalpha() and len(p) >= 2 for p in parts[:2]):
            return "PERSON"
    free = email.split("@", 1)[-1].lower()
    if free in {"gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "live.com"}:
        return "PERSON"
    return "UNKNOWN"


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@dataclass
class NitRecord:
    nit_display: str = ""
    razon_social: str = ""
    city: str = ""
    phone: str = ""
    website: str = ""
    contract_count: int = 0
    contract_sample_url: str = ""
    domain_hint: str = ""


@dataclass
class EmailCandidate:
    email: str
    source_arm: str
    source_url: str = ""
    from_rep_legal: bool = False
    priority: int = 99


def inventory_enrich_files() -> list[tuple[Path, int, bool]]:
    rows: list[tuple[Path, int, bool]] = []
    for p in sorted(WAVE.rglob("enrich.csv")):
        if "00-assemble" in p.parts:
            continue
        data = read_csv_rows(p)
        report = p.parent / "REPORT.md"
        rows.append((p, len(data), report.is_file()))
    return rows


def pick_website_email(rows: list[dict[str, str]]) -> EmailCandidate | None:
    ranked: list[tuple[int, int, str, dict[str, str]]] = []
    for i, row in enumerate(rows):
        em = clean_email(row.get("email"))
        if not em:
            continue
        method = (row.get("method") or "").strip().lower()
        ranked.append((METHOD_RANK.get(method, 9), i, em, row))
    if not ranked:
        return None
    ranked.sort(key=lambda x: (x[0], x[1]))
    _, _, em, row = ranked[0]
    return EmailCandidate(
        email=em,
        source_arm="07-company-websites",
        source_url=row.get("page_url") or "",
    )


def santander_score(city: str) -> int:
    c = (city or "").lower()
    if not c:
        return 0
    for i, hint in enumerate(SANTANDER_CITY_HINTS):
        if hint in c:
            return 100 - i
    if "santander" in c:
        return 50
    return 0


def main() -> None:
    inventory = inventory_enrich_files()

    records: dict[str, NitRecord] = {}
    email_options: dict[str, list[EmailCandidate]] = defaultdict(list)

    def ensure_nit(key: str, display: str) -> NitRecord:
        if key not in records:
            records[key] = NitRecord(nit_display=display or key)
        elif display and not records[key].nit_display:
            records[key].nit_display = display
        return records[key]

    # 01 — universe spine + SECOP proveedor emails
    p01 = WAVE / "01-secop-proveedores" / "enrich.csv"
    for row in read_csv_rows(p01):
        key = nit_join_key(row.get("nit"))
        if not key:
            continue
        rec = ensure_nit(key, row.get("nit") or "")
        if row.get("legal_name"):
            rec.razon_social = row["legal_name"]
        if row.get("city"):
            rec.city = row["city"]
        if row.get("phone"):
            rec.phone = row["phone"]
        if row.get("website"):
            rec.website = row["website"]
        em = clean_email(row.get("email"))
        em_rep = clean_email(row.get("email_rep_legal"))
        url = row.get("source_url") or ""
        if em:
            email_options[key].append(
                EmailCandidate(
                    email=em,
                    source_arm="01-secop-proveedores",
                    source_url=url,
                    from_rep_legal=False,
                    priority=1,
                )
            )
        if em_rep:
            email_options[key].append(
                EmailCandidate(
                    email=em_rep,
                    source_arm="01-secop-proveedores",
                    source_url=url,
                    from_rep_legal=True,
                    priority=1,
                )
            )

    # 07 — website mailto (grouped by NIT)
    p07 = WAVE / "07-company-websites" / "enrich.csv"
    by_nit_07: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_csv_rows(p07):
        key = nit_join_key(row.get("nit"))
        if not key:
            continue
        ensure_nit(key, row.get("nit") or "")
        by_nit_07[key].append(row)
        dom = (row.get("domain") or "").strip()
        if dom:
            records[key].domain_hint = dom
    for key, rows in by_nit_07.items():
        cand = pick_website_email(rows)
        if cand:
            cand.priority = 2
            email_options[key].append(cand)

    # 05 — SSPD
    for row in read_csv_rows(WAVE / "05-sspd-prestadores" / "enrich.csv"):
        key = nit_join_key(row.get("nit"))
        if not key:
            continue
        rec = ensure_nit(key, row.get("nit") or "")
        if row.get("razon_social_ccb") and not rec.razon_social:
            rec.razon_social = row["razon_social_ccb"]
        city = row.get("ciudad_ccb") or row.get("municipio_domicilio") or ""
        if city and not rec.city:
            rec.city = city
        if row.get("telefono") and not rec.phone:
            rec.phone = row["telefono"]
        em = clean_email(row.get("email"))
        if em:
            email_options[key].append(
                EmailCandidate(
                    email=em,
                    source_arm="05-sspd-prestadores",
                    source_url=f"sspd_dataset={row.get('sspd_dataset_id', '')}",
                    priority=3,
                )
            )

    # 06 — other CCB dumps
    for row in read_csv_rows(WAVE / "06-ccb-other-dumps" / "enrich.csv"):
        key = nit_join_key(row.get("nit"))
        if not key:
            continue
        rec = ensure_nit(key, row.get("nit") or "")
        if row.get("razon_social") and not rec.razon_social:
            rec.razon_social = row["razon_social"]
        if row.get("ciudad") and not rec.city:
            rec.city = row["ciudad"]
        if row.get("telefono") and not rec.phone:
            rec.phone = row["telefono"]
        em = clean_email(row.get("email"))
        if em:
            email_options[key].append(
                EmailCandidate(
                    email=em,
                    source_arm="06-ccb-other-dumps",
                    source_url=row.get("source_datasets") or "",
                    priority=4,
                )
            )

    # 08 — OC/GLEIF (emails usually empty)
    for row in read_csv_rows(WAVE / "08-opencorporates-gleif" / "enrich.csv"):
        key = nit_join_key(row.get("nit"))
        if not key:
            continue
        rec = ensure_nit(key, row.get("nit") or "")
        if row.get("name") and not rec.razon_social:
            rec.razon_social = row["name"]
        em = clean_email(row.get("email_if_any"))
        if em:
            email_options[key].append(
                EmailCandidate(
                    email=em,
                    source_arm="08-opencorporates-gleif",
                    source_url=row.get("oc_url") or "",
                    priority=5,
                )
            )

    # 02 — contract signal (no email arm)
    for row in read_csv_rows(WAVE / "02-secop-contratos" / "enrich.csv"):
        key = nit_join_key(row.get("nit"))
        if not key:
            continue
        rec = ensure_nit(key, row.get("nit") or "")
        if row.get("proveedor_name") and not rec.razon_social:
            rec.razon_social = row["proveedor_name"]
        try:
            rec.contract_count = max(rec.contract_count, int(row.get("contract_count") or 0))
        except ValueError:
            pass
        if row.get("sample_process_url") and not rec.contract_sample_url:
            rec.contract_sample_url = row["sample_process_url"]

    # 09 — licensed RUES API examples only (not in email priority list)
    rues_live_rows = 0
    for row in read_csv_rows(WAVE / "09-licensed-rues-apis" / "enrich.csv"):
        if (row.get("row_status") or "").startswith("EXAMPLE"):
            continue
        rues_live_rows += 1
        key = nit_join_key(row.get("nit"))
        if key:
            ensure_nit(key, row.get("nit") or "")

    ARM_ORDER = [
        "01-secop-proveedores",
        "07-company-websites",
        "05-sspd-prestadores",
        "06-ccb-other-dumps",
        "08-opencorporates-gleif",
    ]

    def choose_email(key: str) -> tuple[str, str, str, str, bool]:
        opts = email_options.get(key, [])
        if not opts:
            return "", "", "", "", False
        by_arm: dict[str, list[EmailCandidate]] = defaultdict(list)
        for o in opts:
            by_arm[o.source_arm].append(o)

        for arm in ARM_ORDER:
            arm_opts = by_arm.get(arm, [])
            if not arm_opts:
                continue
            if arm == "01-secop-proveedores":
                non_rep = [o for o in arm_opts if not o.from_rep_legal]
                if non_rep:
                    o = non_rep[0]
                else:
                    o = arm_opts[0]
            else:
                o = arm_opts[0]
            et = classify_email(o.email, from_rep_legal=o.from_rep_legal)
            return o.email, et, o.source_arm, o.source_url, o.from_rep_legal
        return "", "", "", "", False

    union_rows: list[dict[str, str]] = []
    source_contrib = Counter()
    with_email = 0
    blank = 0

    for key in sorted(records.keys(), key=lambda k: (len(k), k)):
        rec = records[key]
        email, email_type, source_arm, source_url, _ = choose_email(key)
        has_contracts = rec.contract_count > 0
        if email:
            with_email += 1
            source_contrib[source_arm] += 1
        else:
            blank += 1
            email_type = ""

        union_rows.append(
            {
                "nit": rec.nit_display,
                "razon_social": rec.razon_social,
                "city_or_municipio": rec.city,
                "email": email,
                "email_type": email_type,
                "phone": rec.phone,
                "website": rec.website,
                "source_arm": source_arm,
                "source_url": source_url,
                "has_secop_contratos_signal": str(has_contracts).lower(),
                "secop_contract_count": str(rec.contract_count) if rec.contract_count else "",
            }
        )

    union_fields = [
        "nit",
        "razon_social",
        "city_or_municipio",
        "email",
        "email_type",
        "phone",
        "website",
        "source_arm",
        "source_url",
        "has_secop_contratos_signal",
        "secop_contract_count",
    ]

    with OUT_UNION.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=union_fields)
        w.writeheader()
        w.writerows(union_rows)

    blank_rows = [r for r in union_rows if not r["email"]]
    with OUT_BLANK.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=union_fields)
        w.writeheader()
        w.writerows(blank_rows)

    resend_fields = ["email", "first_name", "last_name", "company", "nit", "source_arm", "email_type"]
    resend_rows: list[dict[str, str]] = []
    for r in union_rows:
        if not r["email"]:
            continue
        resend_rows.append(
            {
                "email": r["email"],
                "first_name": "",
                "last_name": "",
                "company": r["razon_social"],
                "nit": r["nit"],
                "source_arm": r["source_arm"],
                "email_type": r["email_type"],
            }
        )
    with OUT_RESEND.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=resend_fields)
        w.writeheader()
        w.writerows(resend_rows)

    def pilot_sort_key(r: dict[str, str]) -> tuple:
        key = nit_join_key(r["nit"])
        rec = records.get(key)
        city = r.get("city_or_municipio") or ""
        domain = (rec.domain_hint if rec else "") or ""
        website = (rec.website if rec else "") or r.get("website") or ""
        hint = 1 if (domain or website) else 0
        return (-santander_score(city), -hint, r.get("razon_social") or "")

    pilot_candidates: list[dict[str, str]] = []
    for r in blank_rows:
        key = nit_join_key(r["nit"])
        rec = records[key]
        domain = rec.domain_hint
        if not domain and rec.website:
            domain = re.sub(r"^https?://(www\.)?", "", rec.website.lower()).split("/")[0]
        pilot_candidates.append(
            {
                "nit": r["nit"],
                "razon_social": r["razon_social"],
                "city": r["city_or_municipio"],
                "domain": domain,
                "crm_id": "",
                "website_hint": rec.website or (f"https://{domain}" if domain else ""),
            }
        )

    pilot_candidates.sort(key=pilot_sort_key)
    pilot_top = pilot_candidates[:80]
    pilot_fields = ["nit", "razon_social", "city", "domain", "crm_id", "website_hint"]
    with OUT_PILOT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=pilot_fields)
        w.writeheader()
        w.writerows(pilot_top)

    # REPORT
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    absent = []
    for folder, label in (
        ("03-rues-public", "Hand 3 — RUES public"),
        ("04-made-in-santander", "Hand 4 — Made in Santander"),
    ):
        if not (WAVE / folder).is_dir():
            absent.append(label)

    inv_lines = []
    for path, count, has_report in inventory:
        rel = path.relative_to(WAVE)
        inv_lines.append(
            f"| `{rel}` | {count} | {'yes' if has_report else 'no'} |"
        )

    email_type_counts = Counter(r["email_type"] for r in union_rows if r["email"])

    report = f"""# Wave 0 assemble — REPORT

Generated: {ts}

## Input inventory (`enrich.csv`)

| Path | Data rows | REPORT.md |
|------|----------:|:---------:|
{chr(10).join(inv_lines)}

### Absent micro-hands (not merged)

{chr(10).join(f'- **ABSENT:** {a} — no folder on `main` at assemble time' for a in absent) if absent else '- (none)'}

`09-licensed-rues-apis/enrich.csv` contains **{rues_live_rows}** non-example live rows (doc samples only); excluded from email priority per Wave 0 spec.

## Universe

| Metric | Count |
|--------|------:|
| SECOP proveedores universe (01 spine) | 2011 |
| Distinct NIT join keys in `union.csv` | {len(union_rows)} |
| With non-blank email after priority merge | {with_email} |
| Blank email (`email_blank.csv`) | {blank} |
| `02-secop-contratos` NITs with contract signal | {sum(1 for r in union_rows if r['has_secop_contratos_signal'] == 'true')} |

Reference: CCB VPS energy profile cited in hand docs ~922 wf53 allowlist / **2011** SECOP-universe NITs in `01-secop-proveedores`; broader VPS ~2115 not used as assemble spine.

## Email source contribution (winning arm)

| source_arm | NITs |
|------------|-----:|
"""
    for arm, n in sorted(source_contrib.items(), key=lambda x: (-x[1], x[0])):
        report += f"| `{arm}` | {n} |\n"

    report += f"""
## Email type (chosen email)

| email_type | Count |
|------------|------:|
"""
    for et, n in email_type_counts.most_common():
        report += f"| {et} | {n} |\n"

    report += f"""
## Outputs

| File | Rows |
|------|-----:|
| `union.csv` | {len(union_rows)} |
| `email_blank.csv` | {len(blank_rows)} |
| `resend_stage.csv` | {len(resend_rows)} |
| `mailfinder_pilot_candidates.csv` | {len(pilot_top)} |

## Merge rules

1. Join key: see `nit-map.md`.
2. Email priority: `01-secop-proveedores` (correo before rep. legal) → `07-company-websites` (mailto &lt; contact page &lt; homepage) → `05-sspd-prestadores` → `06-ccb-other-dumps` → `08-opencorporates-gleif`.
3. No invented emails; empty stays empty.
4. Resend: staged only — **no API send**.

## Mail Finder pilot (≤80)

From `email_blank.csv`, sort by Santander/Bucaramanga metro city match (desc), then rows with domain/`website` hint, then `razon_social`. Cap **80**.
"""

    OUT_REPORT.write_text(report, encoding="utf-8")
    print(f"union={len(union_rows)} with_email={with_email} blank={blank} resend={len(resend_rows)} pilot={len(pilot_top)}")


if __name__ == "__main__":
    main()
