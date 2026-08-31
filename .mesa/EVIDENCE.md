# Evidencia

`[E]` evidencia verificable · `[I]` inferencia · `[S]` supuesto

## G0 — Encuadre

| # | Hallazgo | Fuente | Tipo | Confianza |
|---|---|---|---|---|
| 1 | El que arma el deck no es dueño del copy: el texto entra "ya aprobado, bloqueado" y los huecos se devuelven a Varu/Pato | `magoya-deck/ROADMAP.md:3, :35, :42` | E | alta |
| 2 | El "agente de copy que reescribe cada texto" no tiene mandato real; lo que hace falta es señalar qué falta | `ai/metodo.md:27` vs. hallazgo 1 | I | alta |
| 3 | Nadie llega con la narrativa pensada: el insumo real es transcript de Granola (16 reuniones), doc de la CEO, decks viejos | `brand-system/PLAN.md:13, :17` | E | alta |
| 4 | La causa documentada de que un deck no cerrara fue "narrativa sin dueño" y "multi-audiencia sin hilo único" — no las plantillas | `brand-system/PLAN.md:21-23` | E | alta |
| 5 | La Fase 1 de metodo.md exige como INSUMO ("escribí LA idea") lo que el equipo nunca produce | `ai/metodo.md:11` vs. hallazgo 3 | I | alta |
| 6 | Los decks de cuenta grande son en inglés y no traducidos; salió material con inglés roto ("tested during the righ ag window") | `VOICE-RESEARCH.md:296, :306` | E | alta |
| 7 | El sistema tiene una sola voz para cinco audiencias | `VOICE-RESEARCH.md:320` | E | alta |
| 8 | El costo se paga en vueltas: 48 commits en 9 días en la propuesta JD, 27 de ellos apply/feedback/fix/sync; slide de inversión retocada ~7 veces; 3 variantes de PDF por audiencia | `john-deere-pilot-proposal` (git log 2026-07-09 → 07-17) | E | alta |
| 9 | El costo de copy inventado ya tiene mitigación puesta (`ai/facts.json`), tras el commit "revert invented copy to grounded/flagged versions" | JD, commit 2026-07-10 | E | alta |
| 10 | **Cero decks reales pasaron por la capa**: salió 2026-08-13, el último deck de cuenta grande es 2026-08-11 | fechas de repo | E | alta |
| 11 | Ningún archivo fuera de `brand-system` referencia `selector.json`, `templates/index.json` ni `metodo.md`. El usuario "cualquier IA de un tercero" todavía no apareció | grep en `/Users/facu/Claude` | E | alta |
| 12 | Bus factor = 1: Facu produce, decide y tiene el material fuente | `ROADMAP.md:245` (R6) | E | alta |
| 13 | Hay cola más barata con exposición directa en cuentas que facturan: roster con nombres falsos (A5, "el placeholder más caro"), cita de Camila (A6), pase de inglés | `ROADMAP.md:123` | E | alta |
| 14 | Faltan tres números para evaluar la inversión: valor de deal por deck, decks/mes y vueltas promedio, horas por vuelta | `ai/facts.json:27` los declara sin fuente | E | alta |

## G1 — Evidencia · investigador (material crudo → deck)

| # | Hallazgo | Fuente | Tipo | Confianza |
|---|---|---|---|---|
| 15 | Ninguna categoría de corrección domina por conteo (~46 commits JD: ~12 visual, ~11 narrativa, ~7 dato, ~5 variante por audiencia) pero **solo la narrativa regresiona**: el commit `0b53c45` tuvo que *restaurar* la tesis mid-market que una ronda anterior había borrado sin que nadie lo notara | `john-deere-pilot-proposal` git log | E | alta |
| 16 | El corpus de feedback más grande es abrumadoramente visual (F01–F60): "el título no dice nada" aparece 2 veces, "el dato no es real" 1 vez. Las rondas 2 y 3 del Knowledge Experience son 14 carpetas de A/B puramente visual, cero variante narrativa | `AUDITORIA-FEEDBACK.md` F14, F35:112, F43:125 · `magoya-deck-round3/` | E | alta |
| 17 | **La capa no se puede calibrar contra lo que la gente pide.** Pide visual porque el copy entra bloqueado y es el único grado de libertad que queda. Hay que calibrar contra lo que se rompe callado: detectar regresión de tesis entre vueltas vale más que detectar títulos flojos | derivado de 15 y 16 | I | alta |
| 18 | El material crudo **crece ~60% y crece justo donde contradice el brief**: 8 slides en el Master Script → 13 en `app/deck.json` → "14 scenes". Los 5 agregados (Agenda, pillars IT-only, mapa, quote de Apeel, foto de founder) no están en el script | `PLAN.md:13` · `app/deck.json:16,73,120,132,136-142` · `magoya-deck/DESIGN-BRIEFS.md:3` | E | alta |
| 19 | Ahí viven las contradicciones: la CEO pidió "sin personas, sin fotos" y el slide agregado s7c es exactamente una foto de persona. Con los datos igual: "16+ years", "20+ years" y "9+ years" conviven en el mismo archivo, y `facts.json` solo respalda 2017 (=9) | `PLAN.md:16, :80` · `app/deck.json:28, :37, :141` · `ai/facts.json:7, :27` | E | alta |
| 20 | **Quién decidió las 5 slides agregadas y con qué criterio no está escrito en ningún archivo.** `PLAN.md:56` describe el paso como "mapear las 8 slides a arquetipos" — mapeo, no expansión | ausencia de registro | E | alta |
| 21 | Paso invisible, mitad 1: **reconciliar copy nuevo contra decisiones estructurales ya tomadas.** El commit `1898eba` se llama literalmente "reconciled with prior structural decisions" y al día siguiente `dca5848` tuvo que elegir autoridad entre fuentes en conflicto. Ese ledger vive solo en la cabeza de Facu | JD git log | E | alta |
| 22 | Paso invisible, mitad 2: **declarar el hueco en la pieza.** Ya existe como conducta humana y como convención inventada — `70e4e1a` "blank Investment values to USD xx (avoid confusion until confirmed)" — y hay 3-4 commits de propagarla a mano a las otras copias del mismo contenido | JD git log `70e4e1a`, `6524f52` | E | alta |
| 23 | **El gate que se le pide a la IA no mide nada de esto**: los 16 chequeos de `.ai/checklist.md` son 16/16 visuales o léxicos (hex, lima, 75/25, chips, emojis, IA-vs-AI). Cero sobre huecos, procedencia del dato, contradicción con decisión previa o adecuación a audiencia | `.ai/checklist.md` | E | alta |

**Huecos declarados por el investigador (no se tapan):**
- n=1 en decks de cliente real: toda la clasificación de vueltas sale de la propuesta JD. Con un segundo deck de cuenta grande clasificado, el hallazgo 17 pasa de inferencia a evidencia.
- **No hay transcript ni doc crudo en disco.** Se leyó el *resumen* del Master Script y de las 16 reuniones en `PLAN.md:12-26`, no las fuentes. No se puede verificar si la CEO manda narrativa o bullets, y eso cambia por completo qué tiene que hacer la capa en el primer paso.
- Quién agregó las 5 slides: sin registro. Si fue Facu de cabeza, es el paso invisible más caro y hay que escribirlo; si lo pidieron Varu/Pato, el hueco es de sincronización con el Master Script, no de criterio.

## G1 — Evidencia · analista-datos (benchmark y medición)

| # | Hallazgo | Fuente | Tipo | Confianza |
|---|---|---|---|---|
| 24 | El mecanismo del mercado es **clasificador con catálogo cerrado**, no elección libre. Presenton (el único auditable, ~9.6k★) hace outline y después fuerza por JSON-schema un índice de layout por slide, con reglas duras sobre la **forma del dato** ("tabla numérica de n columnas → layout de n-1 charts", "no elijas layout con imagen si no hay imagen") | [generate_presentation_structure.py](https://github.com/presenton/presenton/blob/main/servers/fastapi/utils/llm_calls/generate_presentation_structure.py) | E | alta |
| 25 | Ese selector está indexado por **forma del dato**; el de Magoya por **intención retórica**. Son dos ejes distintos y el de forma es el que se puede verificar sin criterio | derivado de 24 | I | alta |
| 26 | **Rellenar es el default del estado del arte**: en todo el backend de Presenton hay 3 menciones de grounding, todas "no inventes citas/valores", y cuando falta un asset inyecta un placeholder **en silencio**. Gamma y Beautiful.ai también eligen de catálogo cerrado por reglas, no freeform | mismo repo · [Gamma](https://gamma.app/explore/content/guides/gamma-flexible-card-layout-presentations) · [Beautiful.ai](https://www.beautiful.ai/smart-slides) | E | alta |
| 27 | Abstenerse sigue sin resolverse en la industria: los modelos de razonamiento **pierden 24% de abstención** vs. sus pares no-razonadores, y lo único que la sube sin costo de precisión es un **system prompt dirigido** → ahí hay diferencial real y barato | [AbstentionBench, arXiv 2506.09038](https://arxiv.org/html/2506.09038v1) (20 modelos, 35k queries) | E | alta |
| 28 | **Las fórmulas de legibilidad sobre texto de slide son humo.** El deck JD ya tiene oraciones sanas (12,8 palabras) y las fórmulas piden ≥100 palabras de prosa corrida; los bullets sin verbo cuentan como oraciones cortísimas e inflan el score. La copy en español de IA en campo ya da FH 84,1 / INFLESZ 80,1 ("fácil") | medición sobre `john-deere-pilot-proposal/index.html` · [Redish sobre límites de las fórmulas](https://redish.net/wp-content/uploads/Redish_on_Readability_Formulas.pdf) | E | alta |
| 29 | **La métrica que sí decide es el test de títulos, y es auditable: solo 2 de 12 títulos del deck JD son aserciones** (sujeto + verbo + claim). Los otros 10 son etiquetas de tema; leídos solos no reconstruyen el pedido | medición sobre el deck JD | E | alta |
| 30 | Base experimental del criterio: assertion-evidence mide mejor comprensión, mejor recall diferido y menor carga cognitiva que topic-subtopic | [Garner & Alley, Penn State, n=110-111](https://writing.engr.psu.edu/ae_comprehension.pdf) · [ASEE](https://peer.asee.org/assertion-evidence-slides-appear-to-lead-to-better-comprehension-and-recall-of-more-complex-concepts.pdf) | E | alta |
| 31 | **El selector alcanza 31 de 41 módulos por camino primario.** Los otros 10 (A5, B2, D3, E4, G2, H2, H3, I2, J2, M2) solo se llegan por una cláusula `alternativa` condicionada a criterio de diseño ("si hay foto potente", "si es conceptual y pide personaje") — exactamente lo que el selector promete evitar en su propio `que_es` | `ai/selector.json` | E | alta |
| 32 | **≥8 tipos de contenido real no tienen fila en el selector**: resumen ejecutivo de dos bloques con links, objetivos del proyecto, journey de dos niveles (el de JD son 3 etapas × 5 sub-pasos, E1 es plano), criterios de éxito con métrica, **cinco** cifras (C1=4, C4=3, el Master Script slide 4 tiene 5), cartera de varios casos en un slide (G1 es uno, el slide 7 son 4), equipo como workstreams con capacidad "6 → 10" (J3 es personas), y apéndice/fuentes | `ai/selector.json` vs. `PLAN.md` §1a y decks reales | E | alta |
| 33 | **`grep -iE 'falta\|hueco\|pendiente\|sin dato'` en `selector.json` = 0 hits.** El selector no tiene camino para "no tengo el dato": solo mapea contenido que existe | `ai/selector.json` | E | alta |
| 34 | **El catálogo está dimensionado más liviano que el contenido que entra**: mediana de presupuesto 694 caracteres/módulo contra mediana real de 1.062 caracteres/slide; solo **12 de 41 módulos** tienen presupuesto para la mediana real | conteo sobre HTML renderizado (orden de magnitud, incluye labels) | I | media |

**Métrica de éxito propuesta por el analista** (reemplaza al criterio difuso de G0):

| | Hoy | Objetivo |
|---|---|---|
| Títulos-aserción en slides de contenido | **17%** (2/12, deck JD jul'26) | ≥80% en el primer deck real que pase por la capa |
| Vueltas de reconciliación | **27 commits** apply/feedback/fix (E8) | ≤10 en el próximo deck de cuenta grande |
| Densidad (guardarraíl) | mediana 135 palabras/slide | mediana ≤110 |

**Instrumentación que no existe y hay que empezar a medir** (el analista lo llama el hallazgo grave):
1. **Precisión y recall de la declaración de huecos**: por deck, cuántos huecos declaró la IA vs. cuántos apareció después el humano. Sin este número **el reencuadre de G0 no es evaluable**, y hoy no hay ningún registro.
2. Fit-rate de primera pasada: % de slides que entra en el presupuesto del módulo elegido sin tocar la fuente.
3. Los tres números de E14 siguen sin fuente. La disidencia de negocio no se puede resolver con dato, solo con preferencia.

**Corrección de cifra:** son 344 slots en total, de los cuales 339 son de texto con límite y 5 son de gráfico/tabla (sin límite de caracteres por diseño).

## G1 — Evidencia · prueba a ciegas B (material crudo real: Master Script v6)

Una IA con **solo** `https://brand.magoya.com/ai/claude.md` y el material de la CEO. Declaró sus
fuentes: solo `brand.magoya.com` + el checklist de GitHub. Tenía skills y memoria local a mano y
**declaró no haberlas abierto** — la corrida es válida.

### Lo que funcionó (importante: el reencuadre de G0 ya funciona a medias)

| # | Hallazgo | Tipo | Confianza |
|---|---|---|---|
| 35 | El flujo copiá-pegá funciona de verdad: `selector.json → templates/index.json → <ID>.txt` es un camino sin ambigüedad, y el `max_caracteres_aprox` por slot le permitió validar cada texto antes de renderizar. 0 desbordes, 0 imágenes rotas, 0 hex fuera de tokens, geometría intacta | E | alta |
| 36 | **El aviso anti-resumen se activó en la vida real**: su primer fetch devolvió exactamente el resumen sin links que el aviso anticipa. La mitigación de la v1.5 era necesaria y sirvió | E | alta |
| 37 | **Declaró los huecos en vez de rellenar**: marcó las 5 métricas de la CEO como no verificables, **se negó a usar el 95% de retención** (pendiente en `facts.json`), dejó `[PENDIENTE]`/`[XX]` en los casos, y detectó que "25 organizaciones" **contradice** los 17 clientes aprobados. También reescribió el título más débil por su cuenta | E | alta |
| 38 | Línea de base de declaración de huecos (la instrumentación que pedía el analista): **11 bloques declarados** en una pasada, 7 de dato/contenido y 4 de bloqueo del sistema | E | alta |

### Contradicciones del spec — verificadas por mí una por una

| # | Contradicción | Verificación | Tipo |
|---|---|---|---|
| 39 | `constraints.json` exige "exactamente un golpe de lima por slide", pero **M2, L1, C1, A1, E2 y M1 tienen CERO lima**. Las plantillas oficiales no pueden cumplir su propio constraint sin tocar geometría. Y el checklist #5 lo perdona ("falla si hay dos o más"): los dos documentos no dicen lo mismo | `grep` de lima en las 6 plantillas = 0 | E |
| 40 | `selector.json` dice que M3 tiene **CUATRO** pasos y "llená los cuatro, no borres ninguno"; `templates/index.json` dice "**Tres** próximos pasos concretos" | confirmado en ambos archivos | E |
| 41 | Checklist #1 (cualquier hex de `tokens.json` es válido) y #2 (prohibido todo hue 20–65° salvo `#FFC67B`) no pueden ser ciertos a la vez: `tokens.json` incluye `#E0A33A`, **hue 38°** | calculado: 38.0° | E |
| 42 | El manifiesto tenía **239** archivos y se publicaba **247** en 6 lugares. Causado por mi propio cambio de bajar `assets/refs` (que eran 404). El validador no lo detectó porque cruzaba estructura, no prosa | corregido + chequeo nuevo en `validar.py` | E |
| 43 | La portada M2 es prácticamente 100% verde profundo y el checklist #6 falla la pieza 100% verde. El chip de M2 viene en sentence case y el checklist #14 lo falla; corregirlo pide tracking, que es tipografía bloqueada. **Sin salida dentro de las reglas** | reportado, no re-verificado | E |
| 44 | `constraints.json` dice que ningún texto cruza el margen interior del 7% (92.5cqw), pero las cajas de B3 terminan en 94.5cqw y las de G1 en 93.1cqw | medido en navegador por el agente | E |
| 45 | `fondos_permitidos` de slides nombra `#133825`, pero M2 usa `#0C2117`. Los dos están en tokens | reportado | E |

### Módulos que faltan — confirma y amplía el hallazgo 32

| # | Hallazgo | Tipo |
|---|---|---|
| 46 | **No hay módulo para 3 pilares**, que es un beat clásico de deck comercial: E2 pide 6 ítems en 2 columnas, B1 tiene 3 pero está documentado para "los tres modelos de trabajo". Tuvo que elegir contra el selector y declararlo | E |
| 47 | **Y repurposar un módulo trae un defecto invisible**: el golpe de lima de B1 está en la card del medio, "el modelo que estás proponiendo". Usado para pilares, eso destaca **Confidence sin ningún motivo semántico**, y no se puede mover porque es geometría | E |
| 48 | Tampoco hay módulo para **5 métricas** (C1 tope 4, C4 son 3 — y el Master Script trae 5) ni para **4 casos**: G1 y G2 traen logos de cliente `data-locked`, así que el 3er y 4to caso exigen romper un lock. Paró, entregó 2 y documentó el bloqueo en el HTML | E |
| 49 | Dos pedidos de la CEO son **imposibles dentro del sistema** y no hay dónde leerlo antes de intentarlo: "métricas interactivas" (las plantillas son HTML posicionado con salida a pptx) y "dark mode preferido" (`constraints.json` limita fondos a blanco, sage y `#133825` solo en apertura/cierre) | E |

### Lo que tuvo que asumir porque no está escrito

| # | Hueco | Tipo |
|---|---|---|
| 50 | Desde qué número arranca la numeración de páginas: el starter dice "correlativo en 2 dígitos desde la primera slide de contenido" y no dice desde cuál | E |
| 51 | El idioma. Nunca se dice quién es el destinatario; asumió inglés por `BRAND.md` | E |
| 52 | **Si la CEO cuenta como fuente aprobada.** `facts.json` dice "lo que no está acá NO existe" y a la vez "si falta un dato, pedíselo al usuario". La CEO *es* la fuente última, pero sus números llegaron de segunda mano y uno contradice un dato aprobado. No supo si dejar la slide marcada o bloquearla entera | E |
| 53 | Repurposó los slots `t5/t8/t11` de B1 (que son "Learn more ↗") como línea de prueba por pilar. Respeta `max_caracteres` y la regla de voz, pero cambió la intención del slot por decisión propia | E |

**Las dos veces que no supo cómo seguir** (son huecos de spec, no del material): la slide de 5 métricas
con una que contradice un dato aprobado, y el conflicto "hacé 4 casos" vs. "no toques los `data-locked`".

### El hallazgo que ordena G2

**El validador determinístico da 0 fallas y al mismo tiempo hay 7 contradicciones reales del spec.**
`validar.py` cruza estructura (¿resuelven los links, tienen límite los slots) y no **consistencia entre
reglas en prosa de distintos documentos**. La prueba a ciegas es el único instrumento que las encontró.

## G1 — Evidencia · prueba a ciegas A (solo la URL, sin material)

Declaró fuentes: solo `brand.magoya.com` + el checklist de GitHub. Ninguna memoria local.

| # | Hallazgo | Verificación mía | Tipo |
|---|---|---|---|
| 54 | **El límite de 3 niveles tipográficos es incumplible con las plantillas oficiales.** Conté los `font-size` distintos: **M1=4, A1=3, F2=5, L1=5, M3=7**. El chequeo #7 falla con 4+. O sea que 4 de 5 plantillas fallan el checklist oficial recién sacadas de la caja, y la regla 1 prohíbe corregirlo | confirmado, y peor de lo reportado | E |
| 55 | **El 75/25 no se puede sostener slide por slide**: la portada M1 es una foto tapada al 70% por un scrim verde profundo. `BRAND.md` dice que la proporción es obligatoria "en todo lo que se produce" y el checklist la audita "por pieza". Asumió que se mide sobre el deck completo — **es la asunción más grande del deck y no está dicha en ninguna parte** | razonamiento verificable | E |
| 56 | **Tres `cuando_usarlo` prometen control editorial que la geometría bloqueada niega.** A1: "la frase que carga el sentido va en lima" — A1 no tiene un solo elemento lima. B1: "el ícono en lima marca el modelo que estás proponiendo" — está hardcodeado en la card 2 y es `data-locked`. B3: "el destacado va en lima" — clavado en la celda *Data & AI*. Le costó rehacer una slide entera | coincide con el hallazgo 47, e independientemente | E |
| 57 | **El selector parchó un bug en vez de arreglarlo**: `index.json` dice que M3 tiene tres pasos, la plantilla tiene cuatro, y `selector.json` lo corrige explícitamente. Funciona, pero quien lea solo `index.json` se equivoca | confirmado (hallazgo 40) | E |
| 58 | **El chequeo #15 (espaciado base-4) es inauditable en slides**: la escala está en píxeles y las plantillas en `cqw`, sin factor de conversión documentado. El chequeo no se puede verificar sobre el formato al que más aplica. Lo declaró como no verificado en vez de decir que pasaba | correcto — el chequeo lo agregué yo sin resolver esto | E |
| 59 | **La numeración de página produce un deck donde la tercera slide dice "02"**: M1 y A1 no tienen slot de número, y la regla dice "correlativo desde la primera slide de contenido". No hay forma de saber la convención real desde la documentación | confirmado (hallazgo 50) | E |
| 60 | **El ejemplo de la plantilla oficial le enseña lo contrario al checklist**: el chip de M1 viene "Partnership proposal · 2026" en sentence case, y el chequeo #14 falla el chip en sentence case | confirmado (hallazgo 43, otra plantilla) | E |
| 61 | **L1 no puede cumplir su propia regla**: `assets.json` pide "tamaño óptico parejo" pero L1 usa 12 cajas idénticas con `object-fit:contain`, así que el tamaño depende del aspect ratio de cada SVG — Syngenta y Bunge dominan, Bayer Crop Science y GDM quedan chicos. Se ve en el render | reportado | E |
| 62 | **Hay slots dimensionados para un copy que la propia voz de marca prohíbe escribir**: las cards de F2 miden 28,2cqw con caption para 11 líneas, y `BRAND.md` pide oraciones cortas. Con voz Magoya real (3-4 líneas) queda un tercio de card vacío. Alargó a 4-5 líneas: "relleno con disfraz". Mismo problema en B3 | reportado | E |
| 63 | **El checklist tiene 16 filas pero se titula "Quince chequeos"**, y `constraints.json` (×1), `metodo.md` (×2) y `llms-full.txt` (×4) dicen "15 chequeos". Peor: **la fila 16 está separada por una línea vacía, o sea fuera de la tabla markdown** — no renderiza como fila. Es mi edición | confirmado | E |
| 64 | **"17 clientes" es el número de logos, no de clientes**: los pendientes de `BRAND.md` mencionan que faltan los vectoriales de ProducePay, HabiTerre e IntelinAir — tres clientes reales sin logo. La cifra aprobada probablemente subcuenta | confirmado en BRAND.md | E |
| 65 | El `cuando_usarlo` de L1 en `index.json` **está cortado a la mitad**: termina en "…o antes del cierre. Logos" | confirmado literal | E |
| 66 | **Publicar como Artifact rompe la pieza en silencio y no está documentado**: el CSP del artifact bloquea `brand.magoya.com`, así que un deck pegado tal cual sale sin foto de portada, sin wordmark y sin los 12 logos; y el artifact se publica sin `<head>` propio, así que se pierde el `meta charset` y el punto medio del chip sale mojibake. Propone un `ai/presets/claude-artifact.md` de dos líneas | reportado, mecanismo verosímil | E |
| 67 | El único lugar donde **no supo cómo seguir** fue el idioma: `BRAND.md` reparte español/inglés/portugués por tipo de uso, pero no dice en qué idioma va un deck comercial. Es la única decisión que tomó sin respaldo, y la que más cambia la pieza | E |

### Distinción crítica que salió del cruce entre las dos pruebas

| # | Hallazgo | Tipo |
|---|---|---|
| 68 | **Declarar el hueco no es lo mismo que negarse a entregarlo.** La prueba B marcó las 5 métricas de la CEO como no verificables **en su reporte** pero las dejó escritas en la slide; la prueba A, que leyó ese archivo por accidente, las detectó como cifras que `facts.json` prohíbe. O sea: la declaración fue precisa y la pieza igual salió con el dato. La métrica de éxito tiene que separar **detección** de **contención** | E | alta |

### Defecto de mi diseño de prueba (lo registro para el protocolo semanal)

Los dos agentes a ciegas trabajaron en `/Users/facu/Claude` y **uno sobreescribió el script del otro**.
No invalidó los resultados (A verificó que su deck salió intacto y declaró no haber adoptado nada), y
de hecho produjo el hallazgo 68 por accidente. Pero el protocolo tiene que darle a cada agente a
ciegas un directorio aislado (`isolation: worktree`). Va como cambio obligatorio a
`.ai/agente-validacion-ia.md`.

## G1 — Evidencia de campo · el primer uso real (Pato, 2026-08-19)

Vale más que las dos pruebas a ciegas juntas: es el **primer deck real que pasó por la capa** (negocio
había registrado en E10 que eran cero) y falló de una forma que **ninguno de nuestros instrumentos
detectaba**.

| # | Hallazgo | Tipo | Confianza |
|---|---|---|---|
| 69 | La IA produjo un deck **soso** y lo admitió al ser confrontada: *"the mix I chose leans on the text-heavy ones (white and sage canvases back to back), and the brand book has rhythm rules and more visual modules precisely to avoid that"*. O sea: **la regla existía y no estaba en el camino que la IA recorre** — la leyó recién cuando el usuario la empujó | E | alta |
| 70 | **La única regla de ritmo del sistema era "nunca dos slides seguidas del mismo módulo"** (bullet 3 de 4 en `reglas_de_seleccion`). Necesaria pero insuficiente: el deck la cumplía. Nada gobernaba el lienzo ni el peso visual, y nada lo medía | E | alta |
| 71 | **El catálogo sí tiene variedad, medida: 21 lienzos blancos, 14 sage, 3 verde-profundo, 3 foto; 19 módulos de peso visual contra 15 de texto.** El problema no era falta de módulos: era que el selector mapea contenido → módulo fila por fila y **nadie gobierna la secuencia** | E | alta |
| 72 | **Segunda falla, peor que la primera:** al señalarle que estaba soso, la IA agregó *"carátulas con más onda"* — "un desastre". Reachó por **decoración** en vez de cambiar de módulo. El sistema no tenía ninguna regla que dijera que la variedad sale del catálogo y no de decorar | E | alta |
| 73 | El costo real: el usuario **abandonó** y se fue a otro chat con otro modelo, en vez de iterar. Confirma la lectura de negocio de que el costo se paga en vueltas — pero acá la vuelta ni siquiera ocurrió | E | alta |
| 74 | Corriendo el chequeo nuevo sobre los dos decks de la auditoría: el de 9 slides **falla** (3 seguidas de peso texto, cierre G1→G2→M3 todo texto sobre blanco y sage) y el de 5 slides **pasa** (2 visuales, 3 lienzos). La medición coincide con el juicio humano en los dos casos | E | alta |
