# Medición de impacto — Datalab CleantechHUB

**Fuentes:**

- Entrevista de seguimiento AuRA y correo resumen a Cubo Social, **6 nov 2026**.
- Memo técnico Air4U en repo: `matters/AIR4U-DATALAB-2026/L3-CUSTODY-MEMO.md` (rama remota `origin/cursor/air4u-l3-custody-memo-2fd4`; no fusionado en `main` al 10 nov 2026).
- Vitrina pública: https://datalab.cleantechhub.net/

---

## 1. Calificación citada en la entrevista AuRA

En el seguimiento a seis meses, Gideon comunicó que la medición de impacto del programa operado por CTH se ubicaba en torno a **~3,8** (escala y metodología de auditoría no detalladas en el correo).

| Dato | Valor | Fuente |
|------|-------|--------|
| Calificación comunicada | ~3,8 | Correo / entrevista 6 nov 2026 |
| Herramienta | Datalab | Correo 6 nov 2026 |

**PENDIENTE:** confirmar contra qué escala y periodo se midió el **~3,8** del 6 de noviembre (podría ser un indicador de Datalab o del portafolio, distinto de la rúbrica de selección CLP). Hasta tener ese cruce, no se usa el ~3,8 como equivalente al puntaje de clima en convocatoria.

### Impacto climático en la rúbrica de selección (Colombia, 28 may 2026)

Con el instrumento documentado en **«Copia de Criterios de selección 2026»** (criterio *Climate Impact*, escala 1–5), la cohorte **seleccionada en Colombia** (25 equipos) promedió **3,52/5** en el criterio **Clima**. El conjunto evaluado (79) promedió **3,06/5** en el mismo criterio.

| Métrica | Evaluadas (79) | Seleccionados (25) | Fuente |
|---------|----------------|---------------------|--------|
| Clima (1–5) | 3,06 | **3,52** | Matriz Colombia 28 may 2026; `01-matriz-anonimizada.csv` |

---

## 2. Dimensiones de impacto (marco comunicado a AuRA/Cubo Social)

Dimensiones mencionadas en la síntesis del 6 nov 2026:

| Dimensión | En repo |
|-----------|---------|
| Agua | Criterio citado en entrevista — sin ficha de indicador en `cth-matters` |
| Emisiones | Idem |
| Economía circular | Idem |
| Energía | Idem |
| Triple impacto (ambiental, social, económico) | Idem |

No hay en este repositorio el catálogo maestro de KPIs por vertical startup. La vitrina **datalab.cleantechhub.net** y el deck CLP26 son los enlaces operativos que Valentina aceptó usar.

---

## 3. Ejemplo público en Datalab: Air4U

El correo del 6 nov 2026 señala **https://datalab.cleantechhub.net/** con **Air4U** como ejemplo de tablero.

El memo Air4U del repo describe, a nivel de **arquitectura de datos y trazabilidad** (no como promesa de producción desplegada), un patrón de registro que sirve de referencia para “cómo se registran y verifican” lecturas en un living lab:

### 3.1 Indicadores / variables (ejemplo técnico Air4U, sandbox)

| Variable | Unidad / notas | Fuente repo |
|----------|----------------|-------------|
| O₃ | µg/m³ | `L3-CUSTODY-MEMO.md` §1 (tabla `raw_readings`) |
| PM1, PM2.5, PM10 | µg/m³ | Idem |
| CO₂ | ppm | Idem |
| Marca de tiempo | UTC + `America/Bogota` local | Idem |
| `qc_flag` | `valid` / `invalid` | Idem |
| Completitud serie horaria | Regla de supresión si &lt;75 % completitud (promedios horarios) | Idem (descripción `hourly`) |

**Nota:** este ejemplo es **calidad de aire interior** (Air4U), no agua/circularidad. Ilustra el **mecanismo** Datalab; los indicadores de agua, emisiones, energía y circularidad del portafolio CLP/Nexus **PENDIENTE** de exportar desde Datalab o documentación de producto.

### 3.2 Fuentes de datos (ejemplo Air4U)

| Fuente | Rol | Fuente repo |
|--------|-----|-------------|
| Sensores / dispositivo (`device_id`, firmware) | Ingesta L3 | Memo §1 |
| Registro de calibración (`calibration_records`, gancho ONAC / ISO 17025) | Trazabilidad metrológica | Memo §1 |
| Etiquetas de datos | p. ej. `Datos supuestos` en semillas sintéticas | Memo §1 |

### 3.3 Registro del resultado

Pipeline descrito en el memo (rama Air4U):

1. **Ingesta** → tabla `raw_readings` (SQLite en sandbox documentado).  
2. **Limpieza / QC** → `qc_flag`, reglas de sector (ej. umbral O₃ para sector salud en código citado).  
3. **Agregación horaria** → tabla `hourly` con completitud.  
4. **Auditoría de etapas** → `audit_events` y JSONL por etapa (ingesta, limpieza, diagnóstico, tablero).  
5. **Control de acceso por rol** → tokens con alcance por `client_id` / steward.

**Fuente:** `matters/AIR4U-DATALAB-2026/L3-CUSTODY-MEMO.md`, sección 1.

### 3.4 Verificación

| Mecanismo | Descripción | Fuente |
|-----------|-------------|--------|
| QC en ingestión | Flags válido/inválido | Memo §1 |
| Calibración documentada | Registro con método, periodo, coeficientes; campos ONAC como hooks | Memo §1 |
| Reglas de publicación | La vitrina pública no expone L3 crudo ni calibración (contrato v0.2 citado en memo) | Memo §2 |
| Acceso trazable | Roles cliente / innovación / steward; auditoría de pipeline (con nota de que HTTP read no se loguea en el prototipo) | Memo §§1–2 |

Para el portafolio general (Nexus), el correo del 6 nov 2026 indica **~200 startups desde 2021** y **~600 ideas** en https://nexus.cleantechhub.net/ — inventario relacional, no sustituye KPIs ambientales por startup.

---

## 4. Watson (acompañamiento e impacto)

| Dato | Valor | Fuente |
|------|-------|--------|
| Bot Watson | Piloto en el año de la entrevista; **obligatorio** el año siguiente | Correo 6 nov 2026 |

**PENDIENTE:** flujo documentado de cómo Watson alimenta o valida indicadores en Datalab.

---

## 5. Resumen para Cubo Social

| Pregunta de Valentina | Respuesta con fuentes actuales |
|----------------------|--------------------------------|
| Indicadores de ejemplo | Triple impacto + agua, emisiones, circularidad, energía (6 nov); detalle por startup **PENDIENTE** |
| Fuentes | Sensores / operación startup / registros en Datalab; ejemplo técnico Air4U en memo repo |
| Registro y verificación | Pipeline QC, calibración, agregación, auditoría de etapas (memo Air4U); vitrina en datalab.cleantechhub.net |
