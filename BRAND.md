# Magoya · Brand System v1.2

> Manual de marca en Markdown, pensado para ser consumido por personas y por modelos de AI.
> Tokens exactos en [`tokens.json`](tokens.json) y [`tokens.css`](tokens.css). Manual visual navegable en [`brand-book.html`](brand-book.html).
> **Las reglas visuales de este archivo espejan las del brand book visual.** Si una regla cambia acá, cambia allá, y al revés.

**Regla madre del sistema:** todo asset que se puede usar tiene que estar en el brand, con su ficha: qué es, cuándo se usa, cuándo no, y de dónde se baja ([`library.html`](library.html)).

## 1. Qué es Magoya

> **Capa verbal: Magoya Brand Playbook y Guía editorial V2 (octubre de 2026).** La identidad, el posicionamiento, los territorios, la oferta, los espacios y el Método Magoya salen del playbook; la voz, el estilo, el vocabulario y la adaptación editorial salen de la Guía editorial ("Manual voz y tono MAGOYA V2"), en [`.ai/verbal/guia-editorial.md`](.ai/verbal/guia-editorial.md), cuya Parte II son las instrucciones operativas para agentes de AI. Esta sección resume lo esencial; el detalle vive en `estrategia.html`, `voz.html`, `lenguaje.html` y `aplicacion.html`, y en su versión machine-readable: [`.ai/verbal/estrategia.md`](.ai/verbal/estrategia.md), [`.ai/verbal/voz.md`](.ai/verbal/voz.md), [`.ai/verbal/lenguaje.md`](.ai/verbal/lenguaje.md), [`.ai/verbal/aplicacion.md`](.ai/verbal/aplicacion.md) y [`vocabulary.json`](vocabulary.json). Antes de entregar un texto: [`.ai/checklist-verbal.md`](.ai/checklist-verbal.md). Si algo de acá difiere de la fuente que corresponde, prevalece la fuente. La capa visual (§2 a §9) se actualizó con el feedback del equipo del 22 de octubre de 2026.

**Definición.** Magoya es una consultora hands-on en software y AI para empresas del agro. *Magoya is a hands-on software and AI consulting firm for agribusiness.* "Estrategia y ejecución" no se usa para definir a Magoya: lo reemplaza **hands-on**; y "tecnología" no reemplaza a "software y AI" en la definición o el tagline (en otros contextos puede usarse).

**Tagline.** **Software and AI for agribusiness.**

**Territorios de posicionamiento, por peso en los mensajes:** **Uso 50%** ("El éxito no es llegar al lanzamiento del producto. El éxito es que ese producto se use.") · **Integración 30%** ("Nuestra primera opción es construir sobre lo que ya existe.") · **Hands-on 20%** ("Ejecutamos lo que proponemos."). El 50/30/20, y el 70/30 de cada vocero, son guías de planificación de contenidos, no un chequeo de cada texto.

**Personalidad:** cuatro rasgos, en este orden, y cada uno ecualiza al siguiente: **Estratega · Responsable · Curiosa · Franca**. En inglés, Responsable se traduce *Accountable*, no *responsible*.

**AI.** Se escribe **AI**, en inglés, para nombrar la inteligencia artificial en cualquier idioma del texto. Única excepción: **IA en Campo**, nombre propio del programa, que se escribe siempre así (nunca "AI en Campo").

**Voz.** Convicción sin soberbia, constructiva, como partner, clara y honesta, centrada en el uso y el valor. Los diales por país son orientativos: la identidad no cambia por mercado.

**Vocabulario.** Se evitan las etiquetas reductoras para definir a Magoya (software factory, dev shop, agtech como categoría identitaria, custom como promesa central, transformación digital como definición); no son palabras universalmente vetadas, se evalúan por función y contexto. La lista del playbook (agtech · digital (solo) · transformación digital · custom · software factory · dev shop · agencia · tecnología (sola) · ayudar · adopción como sinónimo de uso · DIPI · building blocks), con sus reemplazos y el glosario ES · EN · PT, está en [`vocabulary.json`](vocabulary.json). Decimos "uso" antes que "adopción".

**Reglas operativas para AI (guía, Parte II).** No se inventan hechos, cifras, resultados, citas ni clientes. Toda métrica real la valida alguien del equipo (fuente, responsable, fecha, definición y alcance) y vive en [`ai/facts.json`](ai/facts.json). Los clientes no se nombran por defecto. Se distingue hecho validado, interpretación, hipótesis y ejemplo ilustrativo. Si hay decisiones, riesgos o cifras en juego, se entrega un borrador pendiente de revisión. Un conflicto entre fuentes se señala, no se resuelve en silencio.

**Idioma.** El inglés es el idioma principal del website, de LinkedIn y de Instagram. La personalidad es la misma en Argentina, Brasil y Estados Unidos; lo que cambia por mercado es el vocabulario, el estadio de construcción y el énfasis por audiencia.

## 2. Logo & avatares

- **Wordmark** redondeado (4 versiones: verde digital `#00DE68` sobre blanco · crema sobre verde profundo · negro `#161616` sobre blanco · verde profundo sobre crema). Nunca reconstruir ni alterar espaciado. Versión web animada: `assets/magoya-wordmark-animado.svg`.
- **Avatares** (círculo `#00DE68` + marca blanca): `go`, `o`, `cara`, `m`. La **cara** = redes de comunidad; la **m** = monograma funcional (favicon, app icon, canales corporativos).
- Aire mínimo: la altura de la "m". Tamaño mínimo: 90px pantalla / 24mm impreso. Más chico que eso, usar el avatar "m".
- ✗ No estirar, rotar, sombrear, degradar. ✗ Wordmark en lima. ✗ Recolorear avatares.

## 3. Color

| Color | HEX | Pantone (aprox.) | Rol |
|---|---|---|---|
| Verde Magoya | `#133825` | PMS 553 | **El verde protagonista de Magoya**: fondos, overlays, superficies oscuras, texto sobre claro |
| Verde digital | `#00DE68` | PMS 3282 | Identidad: wordmark, avatares, micro-acentos y data-viz. **Resalta la frase clave de un titular sobre fondo oscuro.** Como texto SOLO sobre oscuro |
| Lima | `#A2FF00` | PMS 382 2X | **Poca superficie: acentos, detalles, CTA o resaltar una palabra con la miscelánea gestual.** Nunca texto sobre blanco |
| Crema Magoya | `#ECE3DB` | PMS Warm Gray 2 | Neutro cálido; texto sobre verde profundo |
| Sage | `#EEF2EC` | PMS Cool Gray 1 | Superficie clara |
| Negro Magoya | `#161616` | PMS Black 5 2X | Texto, titulares, cards dark |

Los Pantone son el **match más cercano por distancia RGB** contra la librería Solid Coated (no existe una conversión exacta hex→Pantone): confirmar contra el libro físico antes de mandar a producción.

**Regla de color.** Ahora que el lima es uno de los colores de la paleta de IA en Campo, Magoya potencia el **Verde Magoya `#133825`** como su verde protagonista y deja el **lima** para acentos, detalles o CTA, con **mucha menos proporción** que el Verde Magoya. Para resaltar la frase clave de un titular sobre fondo oscuro se usa el **Verde digital `#00DE68`**, no el lima (ejemplo: "Software and AI **for agribusiness.**"). Respetá la paleta en todas las piezas, tanto en los posteos con foto como en los más vectoriales.

**Proporciones de uso.** El Verde Magoya ocupa la mayor superficie y el lima mucha menos. Los porcentajes exactos todavía no están definidos: no apliques porcentajes ni inventes una proporción numérica.

**Accesibilidad (no negociable):** lima nunca como texto sobre claro (1.25:1). Verde sobre blanco como texto = `#009145` y solo ≥24px bold. `#00DE68` como texto solo sobre fondos oscuros. Captions sobre claro: mínimo `#6E756D`.

## 4. Tipografía

**Manrope** (variable 200–800, self-hosted). Fallback: **Arial**. Display ExtraBold 800 con tracking −3%; cuerpo Regular 400. Kickers MAYÚSCULAS +12% tracking.

Reglas: **3 niveles tipográficos** por pieza; el peso hace la jerarquía; labels de botón en sentence case. **Emojis: nunca en títulos**; solo se permiten manitos que señalan (👈 👉 👇) para dirigir a un CTA y banderas de países para geografía, ningún otro.

**Resaltar una palabra.** Para resaltar en un titular hay dos formas: color (Verde digital #00DE68 sobre fondo oscuro) o el círculo gestual de la miscelánea nueva (`assets/marks/circle1.svg`, `circle2.svg`). Flechas, círculos, X y ✓ (`assets/marks/`): lima para detalles, acentos o resaltar una palabra; Verde digital; o Verde Magoya cuando el fondo contrasta (por ejemplo sobre Verde digital). Nunca subrayado ni bloque resaltador sólido detrás del texto. El círculo es más propio de IA en Campo: en Magoya se usa con medida y siempre con el trazo gestual nuevo. Los archivos vienen en verde oscuro (#003922): se recolorean según la regla de arriba.

## 5. Fotografía

Dos familias fotográficas, cada una con su regla:
- **Aérea de campo**: color natural, con **overlay verde profundo** (scrim 55–86%) para fondos con texto. **Siempre enfoque cenital.** El scrim es el único gradiente permitido.
- **Personas**: gente real del equipo, **siempre a color** (5 fotos aprobadas: `varu-ceo-color.jpg`, `equipo-campo-planta.jpg`, `equipo-campo-remera.jpg`, `equipo-campo-espalda.jpg`, `equipo-campo-remera-verde.jpg`; el banco suma más con la sesión nueva) y mejor **en espacios abiertos**. Sin ningún detalle encima: ni barra, ni acento verde, ni overlay. Luz natural, gesto genuino.
- ✗ Stock corporativo posado, oficinas genéricas. ✗ Fotos de personas en blanco y negro o con un detalle de color encima. ✗ Fotos de campo que no sean cenitales.

## 6. Iconografía

Línea 2px, terminaciones y esquinas redondeadas, grid 24×24, `currentColor`. **Set agro de 16 íconos + 10 logos de AI + 13 de redes en `assets/studio/icons/`, los mismos archivos que usa Magoya Studio.** Negro sobre claro, crema sobre oscuro, **lima solo el ícono destacado (uno por pieza)**. Librería propia de 58 iconos en 7 categorías (`icons.html`); completar con Lucide (misma gramática) si hace falta volumen. Nunca rellenos sólidos ni 3D.

## 7. Componentes

- **CTA, botón, box y chip.** CTA = pill de radio 44px en Verde digital o lima, con la flecha en un círculo Verde Magoya (`assets/components/cta.svg`), uno por pieza. Botones secundario (verde profundo) y terciario (outline): rectángulo de radio 10px. Box = radio 12px, cualquier color de la marca menos lima, una sola imagen en el rectángulo claro y el texto sobre el pleno (`assets/components/box.svg`). Chip = pill outline, nunca sólido.
- **Espaciado sistematizado.** Todo margin/padding/gap sale de la escala base-4 de `tokens.json` (4/8/12/16/24/32/48/64/96), nunca valores arbitrarios. Aire entre bloques ≥24; dentro de un componente 8–16. Paddings canónicos: botón 13px/26px, chip 6px/15px (spec completa en `components` de `tokens.json`).
- **Alineación.** Una pieza tiene UN eje principal (por defecto, izquierda): todos los bloques de texto arrancan ahí. Los elementos de una fila comparten centro vertical y un gap único (8 o 12). Padding interno simétrico, nunca 4 valores distintos.
- Estados: hover (lima→`#8BDB00`, resto brightness), focus ring `rgba(0,222,104,.45)` sin blur.
- **Cards: siempre en mosaico**: misma grilla, mismos aires, alturas que calzan; nunca sueltas. Tipos: hiring (negro + lima), quote (foto + cita), stat (número 800 −3%). El contacto dentro de una card dark es un **link en lima**, no un botón (los botones viven fuera de las cards).
- ✗ **El monograma "m" circular NO va en cards.** El avatar "m" es identidad de canal (favicon, app icon, perfil corporativo) y pie de papelería; dentro de una card compite con el wordmark y agrega un segundo logo a la pieza. En una card, la marca es el wordmark.
- Logo wall: logos **siempre reales**, en gris, grilla pareja.

## 8. Papelería & corporativo

- **Posteos de redes**: 8 posteos de referencia en PNG 1080×1350 (`assets/social/`, ZIP `assets/downloads/magoya-redes.zip`). Son referencias, no archivos editables. Respetan la paleta tanto con foto como en versión vectorial, y cuando usan los recursos (CTA, box, flechas, círculos, X y ✓) siguen sus reglas.
- **Templates de deck**: dos bases. *Uso interno* (índice, carátulas e internas): PDF de 17 slides en `assets/deck/magoya-interno.pdf`. *Uso con clientes* (más institucional): solo previews en `assets/deck/clientes-*.jpg`; el PDF completo no se publica porque incluye condiciones de cada cliente. Las bases también están armadas en Claude.
- **Membrete A4**: wordmark verde arriba-izq (20% del ancho), pie con filete verde digital + avatar m. Header y footer vectoriales listos: `assets/downloads/doc-header.svg` · `doc-footer.svg`.
- Docs: wordmark esquina sup-izq ≤1/5 del ancho; Manrope o Arial; nunca logo como marca de agua.

## 9. Reglas de oro (resumen ejecutable)

1. El Verde Magoya `#133825` es el verde protagonista y ocupa la mayor superficie. Los porcentajes exactos no están definidos: no apliques porcentajes.
2. Lima en poca superficie: acentos, detalles, CTA o resaltar una palabra con la miscelánea gestual.
3. Verde digital `#00DE68` = identidad (logo/avatares) y resaltado de la frase clave en titulares sobre oscuro; lima ≠ logo.
4. Personas siempre a color, sin ningún detalle encima, mejor en espacios abiertos. Aérea de campo siempre cenital. Magoya no usa ilustración.
5. Logos de clientes SIEMPRE reales, jamás placeholders.
6. Todo redondeado, como el wordmark. CTA pill 44px (Verde digital o lima), botón rect 10px, box radio 12px (nunca lima), chip pill outline.
7. Resaltar: color (Verde digital sobre oscuro) o el círculo gestual nuevo. Flechas, círculos, X y ✓ en lima, Verde digital o Verde Magoya según el fondo. Nunca subrayado.
8. El monograma "m" no va en cards.
9. **Emojis prohibidos**: la única excepción son las manitos que señalan (👈 👉 👇) hacia un CTA y las banderas de países para geografía. Nunca en títulos.
10. ✗ Pieza 100% negra o 100% verde (siempre equilibrio) · ✗ Resaltador sólido tras texto · ✗ gradientes glossy/3D/estética AI · ✗ puzzle (metáfora del brand viejo) · ✗ naranja/amarillo del brand viejo.
11. **AI, en cualquier idioma**: se escribe AI para nombrar la inteligencia artificial, también en textos en español. Única excepción: el nombre propio **IA en Campo**. Regla del Brand Playbook (slide 50); el resto de la capa verbal en §1.

## 10. IA en Campo (manual propio)

**No es una sección de este brand: es una marca de programa presentada por Magoya, con su propio sistema de marca** (`ai-en-campo/`, octubre 2026). Programa abierto de AI aplicada al agro: carruseles, reels, webinars y capacitaciones abiertas, por ahora solo en Argentina. Magoya habla de AI desde el lado de quien la construye; IA en Campo, desde el lado de quien la usa. **Cuándo NO:** propuestas comerciales, casos de cliente formales, deck de ventas, sitio: eso es core Magoya.

**Logo.** Signo ‹ia + leyenda EN CAMPO, en tres versiones: con placa, simple y con "Una iniciativa de Magoya" (`ai-en-campo/assets/descargas/logos.zip`). La minúscula es solo del logo: en texto se escribe siempre **IA en Campo**.

**Paleta (alto contraste, llamativa a propósito).** Comparte con Magoya la base (verde profundo `#003922`, verde lima `#80FF00`, negro `#161616`); sale el verde pleno y el crema; entran **violeta eléctrico `#B700FF`** y **blanco `#FFFFFF`**. El violeta es el acento y marca todo lo que es AI y el contenido de IA en Campo News. Combinaciones: frase clave texto oscuro sobre lima · título blanco sobre negro · botón blanco sobre violeta.

**Tipografía.** Par propio, distinto del de Magoya: **Plus Jakarta Sans** (variable 200–800, OFL) para títulos y bajadas; **Helvetica** para texto largo y pies (fallback Arial). Título 800 con tracking −3% (~14% del ancho en un posteo de 1080 px), bajada 500 Medium (~6,5%). Máximo 3 niveles por pieza; nunca una tercera familia; cuerpo nunca menos de 11 px.

**Resaltado.** Una sola frase por título, en MAYÚSCULAS, sobre bloque verde lima con texto oscuro (puede ir levemente inclinado). Emojis: nunca en títulos; solo la manito que señala (👈 👉 👇) para dirigir al botón.

**Imágenes.** Lo humano del campo, de cerca: planos cortos, nítidos, color natural, verdes vivos. La foto trae lo humano; lo gráfico trae la AI.

**Íconos.** 16 íconos pixelados (siguen el lenguaje del logo), monocromos: negro sobre claro, blanco sobre oscuro; uno destacado por pieza (lima sobre oscuro).

**Personaje.** Tiene la forma de las fichas de herramientas (ChatGPT, Gemini): es la ficha de IA en Campo que cobró vida. Mueve la mirada y pone la emoción; no explica. Siempre interactúa con algo y va anclado a un borde (10–15% del ancho), una aparición por pieza (en carruseles, portada y cierre como máximo), mira hacia lo importante y nunca tapa datos. No va en piezas con personas reales ni donde el dato tiene que leerse serio.

**Componentes.** Todo toma la forma de la placa del logo: **esquinas cortadas en diagonal**. Botones en tres niveles (primario violeta, secundario lima, terciario outline), label en minúscula salvo la primera letra, un solo primario por pieza, hover con sombra sólida tipo píxel; sobre violeta, el primario pasa a lima. Chips: etiqueta rectangular sólida, MAYÚSCULAS, sin punto ni ícono, sin hover. Cards en mosaico con esquina cortada: lima para preguntas del lote, violeta para IA en Campo News, verde profundo para webinars y citas. Nada de esto vuelve al core.

**Formatos.** Piezas para redes que hacen decir "a ver" (no buscan un feed uniforme) y miniaturas de YouTube 16:9 con la frase clave en bloque lima sobre fondo oscuro verde y violeta.

**Pendientes que marca el propio manual:** componentes como primera propuesta; colores de caption, link y check "a confirmar"; el verde `#009145` del ícono destacado sobre claro no está en la paleta; alinear el lima `#80FF00` con el de Magoya; una miniatura de YouTube usa la sigla en español en lugar de AI; el logo con placa necesita versión en alta o SVG.

**Identidad anterior (retirada).** El lienzo verde digital pleno, la placa negra con texto crema, el lockup "IA en Campo · por Magoya" en Manrope y los doodles/flourishes del Studio eran la identidad previa del programa: se retiraron del repo el 29 oct 2026 y no se usan en piezas nuevas.

## Mapa de archivos del sistema

| Página | Qué documenta |
|---|---|
| `estrategia.html` · `voz.html` · `lenguaje.html` · `aplicacion.html` | Capa verbal del Brand Playbook (octubre 2026) |
| `brand-book.html` | Identidad visual: logo, color, tipografía, fotografía, iconografía, componentes, reglas de oro |
| `library.html` | Recursos: ficha + descarga de cada asset aprobado |
| `icons.html` | 58 iconos copiables |
| `logos.html` | Logos de clientes y stack tecnológico |
| `ai-en-campo/` | Sistema de marca de IA en Campo (sitio propio, octubre 2026) |
| `ai.html` | Integrar con AI: cómo cargar esta marca en una herramienta de AI y cómo validar el resultado |

Capa machine-readable: `llms.txt` (resumen estable), `.ai/brand-prompt.md` y `.ai/brand-prompt-short.md` (prompts para pegar), `.ai/checklist.md` (validación visual), `.ai/checklist-verbal.md` (validación de texto), `.ai/verbal/` y `vocabulary.json` (capa verbal) y `.ai/presets/` (uno por herramienta). **Todos derivan de este archivo: si una regla cambia acá, hay que propagarla ahí.**

`assets/refs/` es **material fuente no publicable** (exports originales del diseñador): se conserva como referencia de trazado, no se enlaza ni se distribuye.

---

*Pendientes de contenido: porcentajes exactos de uso del color; archivos vectoriales de la miscelánea nueva de redes (círculo y flechas); link al Artifact base del deck; logos vectoriales de ProducePay/HabiTerre/IntelinAir; validación de Staff Augmentation; unificación del email de contacto (hoy conviven `people@` e `info@`).*
