# L3 custody memo · Air4U sandbox × contrato de vitrina v0.2

Borrador del maker para revisión de Gideon (Legal). No es la decisión, no es asesoría cerrada y no autoriza firma ni carga de datos reales.

Estado: sin firmar. Contrato leído: vitrina v0.2, id `cth-showcase-001`, 14 oct 2026, más el archivo de cláusulas propuestas. Código leído: draft PR #26 de `gideonblaauw-creator/cth-datalab` (https://github.com/gideonblaauw-creator/cth-datalab/pull/26), rama `cursor/air4u-closed-sandbox-3eee`, commit `1620ee71230a9813313f87670212ca812742c30c`, abierto, no fusionado, no desplegado. Notas de reunión accesibles: no hay decisión registrada sobre custodia de L3, ONAC, Clínica Colombia ni el cliente de cannabis.

## English summary

The vitrina draft does not contain the sentence “CTH does not store raw L3”. Clause 3 forbids **publishing** raw L3, calibration, sensor metadata and the living-lab hourly series. Clause 4bis.4 calls Air4U the holder of the raw data and says the steward does not use it for CTH’s own purposes. Clause 2 sends living-lab and client-product data to a separate sandbox contract (`cth-sandbox-air4u-001`), which this memo did not have. PR #26 states that the sandbox contract still says CTH does not store raw L3.

PR #26 already persists raw readings. The local SQLite table `raw_readings` stores pollutant value, unit, UTC and `America/Bogota` timestamps, `device_id`, `site_id`, `client_id`, `location_code`, nullable latitude and longitude, `calibration_id`, QC flag and purifier state. The same database holds the client, the sector, the site and a calibration record whose ONAC / ISO/IEC 17025 fields are empty hooks. A synthetic CSV of those rows is committed in the repository. Seeded rows are labelled `Datos supuestos`, use `client_001` / `client_002`, sector `por_validar`, and null coordinates. Clínica Colombia and the Barranquilla cannabis company are not in the code. The schema is built so that real rows would land in a CTH-operated store, and the CTH steward token can read every row. HTTP reads are not logged.

Under Ley 1581 de 2012, article 3(c), a reading is personal data only when it relates to an identified or identifiable natural person. Indoor location, a timestamp joined to a shift or a patient, or CO2 used as occupancy of an assigned room crosses that line. It is sensitive data under article 5 when it reveals a person’s health, and article 6 then prohibits processing except in the listed cases. Clinic building air and a cannabis licensee’s site security stay confidential commercial information, including as a trade secret, unless a natural person is identifiable. Clinical-record rules apply only if the series is part of or can reconstruct a historia clínica. [VERIFICAR] the clinical-record and cannabis-licence instruments, and any ONAC retention period.

Ley 1581 article 25 is the National Database Registry, not the processor contract. The transmission contract is Decreto 1377 de 2013, article 25, reproduced in a circulating text of Decreto 1074 de 2015 as article 2.2.2.25.5.2. [VERIFICAR] the consolidated numbering.

Maker’s proposal, for Gideon to accept or reject: **option B, conditioned**. Where rows are personal data and sit on CTH systems, CTH is Encargado under a transmission contract, purpose-limited to sandbox validation and the later traceability file, with a fixed retention period, security, deletion or return, no own use, and no showcase use except aggregated anonymized output. Segregated storage and a location pseudonym whose key stays with Air4U (option C) are technical measures inside that contract. Air4U remains the party that decides purpose and the laboratory of record (the control piece of option A). Pure A does not match a SQLite file and a committed CSV inside CTH’s repository. Pure C leaves the Ley 1581 role unnamed.

---

## 1. Qué guarda el PR #26

Fuente: esquema en `living-lab/air4u-sandbox/air4u_sandbox/store.py`, generación en `synthetic.py`, registro de calibración en `clean.py`, acceso en `access.py` y `serve.py`, descripción en `living-lab/air4u-sandbox/README.md` y en el cuerpo del PR.

El sandbox está fuera de `app/`, no está en la API pública y el README ordena no copiarlo al VPS. Eso describe el despliegue. No describe el archivo: el código crea un SQLite local (`var/sandbox.sqlite3`, gitignored) y el PR añade `living-lab/air4u-sandbox/data/datos_supuestos.csv` (12.117 líneas añadidas) dentro del repositorio.

Tabla `raw_readings`, una fila por contaminante y por marca de tiempo:

| Campo | Qué es en el código |
|---|---|
| `value`, `pollutant`, `unit` | Lectura cruda. O3, PM1, PM2.5 y PM10 en µg/m³; CO2 en ppm. |
| `ts_utc`, `tz`, `ts_local` | Marca UTC, zona `America/Bogota` y hora local con desfase. Cadencia sembrada: 5 minutos. |
| `device_id`, `site_id`, `client_id` | Equipo, sitio y cliente. Sembrados `ag-syn-00N`, `site_00N`, `client_001` y `client_002`. |
| `location_code`, `lat`, `lon` | `location_code` es el `site_id`. Latitud y longitud existen y hoy van en nulo. |
| `calibration_id`, `qc_flag` | Enlace al registro de calibración. Flag `valid` o `invalid`. |
| `purifier_state`, `data_label` | Estado del purificador, hoy `por_validar`. Etiqueta `Datos supuestos`. |

En la misma base, no en otro almacén:

- `clients`: `client_id`, `sector`, `solution_owner` (`air4u`). El sector sembrado es `por_validar`. El código tiene rama `health` que bloquea el cierre si O3 supera 100 µg/m³, y no se la asigna al cliente sembrado.
- `sites`: zona, `location_label` (hoy `por_validar`), latitud y longitud.
- `devices`: intervalo, firmware `airgradient-open-pattern+o3-prototype`, origen del canal O3 `air4u_prototype`.
- `calibration_records`: JSON con método (co-ubicación lineal contra RMCAB/SDA), periodo, coeficientes en nulo, transformada identidad marcada como no calibración, y un bloque `onac` con `method_id`, `scope`, `certificate_id`, `uncertainty`, `traceability` y `personnel` en nulo. `equipment_id` es el texto `device_id`, no un identificador de equipo.
- `hourly`: promedios, mínimo, máximo, completitud y si el promedio se suprimió por la regla del 75 %.
- `gate_results`: sector, resultado de la prueba O3 y estado de cierre, incluido el rótulo de cierre sanitario.
- `tokens`: solo SHA-256 del bearer, rol, parte, `client_id`, admin, alta y vencimiento. El token en claro se escribe una vez en `var/local_tokens.json`, gitignored.
- `audit_events` y cuatro JSONL: etapas del pipeline (ingesta, limpieza, diagnóstico, tablero). `serve.py` descarta el log HTTP (`log_message` vuelve sin escribir).

Acceso que el código concede hoy, en local y con token:

- Cliente (`implementing_partner`): solo sus sitios.
- Air4U (`innovation_partner`, parte `air4u`): todos los sitios cuyo dueño de solución es `air4u`, los dos clientes sembrados.
- CTH (`steward` con `admin`): todas las filas.
- Sin token: rechazo.

`client_002` es un fixture de aislamiento, no una parte. El PR dice que los nombres del encargo no están en código, semilla ni tablero. Clínica Colombia y la empresa de cannabis de Barranquilla no aparecen en lo leído.

## 2. Conflicto con el v0.2

Partes del v0.2: Fundación CleantechHUB, NIT 901.523.941-9, custodio; Miguel Ángel Rozo, persona natural, nombre comercial Air4U. Borrador. Cargo y facultades del representante, cédula y matrícula de Air4U siguen en [VERIFICAR] dentro del propio borrador.

| Texto v0.2 | Qué hace | Qué hace el PR #26 |
|---|---|---|
| Cláusula 2 | La vitrina regula solo lo público. Living lab y producto cliente se rigen por `cth-sandbox-air4u-001`. | El sandbox vive en el repo del Datalab y su README dice que el contrato vigente del API sigue sin guardar L3 crudo, y que este sandbox guarda crudo sintético en su SQLite. |
| Cláusula 3, cierre | No se publicará L3 crudo, ni calibración, ni metadatos de sensores, ni la serie horaria del living lab, ni nombre o logo del cliente. | No publica eso en la vitrina. Sí lo persiste en SQLite y, en sintético, en un CSV del repo. |
| Cláusula 4bis.4 | Air4U, «como titular de los datos crudos y de la calibración», autoriza qué se entrega. El custodio no usa esos datos para fines propios. | CTH admin lee todas las filas crudas. No hay un fin propio codificado. Tampoco hay un control que impida copiarlas o conservarlas. |
| Cláusula 4bis.3 | El custodio registra los accesos. | El pipeline se audita. La lectura HTTP no. |
| Cláusula 4bis.6 | Si hay dato personal, Air4U es Responsable y CTH Encargado, salvo que el sandbox diga otra cosa. | No hay contrato de transmisión en el PR. El PR deja el DPA como pendiente. |
| Cláusula 8 y 11 | La API pública no sirve L3. Lo publicado no contendrá datos personales. | Coherente con la vitrina. El archivo crudo está al lado, en el sandbox. |
| Cláusula 1 y 10 | CTH muestra y no se adueña. La licencia de publicación es no exclusiva y revocable, y cubre lo publicado. | La licencia de la cláusula 10 no cubre el L3, porque el L3 no se publica. El almacenamiento queda sin cláusula. |

La frase «CTH no almacena L3 crudo» no está en el v0.2 leído. Está en la descripción que el PR hace del contrato de sandbox, que este memo no tuvo. [VERIFICAR] el texto de `cth-sandbox-air4u-001`.

El conflicto operativo, con lo que sí está leído, es este: la vitrina prohíbe publicar el crudo y trata a Air4U como quien tiene los crudos; el PR abre un archivo de crudos dentro de un repositorio que opera CTH, con lectura total del steward. Hoy las filas son sintéticas y etiquetadas. El esquema admite, sin cambio de tablas, valor real, coordenada, sector `health`, estado de purificador y el gancho ONAC. Cargar ahí a Clínica Colombia o al licenciatario de Barranquilla deja el archivo sin regla de custodia en el v0.2.

La palabra «titular» en la cláusula 4bis.4 choca con la Ley 1581 de 2012, artículo 3, literal f: Titular es la persona natural cuyos datos se tratan. Air4U puede ser Responsable (artículo 3, literal e) o dueño del dato no personal. No es el Titular por el hecho de haber medido el aire.

## 3. Cuándo es dato personal, sensible, o ninguna de las dos

Ley 1581 de 2012, artículo 3, literal c: dato personal es cualquier información vinculada o que pueda asociarse a una o varias personas naturales determinadas o determinables. El literal d define Encargado como quien trata por cuenta del Responsable. El literal g incluye el almacenamiento dentro del tratamiento.

La semilla actual no es dato personal. `client_001`, `site_001` y una coordenada nula no señalan a una persona natural. Una persona jurídica, por esa definición, no es Titular. El dato de la clínica como organización, o de la empresa de cannabis como organización, cae fuera del artículo 3 mientras no identifique a una persona natural.

Pasa a ser dato personal cuando la fila, sola o unida a otra información que las partes tienen, hace determinable a una persona natural:

- Ubicación interior de una habitación, cama, consultorio, puesto de trabajo o turno con un ocupante asignado. Un `location_code` que en la tabla de Air4U es «habitación 4» de Clínica Colombia, más la marca de tiempo, puede hacer determinable al paciente o al trabajador aunque CTH no guarde el nombre.
- Marca de tiempo unida a agenda, turno, carnet o al técnico que enciende el purificador. El campo `purifier_state`, hoy `por_validar`, hace eso si el estado queda ligado a una persona.
- Inferencia de ocupación. CO2 (y, en menor grado, el material particulado) a cada cinco minutos indica si el recinto estuvo ocupado y en qué horario. En un cuarto asignado a una persona, la ocupación es dato de esa persona. En un recinto mecánico compartido, sin roster y sin asignar, la serie sigue siendo dato del inmueble.
- Token de una persona con nombre. El hash no identifica. La fila sí, si `label` o `party` llevan el nombre del empleado. Las etiquetas sembradas (`local client_001`, `local cth admin`) no lo hacen.

Sigue fuera de la Ley 1581 cuando el sitio es una zona no asignada a una persona, la clave sitio–recinto–persona la tiene solo el cliente y no es razonablemente obtenible por quien trata la serie, y no hay turno ni paciente en el archivo. Con dos clientes conocidos en el encargo, el sector `health` reidentifica a la organización clínica. Eso es confidencialidad del cliente. No convierte, por sí solo, la serie en dato de una persona natural.

Es dato sensible, artículo 5, cuando revela la salud de esa persona: sensor en aislamiento, en un servicio cuya presencia revela diagnóstico o tratamiento, o una serie incorporada al estado de salud de un paciente identificable. El O3 o el PM2.5 de un corredor, sin ese vínculo, es medición del aire, no dato de salud. El artículo 6 prohíbe el tratamiento del dato sensible salvo los casos que lista, entre ellos la autorización explícita del Titular (literal a) y la finalidad histórica, estadística o científica con supresión de identidad (literal e). Una compuerta de calidad de aire para un living lab no es, sin más, el literal e.

Artículo 7: queda proscrito el tratamiento de datos personales de niños, niñas y adolescentes, salvo los de naturaleza pública. Si una habitación de Clínica Colombia hace determinable a un paciente menor, la serie no se trata con la autorización ordinaria del artículo 9. [VERIFICAR] el régimen vigente de datos de niños, que el Decreto 1377 de 2013 desarrolla, antes de cualquier sensor en pediatría.

Autorización del Titular: artículo 9, previa e informada, por medio consultable después. El artículo 10 lista los casos en que no hace falta. La validación de un sandbox comercial y un archivo futuro de acreditación no están en esa lista. La urgencia médica o sanitaria del literal c es un supuesto estrecho; una vitrina y un living lab no lo cumplen por estar en un hospital.

Principios que el archivo tiene que poder mostrar, artículo 4: finalidad informada al Titular, libertad, seguridad y confidencialidad. El principio de acceso y circulación restringida añade que el dato personal no público no queda en internet u otro medio de divulgación masiva, salvo acceso técnicamente controlable y limitado a Titulares o terceros autorizados. Un CSV de filas reales en un repositorio, aunque el repositorio sea privado, es circulación hacia el alojamiento de ese repositorio. El CSV sintético actual no es dato personal. El mismo camino, con filas reales identificables, sí lo sería.

## 4. Confidencialidad de sector, distinta del dato personal

### Clínica Colombia

La serie de calidad de aire del edificio es información operativa de la clínica. Es confidencial por el contrato con el cliente. Entra en la historia clínica solo si se incorpora al registro asistencial de un paciente o si permite reconstruirlo. [VERIFICAR] el instrumento vigente de historia clínica, en particular la Resolución 1995 de 1999 y las normas posteriores de historia clínica electrónica, y si alguna obliga a tratar la medición ambiental del edificio como parte de ese registro. Hasta esa verificación, el maker no aplica el régimen de historia clínica a un sensor de zona.

Si el vínculo con el paciente existe, concurren el artículo 5, el artículo 6 y el régimen de historia clínica. La autorización del representante de la clínica no reemplaza la autorización del Titular cuando el dato es personal, salvo un supuesto del artículo 10.

### Cannabis medicinal, Barranquilla

La razón social no está en el expediente. [PENDIENTE]. Ubicación del cultivo o del proceso, layout de seguridad, volúmenes, estado de licencia y estado del purificador son información de un operador licenciado. Se tratan como secreto empresarial e información de seguridad, y como dato confidencial del cliente. [VERIFICAR] los artículos de secretos empresariales de la Decisión 486 de la Comunidad Andina y el artículo de violación de secretos de la Ley 256 de 1996. [VERIFICAR] el decreto vigente de cannabis medicinal y científico, y qué datos de seguridad el licenciatario no puede sacar del sitio.

Esa información no es dato personal por ser de una licencia. Pasa a serlo si identifica al representante legal, al responsable técnico o a un trabajador por su presencia en un recinto asignado. La autorización del cliente cubre el secreto y la confidencialidad. Cubre el dato personal solo en la medida en que el cliente sea el Responsable y tenga, a su vez, autorización del Titular o un supuesto del artículo 10.

Ninguno de los dos clientes es parte del v0.2. Su autorización va en el addendum, no se presume por el OK de Air4U a la vitrina.

## 5. Qué pide en la práctica una trazabilidad tipo ONAC / ISO/IEC 17025

ONAC acredita organismos de evaluación de la conformidad. Una acreditación bajo ISO/IEC 17025 no es un certificado del producto ni de la clínica, y el PR lo dice: el bloque `onac` es un gancho, no una certificación. [VERIFICAR] el esquema y los criterios específicos de ONAC que aplicarían a este método de aire interior, y si el organismo que buscaría la acreditación sería Air4U, un laboratorio tercero, o CTH. Quien declara el sistema de gestión es quien conserva el expediente.

En la práctica, un expediente de ese tipo conserva:

- la observación original, no solo el promedio;
- la hora de la medición y la zona horaria;
- la identidad del método, del equipo y de su estado de calibración;
- la cadena de trazabilidad metrológica (aquí, el diseño apunta a co-ubicación contra RMCAB/SDA; los coeficientes están vacíos);
- la incertidumbre, hoy nula;
- la persona que ejecutó la actividad, hoy nula;
- información suficiente para repetir la medición en condiciones próximas a las originales.

El plazo de conservación lo fija el procedimiento del laboratorio. Cubre el ciclo de acreditación que el laboratorio declare y la ventana de controversia con el cliente. Este memo no fija un número de años. [VERIFICAR] contra el manual de calidad que Air4U aún no tiene, contra el criterio ONAC aplicable y contra la cláusula de retención del contrato. [VERIFICAR] la numeración de ISO/IEC 17025:2017 en registros técnicos, trazabilidad metrológica, equipos, informe de resultados y control de registros. No se transcribe la norma.

El PR no tiene borrado ni plazo. Los tokens vencen a los 90 días. Las filas no. Un archivo «hasta que haya acreditación», sin fecha, no cumple una finalidad limitada si el dato es personal (artículo 4, literal b).

Si el laboratorio de archivo es Air4U, el original del expediente vive con Air4U. Una copia en CTH, para el sandbox o para ayudar a armar el expediente, es tratamiento por cuenta de Air4U mientras CTH no decida la finalidad. Si CTH decidiera qué se conserva y para qué, CTH sería Responsable o corresponsable. El v0.2, cláusula 1, dice que CTH no usa los datos de la startup para fines propios. Esa frase empuja a Encargado, no a Responsable.

## 6. Corrección de la cita que se había propuesto para el DPA

La Ley 1581 de 2012, artículo 25, define el Registro Nacional de Bases de Datos, directorio público administrado por la Superintendencia de Industria y Comercio. No es el contrato de encargado. Lo reglamenta el Decreto 886 de 2014, recogido en el Decreto 1074 de 2015, y el ámbito de inscripción fue modificado por el Decreto 90 de 2018. [VERIFICAR] si los activos de la Fundación superan el umbral y si una base con dato personal de este sandbox debe inscribirse. La inscripción, cuando existe, es deber del Responsable.

El contrato de transmisión está en el Decreto 1377 de 2013, artículo 25. Debe fijar el alcance, las actividades que el Encargado hace por cuenta del Responsable, y las obligaciones del Encargado frente al Titular y al Responsable. El Encargado se obliga a aplicar la política de tratamiento del Responsable, a tratar solo para la finalidad autorizada, a dar tratamiento conforme a los principios, a salvaguardar la seguridad de las bases y a guardar confidencialidad. Un texto en circulación del Decreto 1074 de 2015 lo reproduce como artículo 2.2.2.25.5.2 y lo atribuye al artículo 25 del Decreto 1377. Otra nota de compilación dice que ese artículo del Decreto 1377 no quedó compilado y remite al artículo 3.1.1 del Decreto 1074. [VERIFICAR] la numeración vigente en el decreto único consolidado. La obligación sustantiva, en el Decreto 1377, está leída.

El artículo 24 del Decreto 1377 distingue transferencia y transmisión. La transmisión es la comunicación, dentro o fuera de Colombia, para que el Encargado trate por cuenta del Responsable. La transmisión internacional entre Responsable y Encargado no requiere ser informada al Titular ni contar con su consentimiento cuando existe el contrato del artículo 25. La transferencia, en la que el receptor es Responsable, sigue la Ley 1581, artículo 26.

Los deberes del Encargado están en la Ley 1581, artículo 18, incluidos conservar la información con seguridad, actualizar o suprimir, y permitir el acceso solo a quien puede tenerlo. Los del Responsable, en el artículo 17, incluyen pedir y conservar la autorización y exigir al Encargado las condiciones de seguridad.

El alojamiento OVH en la Unión Europea, cláusula 12 del v0.2, aplica al Datalab. El PR #26 no está desplegado ahí: el visor escucha en `127.0.0.1` y el README prohíbe copiar la carpeta al VPS. Si más adelante el SQLite o el CSV real se alojan en OVH, o si filas reales se suben al repositorio, hay comunicación fuera de Colombia. Con CTH como Encargado y un contrato de transmisión, el camino del Decreto 1377, artículo 24, numeral 2, es transmisión, no transferencia. OVH y el alojamiento del repositorio serían sub-encargados. [VERIFICAR] que sus contratos recojan el artículo 25 del Decreto 1377. Sin ese contrato, el artículo 26 de la Ley 1581 vuelve a ser la regla de la transferencia, incluida la declaración de conformidad de la SIC cuando no hay excepción. [VERIFICAR] si la SIC tiene declarado nivel adecuado para el país de destino concreto. No se afirma aquí.

## 7. Opciones de cláusula

Cada texto está para pegar. Ninguno está firmado. En las tres, el addendum de cliente es parte de la opción. «Dato crudo L3» significa la fila de `raw_readings` y sus metadatos de sitio, equipo, calibración, sector y purificador, más el CSV o export que la reproduzca.

### A. Custodia de Air4U, con lectura de CTH auditada y limitada

**Cláusula. Custodia del L3 por Air4U**

A.1 Air4U conserva el original de los datos crudos L3, de la calibración y del expediente de trazabilidad, en sistemas que Air4U controla. CTH no aloja, no copia de forma persistente y no versiona en su repositorio ese original.

A.2 CTH puede consultar el L3, en solo lectura, para dos finalidades: validar el sandbox del living lab y apoyar el armado del expediente de trazabilidad que Air4U le pida por escrito. Cada consulta queda en un registro inmutable con identidad del consultante, hora, finalidad y conjunto de sitios. CTH no usa la consulta para fines propios, no la publica y no la retiene más de [PLAZO CORTO, PENDIENTE] después de cerrada la consulta.

A.3 La vitrina sigue sin L3, sin calibración, sin metadatos de sensor y sin serie horaria del living lab. Lo que llegue a publicarse será agregado y anonimizado conforme a la cláusula 4.

A.4 Si una consulta hace determinable a una persona natural, esa consulta es tratamiento. Air4U es Responsable y CTH es Encargado solo por la consulta y por su registro, bajo el contrato de transmisión del Decreto 1377 de 2013, artículo 25 [VERIFICAR numeración en el Decreto 1074 de 2015]. El registro de acceso se borra o se devuelve con el mismo plazo de A.2, salvo el mínimo necesario para demostrar la auditoría.

**Addendum de cliente, opción A.** El cliente autoriza a Air4U a conservar el L3 de sus sitios y a permitir la consulta de CTH en los términos de A.2. El cliente declara el sector y si algún sitio está asignado a una persona natural, a un paciente o a un menor. Si lo está, el cliente no entrega el L3 hasta tener la autorización del Titular exigida por la Ley 1581 de 2012, artículos 6, 7 y 9, o un supuesto del artículo 10. Clínica Colombia instruye que el L3 no entre a la historia clínica salvo decisión escrita aparte. El licenciatario de cannabis marca como confidenciales de seguridad y secreto empresarial la ubicación, el layout, los volúmenes, el estado de licencia y el estado del purificador, y prohíbe sacarlos del entorno de Air4U hacia la vitrina.

**A favor.** Coincide con la cláusula 4bis.4 y con la frase de no almacenamiento que el PR atribuye al contrato de sandbox. Deja el expediente en quien sería el laboratorio. Reduce el papel de CTH.

**En contra.** El PR no está construido así. El original hoy es un SQLite en el árbol del sandbox y un CSV en el repositorio de CTH. Cumplir A exige mover ese original y prohibir el commit de filas reales.

**Riesgos.** Una consulta que materializa filas en disco de CTH es almacenamiento, y A.1 quedaría incumplida. El log de acceso puede ser dato personal. Si el cliente cree que «CTH no guarda nada» y el CSV sigue en git, la declaración es falsa. Miguel Ángel Rozo, persona natural, cargaría con el expediente hasta la cesión de la cláusula 16.

### B. CTH como Encargado, con contrato de transmisión

**Cláusula. Tratamiento del L3 por CTH como Encargado**

B.1 Cuando el L3, solo o unido a otra información, sea dato personal según la Ley 1581 de 2012, artículo 3, literal c, Air4U es el Responsable del Tratamiento y CTH es Encargado. CTH trata por cuenta de Air4U y no decide la finalidad. Encargado se entiende como en el artículo 3, literal d, con los deberes del artículo 18. Esta cláusula es el contrato de transmisión del Decreto 1377 de 2013, artículo 25 [VERIFICAR numeración en el Decreto 1074 de 2015, artículo 2.2.2.25.5.2].

B.2 Finalidades, y ninguna otra: (i) validar el sandbox del living lab de Air4U; (ii) conservar el expediente de trazabilidad que Air4U necesite para una acreditación futura tipo ONAC, con los campos de método, equipo, calibración, incertidumbre, persona y observación original. CTH no usa el L3 para fines propios, no lo cede, no entrena modelos con él y no lo muestra en la vitrina. La vitrina solo recibe salidas agregadas y anonimizadas que superen la revisión de vinculabilidad de la cláusula 4.

B.3 Conservación. El L3 personal se conserva por el plazo que Air4U fije por escrito al cargarlo, nunca superior a [PLAZO MÁXIMO, PENDIENTE] contados desde la última medición del sitio, y en todo caso se suprime o se devuelve a Air4U dentro de los 30 días siguientes al fin del sandbox o a la revocación de este contrato, lo que ocurra primero, salvo que una norma exigiera un plazo distinto [VERIFICAR]. CTH certifica la supresión. Los respaldos siguen el mismo plazo.

B.4 Seguridad y sub-encargados. Medidas técnicas, humanas y administrativas del artículo 4, literal g, de la Ley 1581. Acceso mínimo: Air4U a sus sitios, cada cliente solo a los suyos, CTH en roles nominados y solo para B.2. Cada lectura de CTH queda registrada. CTH no transmite el L3 a otro encargado, incluido el alojamiento, sin contrato equivalente al artículo 25 del Decreto 1377 y sin aviso previo a Air4U. Queda prohibido versionar L3 real en el repositorio de código.

B.5 El L3 que no sea dato personal se rige por el addendum de confidencialidad, con las mismas finalidades, el mismo plazo y la misma prohibición de vitrina. CTH no adquiere propiedad sobre él.

B.6 Roles. La frase «salvo que el contrato de sandboxing defina otra cosa» no cambia el papel de Encargado sin un escrito firmado por Air4U y CTH.

**Addendum de cliente, opción B.** El cliente autoriza a Air4U, como Responsable, a transmitir a CTH el L3 de sus sitios para las finalidades B.2, por el plazo B.3. Autoriza el alojamiento que Air4U le informe, hoy no desplegado y, si llegara a serlo, en la Unión Europea según la cláusula 12, como transmisión internacional cubierta por el Decreto 1377 de 2013, artículo 24, numeral 2, mientras exista este contrato. El cliente de salud entrega el inventario de sitios asignados a persona natural, paciente o menor, y no autoriza dato sensible ni dato de niños sin la autorización explícita correspondiente. El cliente de cannabis entrega el L3 como información confidencial de licencia y seguridad, prohíbe su publicación y prohíbe el acceso del otro cliente. Ningún cliente autoriza el uso en vitrina de un dato que permita identificarlo.

**A favor.** Coincide con la cláusula 4bis.6 y con el hecho de que el archivo está en sistemas del repo de CTH. Da plazo, borrado, prohibición de uso propio y prohibición de vitrina. Separa el dato personal, que tiene Encargado, del secreto del licenciatario, que tiene confidencialidad.

**En contra.** CTH asume los deberes del artículo 18 y la cadena de sub-encargados. Hay que borrar el hábito de commitear el CSV si las filas dejan de ser sintéticas. El plazo de acreditación puede ser más largo que el sandbox: hay que escribirlo al cargar, no dejarlo abierto.

**Riesgos.** Si CTH fija solo la finalidad, deja de ser Encargado y pasa a Responsable. Si el sector `health` más el sitio hacen determinable a un paciente, B.2 no basta: hace falta el artículo 6. Inscribir la base en el Registro Nacional, artículo 25 de la Ley 1581, es otra obligación, distinta de este contrato. [VERIFICAR] el umbral. Una transmisión a OVH sin contrato del sub-encargado no usa el atajo del artículo 24, numeral 2, del Decreto 1377.

### C. Híbrido: depósito segregado y ubicación seudonimizada

**Cláusula. Depósito segregado del L3**

C.1 El L3 crudo se guarda en un almacén separado de la vitrina, de la API pública y del repositorio de código. No comparte base, respaldo ni credencial con `datalab.cleantechhub.net`.

C.2 La ubicación que ve CTH es un código opaco. Latitud, longitud, dirección, nombre del sitio y nombre del cliente no entran a ese almacén. La tabla que une el código con el recinto, el cliente y cualquier persona la conserva Air4U, fuera de los sistemas de CTH.

C.3 CTH no intenta reunir el código con el recinto. El cliente y Air4U tampoco envían a CTH la clave, un roster, una agenda ni un plano.

C.4 El depósito dura el plazo de B.3 y se entrega a Air4U o se destruye al final, con acta. La vitrina no lee el depósito. Solo recibe el agregado anonimizado que pase la cláusula 4.

C.5 Si, pese a C.2, una persona natural resulta determinable, se aplica entero el régimen de la opción B desde el momento en que eso ocurra, y se corta la carga hasta cerrar el contrato de transmisión.

**Addendum de cliente, opción C.** El cliente acepta que el depósito no reciba la clave de ubicación y se obliga a no enviarla a CTH. Declara si el código, unido a información que el cliente o Air4U conservan, identifica a una persona natural. Si la identifica, el cliente marca el sitio y se aplica C.5 antes de la primera carga. La clínica y el licenciatario de cannabis mantienen la confidencialidad de sector descrita en A y en B, porque el seudónimo del recinto no cubre el secreto empresarial ni la reserva asistencial frente a quien sí tiene la clave.

**A favor.** Acerca el archivo a lo que la cláusula 4 ya hace en la vitrina: zona sin coordenada y sin nombre. El PR ya deja latitud y longitud en nulo y el rótulo en `por_validar`. Bajar la clave de sitio reduce la chance de que CTH tenga dato personal.

**En contra.** La Ley 1581 no define seudonimización. El artículo 3 mira si la persona es determinable, también con una clave que otra parte del mismo proyecto posee. `site_001` no es opaco entre quienes ya saben que el encargo es Clínica Colombia y un licenciatario en Barranquilla. El depósito no es una figura de la Ley 1581: quien opera el depósito trata, y necesita un nombre, Responsable o Encargado.

**Riesgos.** Falsa tranquilidad. El esquema actual guarda `client_id`, `sector` y `location_code` igual al `site_id` en la misma base. Eso no es C.2. Un depósito operado por CTH sin cláusula B es custodia innominada. Para ONAC, un código opaco sin la clave en el expediente del laboratorio puede dejar la observación incompleta; la clave tiene que vivir en el expediente de Air4U, no perderse.

## 8. Recomendación del maker

**Opción B, condicionada, con las medidas de C y el control de A.**

CTH es Encargado, y solo Encargado, respecto del L3 que sea dato personal y que repose en sistemas que CTH opera. Air4U sigue siendo quien decide la finalidad y el laboratorio que guarda el expediente de acreditación. El almacén va segregado de la vitrina y del repositorio, y la clave de ubicación física no entra a CTH. El L3 que no sea dato personal viaja con el addendum de confidencialidad, no dentro de una calificación forzada de dato personal.

A pura quedaría como la regla correcta el día en que el original salga del repositorio y de los servidores de CTH. Con el SQLite y el CSV donde están, declararla hoy no coincidiría con el sistema. C pura deja sin rol de la Ley 1581 a quien tiene las filas.

Condiciones para que B sea usable, antes de cualquier fila que no sea `Datos supuestos`:

1. Firmar la cláusula 4 ter de la sección 9 y el addendum con cada cliente.
2. Alinear `cth-sandbox-air4u-001` con esa cláusula. [VERIFICAR] su texto.
3. Dejar de commitear L3. El CSV sintético puede permanecer etiquetado; el real no entra al git.
4. Registrar la lectura del steward, que hoy `serve.py` no registra.
5. Escribir el plazo al momento de la carga. No usar «hasta ONAC» sin fecha.
6. Inventario del cliente: qué sitios hacen determinable a una persona, a un paciente o a un menor. Sin inventario, el sector `health` no se asigna.

## 9. Enmienda exacta al v0.2

No se reemplaza la prohibición de publicar. Se separa publicación y custodia. Se corrige «titular». Se inserta 4 ter, que es B con las medidas de segregación y de clave fuera de CTH.

### 9.1 Cláusula 2, párrafo ES. Añadir al final, sin borrar lo demás

Texto vigente, cierre del párrafo: «Los datos del living lab y del producto cliente se rigen por el contrato de sandbox (cth-sandbox-air4u-001). Algo de allí solo llega a la vitrina mediante este contrato.»

Añadir: «La custodia de datos crudos L3 en sistemas de CTH, si llega a existir, se rige por la cláusula 4 ter de este contrato. El contrato de sandbox se modificará para decir lo mismo antes de cargar L3 que no esté etiquetado como dato supuesto. Hasta esa modificación, CTH no carga L3 de un cliente real.»

### 9.2 Cláusula 3, frase final ES. Sustituir esa frase

Texto vigente: «Nada más se publicará: ni datos crudos L3, ni calibración, ni metadatos de sensores, ni la serie horaria del living lab, ni el nombre o el logo del socio implementador o del cliente final.»

Texto de reemplazo: «Nada más se publicará: ni datos crudos L3, ni calibración, ni metadatos de sensores, ni la serie horaria del living lab, ni el nombre o el logo del socio implementador o del cliente final. Esta frase prohíbe la publicación. No autoriza a CTH a almacenar L3 crudo. El almacenamiento, cuando exista, queda solo en la cláusula 4 ter.»

### 9.3 Cláusula 4bis.4. Reemplazar el numeral entero

Texto vigente: «Air4U, como titular de los datos crudos y de la calibración, autoriza por escrito qué datos se entregan a cada cliente final. El Custodio no usa esos datos para fines propios.»

Texto de reemplazo: «4bis.4 Air4U decide sobre los datos crudos y sobre la calibración, y autoriza por escrito qué datos se entregan a cada cliente final. En esta cláusula, Air4U no se llama Titular: Titular, en la Ley 1581 de 2012, artículo 3, literal f, es la persona natural cuyos datos se tratan. Si los datos son personales, Air4U es Responsable y CTH es Encargado en los términos de la cláusula 4 ter. El Custodio no usa esos datos para fines propios.»

### 9.4 Cláusula 4bis.6, última oración. Reemplazar esa oración

Texto vigente: «Air4U actuará como Responsable del Tratamiento de los datos que recolecta, y CTH como Encargado cuando trate esos datos por cuenta de Air4U, salvo que el contrato de sandboxing defina otra cosa [VERIFICAR roles caso a caso].»

Texto de reemplazo: «Air4U actuará como Responsable del Tratamiento de los datos personales que recolecta, y CTH como Encargado cuando los trate por cuenta de Air4U, conforme a la cláusula 4 ter y al Decreto 1377 de 2013, artículo 25 [VERIFICAR su numeración en el Decreto 1074 de 2015]. Otro rol exige un escrito firmado por Air4U y por CTH. El contrato de sandbox no lo cambia por silencio.»

### 9.5 Cláusula nueva 4 ter. Insertar después de 4bis.7

«4 ter. Custodia del L3 crudo.

4ter.1 Esta cláusula regula el almacenamiento de datos crudos L3, metadatos de sitio, equipo y calibración, y cualquier export que los reproduzca, cuando reposen en sistemas que CTH opera. No regula la vitrina. La vitrina sigue en las cláusulas 3, 4 y 11.

4ter.2 Si ese L3 es dato personal según la Ley 1581 de 2012, artículo 3, literal c, Air4U es Responsable y CTH es Encargado, artículo 3, literales d y e, con los deberes del artículo 18. CTH trata por cuenta de Air4U y no decide la finalidad. Este numeral es el contrato de transmisión del Decreto 1377 de 2013, artículo 25 [VERIFICAR numeración en el Decreto 1074 de 2015]. CTH aplica la política de tratamiento de Air4U, trata solo para la finalidad de 4ter.3, salvaguarda la seguridad de la base y guarda confidencialidad.

4ter.3 Finalidades: validar el sandbox del living lab, y conservar el expediente de trazabilidad que Air4U le encargue por escrito para una acreditación futura, con la observación original, la hora, el equipo, la calibración, la incertidumbre y la persona que midió, en la medida en que Air4U las entregue. No hay otra finalidad. CTH no usa el L3 para fines propios, no lo vende, no lo cede y no entrena modelos con él.

4ter.4 El L3 que no sea dato personal permanece en confidencialidad a favor de Air4U y del cliente final, con el mismo plazo y las mismas prohibiciones. CTH no adquiere propiedad sobre él. La información de licencia, seguridad y layout de un operador de cannabis, y la información operativa de un prestador de salud que no sea dato personal, se tratan como confidenciales y, donde el cliente lo declare, como secreto empresarial [VERIFICAR régimen].

4ter.5 Almacén. El L3 vive separado de la vitrina, de la API pública y del repositorio de código. Queda prohibido versionar L3 de un cliente real en git. La ubicación que CTH almacena es un código opaco. Dirección, coordenadas, nombre del sitio y nombre del cliente no entran al almacén de CTH. La clave que une el código con el recinto y con cualquier persona natural la conserva Air4U. CTH no la pide y no intenta reconstruirla.

4ter.6 Plazo. El que Air4U fije por escrito al cargar cada sitio, con un máximo de [PLAZO MÁXIMO, PENDIENTE] desde la última medición de ese sitio. Al terminar el sandbox, o al revocarse este contrato, CTH devuelve el L3 a Air4U o lo suprime en un plazo de 30 días, y certifica la supresión, incluidos los respaldos. Un plazo distinto por norma de acreditación se escribe antes de la carga [VERIFICAR].

4ter.7 Acceso. Cada cliente final solo a sus sitios. Air4U a los sitios cuya solución opera. CTH, por roles nominados, solo para 4ter.3. Cada acceso de CTH queda en un registro con persona, hora, finalidad y sitios. Sin ese registro el acceso no se abre.

4ter.8 Vitrina. Del L3 no sale hacia la vitrina otra cosa que un agregado anonimizado que haya pasado la cláusula 4. No se publica un dato que permita identificar a un cliente final, a un sitio o a una persona natural.

4ter.9 Sub-encargados. Incluido el alojamiento. CTH no les transmite L3 sin un contrato de transmisión equivalente y sin aviso previo a Air4U. Mientras el sandbox no esté desplegado, el tratamiento permanece en el entorno local acordado y no se sube al VPS ni a un tercero.

4ter.10 Dato sensible y niños. CTH no recibe L3 que revele la salud de una persona natural, ni L3 que haga determinable a un niño, niña o adolescente, sin la autorización explícita que exigen los artículos 6 y 7 de la Ley 1581 de 2012, o sin un supuesto escrito del artículo 10. El inventario de sitios lo entrega Air4U antes de la carga. A falta de inventario, CTH no asigna sector salud y no carga el sitio.

4ter.11 Clientes. Clínica Colombia y el operador de cannabis medicinal de Barranquilla no son parte de la vitrina. Su L3 no se carga sin el addendum de autorización y confidencialidad firmado por ese cliente, por Air4U y por CTH. El addendum recoge 4ter.3 a 4ter.10, la declaración de qué sitios identifican persona natural, paciente o menor, y la marca de secreto o reserva de seguridad.

4ter.12 Cesión. Si Air4U cede este contrato según la cláusula 16, la posición de Responsable y la decisión sobre el L3 no personal pasan a la Sociedad Cesionaria con la cesión. CTH sigue siendo Encargado, por cuenta de la Sociedad Cesionaria, sin un nuevo uso.

4ter.13 Lo supuesto. Las filas etiquetadas como datos supuestos, sin cliente real y sin persona determinable, pueden permanecer en el sandbox de desarrollo. No se usan como medición de un cliente y no se publican como medición real.»

### 9.6 Cláusula 11. Añadir una frase

Texto vigente: «Lo publicado no contendrá datos personales. Si apareciera alguno, se retira y se revisa con Legal según la Ley 1581 de 2012 y el Decreto 1377 de 2013 por validar; en la UE aplica además el RGPD.»

Añadir: «El L3 no publicado que sea dato personal se rige por la cláusula 4 ter, no por esta cláusula 11. El RGPD se mira solo cuando el tratamiento ocurra en la Unión Europea. Hoy el sandbox del PR #26 no está en ese alojamiento.»

### 9.7 Qué no se toca

Las cláusulas 4 (reglas de no reidentificación de lo publicado), 8 (API pública sin L3) y 16 (cesión a la sociedad de Air4U) se mantienen. 4ter.12 engancha la cesión. El anexo de firmas no cambia.

## 10. PENDIENTE para Gideon

1. PENDIENTE. Leer `cth-sandbox-air4u-001` y señalar la frase exacta que dice que CTH no almacena L3, si existe. Este memo no la tuvo. La enmienda de la cláusula 2 queda colgando de ese texto.
2. PENDIENTE. Aceptar, recortar o rechazar la opción B condicionada. A pura queda disponible si el original se mueve a sistemas de Air4U.
3. PENDIENTE. Fijar el plazo máximo de 4ter.6 y el plazo corto de consulta, contra el criterio ONAC aplicable y el manual que Air4U no tiene. [VERIFICAR] numeración de ISO/IEC 17025:2017.
4. PENDIENTE. Confirmar la numeración vigente del contrato de transmisión en el Decreto 1074 de 2015. La obligación leída es el Decreto 1377 de 2013, artículo 25. No usar el artículo 25 de la Ley 1581 como base del DPA: ese artículo es el Registro Nacional de Bases de Datos.
5. PENDIENTE. Decidir si la base, el día que tenga dato personal, se inscribe en ese Registro. [VERIFICAR] umbral de activos tras el Decreto 90 de 2018.
6. PENDIENTE. Razón social, NIT y representante del operador de cannabis en Barranquilla, y si su licencia restringe sacar ubicación o datos de seguridad del establecimiento. [VERIFICAR] decreto vigente de cannabis medicinal.
7. PENDIENTE. Inventario de Clínica Colombia: zonas asignadas a paciente, trabajador o menor, y si alguna serie entraría a la historia clínica. [VERIFICAR] Resolución 1995 de 1999 y normas posteriores antes de afirmar que el sensor de edificio queda fuera.
8. PENDIENTE. Sub-encargados. El PR no despliega en OVH. Si se despliega, hace falta el contrato de transmisión con el alojamiento y la confirmación de si la SIC tiene declarado nivel adecuado para ese país. [VERIFICAR].
9. PENDIENTE. Si el dato personal llega a tratarse en la Unión Europea, qué parte del RGPD añade deberes encima de la Ley 1581. La cláusula 11 del v0.2 lo menciona. El sandbox leído está en local.
10. PENDIENTE. Facultad del representante de CTH y existencia de matrícula o marca de Air4U, ya marcadas en el v0.2. La cesión de la cláusula 16 arrastra la posición de Responsable; conviene que el DPA nazca ya con esa cesión prevista, como hace 4ter.12.
11. PENDIENTE. Borrar o aislar el patrón del CSV commiteado antes de que exista una fila real. El archivo sintético, etiquetado, puede quedar.
12. PENDIENTE. Log de lectura del steward. El código audita el pipeline y no la consulta HTTP. 4ter.7 no se cumple con el PR tal como está.

Nada en este memo se envía a Air4U, a los clientes ni a un tercero.
