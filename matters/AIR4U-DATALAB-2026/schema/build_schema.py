#!/usr/bin/env python3
"""Rebuild three-party-schema.svg from the custody memo.

The SVG is the graphic source that render.py rasterizes. This script
rewrites that SVG from the copy below. Hand edits to the SVG are lost
if this script is run again.
"""

from __future__ import annotations

from pathlib import Path

from PIL import ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "three-party-schema.svg"
FONT_DIR = ROOT / "fonts"

W, H = 3508, 2480
NAVY, CYAN, SAGE, GREEN, BLUE, WHITE = (
    "#0C498A",
    "#B2EEFA",
    "#9DC384",
    "#669348",
    "#69B5FA",
    "#FFFFFF",
)

# Layout. A4 landscape at 300 px/in is 3508 × 2480.
M = 50
GAP = 18
CARD_W = 1124
CARD_Y, CARD_H = 228, 808
FLOW_Y, FLOW_H = 1052, 568
LINK_Y, LINK_H = 1636, 452
FOOT_Y, FOOT_H = 2104, 348


def load_font(weight: str, size: int) -> ImageFont.FreeTypeFont:
    name = {"400": "OpenSans-Regular.ttf", "600": "OpenSans-Semibold.ttf", "700": "OpenSans-Bold.ttf"}[
        weight
    ]
    return ImageFont.truetype(str(FONT_DIR / name), size, layout_engine=ImageFont.Layout.BASIC)


def text_width(text: str, size: int, weight: str = "600") -> float:
    return load_font(weight, size).getlength(text)


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def rich(text: str) -> str:
    """Escape text. **bold**, [[PENDIENTE]] and [[VERIFICAR]] become markup."""
    token_p, token_v = "\x00P\x00", "\x00V\x00"
    raw = text.replace("[[PENDIENTE]]", token_p).replace("[[VERIFICAR]]", token_v)
    raw = esc(raw)
    parts = raw.split("**")
    html: list[str] = []
    for i, part in enumerate(parts):
        html.append(f"<b>{part}</b>" if i % 2 else part)
    out = "".join(html)
    out = out.replace(token_p, '<b class="pend">PENDIENTE</b>')
    out = out.replace(token_v, "<b>[VERIFICAR]</b>")
    return out


def fo(x: int, y: int, w: int, h: int, paragraphs: list[str], size: int = 31) -> str:
    body = "\n".join(f'        <p>{rich(p)}</p>' for p in paragraphs)
    return f"""    <foreignObject x="{x}" y="{y}" width="{w}" height="{h}">
      <div xmlns="http://www.w3.org/1999/xhtml" class="copy" style="font-size:{size}px;line-height:1.28">
{body}
      </div>
    </foreignObject>"""


class Svg:
    def __init__(self) -> None:
        self.parts: list[str] = []

    def add(self, chunk: str) -> None:
        self.parts.append(chunk)

    def rect(self, x, y, w, h, fill, stroke="none", sw=0, rx=0, dash=None, opacity=None) -> None:
        extra = ""
        if dash:
            extra += f' stroke-dasharray="{dash}"'
        if opacity is not None:
            extra += f' fill-opacity="{opacity}"'
        stroke_attr = f' stroke="{stroke}" stroke-width="{sw}"' if stroke != "none" else ""
        self.add(
            f'    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}"{stroke_attr}{extra}/>'
        )

    def line(self, x1, y1, x2, y2, color, sw=4, marker="arr", dash=None) -> None:
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        marker_attr = f' marker-end="url(#{marker})"' if marker else ""
        self.add(
            f'    <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round"'
            f'{marker_attr}{dash_attr}/>'
        )

    def text(self, x, y, s, size, weight="400", fill=NAVY, anchor="start") -> None:
        self.add(
            f'    <text x="{x}" y="{y}" text-anchor="{anchor}" fill="{fill}" '
            f'font-size="{size}" font-weight="{weight}">{esc(s)}</text>'
        )

    def node(self, x, y, w, h, label, fill, stroke, size=28) -> None:
        self.rect(x, y, w, h, fill, stroke, 3, 12)
        tw = text_width(label, size, "700")
        if tw > w - 24:
            raise SystemExit(f"Node label too wide ({tw:.0f}>{w - 24}): {label}")
        self.text(x + w / 2, y + h / 2 + size * 0.35, label, size, "700", NAVY, "middle")


def pill_row(svg: Svg, labels: list[str], y: int, x0: int, max_x: int) -> None:
    size = 26
    pad_x = 18
    h = 44
    gap = 12
    widths = [text_width(label, size, "600") + pad_x * 2 for label in labels]
    total = sum(widths) + gap * (len(labels) - 1)
    if total > max_x - x0:
        raise SystemExit(f"Pills overflow: {total:.0f} > {max_x - x0}")
    x = x0
    for label, w in zip(labels, widths):
        svg.rect(x, y, w, h, WHITE, NAVY, 2, 22)
        svg.text(x + w / 2, y + 30, label, size, "600", NAVY, "middle")
        x += w + gap


def card_header(svg: Svg, x: int, y: int, w: int, h: int, title: str, line2: str, line3: str) -> None:
    # Square the bottom of the header so the card radius only shows at the top.
    svg.rect(x, y, w, h, NAVY)
    svg.rect(x, y + h - 16, w, 16, NAVY)
    svg.text(x + 28, y + 48, title, 40, "700", WHITE)
    svg.text(x + 28, y + 80, line2, 26, "600", CYAN)
    svg.text(x + 28, y + 110, line3, 24, "600", CYAN)


def flow_lane(svg: Svg, y: int, h: int, label: str, wash: bool) -> tuple[int, int, int, int]:
    x = M
    w = W - 2 * M
    if wash:
        svg.rect(x + 8, y, w - 16, h, CYAN, opacity=0.55)
    svg.rect(x + 24, y + (h - 46) / 2, 168, 46, NAVY, rx=10)
    svg.text(x + 24 + 84, y + (h - 46) / 2 + 31, label, 24, "700", WHITE, "middle")
    return x + 212, y, w - 236, h


def place_flow(svg: Svg, box, spec) -> None:
    """spec items are ('node', label, width, fill, stroke) or ('arrow', label, color)."""
    x, y, w, h = box
    nodes = [item for item in spec if item[0] == "node"]
    arrows = [item for item in spec if item[0] == "arrow"]
    node_w = sum(item[2] for item in nodes)
    free = w - node_w
    if free < 80 * max(1, len(arrows)):
        raise SystemExit(f"Flow overflow in lane: free={free:.0f}")
    arrow_w = free / max(1, len(arrows)) if arrows else 0
    cursor = x
    node_h = 48
    node_y = y + 8
    for kind, *rest in spec:
        if kind == "node":
            label, nw, fill, stroke = rest
            svg.node(cursor, node_y, nw, node_h, label, fill, stroke, 26)
            cursor += nw
        else:
            label, color = rest
            marker = "arrG" if color == GREEN else "arr"
            x1 = cursor + 8
            x2 = cursor + arrow_w - 8
            mid_y = node_y + node_h / 2
            svg.line(x1, mid_y, x2, mid_y, color, 4, marker)
            if label:
                label_w = text_width(label, 24, "700")
                if label_w > arrow_w - 8:
                    raise SystemExit(f"Arrow label too wide ({label_w:.0f}>{arrow_w - 8:.0f}): {label}")
                svg.text((x1 + x2) / 2, mid_y - 12, label, 24, "700", color, "middle")
            cursor += arrow_w


def build() -> str:
    svg = Svg()
    # Brand strip
    stripe_w = [702, 702, 702, 701, 701]
    sx = 0
    for color, sw in zip((NAVY, BLUE, CYAN, SAGE, GREEN), stripe_w):
        svg.rect(sx, 0, sw, 14, color)
        sx += sw

    # Header
    svg.rect(0, 14, W, 136, NAVY)
    svg.text(M, 72, "Esquema vivo · tres partes", 52, "700", WHITE)
    svg.text(M, 114, "Sandbox Air4U · Datalab · opción B condicionada, sin firmar", 30, "600", CYAN)
    svg.text(W - M, 62, "Propuesta del maker para Legal", 28, "600", WHITE, "end")
    svg.text(W - M, 98, "No es decisión. No autoriza carga real.", 28, "400", CYAN, "end")
    svg.text(W - M, 132, "Fuente: L3-CUSTODY-MEMO.md", 26, "600", WHITE, "end")

    pill_row(
        svg,
        [
            "Sin firmar",
            "PR #26 abierto, no fusionado",
            "No desplegado",
            "Hoy: datos supuestos",
            "Sandbox no visto por Legal",
            "Costos: PENDIENTE",
        ],
        164,
        M,
        W - M,
    )

    # Party cards
    cards = [
        {
            "fill": CYAN,
            "stroke": NAVY,
            "title": "Air4U",
            "l2": "Miguel Ángel Rozo · persona natural",
            "l3": "Dueño de la solución · Responsable del dato",
            "copy": [
                "**Responsabilidad.** Decide la finalidad y es el laboratorio de archivo. Art. 17: pide la autorización y exige seguridad a CTH. Inventario de sitios antes de cargar. Cesión cl. 16: la posición de Responsable pasa a la sociedad. Incorporación prevista antes de dic. 2026. No es Titular (Ley 1581, art. 3, lit. f).",
                "**Flujo.** Guarda la clave sitio–recinto–persona, fuera de CTH, y el original del expediente tipo ONAC. En el tablero ve los sitios de su solución.",
                "**Riesgo.** Hasta la cesión responde la persona natural. Cédula, matrícula y facultades: [[VERIFICAR]]. Dato personal solo si hay persona natural determinable (art. 3, lit. c).",
                "**Costo.** [[PENDIENTE]]. El memo no dice quién paga.",
                "**Contrato.** Vitrina v0.2. Transmisión Air4U→CTH, Decreto 1377 de 2013, art. 25. Acuerdo con cada cliente. Sandbox [[VERIFICAR]].",
            ],
        },
        {
            "fill": WHITE,
            "stroke": BLUE,
            "title": "Fundación CleantechHUB",
            "l2": "NIT 901.523.941-9",
            "l3": "Operador del sandbox · custodio · Encargado (opción B)",
            "copy": [
                "**Responsabilidad.** Encargado solo del dato personal que esté en sistemas de CTH. Trata por cuenta de Air4U y no decide la finalidad (art. 3, lit. d; art. 18). Fines: validar el sandbox y el expediente encargado por escrito. Acceso nominado, con registro. Plazo máximo [[PENDIENTE]]; luego suprime o devuelve en 30 días. L3 real prohibido en git.",
                "**Flujo.** L3 en almacén segregado, código opaco, sin dirección, coordenada ni nombre. No tiene la clave ni el original ONAC.",
                "**Riesgo.** Si fija la finalidad, deja de ser Encargado. El PR #26 no registra la lectura HTTP. Hoy es local: no está en el VPS ni en OVH. Sub-encargados y facultades del representante: [[VERIFICAR]].",
                "**Costo.** [[PENDIENTE]].",
                "**Contrato.** Vitrina v0.2, cth-showcase-001, 14 oct 2026, borrador. DPA: D. 1377/2013, art. 25. [[VERIFICAR]] su número en el D. 1074/2015. Ley 1581, art. 25, es el Registro Nacional, no este contrato.",
            ],
        },
        {
            "fill": WHITE,
            "stroke": GREEN,
            "title": "Clientes de Air4U",
            "l2": "Clínica Colombia · cannabis medicinal, Barranquilla",
            "l3": "No son parte de la vitrina v0.2",
            "copy": [
                "**Responsabilidad.** Autorizan el L3 de sus sitios y marcan qué es confidencial. Esa autorización no reemplaza la del Titular (art. 9), salvo un supuesto del art. 10.",
                "**Flujo.** Clínica Colombia, sector salud: inventario de persona, paciente o menor; tablero solo con sus sitios. Cannabis de Barranquilla: razón social [[PENDIENTE]]; tablero solo con sus sitios; el otro cliente no accede.",
                "**Riesgo.** Sensible solo si revela salud (art. 5). Historia clínica solo con escrito aparte. [[VERIFICAR]] Res. 1995/1999. Cannabis: secreto y seguridad del sitio. [[VERIFICAR]] Decisión 486, Ley 256/1996 y el decreto vigente. Niños: [[VERIFICAR]] antes de pediatría.",
                "**Costo.** [[PENDIENTE]].",
                "**Contrato.** Acuerdo Air4U–cliente: autorización y confidencialidad. No se presume por el OK a la vitrina.",
            ],
        },
    ]
    header_h = 124
    for i, card in enumerate(cards):
        x = M + i * (CARD_W + GAP)
        svg.add(
            f'    <clipPath id="party{i}"><rect x="{x}" y="{CARD_Y}" width="{CARD_W}" '
            f'height="{CARD_H}" rx="18"/></clipPath>'
        )
        svg.add(f'    <g clip-path="url(#party{i})">')
        svg.rect(x, CARD_Y, CARD_W, CARD_H, card["fill"])
        card_header(svg, x, CARD_Y, CARD_W, header_h, card["title"], card["l2"], card["l3"])
        stripe = (CYAN, BLUE, SAGE)[i]
        svg.rect(x, CARD_Y + header_h, CARD_W, 8, stripe)
        svg.add(
            fo(
                x + 24,
                CARD_Y + header_h + 16,
                CARD_W - 48,
                CARD_H - header_h - 28,
                card["copy"],
                32,
            )
        )
        svg.add("    </g>")
        svg.rect(x, CARD_Y, CARD_W, CARD_H, "none", card["stroke"], 3, 18)

    # Flow panel
    svg.rect(M, FLOW_Y, W - 2 * M, FLOW_H, WHITE, NAVY, 3, 18)
    svg.text(M + 28, FLOW_Y + 40, "Flujos de datos", 34, "700", NAVY)
    svg.text(
        W - M - 28,
        FLOW_Y + 38,
        "Lo de abajo es la regla propuesta, no lo que el PR hace hoy",
        24,
        "600",
        GREEN,
        "end",
    )

    chip_y = FLOW_Y + 52
    chip_h = 78
    chip_w = (W - 2 * M - 56 - 16) // 2
    svg.rect(M + 28, chip_y, chip_w, chip_h, CYAN, rx=12)
    svg.rect(M + 28 + chip_w + 16, chip_y, chip_w, chip_h, SAGE, rx=12)
    svg.add(
        fo(
            M + 40,
            chip_y + 8,
            chip_w - 24,
            chip_h - 12,
            [
                "**Hoy.** PR #26, abierto, no fusionado, no desplegado. SQLite local y CSV sintético «Datos supuestos». El steward admin lee todas las filas. La lectura HTTP no se registra. Los dos clientes no están en el código."
            ],
            24,
        )
    )
    svg.add(
        fo(
            M + 40 + chip_w + 16,
            chip_y + 8,
            chip_w - 24,
            chip_h - 12,
            [
                "**Propuesta.** Opción B condicionada, sin firmar. CTH es Encargado solo del dato personal en sus sistemas. Air4U decide la finalidad, guarda la clave y el original ONAC. Almacén segregado. L3 real fuera de git."
            ],
            24,
        )
    )

    lane_top = chip_y + chip_h + 8
    lane_area = FLOW_Y + FLOW_H - lane_top - 12
    heights = [104, 86, 102, 120]
    if sum(heights) > lane_area:
        raise SystemExit(f"Lanes {sum(heights)} > {lane_area}")
    # Distribute leftover pixels onto the lanes.
    extra = lane_area - sum(heights)
    heights = [h + extra // 4 for h in heights]
    heights[-1] += extra - 4 * (extra // 4)

    y = lane_top
    boxes = []
    for i, (label, lh) in enumerate(zip(("L3 crudo", "Clave", "ONAC", "Tablero"), heights)):
        boxes.append(flow_lane(svg, y, lh, label, wash=i % 2 == 0))
        y += lh

    place_flow(
        svg,
        boxes[0],
        [
            ("node", "Cliente entrega", 400, SAGE, GREEN),
            ("arrow", "entrega", NAVY),
            ("node", "Air4U autoriza", 420, CYAN, NAVY),
            ("arrow", "código opaco", NAVY),
            ("node", "CTH · almacén segregado", 560, WHITE, BLUE),
        ],
    )
    svg.text(
        boxes[0][0],
        boxes[0][1] + boxes[0][3] - 14,
        "Separado de la vitrina, de la API y de git. L3 real prohibido en el repositorio.",
        24,
        "600",
        NAVY,
    )

    place_flow(
        svg,
        boxes[1],
        [
            ("node", "Air4U guarda la clave", 520, CYAN, NAVY),
            ("arrow", "no entra", GREEN),
            ("node", "CTH", 240, WHITE, BLUE),
            ("arrow", "no se publica", GREEN),
            ("node", "Vitrina", 280, WHITE, NAVY),
            ("arrow", "no se comparte", GREEN),
            ("node", "Otro cliente", 320, SAGE, GREEN),
        ],
    )

    place_flow(
        svg,
        boxes[2],
        [
            ("node", "Air4U · original del expediente", 620, CYAN, NAVY),
            ("arrow", "solo con encargo escrito", NAVY),
            ("node", "CTH puede apoyar el armado", 560, WHITE, BLUE),
        ],
    )
    svg.text(
        boxes[2][0],
        boxes[2][1] + boxes[2][3] - 14,
        "El gancho onac del PR está vacío. No es acreditación. Quién se acredita: [VERIFICAR]. Plazo máximo: PENDIENTE.",
        24,
        "600",
        NAVY,
    )

    place_flow(
        svg,
        boxes[3],
        [
            ("node", "Clínica · solo lo suyo", 460, SAGE, GREEN),
            ("arrow", "", NAVY),
            ("node", "Cannabis · solo lo suyo", 500, SAGE, GREEN),
            ("arrow", "", NAVY),
            ("node", "Air4U · sus sitios", 420, CYAN, NAVY),
            ("arrow", "", NAVY),
            ("node", "CTH · fines de B.2", 420, WHITE, BLUE),
        ],
    )
    bar_x = boxes[3][0]
    bar_w = boxes[3][2]
    bar_y = boxes[3][1] + 62
    svg.rect(bar_x, bar_y, bar_w, 44, NAVY, rx=10)
    svg.text(
        bar_x + bar_w / 2,
        bar_y + 29,
        "Vitrina pública · agregado y anonimizado · cláusula 4 · sin L3, calibración, metadatos, serie horaria, nombre ni logo",
        24,
        "700",
        WHITE,
        "middle",
    )

    # Link cards
    links = [
        {
            "title": "Enlace · Air4U ↔ CTH",
            "sub": "Bilateral · vitrina y transmisión",
            "stroke": NAVY,
            "dash": None,
            "stripe": BLUE,
            "copy": [
                "**Responsabilidad.** Air4U decide la finalidad. CTH trata por cuenta de Air4U y no la decide.",
                "**Flujo.** L3 opaco al almacén de CTH. La clave y el original ONAC no cruzan. La vitrina solo recibe el agregado anonimizado.",
                "**Riesgo.** El PR #26 atribuye al sandbox «CTH no almacena L3». Esa frase no está en el v0.2 leído.",
                "**Costo.** [[PENDIENTE]].",
                "**Contrato.** Vitrina v0.2 y DPA Air4U→CTH, Decreto 1377 de 2013, art. 25. [[VERIFICAR]] el número en el Decreto 1074 de 2015.",
            ],
        },
        {
            "title": "Enlace · Air4U ↔ cliente",
            "sub": "Uno por cliente · autorización y reserva",
            "stroke": GREEN,
            "dash": None,
            "stripe": SAGE,
            "copy": [
                "**Responsabilidad.** El cliente declara sector y sitios. Air4U es Responsable si el dato es personal.",
                "**Flujo.** El cliente entrega el L3 y el inventario. La clave queda en Air4U. De vuelta, solo su tablero.",
                "**Riesgo.** Sin inventario no se asigna sector salud ni se carga el sitio.",
                "**Costo.** [[PENDIENTE]].",
                "**Contrato.** Acuerdo de autorización y confidencialidad. No se presume por el OK a la vitrina.",
            ],
        },
        {
            "title": "Enlace · sandbox tripartito",
            "sub": "Air4U · CTH · cada cliente",
            "stroke": NAVY,
            "dash": "10 8",
            "stripe": CYAN,
            "copy": [
                "**Responsabilidad.** Los clientes no son parte de la vitrina. El addendum 4 ter.11, propuesto y sin firmar, lo firman cliente, Air4U y CTH.",
                "**Flujo.** Living lab y producto cliente salen de lo público por la cláusula 2.",
                "**Riesgo.** Cargar un cliente real sin ese texto deja el archivo sin regla de custodia leída en el v0.2.",
                "**Costo.** [[PENDIENTE]].",
                "**Contrato.** cth-sandbox-air4u-001, tripartito. Legal no ha visto el texto. [[VERIFICAR]].",
            ],
        },
    ]
    link_header = 78
    for i, link in enumerate(links):
        x = M + i * (CARD_W + GAP)
        svg.add(
            f'    <clipPath id="link{i}"><rect x="{x}" y="{LINK_Y}" width="{CARD_W}" '
            f'height="{LINK_H}" rx="16"/></clipPath>'
        )
        svg.add(f'    <g clip-path="url(#link{i})">')
        svg.rect(x, LINK_Y, CARD_W, LINK_H, WHITE)
        svg.rect(x, LINK_Y, CARD_W, link_header, NAVY)
        svg.rect(x, LINK_Y + link_header - 14, CARD_W, 14, NAVY)
        svg.rect(x, LINK_Y + link_header, CARD_W, 8, link["stripe"])
        svg.text(x + 24, LINK_Y + 36, link["title"], 30, "700", WHITE)
        svg.text(x + 24, LINK_Y + 66, link["sub"], 24, "600", CYAN)
        svg.add(
            fo(
                x + 22,
                LINK_Y + link_header + 16,
                CARD_W - 44,
                LINK_H - link_header - 26,
                link["copy"],
                28,
            )
        )
        svg.add("    </g>")
        svg.rect(x, LINK_Y, CARD_W, LINK_H, "none", link["stroke"], 3, 16, dash=link["dash"])

    # Footer — risks in navy on cyan/white, never red. Cost column in sage.
    svg.rect(M, FOOT_Y, W - 2 * M, FOOT_H, WHITE, NAVY, 3, 16)
    svg.rect(M, FOOT_Y, 12, FOOT_H, GREEN)
    left_w = 2280
    svg.text(M + 32, FOOT_Y + 36, "Riesgos que cruzan el esquema", 28, "700", NAVY)
    svg.rect(M + left_w, FOOT_Y, W - 2 * M - left_w, FOOT_H, SAGE, rx=16)
    # Cover the left radius of the sage panel so it sits flush.
    svg.rect(M + left_w, FOOT_Y, 20, FOOT_H, SAGE)
    svg.text(M + left_w + 28, FOOT_Y + 36, "Costos · quién paga", 28, "700", NAVY)

    svg.add(
        fo(
            M + 32,
            FOOT_Y + 48,
            left_w - 56,
            230,
            [
                "**Art. 3.c.** Personal solo si hace determinable a una persona natural. Zona sin asignar y sin roster: dato del inmueble. El sector health identifica a la clínica como organización; eso es reserva, no dato personal por sí solo.",
                "**Art. 5, 6 y O3.** Sensible solo si revela salud. O3 o PM2.5 de un corredor, sin ese vínculo, es medición del aire. El código bloquea el cierre si O3 supera 100 µg/m³ en sector health y guarda un rótulo sanitario: no autoriza un claim de salud ni es, por sí solo, el art. 6, lit. e.",
                "**Secreto, historia clínica, niños, responsabilidad.** Cannabis: [[VERIFICAR]] Decisión 486 y Ley 256/1996. Historia clínica: [[VERIFICAR]] Res. 1995/1999. Niños, art. 7: [[VERIFICAR]] antes de pediatría. Hasta la cesión cl. 16 responde la persona natural. Si CTH fija la finalidad, deja de ser Encargado. RNBD (Ley 1581, art. 25): deber del Responsable, umbral [[VERIFICAR]]. No es el DPA.",
            ],
            26,
        )
    )
    svg.add(
        fo(
            M + left_w + 28,
            FOOT_Y + 48,
            W - 2 * M - left_w - 48,
            220,
            [
                "Sandbox, sensores, living lab, alojamiento, acreditación tipo ONAC, RNBD y asesoría: [[PENDIENTE]].",
                "El memo no asigna pagador ni cifra.",
                "Hoy no está desplegado. El OVH de la cláusula 12 no aplica a este PR.",
            ],
            26,
        )
    )
    svg.line(M + 28, FOOT_Y + FOOT_H - 64, W - M - 28, FOOT_Y + FOOT_H - 64, NAVY, 2, marker="")
    svg.text(
        M + 32,
        FOOT_Y + FOOT_H - 28,
        "Borrador para Gideon (Legal). No es asesoría cerrada ni autoriza firma o carga real. [VERIFICAR] = punto abierto. PENDIENTE = hecho o costo que el memo no fija. No se envía a Air4U, a los clientes ni a un tercero.",
        26,
        "600",
        NAVY,
    )

    body = "\n".join(svg.parts)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Open Sans, sans-serif">
  <title>Esquema vivo · Air4U, CleantechHUB y clientes</title>
  <desc>Propuesta del maker, opción B condicionada, a partir de L3-CUSTODY-MEMO.md. No es una decisión ni asesoría cerrada. [VERIFICAR] y PENDIENTE se conservan literales.</desc>
  <defs>
    <style><![CDATA[
      @font-face {{ font-family: "Open Sans"; src: url("fonts/OpenSans-Regular.ttf") format("truetype"); font-weight: 400; font-style: normal; }}
      @font-face {{ font-family: "Open Sans"; src: url("fonts/OpenSans-Semibold.ttf") format("truetype"); font-weight: 600; font-style: normal; }}
      @font-face {{ font-family: "Open Sans"; src: url("fonts/OpenSans-Bold.ttf") format("truetype"); font-weight: 700; font-style: normal; }}
      text {{ font-family: "Open Sans", sans-serif; -webkit-font-smoothing: antialiased; }}
      .copy, .copy p, .copy b {{ font-family: "Open Sans", sans-serif; color: {NAVY}; -webkit-font-smoothing: antialiased; }}
      .copy p {{ margin: 0 0 7px 0; }}
      .copy b {{ font-weight: 700; }}
      .pend {{ background: {SAGE}; padding: 0 6px; font-weight: 700; }}
    ]]></style>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="{NAVY}"/>
    </marker>
    <marker id="arrG" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="{GREEN}"/>
    </marker>
    <marker id="none" viewBox="0 0 1 1" refX="0" refY="0" markerWidth="0" markerHeight="0">
      <path d="M 0 0"/>
    </marker>
  </defs>
  <rect width="{W}" height="{H}" fill="{WHITE}"/>
{body}
</svg>
"""


def main() -> None:
    svg = build()
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
