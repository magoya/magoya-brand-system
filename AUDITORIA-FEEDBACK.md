# Auditoría de feedback — qué pediste, qué está hecho, cómo se valida

> Revisión profunda de **todo** tu feedback contra el estado real de los archivos, al 5 de agosto de 2026.
> Cada punto tiene evidencia verificable (archivo:línea o comando) y un criterio de aceptación que se puede chequear sin criterio subjetivo.
> Nada acá dice "listo" sin que lo haya medido. Si dice NO HECHO, es porque lo busqué y no está.

## Cómo leer los estados

| Estado | Significa |
|---|---|
| **LISTO** | Aplicado y verificado con evidencia en este documento |
| **PARCIAL** | Está el asset o la mitad del pedido, falta la aplicación o la ficha |
| **NO HECHO** | Lo busqué en los archivos y no existe |
| **BLOQUEADO** | Depende de un insumo que no está en disco |
| **CONTRADICE** | Choca con una decisión nueva del proceso con Proteína — hay que resolverlo antes de tocar código |

---

## Ronda de feedback · 22 de octubre de 2026 ("Brand System Online - Magoya")

Fuente: presentación de feedback del equipo (9 slides), más dos decisiones de Facu en chat: Recursos mantiene los logos de clientes y el membrete, y la firma de email se va.

| # | Feedback | Estado | Evidencia |
|---|---|---|---|
| 1 | La navegación cambiaba entera al entrar a "Elegir una plantilla" | **LISTO** | Una sola barra en las 11 páginas (`nav.css`, `nav.js`): Inicio · Conocer la marca · Recursos · Integrar con AI · IA en Campo |
| 2 | Piezas y plantillas: eliminar por completo; se descargan tipografía, elementos y paleta, no piezas editables | **LISTO** | Borradas `piezas.html`, `slides.html`, `plantillas.html`, `pieces.html`, `app/`, `ai/slides*`, `ai/templates/`, `ai/decks/`, `ai/selector.json` y `.mesa/` (la iniciativa de decks) |
| 3 | Lima ahora es de IA en Campo: en Magoya se potencia el Verde Magoya y el lima queda para acentos, detalles o CTA | **LISTO** | Sección Color de `brand-book.html`, `BRAND.md` §9, `tokens.json` `color.usage`. Se sacó la barra con porcentajes y la muestra del verde de ilustración en el inicio |
| 4 | Fotografía: sacar la foto que no es cenital; personas a color, sin detalle, mejor en espacios abiertos | **PARCIAL** | Fuera `field-corn.jpg` y todos los retratos B&N. Texto de fotografía literal del feedback. Falta: fotos a color del equipo (hoy solo la de Varu) |
| 5 | Eliminar ilustración y motivos hasta iconografía ("Ilustración no tenemos") | **LISTO** | Secciones Ilustración y Convivencia fuera del brand book; borrados `assets/illus/`, motivos y doodles del core |
| 6 | Reglas de oro: lima para acentos y CTA; personas a color; borrar "máximo dos recursos"; no subrayado, solo círculo o flechas | **LISTO** | Reglas de `brand-book.html` y `BRAND.md` §9. El brand book muestra el círculo como ejemplo de resaltado; círculo y flecha descargables en Recursos |
| 7 | Sacar el archienemigo 3 (decisión de Varu) | **LISTO** | `voz.html` y `.ai/verbal/voz.md`: once archienemigos |
| 8 | Cuando estén listos, sumar estilo de feed-placas y Deck | **BLOQUEADO** | Depende del material nuevo. Anotado en `ROADMAP.md`. Mientras tanto se sacaron las recetas y medidas de feed y story (`BRAND.md`, `constraints.json`, `tokens.json`, `ai.html`) |
| 9 | Sacar lo que no se usa para que no meta ruido en llamados externos | **LISTO** | Ninguna página, archivo para AI ni `llms*.txt` menciona lo eliminado. La revisión adversarial sumó: wordmark de bordado de merch (y el logo kit rehecho con 4 wordmarks), avatares recoloreados y trama, mockups de dispositivo, duplicados de la raíz, `VOICE-RESEARCH.md` y CSS sin uso. `python3 ai/validar.py`: 2 fallas previas a esta ronda (la pieza de IA en Campo con "con IA" y el wordmark animado con otro dibujo) |

**Pendientes de esta ronda:** proporciones nuevas de uso del color, fotos a color del equipo, y la pieza `assets/pieces/fecha-marcada-ig-portrait.svg` que todavía dice "con IA".

---

## 0. Lo que cambia el plan: el proceso con Proteína está en marcha

Busqué en las reuniones qué pasó con la voz "hasta hoy". No hubo un ajuste de copy: hay **un proceso de estrategia de marca en curso** que este sistema todavía no refleja. Fuente: notas de reunión del 17, 20, 22, 28 y 30 de julio y del 4 de agosto de 2026.

**Diagnóstico que acordaron con Proteína (Anita Figueiredo + Estrella):** nueve años de inconsistencia narrativa; Magoya se adaptó tanto al cliente que no construyó espacio propio.

**Calendario:**

| Fecha | Hito | Qué implica para este sistema |
|---|---|---|
| 28 jul 2026 | Kickoff | Ya pasó |
| **10 ago 2026** | Presentación preliminar de Proteína — **prework obligatorio** | Faltan **5 días**. Este brand system es parte del prework |
| **13 ago 2026** | Workshop principal, jornada completa, presencial, sin tecnología | Si falta alguien clave no se hace |
| 2 sep 2026 | Segundo workshop (9–17 h) | |
| post 13/8 | Módulo 1: posicionamiento, propuesta de valor, arquitectura de marca | **Puede reescribir la §1 de este manual** |
| post 2/9 | Módulo 2: **playbook consumible por IA** + vocabulario acordado. Diseño: Nat | **Es exactamente lo que estoy construyendo** — hay que decidir si converge o compite |

**Decisión ya tomada que me condiciona:** avanzar con el mood actual **sin rediseño profundo**, esperando que Proteína defina la dirección visual antes de invertir más. Y: *sin cambios estructurales de marca hasta tener el output del módulo 1*.

Esto reordena la prioridad: **hasta el 13 de agosto conviene cerrar huecos y consistencia, no abrir capítulos nuevos.**

### Tres contradicciones nuevas que hay que resolver antes de seguir

| # | La decisión de la reunión | Lo que dice hoy el sistema | Por qué importa |
|---|---|---|---|
| C1 | *"No se usarán logos, casos de éxito ni métricas de clientes como eje de comunicación (por ahora)"* | `BRAND.md` §1: *"ninguna afirmación de valor viaja sin cifra, nombre de cliente, plazo o captura"* · `logos.html` publica 17 logos de clientes · `slides.html` tiene familia G de casos de éxito y el módulo **"Proof, not promises"** | Es la regla de voz más fuerte que escribí y podría estar apuntando al lado contrario. Mi lectura: la decisión es sobre **el eje de comunicación en redes**, no sobre el material de venta uno-a-uno — pero no lo puedo decidir yo |
| C2 | *"'Problem solver' en inglés para EE.UU. está definido. Para Argentina falta bajar voz, tono y lenguaje local — no es traducción literal"* · *"multipaís no es localización, es de raíz"* | El manual tiene **una** voz con una regla de idioma (§1). No tiene voz por territorio | Falta un capítulo: **voz por mercado**, con AR y US partiendo de lugares distintos |
| C3 | *"AI no es el claim principal, pero tiene que aparecer"* | `ai-en-campo.html` es una marca anexa completa y hay familia K de capacidades IA en slides | Hay que fijar el techo: cuánta IA antes de que se lea como claim principal |

### Un dato que corrige mi propia investigación

En `VOICE-RESEARCH.md` inferí que **Proteína era la agencia del rebranding 2022**. Las reuniones muestran que Proteína arrancó el **28 de julio de 2026**. La atribución del `Manual de Marca` 2022 queda **sin fuente** — y **Nat es la diseñadora original de Magoya**, que ahora hace el diseño del playbook. Corregido en el documento.

---

## 1. Navegación y entrada al sistema

| ID | Pedido | Estado | Evidencia / qué hice |
|---|---|---|---|
| F01 | *"no veo el mood"* — la portada moodboard | **LISTO hoy** | Estaba **huérfana**: `grep -l intro.html *.html` devolvía solo intro.html. Ninguna página la linkeaba, por eso no existía para vos. Ahora el moodboard **es la raíz** (`index.html`) y el brand book pasó a `brand-book.html`; "Inicio" es el primer ítem del topbar en las 8 páginas internas |
| F02 | *"si estoy en la home no debería poder hacer click en el logo para volver a la home"* | **LISTO hoy** | En la home el logo es `<span class="brandmark">`, no `<a>`. En las otras 8 el logo lleva a `index.html` |
| F03 | *"y lo pondría más grande, debería estar más destacado"* (el logo) | **LISTO hoy** | `.mg-topbar img` de 28px → **34px** en las 9 páginas |
| F04 | *"la sección piezas le cambiaría el nombre… y logos tampoco es auto-explicativa"* | **LISTO** | Topbar dice **"Comerciales"** y **"Clientes"**, no "Piezas" ni "Logos" |
| F05 | *"todo lo que es para descargar te saca de la navegación"* | **LISTO** | Panel de descarga contextual, sin salto de página |
| F06 | *"la animación de popup solo si se cambia de sección, y si esa sección no tiene nada tiene que desaparecer"* | **LISTO** | Scroll-spy por posición (IntersectionObserver fallaba con anclas cortas); verificado: Convivencia y Componentes muestran el panel oculto |
| F07 | *"el menú de Aladino… si entro al espacio verde disminuye el tamaño de la sección actual"* | **LISTO** | `:has(a:hover) a.act:not(:hover)` en vez de `:hover` del contenedor, en las 9 páginas |
| F08 | *"las animaciones se traban y parecen poco fluidas"* | **LISTO** | `transform:scale()` (compositor) en vez de `font-size`, y scroll-spy con `requestAnimationFrame` que no toca el DOM si no cambió |
| F09 | *"la flechita de IA en campo ponela del lado derecho, que sea toda el área clickeable"* | **LISTO** | `.side a.anx` con `display:flex;justify-content:space-between`; medido en el navegador: la flecha queda a 8px del borde derecho del `<a>`, que ya ocupa el ancho completo del dock (heredado del flex del sidebar) |

## 2. Ilustración, motivos y marcas a mano

| ID | Pedido | Estado | Evidencia / qué falta |
|---|---|---|---|
| F10 | *"las que tienen caminos están mal cortadas"* / *"los motivos está bien que estén al corte pero nunca que se vean cortados"* | **LISTO** | Regla de sangrado documentada (`BRAND.md` §6); motivos de líneas retirados |
| F11 | *"en motivos las líneas no son algo que caracteriza la marca"* | **LISTO** | `motif-estratos.svg` y `camino-*.svg` retirados de la doctrina, sin ficha |
| F12 | *"esto no lo quiero como motivo"* (banda festoneada) | **LISTO** | Asset borrado; único motivo = paño de semicírculos |
| F13 | *"les faltan las zapatillas"* | **LISTO** (corregido en segunda pasada) | La primera pasada solo resolvió `char-jumping` y `char-laptop`, y descartó mal los otros dos: en `char-experts-talking` los pantalones del personaje derecho terminaban 45px ANTES del borde del artboard (muñones flotantes, no recorte válido) — se le agregaron 4 zapatillas verdes reales (verde digital + suela #161616 + cordones blancos) asomando bajo los ruedos, con el viewBox extendido de 574 a 606 de alto; y en `char-chart-duo` los dos zapatos del personaje izquierdo eran NEGROS (contra la regla "zapatillas verdes") — recoloreados a verde digital con suela y cordones agregados siguiendo el ángulo real de cada pie (11° el del piso, 34° el del banquito) |
| F14 | *"la sección de marcas a mano: el título es malo, y cómo están aplicadas también; no cubre toda la palabra, no repetán lo que dicen, y el stroke parece que da vergüenza — quiero una marca fuerte de principio a fin"* | **LISTO** | Resuelto de raíz: en vez de seguir parchando el subrayado débil, se retiró (ver F15) — ya no hay una versión débil que mostrar |
| F15 | *"el subrayado quedó fuera"* (implícito en F14: solo círculo y flecha) | **LISTO** | `grep -rn flourish-underline *.html` → cero coincidencias (el asset y sus 4 usos migrados: `brand-book.html` sacó la tarjeta, `slides.html` A1/J2 pasan la frase a lima con `<em>`, `library.html` sacó la ficha). Doctrina actualizada en `BRAND.md`, `README.md`, `ROADMAP.md`, `tokens.json` |
| F16 | *"un patito en motivos semicirculares está deformado"* | **LISTO** | Era `preserveAspectRatio="none"`; el asset se retiró después |
| F17 | *"la regla es cubrir los espacios, no que quede algo chiquito como detalle; si hay algo es para que se vea"* | **LISTO** | Regla "ocupar el espacio" en `BRAND.md` §6 con números (gráfico = ancho de columna, cifra ~70%, personaje 40–55%, paño al corte); gráficos de slides agrandados (`.bars` 26cqw → 42cqw, `.donut` 20 → 34cqw) |
| F18 | *"rehacer las piezas de convivencia — los fondos son raros y la persona, los chips no están bien"* + *"no sé qué significa área mosaico"* | **LISTO** | El motivo pasó de `<img object-fit:cover>` (una sola instancia recortada, se veía sparse/rota) a `background-repeat` en tile continuo — verificado visualmente en los dos ejemplos. El retítulo ya había pasado a "Cards — siempre en mosaico" en una ronda anterior. La persona (task previa) y los chips (pill + tags) ya estaban bien |

## 3. Iconografía

| ID | Pedido | Estado | Evidencia |
|---|---|---|---|
| F19 | *"quiero tener suficientes para poder hablar de cualquier tema, incluso redes sociales, AI o plataformas"* | **LISTO** | 58 íconos línea redondeada |
| F20 | *"si lo pego me pega un código, me gustaría que sea el ícono en PNG"* | **LISTO** | `toPngBlob()` + `ClipboardItem`; pega como imagen |
| F21 | *"que se puedan descargar todos, algunos o uno"* | **LISTO** | Descarga individual + ⌘-click múltiple con barra de selección |
| F22 | *"mostrá cómo se aplica en cada sección — slide, piezas, ícono — pensá en la persona que viene de la nada"* | **LISTO** | 3 ejemplos por contexto de uso, distintos de la home |
| F23 | *"hay ejemplos de íconos grandes que me gustaron mucho en los slides — llevá más referencias de ahí al brand"* | **LISTO** | 3 ejemplos reales agregados al capítulo de iconografía, cada uno con link al módulo de origen: ícono protagonista de statement (slides A5), ícono en badge circular (slides B3), ícono líder de fila en capacidades de IA (slides K2). De paso, encontrado y corregido un bug real: la clase nueva `.icm.hero` colisionaba con `.hero` (el header de la página, `min-height:88vh`) e inflaba el ícono a 335px de alto — renombrada a `.icm.xl` |

## 4. Logos, descargas y aplicación web

| ID | Pedido | Estado | Evidencia |
|---|---|---|---|
| F24 | *"los logos de IA + los de redes deberían poder descargarse en PNG o SVG, a color o negro, con contenedor o solo el isologo"* | **LISTO** | Los logos de IA y redes viven en `ai-en-campo.html` (no en `logos.html`, que es para clientes/partners). Cada uno tiene 4 variantes reales: SVG color, SVG negro, PNG con contenedor, PNG negro con contenedor — generadas client-side, sin pre-generar 92 archivos. De paso se corrigieron 4 colores mal atribuidos (Meta, Ollama, OpenAI, Perplexity) verificados contra fuentes independientes |
| F25 | *"deberíamos tener cómo se aplica en web, el favicon y demás"* | **LISTO** | `assets/favicon/` tiene los 4 PNG + SVG generados desde el avatar "m" (rasterizado con QuickLook, sin instalar librerías). Las 9 páginas cargan los 4 `<link>` (icon SVG, PNG 32, PNG 16, apple-touch-icon 180) — verificado por página. Ficha completa con las 5 descargas en `library.html` |
| F26 | *"las fotos se debería poder bajar una"* | **LISTO** | 6 fotos con descarga individual en `library.html` |
| F27 | *"los textos no son referenciales"* (descargas) | **LISTO** | Auditadas las fichas de `library.html`, `brand-book.html` y `logos.html` contra `ls -la` real. La mayoría ya coincidía; se corrigieron 3 bugs reales: `varu-ceo-bw.jpg` decía PNG·55KB·290×290 (es JPG·15KB·400×400), 4 SVG mostraban "0 KB" en vez de precisión sub-KB, y 2 menciones a "loop" quedaron obsoletas tras sacarle el loop a la firma animada |
| F28 | *"el hacer y evitar en la foto parece que corresponde a las fotos de arriba"* | **LISTO** | Reordenado |
| F29 | *"el hacer y evitar lo dejaría en algún contenedor que lo separe más, pero que se note que es contexto"* | **LISTO** | Bloque `.dodont` universal agregado en `slides.html` (antes de la familia A) y en `pieces.html` (antes de los tabs) — `grep -c dodont slides.html pieces.html` = 3 en ambos |

## 5. Firma, papelería y merch

| ID | Pedido | Estado | Evidencia |
|---|---|---|---|
| F30 | *"no va la carita, siempre el logo"* (firma) | **LISTO** | Firma = wordmark |
| F31 | *"la firma quiero que sea el logo animado — animalo y ponelo descargable, y también el header del doc, el footer, la firma estática"* | **LISTO** | GIF 200×70 / 26 frames + PNG + `doc-header.svg` + `doc-footer.svg` + instructivo de Gmail |
| F32 | *"mostrar si lo tiene que aplicar en un Excel u otro documento"* | **LISTO** | Membrete A4 + pie con avatar "m" (uso permitido de papelería) |
| F33 | *"le falta lo de LinkedIn — IA en campo, qué puede aportar a la firma más datos"* | **LISTO** | Firma de email suma ícono de LinkedIn (16px, linkeado al perfil) y link a IA en campo bajo el contacto — instructivo de Gmail actualizado con el paso para sumarlos |
| F34 | *"la referencia real — Buzo Propuesta 1 no es una referencia para llevar al frente; primero va el catálogo de merch con aplicación"* | **LISTO** (foto real, F35 sigue pendiente) | Catálogo de 10 productos ahora abre la sección; el buzo pasó a "Especificación de producción" después, retitulado para no leerse como la pieza a mostrar primero |
| F35 | *"las fotos no son reales; si querés poné 'a modo ilustrativo', pero tomá todas las que te pasé, recortalas y ponelas bien"* | **BLOQUEADO** | `assets/photos/merch/` tiene **solo `LEEME.txt`**. Busqué en Desktop, Downloads y Claude por remera/gorra/mochila/vaso/medias/cuaderno/sticker/hoodie: no están en disco. Las veo en el chat, no las puedo extraer de una imagen pegada — necesito los archivos |
| F36 | *"aplicación en branding: remeras, buzos, gorra, vaso térmico, cuaderno, lapiceras"* | **PARCIAL** | Especificación de los 9 productos escrita; falta la foto de cada uno (F35) |

## 6. Slides y piezas comerciales

| ID | Pedido | Estado | Evidencia |
|---|---|---|---|
| F37 | *"le falta más componentes, más template: una tabla, un gráfico, una foto y texto, una ilustración de persona y un texto al palo"* | **LISTO** | 41 módulos en 13 familias |
| F38 | *"esto debería poder abrirte en Google Slides con el template full y que selecciones cuáles querés"* | **LISTO** | Exportador `.pptx` real con selección por checkbox (PptxGenJS, gráficos y tablas nativas) |
| F39 | *"la bajada del 95% casi tocando los números"* | **LISTO** | `.stat-d` margin-top .5cqw → **1.5cqw** |
| F40 | *"el 10 5+ parece una escalera, no están alineados"* | **LISTO** | `.big3` con `align-items:end` + columnas flex justificadas al fondo |
| F41 | *"los gráficos no cubren"* | **LISTO** | Ver F17 |
| F42 | *"en las piezas me gusta cómo lo armaste pero tienen modelo distinto cada una — lo haría más notorio"* | **LISTO** | Grid comparativo de 3 modelos + badge por modelo |
| F43 | *"el T2 y T3 no dicen nadaaaaaaaa, y prefiero que estén en solapas y no uno debajo del otro"* | **LISTO** | Solapas (`.tab`/`.tpanel`) + contenido real en las 3 |
| F44 | *"el one pager está ok"* | **LISTO** | Sin cambios |

## 7. Reglas transversales

| ID | Pedido | Estado | Evidencia |
|---|---|---|---|
| F45 | *"nunca pongas emoji en los títulos; solo manitos para señalar o banderas de países"* | **LISTO** | `grep -nP '[emoji]' *.md` en títulos → cero coincidencias. Los 5 casos violados (`ROADMAP.md`, `PLAN.md`, `VOICE-RESEARCH.md`) están corregidos |
| F46 | *"quedaron textos centrados y títulos a la derecha — sé consistente"* | **LISTO** | Contenedor `.inner` único anclado a la izquierda; verificado un solo left (294px) en 13 secciones |
| F47 | *"grand full responsive"* | **LISTO** | Breakpoint 880px en las 9 páginas |
| F48 | *"si creas algo nuevo que puede ir, tiene que estar en el brand"* (regla madre) | **LISTO como regla, PARCIAL en cumplimiento** | Escrita en `README.md` y `BRAND.md`. Pero F24, F25 y F13 son casos abiertos: hay especificación sin asset, o asset sin aplicación |
| F49 | *"el cómo aplicamos el contenido es cómo la gente lo puede llegar a usar — muchos son literales con los criterios; este brand tiene que educar, enseñar y compartir desde el mismo brand"* | **LISTO** | Criterio transversal en el `ROADMAP.md` con tabla de 4 capas por sección. Los dos huecos pedagógicos concretos que se habían identificado (F29: slides y comerciales sin Hacer/Evitar · F23: íconos sin ejemplo a escala) ya están cerrados — es un criterio transversal, así que vale seguir vigilándolo en piezas nuevas |
| F50 | *"validá que integrar con IA sea algo que las IA hoy estén usando — no se inventa, se tiene que validar"* | **LISTO** | Convenciones verificadas contra documentación vigente: `llms.txt`, `CLAUDE.md` + `.claude/rules/`, knowledge de Custom GPT, `.cursor/rules/*.mdc` (renombrado al formato vigente), `.github/copilot-instructions.md` |
| F51 | *"revisá si algo nos falta del brand que no consideramos y deberíamos, algo esencial que no supimos"* | **PARCIAL** | `VOICE-RESEARCH.md` §6 lista 8 ausencias. Falta el hallazgo mayor: **no hay capítulo de voz por mercado** (C2) y **no hay arquitectura de marca** — que es justamente un entregable del módulo 1 de Proteína |

---

## Roadmap de ejecución

Ordenado por la fecha real que manda: **10 de agosto**, prework de Proteína.

### Ola 1 — antes del 10 de agosto: que el sistema cumpla sus propias reglas

**Completa — los 12 puntos cerrados.** Todo acá era cerrar huecos, no abrir capítulos. Ninguno dependía de Proteína.

Nota sobre el punto 2: el criterio original pedía agrandar el óvalo del subrayado; la resolución real fue retirarlo del sistema (decisión F15, "el subrayado quedó fuera"), que es la que efectivamente cierra F14 sin dejar una versión débil que seguir parchando.

| # | Tarea | Criterio de aceptación verificable |
|---|---|---|
| 1 | **F45** Sacar emojis de títulos en mis 3 archivos | `grep -n "^#.*[emoji]" *.md` devuelve vacío |
| 2 | **F14 + F15** Cerrar marcas a mano: solo círculo y flecha, stroke que cubre la palabra completa, título nuevo, subrayado fuera y sus 4 usos migrados | `grep -c flourish-underline *.html` = 0 · el óvalo mide ≥100% del ancho de la palabra medido en el navegador · la columna Evitar dice que el subrayado salió del sistema |
| 3 | **F25** Favicon real en las 9 páginas + set 16/32/180/512 + ejemplo de aplicación web | `grep -c 'rel="icon"' *.html` = 9 · los 4 PNG existen en `assets/favicon/` con ficha en `library.html` |
| 4 | **F24** Logos de IA y redes descargables: PNG/SVG × color/negro × con contenedor/isologo | Cada logo ofrece 4 variantes reales · los archivos existen · ficha en la librería |
| 5 | **F29** Hacer/Evitar en `slides.html` y `pieces.html` | `grep -c dodont slides.html pieces.html` > 0 en ambos |
| 6 | **F23** Íconos a escala grande: llevar al capítulo de iconografía las aplicaciones que funcionan en slides | El capítulo muestra ≥3 usos a escala grande con link al módulo de origen |
| 7 | **F09** Flecha de IA en campo a la derecha, área completa clickeable | El `<a>` mide el ancho del dock y la flecha queda pegada al borde derecho, medido en el navegador |
| 8 | **F34** Catálogo de merch primero, render del buzo después como especificación | El catálogo aparece antes en el orden del DOM |
| 9 | **F27** Textos de descarga con formato, peso y dimensiones reales | Ningún texto de ficha es genérico; los pesos coinciden con `ls -la` |
| 10 | **F13** Dibujar el calzado en los 4 personajes | Los 4 SVG tienen calzado visible, no solo `viewBox` corregido |
| 11 | **F18** Rehacer las piezas de convivencia y retitular "área mosaico" | Fondos y chips consistentes con los tokens · el título dice qué es sin necesidad de explicación |
| 12 | **F33** LinkedIn y IA en campo en la firma | La firma incluye el ícono y la línea, con instructivo actualizado |

### Ola 2 — 10 al 13 de agosto: llevar el sistema al workshop

| # | Tarea | Criterio |
|---|---|---|
| 13 | **C1** Resolver con Varu si "no logos ni métricas ni casos" aplica al material de venta o solo al eje de redes | La regla de §1 queda confirmada o reescrita, con la fuente citada |
| 14 | **C3** Fijar el techo de IA en el discurso | Regla escrita: cuánta IA antes de leerse como claim principal |
| 15 | Preparar el sistema como prework: qué preguntas del workshop ya tienen respuesta acá y cuáles no | Una hoja de 1 página que Proteína pueda leer antes del 13 |

### Ola 3 — post módulo 1 (después del 13 de agosto)

| # | Tarea | Criterio |
|---|---|---|
| 16 | **C2 / F51** Capítulo de voz por mercado: AR y US desde lugares distintos, no traducción | Cada mercado tiene ejemplos propios de copy, no versiones traducidas |
| 17 | Arquitectura de marca (core, IA en campo, y lo que defina Proteína) | Diagrama + regla de cuándo usar cada marca |
| 18 | Converger con el playbook del módulo 2 en vez de duplicarlo | Decisión explícita: este repo es la capa técnica del playbook, o se fusiona |
| 19 | **F35** Catálogo de merch con las fotos reales | 9 productos con foto, recortadas, con "a modo ilustrativo" |

---

## Revisión de Luca Cantarelli (5 de agosto de 2026)

Feedback de una llamada mostrándole el sistema en vivo. Separado en dos partes desde el principio: lo que es de este repo, y lo que es de la app de Magoya Studio (esa parte no se toca acá — queda para el otro proyecto).

### Aplicado en este repo

| # | Lo que vio Luca | Causa real (verificada, no a ojo) | Fix |
|---|---|---|---|
| L1 | En IA en campo, una flecha "pisa" la palabra "vende" — en su resolución nada más | Medido en el navegador a 1280px: la flecha (52px) empezaba 52px arriba de las cifras, pero el margen debajo del párrafo era de solo 30px — 22px de la flecha caían dentro del texto | Flecha reducida a 26px, margen del párrafo a 36px. Verificado sin superposición en 1100/1280/1440px — ya no depende del ancho de pantalla |
| L2 | El índice lateral (dock): al hacer hover, el texto se corta — "Ilustración & motivos" queda en "Ilustración & motivo" | `.side{overflow-y:auto}` sin `overflow-x` declarado — el spec de CSS fuerza `overflow-x` a `auto` también cuando solo se fija un eje, así que el texto agrandado por el hover se recortaba en el borde del dock en vez de desbordar visible | `overflow-x:visible` explícito en las 8 páginas que comparten el dock. Reproducido el bug, aplicado el fix, confirmado que ya no corta |
| L3 | Tipografía "de card generada por IA" en Clientes — pensó que era output crudo sin estilo | Era un zócalo técnico intencional (mono + tag SVG) pero sin separación visual del resto de la card, por eso se leía como un accidente | Hairline + padding-top separando el zócalo del cuerpo de la card en `logos.html` |
| L4 | Nombres de sección inconsistentes entre el dock, el título y el panel de descarga (ej. "Identidad" vs "Logo & avatares"; "Fotografía" vs "Banco de fotos") | El kicker de la sección de logo decía "Identidad" mientras el dock y el H2 ya decían "Logo & avatares" — desalineado dentro de la misma sección. Y el panel de descarga siempre nombra el *producto* (correcto), pero nunca decía de qué *sección* venía | Kicker corregido. El panel de descarga ahora muestra el nombre real de la sección (tomado del propio dock) además del producto — ej. "Fotografía · descarga" arriba de "Banco de fotos" |
| L5 | En la portada, "la pieza canónica" y otros títulos se leen poco contra el fondo de la card al hacer hover | El degradé del hover (`rgba(13,12,12,.82)` solo en el 18% final) dejaba el título en una zona casi transparente del degradé | Degradé reforzado (42% de opacidad ya al 30% de la altura) + text-shadow en título y subtítulo — funciona sobre cualquier color de card, no solo fotos |
| L6 | Una card de "IA en campo" se leía como si fuera una pieza genérica de redes de Magoya — la sub-marca no se notaba hasta pasar el mouse | El único indicador era el `.lb` que solo aparece en hover — en reposo la card no decía nada | Badge "IA en campo" visible siempre, no solo al hover |

### Verificado y descartado (busqué el problema, no está)

- **Botones ≠ chips mezclados**: revisé la sección "Componentes" de `brand-book.html`, que es literalmente la página sobre esta regla. `.btn` usa `border-radius:var(--radius-btn)` (10px, rectángulo) y `.pill` usa `border-radius:var(--radius-full)` (pill completo) — están bien diferenciados. Si Luca lo vio en otro lado (algún mockup con estilo inline), falta que señale la card exacta.

### Documentado para más adelante (real, pero grande para tocar en esta pasada)

- **Escala tipográfica con decimales fuera de múltiplos de 4** (Luca marcó 13.5px como ejemplo): confirmado — hay 5 instancias de 13.5px y decenas más de 9.5/10.5/11.5/12.5/14.5px, repartidas en las 9 páginas. No es un accidente: es una micro-escala deliberada y usada consistentemente para captions/kickers/specs desde el arranque del sistema. Normalizarla a múltiplos de 4 (o a un mínimo de 14px como sugiere Luca) es un cambio real de escala tipográfica que tocaría cientos de instancias — no algo para hacer a ciegas en una pasada. Queda anotado para una revisión dedicada.
- **Rediseño del dock con lógica tipo Notion** (rieles minimalistas que se expanden en hover, con la sección activa siempre en texto y el resto como barritas — la sugerencia concreta de Luca): buena idea, pero es un cambio de interacción completo, no un fix. Se banca hasta una pasada dedicada a navegación.

### Excluido — es feedback de Magoya Studio, no de este repo

Todo esto lo vio en el editor de piezas (canvas, capas, zoom), no en el brand system. Facundo ya lo separó explícitamente: va al otro proyecto, no acá.

- Etiqueta "Detrás" mal traducida (debería ser "Fondo"/"Encima"/"Contenido") — bug de la traducción automática del editor
- Ícono de "Marca" que se confunde con el de Gmail — icono del editor
- Doble barra de navegación horizontal + botón "Volver al inicio" redundante — UI del editor
- Zoom con Ctrl/Cmd+rueda y paneo con clic-rueda — controles del canvas
- Área fuera del artboard para tirar elementos sueltos — feature del canvas
- Mockups de dispositivo de mala calidad — Luca ofreció pasar mejores SVG de la comunidad de Figma; cuando lleguen, revisar si además reemplazan a los que usa este repo en `assets/studio/devices/`

## Revisión de UX / Arquitectura de la Información (7 de agosto de 2026)

Feedback en PDF (`Feedback sobre Magoya Brand System.pdf`, exportado de Notion), revisando el sitio completo con mirada de UX/IA — no bugs puntuales, sino cómo está organizada y presentada la información. El mapeo completo está abajo; el bloque que se ejecutó primero está en "Aplicado en este repo".

| # | Cita | Qué implica | Tamaño |
|---|---|---|---|
| F52 | *"Veo cosas como Iconos, Assets, Slides, Clientes que podrían ser entendidos como elementos del brandbook"* | Repensar la nav superior de las 9 páginas: hoy Iconos/Assets/Slides/Comerciales/Clientes viven como items hermanos de "Brand book" en el top nav, cuando conceptualmente son *partes* del sistema de marca, no páginas paralelas. Implica decidir una jerarquía (¿todo cuelga de "Brand book" con un mega-menú? ¿se renombra la nav para que se lea como capítulos, no como secciones sueltas?) y aplicarla en las 9 páginas | Grande — decisión de IA que toca la nav de todo el sitio |
| F53 | *"Si revisamos la IA podemos también revisar las interacciones que proponemos para navegar. Mantengamos consistencia con los elementos de navegación"* | Consecuencia directa de F52: si se reordena la jerarquía, los patrones de interacción (dock lateral, breadcrumbs, hover states) tienen que quedar consistentes en las 9 páginas a la vez — no se puede resolver la IA sin tocar también cómo se navega | Grande — depende de F52, mismo esfuerzo |
| F54 | *"A simple vista no sé cuál es la diferencia entre IA en campo y Integrar con IA. No sé cuál necesito ver ni por qué"* | Los nombres compiten (ambos dicen "IA") pero son cosas distintas: **IA en campo** = marca anexa de contenido para redes (dirigido a productores agro); **Integrar con IA** = documentación técnica para cargar la marca en Claude/Cursor/GPT (dirigido a quien produce piezas). Implica: o renombrar uno de los dos para que la diferencia sea obvia sin necesidad de entrar, o agrupar visualmente ambos bajo un mismo namespace con sub-etiquetas claras | Mediano — principalmente naming + un ajuste de nav, no una reestructura completa |
| F55 | *"Viendo IA en campo lo que veo es una recarga de elementos... los labels de Sub-marca de magoya y Webinars en vivo arriba del título... las flechas o formas de relleno"* | Concreto y ubicado: el hero de `ai-en-campo.html` (línea ~199-201) tiene dos badges ("Sub-marca de Magoya" + "Webinars en vivo" con ícono doodle) arriba del `<h1>` que no aportan a la historia — son ruido antes de llegar al mensaje. Implica sacar o fusionar esos badges, y revisar el resto de la página buscando decoración que no cuenta nada | Chico — localizado, se puede resolver en una pasada |
| F56 | *"En vez de tener todos los elementos se puede armar un mosaico con categorías. Similar a como lo hace Atlassian (Color, Tipografía, AI patterns… los pilares del brand)"* | Redefine el propósito de `index.html`: hoy es una vidriera con ~19 celdas mostrando piezas sueltas; la sugerencia es agrupar por *pilar* (Color, Tipografía, Iconografía, IA...) en vez de por pieza individual — cambia la grilla y probablemente el copy de cada celda. Esto es exactamente el tipo de cambio que ya estaba anotado en el roadmap (tarea "Rediseñar index.html como vidriera real") — esta cita le da una dirección concreta | Grande — rediseño de la portada, no un ajuste |
| F57 | *"Los do's and don'ts podrían ser más claros y simples a nivel visual... tenemos do's and don'ts inconsistentes en la misma página (El lockup de IA en campo vs Cómo se cuenta la historia)"* | Verificado el segundo punto: en `ai-en-campo.html`, la sección "El lockup de IA en campo" (línea 272) y "Cómo se cuenta la historia" (línea 345) usan el mismo componente `.dodont`/`.dd` pero con tratamientos visuales distintos entre sí — hay que unificarlos al patrón único que ya usa el resto del sistema (brand-book.html, slides.html, pieces.html). Lo de "más simple a nivel visual, estilo Atlassian" es una pregunta de diseño más abierta: ¿iconos en vez de solo texto? ¿color de fondo en vez de solo borde? | La inconsistencia puntual es chica; el rediseño visual del componente es mediano |
| F58 | *"En IA en campo tengo plantillas y recursos que puedo empezar a aplicar desde el momento 0, pero los tengo bastante abajo en el scroll... las cifras que presentamos en el hero pueden ser clickeables tipo anchors"* | Dos cosas: (1) revisar el orden de las secciones de `ai-en-campo.html` — si "Plantillas" es lo más accionable, quizás no debería estar después de Esencia/Color/Logo/Ruido; (2) las 3 cifras del hero (`13 formatos`, `8 plantillas`, `10 reglas`) hoy son texto plano — convertirlas en anchors que salten a `#formatos`, `#plantillas`, `#reglas` es chico y de alto impacto | El anchor de las cifras es chico; reordenar secciones es mediano (hay que revisar qué depende de qué) |
| F59 | *"A nivel UI: todo muy pegoteado, sobrecarga de elementos y poco aire"* | Feedback general, no localizado a una página. Coincide con el patrón ya visto hoy mismo en la trama del paño y en el espaciado de Hacer/Evitar — probablemente hay más instancias de margin/padding chicos repartidas por el sistema. Implica una pasada de auditoría de espaciado, no un fix puntual | Grande si se hace exhaustivo; se puede acotar a los peores casos si se prioriza |
| F60 | *"Integrar con IA es re poderoso para lo que queremos hacer internamente... ¿no podría ser parte de la propuesta de la home?"* | Sugiere agregar una celda/sección en `index.html` que promocione "Integrar con IA" como un pilar de valor, no solo como un ítem de nav más. Depende de la dirección que se tome en F56 (el rediseño de la home) | Mediano, y conviene resolverlo junto con F56, no antes |
| F61 | *"Una versión TLDR? Una table of contents con casos de uso que te permitan navegar derecho a lo que tenés que hacer?"* | Propuesta nueva, no un fix: agregar una capa de navegación por *caso de uso* ("quiero hacer un post de LinkedIn" → salta directo a la receta) en vez de solo por *capítulo*. Es un patrón que no existe hoy en ninguna página. Necesita definir primero cuáles son los casos de uso reales antes de construir la navegación | Grande — es una funcionalidad nueva, no una corrección |

### Cómo lo leo yo (para discutir, no para ejecutar todavía)

- **F55 y el anchor de F58** son los únicos dos puntos genuinamente chicos y sin decisiones abiertas — se podrían resolver en una pasada corta sin pedir nada más.
- **F52/F53/F54** son la misma decisión de fondo (jerarquía de navegación) mirada desde tres ángulos. Conviene resolverlos juntos, una sola vez, no de a uno.
- **F56/F60** son la misma pieza (rediseño de `index.html`) — ya estaba en el roadmap como tarea pendiente, esto le suma dirección concreta (mosaico por pilares, estilo Atlassian) y un contenido nuevo a incluir (Integrar con IA como propuesta de valor).
- **F57** tiene una parte chica y verificable (la inconsistencia puntual entre dos secciones) y una parte abierta (si el componente completo necesita un rediseño visual tipo Atlassian).
- **F59 y F61** son los más grandes y menos definidos — auditoría de espaciado de todo el sistema, y una funcionalidad de navegación por caso de uso que no existe en ningún lado todavía.

### Aplicado en este repo

El usuario priorizó F52/F53 (jerarquía de nav), F56/F60 (mosaico por pilares) y F61 (navegación por caso de uso) como el primer bloque a ejecutar. F54 quedó resuelto como efecto colateral de la misma decisión de nav (se agrupó "IA en campo" e "Integrar con IA" en zonas visualmente distintas). F55, F57, F58 y F59 quedan documentados arriba, sin tocar.

| # | Qué se decidió | Dónde |
|---|---|---|
| F52/F53 | Nav superior agrupada por proximidad (Manual: Brand book + IA en campo · Plantillas: Slides + Comerciales · Recursos: Iconos + Assets + Clientes), sin renombrar nada y sin mega-menú — la jerarquía se lee por espaciado creciente entre clusters, no por texto nuevo | `.mg-topbar` en las 9 páginas (`index.html`, `brand-book.html`, `ai-en-campo.html`, `slides.html`, `pieces.html`, `icons.html`, `library.html`, `logos.html`, `ai.html`) |
| F54 | "Integrar con IA" separado del resto por el único divisor duro de la barra (hairline vertical) — resuelve la confusión con "IA en campo" por contenedor visual, no por renombre | Mismo bloque de nav, las 9 páginas |
| F56/F60 | Primera pasada: `index.html` pasó de 19 cards sueltas a un grid de 10 pilares. **Revisado después con referencia explícita a atlassian.design**: cada card ahora muestra un fragmento REAL de la marca en uso (igual que Atlassian muestra un gráfico real de Jira en su card de "Color", no un swatch suelto) en vez de una muestra abstracta. "Fotografía & ilustración" se separó en dos cards — la propia matriz de convivencia de `brand-book.html#convivencia` dice que foto + ilustración *nunca conviven*, así que fusionarlas en una card violaba la regla del propio manual. "Integrar con IA" volvió a ser pilar propio (12º) — Atlassian trata "AI Patterns" como pilar de primera clase, no como link de nav escondido. **Tercera pasada** (feedback directo sobre esta misma vidriera): se restauró la paleta Pantone visible en la card de Color (se había perdido al priorizar solo componentes en uso); la card de Ilustración & motivo se rehizo con más contraste (fondo verde profundo, headline grande, personaje más grande) porque se leía plana; la card de Identidad (email/firma) se movió al final del grid porque abrir la vidriera con un mockup de mail no funcionaba como primera impresión; y el `.board` dejó de ser un grid uniforme de 4:5 para ser un bento real — tamaños mixtos (grandes, angostas verticales, anchas horizontales) con `grid-auto-flow:dense` para que no queden huecos, tal como se ve en atlassian.design. **Cuarta pasada** (un agente por card + segundo filtro): header estandarizado en las 12 cards — ícono de línea nuevo (mismo estilo del set real: 24x24, stroke 1.75) + título siempre visible en peso extra, sin numeración; en cards con foto full-bleed el header va superpuesto con scrim corto. Regla de consistencia: el chrome del bloque es header + label hover + link; todo lo demás es contenido de la marca en uso. La card de Identidad dejó el mockup de email (no era representativo del pilar) y ahora muestra wordmark + 3 avatares reales (sin el avatar M — regla "nunca el monograma M en cards"); Componentes se partió en dos paneles (kit / aplicación); Tipografía muestra 3 niveles reales del spec; el badge pill de IA en campo fue reemplazado por el header (texto duplicado) | `index.html` — `.board` (bento de 12 pilares con clases `.b1`/`.b2`/`.b3`, headers `.ch`/`.chov`), `.meta` |
| F61 | Revisado: la sección aparte "¿Qué necesitás hacer?" se sacó por pedido explícito del usuario — la intención de uso ahora vive DENTRO de cada card (ej. la card de Identidad muestra un email real con la firma real; la de Iconografía muestra un menú real con íconos + labels reales) en vez de un listado de links separado. Los 7 casos de uso se repartieron como subtítulo de acción en las cards que les corresponden | `index.html` — folded into `.board`, sección `.usecases` eliminada |

## Bloqueado por un insumo tuyo

1. **Fotos de merch** (F35) — dejar los archivos en `assets/photos/merch/` con los nombres que pide cada slot. Se muestran solas al recargar. Los veo en el chat pero no los puedo extraer de una imagen pegada.
2. **Foto de Varu en alta** — la que tengo es 200×200; el retrato B&N se ve blando a tamaño grande.
3. **Cuenta de GitHub conectada** — sin eso no puedo dejar la revisión agendada (falla con 401).

## Preguntas que solo vos podés responder

1. **C1** — ¿"sin logos ni casos ni métricas" aplica a los decks de venta, o solo al eje de comunicación en redes?
2. **C2** — ¿La voz argentina la definimos nosotros ahora o esperamos el módulo 1?
3. ¿Este repo **converge** con el playbook de Proteína o queda como sistema técnico paralelo? Nat hace el diseño del playbook — conviene hablarle antes del 13.
4. Verde para texto chico: `#009145` da 4.09:1, no llega a 4.5:1 para cuerpo. ¿Lo restringimos a ≥24px bold o buscamos un verde más oscuro?
5. Email oficial en papelería: `info@magoya.com` o nominal por persona.
