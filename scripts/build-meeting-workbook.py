#!/usr/bin/env python3
"""Build Sustenttia HITL meeting workbook with Juan/Javier comment columns."""
import shutil
from pathlib import Path
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

OUT = Path("/workspace/sustenttia-meeting-20260915/sustenttia-hitl-workbook-20260915.xlsx")
BIB = Path("/workspace/sustenttia/biblioteca-juan-definitiva-2026-09-03.xlsx")

CLIENT_COLS = ["Comentarios_Juan", "Comentarios_Javier", "Estado_cliente"]
ESTADOS = "Pendiente, Aprobado, Rechazado"
HEADER_FILL = PatternFill("solid", fgColor="1B6B74")
HEADER_FONT = Font(color="FFFFFF", bold=True)
CLIENT_FILL = PatternFill("solid", fgColor="E6F4F4")


def add_client_columns(ws, source_cite_col=None):
    headers = [c.value for c in ws[1]]
    start = len(headers) + 1
    for i, name in enumerate(CLIENT_COLS):
        col = start + i
        cell = ws.cell(row=1, column=col, value=name)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(wrap_text=True)
        for r in range(2, ws.max_row + 1):
            c = ws.cell(row=r, column=col)
            c.fill = CLIENT_FILL
            if name == "Estado_cliente":
                c.value = "Pendiente"
    if source_cite_col is None and "source_cite" not in headers:
        sc = start + len(CLIENT_COLS)
        cell = ws.cell(row=1, column=sc, value="source_cite")
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT


def copy_biblioteca(wb):
    if BIB.exists():
        src = openpyxl.load_workbook(BIB)
        for name in src.sheetnames:
            if name in wb.sheetnames:
                del wb[name]
            ws_src = src[name]
            ws = wb.create_sheet(title=name[:31])
            for row in ws_src.iter_rows(values_only=True):
                ws.append(list(row))
            add_client_columns(ws)
            if name == "Biblioteca":
                # ensure description guidance in first pending row comment area
                pass
        src.close()


def seed_narracion(wb):
    ws = wb.create_sheet("Narracion_por_capitulo", 0)
    headers = [
        "capitulo", "eje_asg", "plantilla_id", "bloque", "texto_plantilla",
        "estado_juan", "source_cite"
    ] + CLIENT_COLS
    ws.append(headers)
    chapters = [
        ("1", "Ambiental", "NAR-001", "Intro", "PENDIENTE_JUAN — validar tono intro", "PENDIENTE_JUAN", "Modelo Word + PR #66"),
        ("2", "Ambiental", "NAR-002", "Energía", "PENDIENTE_JUAN — revisar conexión Fillout Energía Q4", "PENDIENTE_JUAN", "Juan Excel sep 2026"),
        ("3", "Social", "NAR-010", "Talento", "Plantilla base cargada", "BORRADOR", "Gold Standard"),
        ("4", "Gobernanza", "NAR-020", "Ética", "PENDIENTE_JUAN", "PENDIENTE_JUAN", "Workbook HITL"),
    ]
    for ch in chapters:
        ws.append(list(ch) + ["", "", "Pendiente"])
    style_header(ws)
    add_client_columns(ws, source_cite_col=7)


def seed_bp(wb):
    ws = wb.create_sheet("Catalogo_BP", 1)
    headers = [
        "bp_id", "capitulo", "practica", "nivel_0_3", "evidencia_minima",
        "estado", "source_cite"
    ] + CLIENT_COLS
    ws.append(headers)
    rows = [
        ("BP-E01", "Energía", "Medición consumo eléctrico", "", "Respuesta Fillout ≥20%", "PENDIENTE_JUAN", "PR #65 methodology"),
        ("BP-A01", "Agua", "Monitoreo consumo hídrico", "2", "Evidencia cuestionario", "VALIDADO", "4-informe bench"),
        ("BP-S01", "Talento", "Política diversidad", "", "Sin evidencia suficiente", "PENDIENTE_JUAN", "Modelo Word"),
    ]
    for r in rows:
        ws.append(list(r) + ["", "", "Pendiente"])
    style_header(ws)


def seed_riesgos(wb):
    ws = wb.create_sheet("Matriz_riesgos", 2)
    headers = [
        "riesgo_id", "categoria", "descripcion", "probabilidad", "impacto",
        "mitigacion", "estado", "source_cite"
    ] + CLIENT_COLS
    ws.append(headers)
    cats = [
        ("R01", "Ambiental", "Riesgo climático operacional", "Media", "Alto", "PENDIENTE_JUAN — confirmar taxonomía", "PENDIENTE_JUAN", "5-riesgos taxonomy"),
        ("R02", "Social", "Rotación talento clave", "Media", "Medio", "Plantilla base", "BORRADOR", "Modelo"),
        ("R03", "Gobernanza", "Cumplimiento normativo", "Baja", "Alto", "PENDIENTE_JUAN", "PENDIENTE_JUAN", "Juan Excel"),
        ("R04", "Reputacional", "Greenwashing percibido", "Media", "Alto", "Evidence Boundary", "BORRADOR", "PR #60"),
        ("R05", "Cadena suministro", "Proveedores sin ASG", "Alta", "Medio", "PENDIENTE_JUAN — confirmar taxonomía 5 riesgos", "PENDIENTE_JUAN", "Reunión 15 sep"),
    ]
    for r in cats:
        ws.append(list(r) + ["", "", "Pendiente"])
    style_header(ws)


def seed_plantillas(wb):
    ws = wb.create_sheet("Banco_plantillas", 3)
    headers = [
        "template_id", "capitulo", "tipo_bloque", "contenido", "variables",
        "estado", "source_cite"
    ] + CLIENT_COLS
    ws.append(headers)
    rows = [
        ("TPL-001", "Overview", "resumen_ejecutivo", "PENDIENTE_JUAN — completar fila", "{empresa},{sector}", "PENDIENTE_JUAN", "template-first PR #66"),
        ("TPL-002", "Energía", "diagnostico", "Texto determinístico cargado", "{score_energia}", "VALIDADO", "bench sep 2026"),
        ("TPL-003", "Riesgos", "tabla", "PENDIENTE_JUAN — matriz 5 riesgos", "{riesgos}", "PENDIENTE_JUAN", "Workbook"),
    ]
    for r in rows:
        ws.append(list(r) + ["", "", "Pendiente"])
    style_header(ws)


def seed_pendientes(wb):
    ws = wb.create_sheet("Pendientes_Cliente", 0)
    headers = [
        "id", "area", "descripcion", "owner", "prioridad", "fecha_objetivo",
        "estado", "notas_cth", "source_cite"
    ]
    ws.append(headers)
    items = [
        (
            "PC-01", "Biblioteca de casos",
            "Completar Description con (País), capítulos aplicables y vínculo sector/capítulo en filas pendientes",
            "Juan", "Alta", "2026-09-22", "Pendiente",
            "CTH: re-ingest AGT-003 si aplica", "biblioteca-juan-definitiva + Juan promesa re-ingest"
        ),
        (
            "PC-02", "Banco plantillas / BP / Riesgos",
            "Completar filas marcadas PENDIENTE_JUAN en tabs Banco_plantillas, Catalogo_BP y Matriz_riesgos",
            "Juan", "Alta", "2026-09-22", "Pendiente",
            "No es backlog ingeniería CTH", "Workbook HITL PR #66"
        ),
        (
            "PC-03", "Matriz de riesgos",
            "Confirmar taxonomía de 5 riesgos (categorías, descripciones, mitigaciones)",
            "Juan / Javier", "Alta", "2026-09-15", "Pendiente",
            "Reunión mañana", "Modelo Word + Juan Excel"
        ),
        (
            "PC-04", "Pack revisión",
            "Revisar pack 4 empresas (Concremovil, SOLPACK, Crepes & Waffles, Metalúrgica Andina) y devolver feedback",
            "Juan / Javier", "Alta", "2026-09-20", "Pendiente",
            "Pack PASS 14 sep — overviews ON", "https://sustenttia-client-review-20260914-c.vercel.app/"
        ),
        (
            "PC-05", "Fillout Comentarios",
            "Validar en vivo que Comentarios aparecen en todos los capítulos (FIL-001/002)",
            "Javier", "Media", "2026-09-15", "Pendiente",
            "Publish Fillout held HITL Gideon", "sustenttia-fillout.md 2026-09-11"
        ),
        (
            "PC-06", "Narración por capítulo",
            "Validar plantillas de tono y estructura por capítulo (tab Narracion_por_capitulo)",
            "Juan", "Media", "2026-09-22", "Pendiente",
            "", "PR #66 template-first"
        ),
    ]
    for item in items:
        ws.append(list(item))
    style_header(ws)
    ws.column_dimensions["C"].width = 55
    ws.column_dimensions["I"].width = 40


def style_header(ws):
    for cell in ws[1]:
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    for col in range(1, ws.max_column + 1):
        ws.column_dimensions[get_column_letter(col)].width = min(28, max(12, len(str(ws.cell(1, col).value or "")) + 2))


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb = openpyxl.Workbook()
    # remove default sheet after we add ours
    default = wb.active
    seed_pendientes(wb)
    seed_narracion(wb)
    seed_bp(wb)
    seed_riesgos(wb)
    seed_plantillas(wb)
    copy_biblioteca(wb)
    if default.title == "Sheet" and "Sheet" in wb.sheetnames:
        del wb["Sheet"]
    # Pendientes_Cliente first for client UX
    if "Pendientes_Cliente" in wb.sheetnames:
        wb.move_sheet("Pendientes_Cliente", offset=-wb.sheetnames.index("Pendientes_Cliente"))
    wb.save(OUT)
    print(f"Saved {OUT}")


if __name__ == "__main__":
    main()
