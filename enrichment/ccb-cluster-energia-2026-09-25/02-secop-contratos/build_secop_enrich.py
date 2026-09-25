#!/usr/bin/env python3
"""Rebuild CCB energy allowlist (wf53-j577) and intersect with SECOP II contratos (jbjy-vk9h)."""
from __future__ import annotations

import csv
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
WF53_URL = "https://www.datos.gov.co/resource/wf53-j577.json"
SECOP_URL = "https://www.datos.gov.co/resource/jbjy-vk9h.json"

# Same intent as micro-hand 05-sspd: ACTIVO + energy/gas/electricity/combustibles CIIU text.
CIIU_ENERGY_RE = re.compile(
    r"energ|el[eé]ctric|combustib|solar|hidro|biog[aá]s|petr[oó]leo|glp|"
    r"gas natural|gas licuado|producci[oó]n de gas|distribuci[oó]n de combust|"
    r"generaci[oó]n de energ|comercializaci[oó]n de energ|transmisi[oó]n de energ|"
    r"transporte por tuber[ií]as",
    re.I,
)

# Prefer energy-related contract signal when summarizing volume (not for inclusion).
ENERGY_TEXT_RE = re.compile(
    r"energ|el[eé]ctric|\bgas\b|glp|combust|solar|hidro|petr[oó]leo|"
    r"unspsc|servicio p[uú]blico|iluminaci[oó]n|subestaci[oó]n|transformador|"
    r"panel solar|fotovoltaic|termoel[eé]ctric|biog[aá]s|carbon|di[eé]sel|gasolina",
    re.I,
)
# UNSPSC segments commonly used for power / fuels / related MRO (prefix after V1.)
ENERGY_UNSPSC_PREFIXES = ("26", "71", "14", "25")


def http_get_json(url: str, retries: int = 4) -> list | dict:
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt == retries - 1:
                raise
            time.sleep(2**attempt)
    raise RuntimeError("unreachable")


def fetch_wf53() -> list[dict]:
    rows: list[dict] = []
    offset = 0
    page = 50000
    while True:
        q = urllib.parse.urlencode({"$limit": page, "$offset": offset})
        chunk = http_get_json(f"{WF53_URL}?{q}")
        if not chunk:
            break
        rows.extend(chunk)
        if len(chunk) < page:
            break
        offset += page
    return rows


def nit_base(nit: str) -> str:
    """SECOP documento_proveedor uses NIT body without verification digit."""
    return nit.split("-")[0].strip()


def is_energy_contract(row: dict) -> bool:
    parts = [
        row.get("sector") or "",
        row.get("descripcion_del_proceso") or "",
        row.get("objeto_del_contrato") or "",
        row.get("codigo_de_categoria_principal") or "",
    ]
    text = " ".join(parts)
    if ENERGY_TEXT_RE.search(text):
        return True
    code = (row.get("codigo_de_categoria_principal") or "").upper()
    for seg in ENERGY_UNSPSC_PREFIXES:
        if f".{seg}" in code or code.startswith(f"V1.{seg}"):
            return True
    return False


def fetch_secop_for_bases(bases: list[str]) -> list[dict]:
    in_list = ",".join(f"'{b}'" for b in bases)
    where = f"documento_proveedor in ({in_list})"
    fields = [
        "documento_proveedor",
        "proveedor_adjudicado",
        "valor_del_contrato",
        "fecha_de_firma",
        "urlproceso",
        "sector",
        "codigo_de_categoria_principal",
        "descripcion_del_proceso",
        "objeto_del_contrato",
    ]
    params = {
        "$select": ",".join(fields),
        "$where": where,
        "$limit": 50000,
    }
    url = f"{SECOP_URL}?{urllib.parse.urlencode(params)}"
    data = http_get_json(url)
    return data if isinstance(data, list) else []


def main() -> None:
    wf53 = fetch_wf53()
    allowlist = [
        r
        for r in wf53
        if (r.get("estado") or "").strip().upper() == "ACTIVO"
        and CIIU_ENERGY_RE.search(r.get("desc_ciiu1") or "")
    ]
    by_nit: dict[str, dict] = {}
    base_to_nit: dict[str, str] = {}
    for r in allowlist:
        nit = r["nit"]
        by_nit[nit] = r
        base = nit_base(nit)
        base_to_nit[base] = nit

    bases = sorted(base_to_nit.keys())
    batch_size = 35
    contracts: list[dict] = []
    for i in range(0, len(bases), batch_size):
        batch = bases[i : i + batch_size]
        contracts.extend(fetch_secop_for_bases(batch))
        time.sleep(0.15)

    agg: dict[str, dict] = defaultdict(
        lambda: {
            "names": defaultdict(int),
            "count": 0,
            "energy_count": 0,
            "total_value": 0.0,
            "energy_value": 0.0,
            "last_date": "",
            "sectors": set(),
            "sample_url": "",
        }
    )

    for c in contracts:
        base = (c.get("documento_proveedor") or "").strip()
        nit = base_to_nit.get(base)
        if not nit:
            continue
        a = agg[nit]
        a["count"] += 1
        name = (c.get("proveedor_adjudicado") or "").strip()
        if name:
            a["names"][name] += 1
        sector = (c.get("sector") or "").strip()
        if sector:
            a["sectors"].add(sector)
        val = float(c.get("valor_del_contrato") or 0)
        a["total_value"] += val
        if is_energy_contract(c):
            a["energy_count"] += 1
            a["energy_value"] += val
        fd = (c.get("fecha_de_firma") or "")[:10]
        if fd and fd > a["last_date"]:
            a["last_date"] = fd
            url_obj = c.get("urlproceso")
            if isinstance(url_obj, dict) and url_obj.get("url"):
                a["sample_url"] = url_obj["url"]
            elif isinstance(url_obj, str):
                a["sample_url"] = url_obj

    rows_out = []
    for nit, a in agg.items():
        if a["count"] == 0:
            continue
        proveedor_name = max(a["names"], key=a["names"].get) if a["names"] else ""
        sectors_seen = "; ".join(sorted(a["sectors"])[:8])
        if len(a["sectors"]) > 8:
            sectors_seen += f"; +{len(a['sectors']) - 8} more"
        notes_parts = [
            f"contracts={a['count']}",
            f"energy_tagged={a['energy_count']}",
            f"sum_valor_cop={a['total_value']:.0f}",
        ]
        if a["energy_count"]:
            notes_parts.append(f"energy_valor_cop={a['energy_value']:.0f}")
        rows_out.append(
            {
                "nit": nit,
                "proveedor_name": proveedor_name,
                "contract_count": a["count"],
                "last_contract_date": a["last_date"],
                "sample_process_url": a["sample_url"],
                "sectors_seen": sectors_seen,
                "notes": "; ".join(notes_parts),
                "_total_value": a["total_value"],
                "_energy_value": a["energy_value"],
            }
        )

    rows_out.sort(key=lambda r: (-r["contract_count"], -r["_total_value"], r["nit"]))

    csv_path = OUT_DIR / "enrich.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "nit",
                "proveedor_name",
                "contract_count",
                "last_contract_date",
                "sample_process_url",
                "sectors_seen",
                "notes",
            ],
        )
        w.writeheader()
        for r in rows_out:
            w.writerow({k: r[k] for k in w.fieldnames})

    # Sidecar stats for REPORT (not extra deliverable columns)
    stats = {
        "generated_utc": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "wf53_rows": len(wf53),
        "allowlist_nits": len(by_nit),
        "secop_contract_rows_matched": len(contracts),
        "profile_nits_with_secop": len(rows_out),
    }
    top_count = sorted(rows_out, key=lambda r: (-r["contract_count"], -r["_total_value"]))[:15]
    top_value = sorted(rows_out, key=lambda r: (-r["_total_value"], -r["contract_count"]))[:15]

    map_path = OUT_DIR / "nit-map.md"
    map_path.write_text(
        """# NIT join map — CCB (wf53-j577) ↔ SECOP II (jbjy-vk9h)

| Source | Field | Format | Notes |
|--------|--------|--------|--------|
| wf53-j577 | `nit` | `{base}-{dv}` e.g. `890201230-1` | CCB Bucaramanga registry key |
| jbjy-vk9h | `documento_proveedor` | numeric body only e.g. `890201230` | Match `split('-')[0]` on CCB `nit` |
| jbjy-vk9h | `tipodocproveedor` | often `NIT` for juridical persons | Not filtered (CCB set is all juridical NITs) |

**Allowlist rebuild:** `estado = ACTIVO` and `desc_ciiu1` matches energy CIIU regex (documented in `REPORT.md`).

**Energy contract tagging (volume prioritization only):** sector / objeto / descripción / UNSPSC (`codigo_de_categoria_principal`) matched against energy keywords and UNSPSC segments 26, 71, 14, 25.
""",
        encoding="utf-8",
    )

    report_path = OUT_DIR / "REPORT.md"
    lines = [
        "# SECOP II Contratos — Micro-Hand 2/9",
        "",
        f"Generated: {stats['generated_utc']}",
        "",
        "## Datasets",
        "",
        "| ID | Title | Role |",
        "|---|---|---|",
        "| `wf53-j577` | EMPRESAS CÁMARA DE COMERCIO DE BUCARAMANGA | Rebuild **energy profile-fit NIT universe** (allowlist). |",
        "| `jbjy-vk9h` | SECOP II - Contratos Electrónicos | Adjudicated **proveedor** activity signal (counts, values, sample proceso URL). |",
        "",
        "## Allowlist (wf53-j577)",
        "",
        f"- CCB rows downloaded: **{stats['wf53_rows']:,}**",
        f"- Energy-profile allowlist (`estado=ACTIVO` + `desc_ciiu1` regex): **{stats['allowlist_nits']:,}** unique NITs",
        "- Filter (case-insensitive on `desc_ciiu1`): energía/eléctric/combustibles/solar/hidro/biogas/petróleo/GLP, *gas natural* / *gas licuado*, producción-distribución-comercialización-transmisión de energía/gas, transporte por tuberías.",
        "- Join map: see `nit-map.md`.",
        "",
        "## SECOP overlap",
        "",
        "| Metric | Count |",
        "|---|---|",
        f"| Allowlist NITs with ≥1 adjudicated contract row in SECOP | **{stats['profile_nits_with_secop']:,}** / {stats['allowlist_nits']:,} |",
        f"| Total SECOP contract rows pulled for those NITs | **{stats['secop_contract_rows_matched']:,}** |",
        "",
        "Contracts are **national** (all entities); useful for prioritization / recent activity, not jurisdiction-filtered.",
        "",
        "## Top NITs by contract count",
        "",
        "| NIT | Proveedor (SECOP name) | Contracts | Last firma | Sum valor (COP) |",
        "|---|---|---:|---|---:|",
    ]
    for r in top_count:
        lines.append(
            f"| {r['nit']} | {r['proveedor_name'][:60]} | {r['contract_count']} | {r['last_contract_date']} | {r['_total_value']:,.0f} |"
        )
    lines.extend(
        [
            "",
            "## Top NITs by total contract value (valor_del_contrato)",
            "",
            "| NIT | Proveedor (SECOP name) | Sum valor (COP) | Contracts | Energy-tagged rows |",
            "|---|---|---:|---:|---:|",
        ]
    )
    for r in top_value:
        ec = re.search(r"energy_tagged=(\d+)", r["notes"])
        ec_n = ec.group(1) if ec else "0"
        lines.append(
            f"| {r['nit']} | {r['proveedor_name'][:60]} | {r['_total_value']:,.0f} | {r['contract_count']} | {ec_n} |"
        )
    lines.extend(
        [
            "",
            "## Output",
            "",
            "- `enrich.csv` — one row per allowlist NIT with SECOP adjudication history (no invented emails).",
            "- `nit-map.md` — NIT normalization between CCB and SECOP.",
            "",
            "## Notes",
            "",
            "- Prioritization / activity signal only; primary email enrichment remains Proveedores micro-hands.",
            "- No outbound sends and no VPS database writes.",
            "- `energy_tagged` in `notes` uses UNSPSC/sector/text heuristics; non-energy public contracts still count toward totals.",
        ]
    )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(stats, indent=2))
    print(f"wrote {len(rows_out)} rows to {csv_path}")


if __name__ == "__main__":
    main()
