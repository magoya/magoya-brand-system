# Magoya — Brand System v1.1

> Manual de marca en Markdown, pensado para ser consumido por personas y por IAs.
> Tokens exactos en [`tokens.json`](tokens.json) y [`tokens.css`](tokens.css). Manual visual navegable en [`brand-book.html`](brand-book.html).
> **Las secciones 1–13 + §14 espejan una a una las del brand book visual.** Si una regla cambia acá, cambia allá — y al revés.

**Regla madre del sistema:** si se crea algo nuevo que puede ir en una pieza, tiene que estar en el brand. Ningún asset ni componente existe sin su ficha: qué es, cuándo se usa, cuándo no, y de dónde se baja ([`library.html`](library.html)).

## 1. Qué es Magoya

Estudio/partner de **estrategia y desarrollo de producto digital para agribusiness** (desde 2017). *"We partner with modern agribusinesses to design, build, and evolve their products and platforms."* Hero de marca: **"AgTech challenges demand more than code."** Diferenciador: equipos senior **embebidos** en el equipo del cliente — tecnólogos, expertos de producto y agrónomos. Pilares (las 3C): **Clarity** (complejidad → plan claro), **Confidence** (equipos senior con fluidez AgTech), **Commitment** (largo plazo).

**Voz:** **traductora** — hablamos agro y software, y el trabajo es pasar de uno al otro sin perder precisión. **Concreta**: ninguna afirmación de valor viaja sin cifra, nombre de cliente, plazo o captura. **Directa**: oraciones cortas, conclusión primero, cero preguntas retóricas, mínimo de siglas. **Filosa cuando hace falta**: decimos lo que no cierra — ni hype de IA ni negacionismo. **Informal sin ser liviana**: voseo en español, humor cuando aliviana una idea, nunca como adorno; no infantil.

**Idioma:** español para cercanía y comunidad (voseo, léxico del lote); inglés para credencial y cuentas US (nativo-conceptual, nunca traducido, con revisión nativa antes de salir); portugués para Brasil. **En textos en castellano, mínimo de palabras en inglés — y las que van, traducidas.**

**Vocabulario propio:** *levantar el guante · no damos vueltas · talento híbrido / trilingües · traducir · convertir complejidad en decisiones · señal y ruido · equipo embebido (embedded) · claridad, confianza, compromiso · lote, campaña, ventana de siembra.*

**Nunca:** preguntas retóricas · superlativos sobre nosotros mismos ("the best", "unparalleled") · "as a service" para lo que es un servicio a medida · siglas internas (DIPI) · "soluciones end-to-end" · "fracaso" · "familia" para el equipo · "startup" para Magoya · hype de IA · frasecitas de autoayuda.

> Evidencia y trazabilidad de cada regla: [`VOICE-RESEARCH.md`](VOICE-RESEARCH.md) — releva el Manual de Marca 2022 (la única especificación de voz que Magoya tuvo), la estrategia de marca de Varu, los pilares de contenido y las reuniones. **"No whimsical" salió de acá y volvió a ilustración**: era una conclusión sobre los personajes, no sobre la voz — cuatro fuentes piden humor explícitamente.

## 2. Logo & avatares

- **Wordmark** redondeado (4 versiones: verde digital `#00DE68` sobre blanco · crema sobre verde profundo · negro `#161616` sobre blanco · verde profundo sobre crema). Nunca reconstruir ni alterar espaciado.
- **Avatares** (círculo `#00DE68` + marca blanca): `go`, `o`, `cara`, `m`. La **cara** = redes de comunidad; la **m** = monograma funcional (favicon, app icon, canales corporativos).
- Aire mínimo: la altura de la "m". Tamaño mínimo: 90px pantalla / 24mm impreso — menos que eso, usar avatar "m".
- ✗ No estirar, rotar, sombrear, degradar. ✗ Wordmark en lima. ✗ Recolorear avatares.

## 3. Color

| Color | HEX | Pantone (aprox.) | Rol |
|---|---|---|---|
| Verde Magoya | `#133825` | PMS 553 | Core institucional: fondos oscuros, overlays, texto sobre claro |
| Verde digital | `#00DE68` | PMS 3282 | Identidad: wordmark, avatares, micro-acentos, ropa de personajes y data-viz. Como texto SOLO sobre oscuro |
| Lima energía | `#A2FF00` | PMS 382 2X | CTA, display, motivo. **Dosis única por pieza.** Nunca texto sobre blanco |
| Crema Magoya | `#ECE3DB` | PMS Warm Gray 2 | Neutro cálido firma; texto sobre verde profundo |
| Sage | `#EEF2EC` | PMS Cool Gray 1 | Superficie clara de slides |
| Negro Magoya | `#161616` | PMS Black 5 2X | Texto, titulares, cards dark |

Los Pantone son el **match más cercano por distancia RGB** contra la librería Solid Coated (no existe una conversión exacta hex→Pantone) — confirmar contra el libro físico antes de mandar a producción.

**El verde ilustración (`#33DB4E`) se unificó con el verde digital el 6 de agosto de 2026** — eran demasiado parecidos como para convivir como dos colores distintos. El token `--leaf-500` sigue en `tokens.css` como alias de `--emerald-500` por compatibilidad; no es un verde distinto.

**Regla central: "El negro construye, el verde hace crecer."** Neutros ≈75% de cada pieza, verde ≈25%, un solo movimiento verde dominante. Nunca pieza 100% negra ni 100% verde.

**Proporción exacta (confirmada por Varu el 5 de agosto de 2026 como obligatoria — "cualquier diseño que hagas tiene que mantener estas proporciones", deja de ser guía y pasa a ser regla):**

| Color | % de la pieza |
|---|---|
| Blanco / sage | 52% |
| Negro `#161616` | 23% |
| Verde profundo `#133825` | 13% |
| Lima `#A2FF00` | 8% |
| Verde digital `#00DE68` | 4% |

Suma: neutros (blanco+negro) 75%, verde (profundo+lima+digital) 25% — la misma regla de siempre, ahora con el desglose exacto por color, obligatorio en todo lo que se produce.

**Accesibilidad (no negociable):** lima nunca como texto sobre claro (1.25:1). Verde sobre blanco como texto = `#009145` y solo ≥24px bold. `#00DE68` como texto solo sobre fondos oscuros. Captions sobre claro: mínimo `#6E756D`.

## 4. Tipografía

**Manrope** (variable 200–800, self-hosted). Fallback: **Arial**. Display ExtraBold 800 con tracking −3%; cuerpo Regular 400. Kickers MAYÚSCULAS +12% tracking. Escala de slides: hero 126pt · display 84pt · título 56pt · subtítulo 42pt (sobre 1920px).

Reglas: **3 niveles tipográficos** en piezas escritas a mano (web, redes, docs); en slides el techo lo declara el catálogo, que llega a **7** porque cada nivel tiene un rol (kicker, display, bajada, caption, dato, label, pie) — ver el chequeo 7; el peso hace la jerarquía; resaltado por color o **subrayado lima** — prohibido el bloque resaltador sólido detrás de texto; labels de botón en sentence case. **Emojis: nunca en títulos**; solo se permiten manitos que señalan (👈 👉 👇) para dirigir a un CTA y banderas de países para geografía — ningún otro.

## 5. Fotografía

Dos familias, cada una con su regla:
- **Aérea de campo** (color natural): para fondos y portadas, siempre con **scrim verde profundo 55–86%** cuando lleva texto encima. El scrim es el único gradiente permitido.
- **Personas**: gente real del equipo, **siempre B&N** con un acento verde o lima. Remera Magoya, luz natural, gesto genuino.
- ✗ Stock corporativo posado, oficinas genéricas, personas a color en piezas de marca.

## 6. Ilustración & motivos

- **Personajes planos redondeados, sin rostro.** Paleta CERRADA de 5 colores: `#00DE68` (ropa, verde digital) · `#A2FF00` (ropa) · `#DFDFDF` (ropa) · `#FFC67B` (piel) · `#161616` (pelo/detalle). Siempre **recortados por un borde de la pieza**, del lado opuesto al texto — nunca flotando enteros ni centrados como clipart.
- **Motivo de marca: semicírculos**, un único formato — el **paño de textura** en grilla diagonal escalonada (`assets/motif-semis.svg`). **Regla de sangrado: el paño va al corte y siempre nace de un borde de la pieza o queda detrás de un objeto — nunca puede verse cortado flotando en el aire.** Aplicaciones canónicas: franja lateral (el paño ocupa una columna del borde y el contenido vive sobre el blanco) o fondo completo tapado por una card. Colores: verde digital sobre crema/blanco · crema sobre verde profundo · lima sobre oscuro.
- ✗ **La banda festoneada quedó RETIRADA** (no funcionaba como remate y se usaba como adorno genérico). No hay asset de banda: el único motivo es el paño.
- **Ocupar el espacio:** si un recurso está en la pieza, es para que se vea. El gráfico ocupa el ancho de su columna, la cifra ~70% del bloque, el personaje 40–55% de la pieza, el paño llega al corte. Un recurso que no se lee de lejos o crece, o se saca — nada de detalles decorativos chiquitos.
- **Marcas a mano**: **círculo** = marca una fecha o dato puntual · **flecha** = señala el CTA: nace del texto y su punta cae sobre el botón (diagonal, no al costado). Una sola por pieza, en **verde digital #00DE68 sobre claro / lima sobre oscuro** (nunca en negro: contra el texto no resaltan), siempre sobre texto compuesto — nunca sueltas como adorno. Para enfatizar una palabra o frase de un titular, **el color hace el trabajo** (texto en lima), no una marca a mano.
- ✗ RETIRADOS: motivos de líneas (caminos concéntricos `assets/illus/camino-*.svg`, estratos `assets/motif-estratos.svg`), la banda festoneada, el **subrayado** a mano (`flourish-underline.svg` — no cubría bien la palabra completa y el trazo no tenía fuerza; reemplazado por texto en lima), personajes con rostro/monoline/stock, y la metáfora del **puzzle** (brand viejo — su reemplazo narrativo es el paño de semicírculos (crecimiento)). ✗ Naranja y amarillo del brand viejo. Los archivos retirados quedan en disco como historial: **no se usan en piezas nuevas y no tienen ficha en la librería.**

## 7. Convivencia de recursos

La marca tiene seis recursos gráficos. La regla que los ordena: **máximo dos por pieza además de la tipografía** — uno protagonista y otro que acompaña en segundo plano. Con tres o más deja de ser Magoya y se vuelve ruido.

| Combinar… | Foto aérea | Foto B&N | Personaje | Paño ○ | Marca a mano | Ícono |
|---|---|---|---|---|---|---|
| **Foto aérea** | — | ✗ | ✗ | ✗ | ✓ | ✓ |
| **Foto B&N (personas)** | ✗ | — | ✗ | ✓ | ✓ | ✓ |
| **Personaje ilustrado** | ✗ | ✗ | — | ✓ | ✓ | ✗ |
| **Paño de semicírculos** | ✗ | ✓ | ✓ | — | ✓ | ✓ |
| **Marca a mano** | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| **Ícono** | ✓ | ✓ | ✗ | ✓ | ✓ | — |

**La razón de los vacíos es una sola: dos lenguajes del mismo tipo compiten.** Dos imágenes (foto + foto, foto + ilustración), dos texturas (foto + paño) o dos dibujos (personaje + ícono) nunca conviven. La cifra gigante y la tipografía combinan con todo: son la voz, no un recurso.

**Personaje + paño** (la combinación que más se pregunta) **sí funciona**, con una condición: el paño va al fondo y en franja, el personaje al borde opuesto y en primer plano, el texto sobre superficie limpia. Nunca superpuestos.

**Jerarquía de planos** — toda pieza se ordena en cuatro: **(1) lienzo** color plano o foto con scrim · **(2) textura** paño al corte · **(3) sujeto** personaje, foto recortada o cifra gigante · **(4) voz** tipografía, marcas a mano, chips y CTA. Un recurso por plano como máximo, y los planos 2 y 3 nunca se pisan entre sí.

## 8. Iconografía

Línea 2px, terminaciones y esquinas redondeadas, grid 24×24, `currentColor`. **Set agro de 16 íconos + 10 logos de IA + 13 de redes en `assets/studio/icons/` — los mismos archivos que usa Magoya Studio.** Negro sobre claro, crema sobre oscuro, **lima solo el ícono destacado (uno por pieza)**. Librería propia de 58 iconos en 7 categorías (`icons.html`); completar con Lucide (misma gramática) si hace falta volumen. Nunca rellenos sólidos ni 3D.

## 9. Componentes

- **Botón ≠ chip.** Botón: rectángulo radio 10px, fondo sólido (lima = CTA primario, negro, verde profundo, ghost). Chip: **pill outline** — borde y texto del mismo color, fondo transparente. Nunca chip sólido ni botón pill. **El chip lleva SOLO texto** (uppercase, tracking .1em): nunca un punto/bullet delante, nunca un ícono adentro — la pill ya delimita, el punto es ruido (acuerdo explícito del equipo).
- **Espaciado sistematizado.** Todo margin/padding/gap sale de la escala base-4 de `tokens.json` (4/8/12/16/24/32/48/64/96) — nunca valores arbitrarios. Aire entre bloques ≥24; dentro de un componente 8–16. Paddings canónicos: botón 13px/26px, chip 6px/15px (spec completa en `components` de `tokens.json`).
- **Alineación.** Una pieza tiene UN eje principal (por defecto, izquierda): todos los bloques de texto arrancan ahí. Los elementos de una fila comparten centro vertical y un gap único (8 o 12). Padding interno simétrico, nunca 4 valores distintos.
- Estados: hover (lima→`#8BDB00`, resto brightness), focus ring `rgba(0,222,104,.45)` sin blur.
- **Cards: siempre en mosaico** — misma grilla, mismos aires, alturas que calzan; nunca sueltas. Tipos: hiring (negro + lima), quote (foto B&N + cita), stat (número 800 −3%). El contacto dentro de una card dark es un **link en lima**, no un botón (los botones viven fuera de las cards).
- ✗ **El monograma "m" circular NO va en cards.** El avatar "m" es identidad de canal (favicon, app icon, perfil corporativo) y pie de papelería — dentro de una card compite con el wordmark y agrega un segundo logo a la pieza. En una card, la marca es el wordmark.
- Logo wall: logos **siempre reales**, en gris, grilla pareja.

## 10. Aplicaciones (recetas)

- **Hero canónico** (la pieza que define la marca): foto aérea + scrim verde + wordmark crema arriba-izq + CTA lima arriba-der + display ExtraBold abajo-izq con una frase en lima.
- **Feed 1:1** — 3 recetas rotativas: foto (statement sobre aérea) · crema (aviso + avatar de comunidad) · dark (dato lima + personaje recortado). En redes, **display y cifras al ~70% del ancho**: grande o nada.
- **Story 9:16**: foto arriba + bloque verde abajo con display y CTA lima. **Banner de LinkedIn**: foto del equipo en B&N + scrim negro degradado + wordmark crema + filete verde digital al borde (misma receta que la fotografía de personas). **Avatar de perfil**: cara (comunidad) / m (corporativo).
- **Slides**: lienzos blanco/sage, como máximo un golpe de lima por slide (cero es válido: 19 de las 41 plantillas no llevan), margen interior 7% (`slides.html`, 41 módulos en 13 familias, exportables a .pptx). **Piezas comerciales**: one-pager madre + flyers derivados (`pieces.html`).
- **Export**: slides 16:9 1920×1080 · feed 1080×1080 · carrusel retrato 4:5 1080×1350 · story 1080×1920 (zona segura 96px) · favicon = avatar "m" 16/32/180/512px sin padding · print A4 sangrado 3mm, CMYK con prueba de color.

## 11. Merch & indumentaria

- **Textil**: verde profundo + crema, discreto y premium. **El merch se muestra SIEMPRE con foto o render real del producto — nunca ilustración ni esquema vectorial** (referencia de calidad: render "Buzo Propuesta 1"). Catálogo de 10 productos (buzo, remera blanca/negra, gorra, medias, mochila, termo, cuaderno, stickers, equipo usándolo); las fotos van en `assets/photos/merch/` con los nombres del LEEME y el manual las levanta solo. Wordmark chico pecho izquierdo, monograma "m" en espalda, patrón de avatares solo en forros. Bordado > estampa. **Sin lima en textil.**

## 12. Papelería & corporativo

- **Membrete A4**: wordmark verde arriba-izq (20% del ancho), pie con filete verde digital + avatar m. Header y footer vectoriales listos: `assets/downloads/doc-header.svg` · `doc-footer.svg`.
- **Firma de email**: va **SIEMPRE el wordmark — nunca los avatares ni la cara.** Filete verde + nombre 700 + rol y datos en gris. Sin banners, sin frases legales eternas, sin logos de redes. Assets: `assets/downloads/magoya-firma-animada.gif` (Gmail, loop) y `magoya-firma-estatica.png` (correos que no animan). Versión web animada del logo: `assets/magoya-wordmark-animado.svg`.
- Docs: wordmark esquina sup-izq ≤1/5 del ancho; Manrope o Arial; nunca logo como marca de agua.

## 13. Reglas de oro (resumen ejecutable)

1. El negro construye, el verde hace crecer (75/25, un movimiento verde por pieza).
2. Lima = energía en dosis única: un CTA, un display o un motivo por pieza.
3. Verde digital `#00DE68` = identidad (logo/avatares); lima ≠ logo.
4. Personas reales en B&N con acento verde; ilustración plana para conceptos.
5. Logos de clientes SIEMPRE reales — jamás placeholders.
6. Todo redondeado — como el wordmark. Botón rect 10px, chip pill outline.
7. El motivo va al corte: nace de un borde o de detrás de un objeto — nunca cortado al aire.
8. Máximo 2 recursos gráficos por pieza (§7); el monograma "m" no va en cards; en la firma va el wordmark.
9. **Emojis prohibidos** — la única excepción son las manitos que señalan (👈 👉 👇) hacia un CTA y las banderas de países para geografía. Nunca en títulos.
10. ✗ Resaltador sólido tras texto · ✗ gradientes glossy/3D/estética IA · ✗ pieza 100% negra o verde · ✗ personajes con rostro/monoline · ✗ puzzle · ✗ naranja/amarillo · ✗ banda festoneada · ✗ motivos de líneas.
11. **En español se escribe IA, nunca AI** — "IA en campo", "Integrar con IA", "capacidades de IA". "AI" queda solo para copy en inglés (decks US) y nombres propios ajenos ("Data & AI", "AI Studio"). Una pieza en español que diga "AI" está mal escrita.

## 14. Marca anexa "IA en campo" (manual propio)

**No es una sección de este brand: es una marca anexa con su propio manual** (`ai-en-campo.html`). Línea de contenido educativo de IA para el agro (carruseles, reels, webinars). Mismo ADN (Manrope, verdes oficiales) pero **rompe tres reglas del core a propósito**: (1) lienzo **verde digital pleno #00DE68** como fondo dominante; (2) **placa negra** #161616 con texto crema para el dato clave — permitida acá como lenguaje sticker; (3) **ruido con los assets del Studio** (`assets/studio/`): doodles (sparkle, dots, blob, loop), flourishes (arrow, navarrow, circle, underline), badge EN VIVO y logos oficiales de IA/redes — 2–4 por pieza, ±5–15°, en las esquinas, teñidos en verde digital o lima (nunca un color propio: la sub-marca no usa terracota ni ningún acento fuera de la paleta core). Texto secundario verde profundo; display negro. Formato madre: **carrusel retrato 4:5 (1080×1350)** — no el cuadrado 1080×1080, que Instagram dejó de privilegiar para carruseles. Arco narrativo de 4–6 slides (duda real → herramienta → prueba → paso siguiente), sin numerar las slides (el swipe ya lo comunica); **ritmo de color del arco: verde pleno en la primera y la última slide, crema Magoya en las del medio** — todo verde se lee como una sola pieza repetida, no como un recorrido.

**Logo de la sub-marca:** lockup **"IA en campo · por Magoya"** abajo-izquierda — reemplaza al wordmark de Magoya solo en piezas de esta línea. Se compone con Manrope viva (800, tracking −2%), nunca como imagen. Lleva un mark a mano (`assets/studio/mark-ai-campo.svg`, mismo lenguaje de las marcas a mano del core) pegado a la derecha de "IA", a ~65% de su altura — **ese mark existe únicamente en este tamaño**: agrandado y suelto en una esquina como estallido cómic queda fuera del sistema. Negro `#161616` sobre lienzo claro, crema `#ECE3DB` sobre placa negra; nunca lima ni verde digital en el lockup — el color lo pone el fondo, no el logo. "por Magoya" siempre en `font-mono`, mayúsculas, más chico: es la firma, no el título.

Las piezas se producen SIEMPRE desde plantillas del Studio y su receta queda guardada en un `.magoya.json` (template, scheme, accent, anchor, rule, silueta, objetos con x/y/scale/rotation) — esa es la fuente para reproducirlas, no el ojo. Producción en Magoya Studio (30+ plantillas, 13 formatos de red). Nada de esto vuelve al core.

## Mapa de archivos del sistema

| Página | Qué documenta |
|---|---|
| `brand-book.html` | Brand book: 13 secciones + §14 marca anexa |
| `ai-en-campo.html` | Manual completo de la marca anexa |
| `slides.html` | Módulos de presentación |
| `pieces.html` | Piezas comerciales (one-pager + flyers) |
| `icons.html` | 58 iconos copiables |
| `library.html` | Ficha + descarga de cada asset aprobado |
| `logos.html` | Logos de clientes y stack tecnológico |
| `ai.html` | Cómo cargar esta marca en una herramienta de IA y cómo validar el resultado |

Capa machine-readable: `llms.txt` (resumen estable), `.ai/brand-prompt.md` y `.ai/brand-prompt-short.md` (prompts para pegar), `.ai/checklist.md` (validación) y `.ai/presets/` (uno por herramienta). **Todos derivan de este archivo: si una regla cambia acá, hay que propagarla ahí.**

`assets/refs/` es **material fuente no publicable** (exports originales del diseñador): se conserva como referencia de trazado, no se enlaza ni se distribuye. `archive/` son versiones previas del sistema — no usar.

---

*Pendientes de contenido: fotos/nombres reales del equipo, cita completa de Camila López Colmano, logos vectoriales de ProducePay/HabiTerre/IntelinAir, validación de Staff Augmentation, unificación del email de contacto (hoy conviven `people@` e `info@`).*
