#!/usr/bin/env python3
"""Join CCB energy profile-fit NIT universe to SECOP II Proveedores (qmzu-gj57)."""

from __future__ import annotations

import csv
import json
import re
import unicodedata
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / ".cache"
OUT_CSV = ROOT / "enrich.csv"
OUT_REPORT = ROOT / "REPORT.md"
OUT_NITS = ROOT / "universe_nits.txt"

CCB_URL = "https://www.datos.gov.co/resource/wf53-j577.json"
SECOP_URL = "https://www.datos.gov.co/resource/qmzu-gj57.json"
SECOP_SOURCE_PAGE = (
    "https://www.datos.gov.co/Estad-sticas-Nacionales/"
    "SECOP-II-Proveedores-Registrados/qmzu-gj57"
)

# Exact desc_ciiu1 titles from wf53-j577 (Colombian CIIU Rev. 4 A.C.) → code groups per Hands spec.
TITLE_TO_CIIU: dict[str, str] = {
    # 35xx — electricidad, gas, vapor
    "Generación De Energía Eléctrica": "3511",
    "Transmisión De Energía Eléctrica": "3512",
    "Distribución De Energía Eléctrica": "3513",
    "Comercialización De Energía Eléctrica": "3514",
    "Producción De Gas  Distribución De Combustibles Gaseosos Por Tuberías": "3520",
    "Producción De Gas; Distribución De Combustibles Gaseosos Por Tuberías": "3520",
    "Suministro De Vapor Y Aire Acondicionado": "3530",
    # 4322 — instalaciones eléctricas
    "Instalaciones Eléctricas": "4322",
    # 4661 / 4730 — combustibles
    "Comercio Al Por Mayor De Combustibles Sólidos, Líquidos, Gaseosos Y Productos Conexos": "4661",
    "Comercio Al Por Menor De Combustible Para Automotores": "4730",
    # 7112 / 7120 — ingeniería y ensayos (energy-relevant technical services)
    "Actividades De Ingeniería Y Otras Actividades Conexas De Consultoría Técnica": "7112",
    "Ensayos Y Análisis Técnicos": "7120",
    # 27xx — equipos eléctricos
    "Fabricación De Motores, Generadores Y Transformadores Eléctricos": "2711",
    "Fabricación De Aparatos De Distribución Y Control De La Energía Eléctrica": "2712",
    "Fabricación De Pilas, Baterías Y Acumuladores Eléctricos": "2720",
    "Fabricación De Equipos Eléctricos De Iluminación": "2740",
    "Fabricación De Otros Tipos De Equipo Eléctrico N.C.P.": "2790",
    "Fabricación De Hilos Y Cables Eléctricos Y De Fibra Óptica": "2733",
    "Fabricación De Motores, Turbinas, Y Partes Para Motores De Combustión Interna": "2711",
    "Fabricación De Generadores De Vapor, Excepto Calderas De Agua Caliente Para Calefacción Central": "2513",
    # 3314 — mantenimiento equipo eléctrico (manufacturing/repair cluster)
    "Mantenimiento Y Reparación Especializado De Equipo Eléctrico": "3314",
    # 06 / 09 — upstream extractive
    "Extracción De Petróleo Crudo": "0610",
    "Extracción De Gas Natural": "0620",
    "Extracción De Hulla (Carbón De Piedra)": "0510",
    "Extracción De Carbón Lignito": "0520",
    "Actividades De Apoyo Para La Extracción De Petróleo Y De Gas Natural": "0910",
    "Transporte Por Tuberías": "4930",
    # 19 — petroquímica / refinación
    "Fabricación De Productos De La Refinación Del Petróleo": "1921",
    "Fabricación De Productos De Hornos De Coque": "1910",
}


def normalize_title(s: str) -> str:
    return " ".join(s.split())


ALLOWED_TITLES = {normalize_title(t) for t in TITLE_TO_CIIU}
TITLE_TO_CIIU_NORM = {normalize_title(k): v for k, v in TITLE_TO_CIIU.items()}


def nit_join_key(nit: str | None) -> str:
    if not nit:
        return ""
    nit = str(nit).strip()
    if "-" in nit:
        base = nit.split("-", 1)[0]
    else:
        base = nit
    return re.sub(r"\D", "", base)


def fetch_paginated(base_url: str, where: str | None, select: str) -> list[dict]:
    rows: list[dict] = []
    offset = 0
    limit = 50_000
    while True:
        params: dict[str, str | int] = {
            "$limit": limit,
            "$offset": offset,
            "$select": select,
        }
        if where:
            params["$where"] = where
        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        with urllib.request.urlopen(url, timeout=180) as resp:
            batch = json.load(resp)
        if not batch:
            break
        rows.extend(batch)
        if len(batch) < limit:
            break
        offset += limit
    return rows


def clean_secop_value(val: str | None) -> str:
    if val is None:
        return ""
    v = str(val).strip()
    if not v or v.lower() in {"no provisto", "no definido", "n/a"}:
        return ""
    return v


def clean_email(val: str | None) -> str:
    v = clean_secop_value(val)
    if not v:
        return ""
    if "@" not in v:
        return ""
    return v


def main() -> None:
    CACHE.mkdir(parents=True, exist_ok=True)

    ccb_where = "upper(departamento)='SANTANDER' AND upper(estado)!='CANCELADO'"
    ccb_select = "nit,razon_social,desc_ciiu1,ciudad,departamento,estado"
    ccb_rows = fetch_paginated(CCB_URL, ccb_where, ccb_select)

    universe: dict[str, dict] = {}
    title_hits: defaultdict[str, int] = defaultdict(int)
    unknown_titles: set[str] = set()

    for row in ccb_rows:
        title = normalize_title(row.get("desc_ciiu1") or "")
        if title not in ALLOWED_TITLES:
            continue
        nit_raw = row.get("nit") or ""
        key = nit_join_key(nit_raw)
        if not key:
            continue
        title_hits[title] += 1
        if key not in universe:
            universe[key] = {
                "nit": nit_raw,
                "legal_name": row.get("razon_social") or "",
                "city": row.get("ciudad") or "",
                "dept": row.get("departamento") or "",
                "ciiu_title": title,
                "ciiu_code": TITLE_TO_CIIU_NORM[title],
            }

    secop_select = (
        "nit,nombre,correo,correo_representante_legal,telefono,sitio_web,"
        "direccion,departamento,municipio"
    )
    secop_rows = fetch_paginated(SECOP_URL, None, secop_select)

    secop_by_nit: dict[str, dict] = {}
    for row in secop_rows:
        key = nit_join_key(row.get("nit"))
        if not key:
            continue
        # Prefer row with any email when duplicates exist
        prev = secop_by_nit.get(key)
        if prev is None:
            secop_by_nit[key] = row
            continue
        prev_has = bool(clean_email(prev.get("correo")) or clean_email(prev.get("correo_representante_legal")))
        new_has = bool(clean_email(row.get("correo")) or clean_email(row.get("correo_representante_legal")))
        if new_has and not prev_has:
            secop_by_nit[key] = row

    fieldnames = [
        "nit",
        "legal_name",
        "email",
        "email_rep_legal",
        "phone",
        "website",
        "address",
        "city",
        "dept",
        "source_url",
        "matched",
    ]

    matched_count = 0
    with_email_count = 0

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for key in sorted(universe.keys()):
            u = universe[key]
            sec = secop_by_nit.get(key)
            matched = sec is not None
            if matched:
                matched_count += 1
            email = clean_email(sec.get("correo") if sec else None)
            email_rep = clean_email(sec.get("correo_representante_legal") if sec else None)
            if email or email_rep:
                with_email_count += 1
            legal = u["legal_name"]
            if sec and sec.get("nombre"):
                legal = sec.get("nombre") or legal
            writer.writerow(
                {
                    "nit": u["nit"],
                    "legal_name": legal,
                    "email": email,
                    "email_rep_legal": email_rep,
                    "phone": clean_secop_value(sec.get("telefono") if sec else None),
                    "website": clean_secop_value(sec.get("sitio_web") if sec else None),
                    "address": clean_secop_value(sec.get("direccion") if sec else None),
                    "city": clean_secop_value(sec.get("municipio") if sec else None) or u["city"],
                    "dept": clean_secop_value(sec.get("departamento") if sec else None) or u["dept"],
                    "source_url": SECOP_SOURCE_PAGE if matched else "",
                    "matched": "true" if matched else "false",
                }
            )

    with OUT_NITS.open("w", encoding="utf-8") as f:
        for key in sorted(universe.keys()):
            f.write(f"{universe[key]['nit']}\n")

    coverage = (with_email_count / len(universe) * 100) if universe else 0.0
    match_rate = (matched_count / len(universe) * 100) if universe else 0.0

    code_groups = defaultdict(list)
    for title, code in TITLE_TO_CIIU_NORM.items():
        code_groups[code].append(title)

    report_lines = [
        "# SECOP II Proveedores → CCB energy NIT universe",
        "",
        "## Sources",
        f"- CCB empresas: `{CCB_URL}` (dataset `wf53-j577`)",
        f"- SECOP proveedores: `{SECOP_SOURCE_PAGE}` (dataset `qmzu-gj57`)",
        "",
        "## Universe filters (Hands allowlist)",
        "- `departamento` = SANTANDER (case-insensitive)",
        "- `estado` ≠ CANCELADO",
        "- `desc_ciiu1` in energy profile-fit title allowlist (mapped to CIIU codes below)",
        "",
        "## Title → CIIU code map used",
        "",
    ]
    for code in sorted(code_groups.keys()):
        for title in sorted(code_groups[code]):
            n = title_hits.get(title, 0)
            report_lines.append(f"- **{code}** — {title} ({n} empresas in universe)")

    report_lines.extend(
        [
            "",
            "## Row counts",
            f"| Metric | Count |",
            f"|--------|------:|",
            f"| Universe NITs (profile-fit) | {len(universe)} |",
            f"| CCB rows scanned (Santander, non-CANCELADO) | {len(ccb_rows)} |",
            f"| SECOP proveedor rows downloaded | {len(secop_rows)} |",
            f"| Universe NITs matched in SECOP | {matched_count} ({match_rate:.1f}%) |",
            f"| Universe NITs with any email (correo or rep. legal) | {with_email_count} ({coverage:.1f}%) |",
            f"| enrich.csv data rows | {len(universe)} |",
            "",
            "## Outputs",
            f"- `enrich.csv` — one row per universe NIT",
            f"- `universe_nits.txt` — original NIT strings (with DV when present)",
            "",
            "## Join logic",
            "- Join key: NIT base before verification digit (strip `-` DV punctuation); digits only on base.",
            "- Emails only from SECOP fields; `No Provisto` treated as empty (never invented).",
        ]
    )

    OUT_REPORT.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "universe_nits": len(universe),
        "ccb_rows": len(ccb_rows),
        "secop_rows": len(secop_rows),
        "matched": matched_count,
        "with_email": with_email_count,
    }, indent=2))


if __name__ == "__main__":
    main()
