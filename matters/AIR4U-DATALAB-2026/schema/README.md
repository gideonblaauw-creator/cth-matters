# Esquema vivo · tres partes

Propuesta del maker para el sandbox de Air4U en el Datalab: opción B condicionada, leída de `../L3-CUSTODY-MEMO.md`. No es la decisión, no es asesoría cerrada y no autoriza firma ni carga de datos reales.

El PNG es una página A4 horizontal (3508 × 2480 px, 300 ppp, más de 2400 px de ancho).

## Archivos

| Archivo | Para qué |
|---|---|
| `three-party-schema.svg` | Fuente gráfica. Es lo que se edita y lo que se imprime en vector. |
| `three-party-schema.png` | Raster de esa página. |
| `build_schema.py` | Vuelve a escribir el SVG desde los textos de las fichas. |
| `render.py` | Rasteriza el SVG a PNG con Chrome. |
| `fonts/` | Open Sans (regular, semibold, bold), licencia SIL OFL. Ver `fonts/OFL.txt`. |

## Regenerar

Desde esta carpeta:

```bash
python3 build_schema.py
python3 render.py
```

`build_schema.py` reescribe `three-party-schema.svg`. Un retoque hecho a mano en el SVG se pierde si se vuelve a correr.

Para cambiar solo la posición o un rótulo y conservar el resto, edita el SVG y corre únicamente:

```bash
python3 render.py
```

Hace falta Python 3 con Pillow, y Google Chrome en `PATH`. Las fuentes tienen que seguir junto al SVG: el `@font-face` usa `fonts/OpenSans-*.ttf`. `render.py` comprueba el tamaño, la proporción A4 horizontal y que no haya un rojo saturado.

## Cómo leer las marcas

- **[VERIFICAR]** — punto de derecho o de hecho que el memo deja abierto. No se completa aquí.
- **PENDIENTE** — costo o dato que el memo no fija. No hay cifra ni deudor. Sandbox, sensores, living lab, alojamiento, acreditación tipo ONAC, inscripción en el RNBD y asesoría están en PENDIENTE.

## Color y tipo

`#0C498A`, `#B2EEFA`, `#9DC384`, `#669348`, `#69B5FA`. Open Sans. Los riesgos van en azul marino o en verde. No se usa rojo.

## Impresión

A4 horizontal, al 100 %. El PNG ya está a 300 ppp. El SVG usa las mismas medidas (`viewBox` 3508 × 2480).
