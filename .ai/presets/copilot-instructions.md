<!--
CÓMO USAR ESTE ARCHIVO — GITHUB COPILOT
Guardalo tal cual, con este nombre, en:

    .github/copilot-instructions.md

Se lee en cada request de Copilot Chat y de los agentes, en el IDE y en github.com.
Si querés que aplique solo a los archivos de front, movelo a
.github/instructions/magoya-brand.instructions.md y agregale este frontmatter:

    ---
    applyTo: "**/*.{css,scss,html,jsx,tsx,vue,svelte,svg}"
    ---

Este comentario HTML es para vos; podés borrarlo o dejarlo, Copilot lo ignora.
-->

# Magoya — Design System

Magoya es una consultora hands-on en software y AI para empresas del agro (tagline: **Software and AI for agribusiness**). Toda UI, pieza y copy de este repo sigue el brand system: https://brand.magoya.com/ (`BRAND.md` + `tokens.json` + `tokens.css`).

## Color

Si el proyecto importa `tokens.css`, usá las custom properties (`var(--color-text)`, `var(--color-energy)`, `var(--radius-btn)`) en lugar de hex literales.

- `#161616` negro — texto, titulares, cards dark
- `#133825` Verde Magoya — **el verde protagonista**: fondos oscuros, overlays, texto sobre claro
- `#00DE68` verde digital — identidad (wordmark, avatares, micro-acentos) y data-viz. Como texto **solo sobre fondo oscuro**
- `#009145` — verde texto sobre blanco, y solo a ≥24px bold
- `#A2FF00` lima — poca superficie: acentos, detalles, CTA o resaltar una palabra con la miscelánea gestual (la frase clave de un titular sobre fondo oscuro va en Verde digital #00DE68). **Nunca como texto sobre fondo claro.** Hover `#8BDB00`
- `#ECE3DB` crema — texto sobre verde profundo
- `#EEF2EC` sage / `#FFFFFF` — superficies claras
- `#6E756D` — captions sobre claro (mínimo accesible)

Proporciones de uso entre colores: el Verde Magoya ocupa la mayor superficie y el lima mucha menos; los porcentajes exactos no están definidos. No apliques porcentajes ni inventes una proporción numérica. No uses colores que no estén en `tokens.json`. Cero naranja, cero amarillo.

## Tipografía

`font-family: "Manrope", Arial, sans-serif` — variable 200–800.
Display `font-weight:800; letter-spacing:-0.03em; line-height:1.05`. Cuerpo `400; line-height:1.55`. Kicker `800; uppercase; letter-spacing:0.12em`.
Máximo 3 niveles tipográficos por vista. Labels de botón en sentence case, nunca MAYÚSCULAS.

## Componentes

- **Botón**: CTA = pill de radio 44px en Verde digital o lima, con la flecha en un círculo Verde Magoya (`assets/components/cta.svg`), uno por pieza. Botones secundario (verde profundo) y terciario (outline): rectángulo de radio 10px. Box = radio 12px, cualquier color de la marca menos lima, una sola imagen en el rectángulo claro y el texto sobre el pleno (`assets/components/box.svg`). Chip = pill outline, nunca sólido.
- **Chip**: `border-radius:999px`, `background:transparent`, borde y texto del mismo color. Nunca chip sólido. La única pill sólida es el CTA.
- **Focus**: `box-shadow: 0 0 0 3px rgba(0,222,104,.45)` sin blur. No dejes `outline:none` sin reemplazo.
- Radios 6/12/20/28/999px. Espaciado base 4px (4-8-12-16-24-32-48-64-96).
- Iconos SVG inline: `stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"`. Nunca rellenos sólidos ni 3D.

## No hagas

- **Sin emojis** en UI, copy, títulos ni labels. Únicas excepciones: manitos que señalan (👈 👉 👇) apuntando a un CTA, y banderas de países para geografía.
- **Sin gradientes** (`linear-gradient`, `radial-gradient`), sin glassmorphism, sin `backdrop-filter` decorativo, sin sombras de brillo, sin 3D. Único gradiente permitido: overlay verde profundo sobre foto aérea, `linear-gradient(180deg, rgba(12,33,23,.55), rgba(12,33,23,.86))`.
- Para resaltar en un titular hay dos formas: color (Verde digital #00DE68 sobre fondo oscuro) o el círculo gestual de la miscelánea nueva (`assets/marks/circle1.svg`, `circle2.svg`). Flechas, círculos, X y ✓ (`assets/marks/`): lima para detalles, acentos o resaltar una palabra; Verde digital; o Verde Magoya cuando el fondo contrasta (por ejemplo sobre Verde digital). Nunca subrayado ni bloque resaltador sólido detrás del texto.
- Sin logos de clientes inventados o placeholder: van los reales de `assets/logos/clients/`, en gris y grilla pareja.
- Sin la metáfora del puzzle.
- **Sin ilustración**: Magoya no usa ilustración.
- **Fotografía**: aérea de campo en color natural, con overlay verde profundo para fondos con texto, siempre cenital. Personas siempre a color, sin ningún detalle encima (ni barra ni acento verde), mejor en espacios abiertos.
- El monograma "m" circular es funcional (favicon, app icon), no un sello decorativo dentro de cards.

## Copy en UI

Estrategia, posicionamiento, oferta y método salen del Magoya Brand Voice Playbook (octubre de 2026; la edición en español es la fuente de verdad y la edición en inglés define cómo se dice en inglés). Voz, estilo y vocabulario salen de la Guía editorial V2 (https://brand.magoya.com/.ai/verbal/guia-editorial.md). Cifras, casos y clientes, de `ai/facts.json` con validación humana. Objetivo, audiencia, canal, idioma y CTA, del brief, que no redefine la identidad ni autoriza cifras.
- Definición (obligatorio): consultora hands-on en software y AI para empresas del agro (*hands-on software and AI consulting firm for agribusiness*). Tagline, siempre en inglés: **Software and AI for agribusiness**. "Estrategia y ejecución" no la define: lo reemplaza hands-on. "Tecnología" no reemplaza a "software y AI". En inglés, *consulting firm*, nunca *consultancy*, *consultant* ni *agency*.
- Territorios: Uso 50% · Integración 30% · Hands-on colaborativo 20% ("Trabajamos dentro del problema, junto a tu equipo."), como guía de planificación de contenidos, no por texto.
- Rasgos, en orden: Estratega, Responsable, Curiosa, Franca. En inglés, Responsable es siempre *Accountable*, nunca *responsible*. Convicción sin soberbia, constructiva, clara y honesta. Diales por país: orientativos.
- Se escribe **AI** en cualquier idioma. Única excepción: el nombre propio **IA en Campo**.
- Vocabulario vetado (obligatorio): agtech, digital (solo), transformación digital, custom, software factory, dev shop, agencia, tecnología (sola), ayudar, adopción como sinónimo de uso, DIPI, building blocks, usar lo que ya tenés; en inglés también transform, help/helping, end-to-end, innovative solutions, disruption. Reemplazos en `vocabulary.json`. "Uso" antes que "adopción".
- En inglés, nativo y nunca traducido: serial comma, US spelling, títulos en sentence case, sin "the space" para el sector, sin leverage, seamless, cutting-edge, world-class, robust, unlock, empower ni holistic, sin em dashes.
- Instrucciones para agentes de AI (playbook): identificá objetivo, audiencia, canal, idioma, fuente y confidencialidad; si falta algo indispensable, preguntá. No inventes hechos, cifras, resultados, citas, clientes, fechas ni experiencias. Diferenciá hecho validado, interpretación, hipótesis y ejemplo. Si las fuentes o reglas chocan, señalalo; no lo resuelvas en silencio. Con decisiones, riesgos o cifras relevantes, entregá un borrador pendiente de revisión. Confirmá que los números variables estén actualizados. Clientes: ni nombrados ni identificables, tampoco por descarte, sin autorización expresa.
- Pruebas, no adjetivos. Idioma: el del brief; el inglés es el principal de web, LinkedIn e Instagram.
- Detalle: https://brand.magoya.com/BRAND.md (§1) · https://brand.magoya.com/vocabulary.json · checklist de texto: https://brand.magoya.com/.ai/checklist-verbal.md
