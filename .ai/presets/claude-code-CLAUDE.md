<!--
CÓMO USAR ESTE ARCHIVO — CLAUDE CODE

Opción A (un proyecto): copialo a la raíz del repo como CLAUDE.md.
   Si el repo ya tiene CLAUDE.md, pegá esta sección al final en vez de sobrescribir.
Opción B (todos tus proyectos): copialo a ~/.claude/CLAUDE.md.
Opción C (modular, recomendado en repos grandes): copialo a
   .claude/rules/magoya-brand.md y agregale este frontmatter arriba para que
   cargue solo cuando Claude toca archivos de front:

   ---
   paths:
     - "**/*.{css,scss,html,jsx,tsx,vue,svelte,svg}"
   ---

Si el repo usa AGENTS.md para otras herramientas, dejá el CLAUDE.md con
`@AGENTS.md` en la primera línea y esta sección debajo.

Verificá con /context que aparezca bajo "Memory files".
Estos comentarios HTML se descartan antes de entrar al contexto: no gastan tokens.
-->

# Marca Magoya — reglas de diseño

Magoya es una consultora hands-on en software y AI para empresas del agro. Tagline: **Software and AI for agribusiness**. Todo output visual, de UI o de copy sigue estas reglas.

**Fuente de verdad completa** (leela con WebFetch cuando necesites un detalle que no esté acá):
- Doctrina: https://brand.magoya.com/BRAND.md
- Valores exactos: https://brand.magoya.com/tokens.json
- Custom properties + 4 temas: https://brand.magoya.com/tokens.css
- Índice para modelos: https://brand.magoya.com/llms.txt

Si el brand system está clonado o vendorizado en este repo, usá `tokens.css` y `BRAND.md` locales antes que las URLs.

## Color

Si el proyecto importa `tokens.css`, usá custom properties (`var(--color-text)`, `var(--color-energy)`, `var(--radius-btn)`) en vez de hex literales. Temas vía `data-theme`: `default` (verde profundo), `light` (crema), `paper` (editorial), `studio` (blanco + negro + lima, marketing).

| Hex | Token | Rol |
|---|---|---|
| `#161616` | `--ink-900` | Texto, titulares, cards dark |
| `#133825` | `--green-900` | **Verde Magoya, el verde protagonista.** Fondos oscuros, overlays, texto sobre claro |
| `#00DE68` | `--emerald-500` | Identidad: wordmark, avatares, micro-acentos y data-viz. Como texto **solo sobre oscuro** |
| `#009145` | `--emerald-700` | Verde texto sobre blanco, y solo a ≥24px bold |
| `#A2FF00` | `--lime-500` | Poca superficie: solo acentos, detalles o CTA. **Nunca texto sobre claro.** La frase clave de un titular sobre oscuro va en Verde digital #00DE68. Hover `#8BDB00` |
| `#ECE3DB` | `--cream-100` | Texto sobre verde profundo |
| `#EEF2EC` | `--sage-50` | Superficie clara |
| `#6E756D` | — | Captions sobre claro (mínimo accesible) |

Proporciones de uso entre colores: el Verde Magoya ocupa la mayor superficie y el lima mucha menos; los porcentajes exactos no están definidos. No apliques porcentajes ni inventes una proporción numérica. No uses hex que no estén en `tokens.json`. Cero naranja y cero amarillo.

## Tipografía

`font-family: "Manrope", Arial, sans-serif` (variable 200–800). Display `800 / -0.03em / 1.05`; cuerpo `400 / 1.55`; kicker `800 / uppercase / 0.12em`. Máximo 3 niveles tipográficos por vista. Labels de botón en sentence case.

## Componentes

- **Botón**: CTA = pill de radio 44px en Verde digital o lima, con la flecha en un círculo Verde Magoya (`assets/components/cta.svg`), uno por pieza. Botones secundario (verde profundo) y terciario (outline): rectángulo de radio 10px. Box = radio 12px, cualquier color de la marca menos lima, una sola imagen en el rectángulo claro y el texto sobre el pleno (`assets/components/box.svg`). Chip = pill outline, nunca sólido.
- **Chip**: `border-radius:999px`, `background:transparent`, borde y texto del mismo color. Nunca chip sólido. La única pill sólida es el CTA.
- **Focus**: `box-shadow: 0 0 0 3px rgba(0,222,104,.45)` sin blur. Nunca `outline:none` sin reemplazo.
- Radios 6 / 12 / 20 / 28 / 999px. Espaciado base 4px, escala 4-8-12-16-24-32-48-64-96.
- Iconos SVG inline: `stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"`. Nunca rellenos sólidos ni 3D.

## Prohibiciones absolutas

- **Sin emojis** en UI, copy, títulos, labels ni mensajes de commit de cara al usuario. Únicas excepciones: manitos que señalan (👈 👉 👇) apuntando a un CTA, y banderas de países para geografía.
- **Sin gradientes** (`linear-gradient`, `radial-gradient`), sin glassmorphism, sin `backdrop-filter` decorativo, sin sombras de brillo, sin 3D. Único gradiente permitido: overlay verde profundo sobre foto aérea, `linear-gradient(180deg, rgba(12,33,23,.55), rgba(12,33,23,.86))`.
- Para resaltar en un titular hay dos formas: color (Verde digital #00DE68 sobre fondo oscuro) o el círculo gestual de la miscelánea nueva (`assets/marks/circle1.svg`, `circle2.svg`). Flechas, círculos, X y ✓ (`assets/marks/`): lima para detalles, acentos o resaltar una palabra; Verde digital; o Verde Magoya cuando el fondo contrasta (por ejemplo sobre Verde digital). Nunca subrayado ni bloque resaltador sólido detrás del texto.
- Logos de clientes siempre reales desde `assets/logos/clients/` — jamás placeholders ni SVG inventados.
- Sin la metáfora del puzzle.
- **Sin ilustración**: Magoya no usa ilustración.
- **Fotografía**: aérea de campo en color natural, con overlay verde profundo para fondos con texto, siempre cenital. Personas siempre a color, sin ningún detalle encima (ni barra ni acento verde), mejor en espacios abiertos.
- El monograma "m" circular es funcional (favicon, app icon): no es un sello decorativo dentro de cards.
- Lima en poca superficie: acentos, detalles, CTA o resaltar una palabra con la miscelánea gestual. La frase clave de un titular sobre fondo oscuro va en Verde digital #00DE68.

## Copy

Identidad, posicionamiento, territorios, oferta, espacios y Método Magoya salen del Magoya Brand Playbook (octubre 2026). Voz, estilo, vocabulario y adaptación salen de la Guía editorial V2 (https://brand.magoya.com/.ai/verbal/guia-editorial.md). Cifras, casos y clientes, de `ai/facts.json` con validación humana. Objetivo, audiencia, canal, idioma y CTA, del brief, que no redefine la identidad ni autoriza cifras.
- Definición: consultora hands-on en software y AI para empresas del agro (*hands-on software and AI consulting firm for agribusiness*). Tagline: **Software and AI for agribusiness**. "Tecnología" no reemplaza a "software y AI" en la definición o el tagline.
- Territorios: Uso 50% · Integración 30% · Hands-on 20%, como guía de planificación de contenidos, no por texto.
- Rasgos, en orden: Estratega, Responsable (en inglés *Accountable*), Curiosa, Franca. Convicción sin soberbia, constructiva, clara y honesta. Diales por país: orientativos.
- Se escribe **AI** en cualquier idioma. Única excepción: el nombre propio **IA en Campo**.
- Vocabulario: para definir a Magoya, evitá etiquetas reductoras (software factory, dev shop, agtech como categoría, custom como promesa, transformación digital como definición). No son vetos universales: cada palabra se evalúa por función y contexto (lista en `vocabulary.json`). "Uso" antes que "adopción".
- No inventes hechos, cifras, resultados, citas ni clientes. Distinguí hecho, interpretación, hipótesis y ejemplo ilustrativo. No nombres clientes sin autorización expresa. Con decisiones, riesgos o cifras en juego, entregá un borrador pendiente de revisión. Si las fuentes chocan, señalalo; no lo resuelvas en silencio.
- Pruebas, no adjetivos. Idioma: el del brief; el inglés es el principal de web, LinkedIn e Instagram.
- Detalle: https://brand.magoya.com/.ai/verbal/guia-editorial.md · https://brand.magoya.com/vocabulary.json · checklist de texto: https://brand.magoya.com/.ai/checklist-verbal.md

## Antes de dar por terminada una pieza

Corré la checklist: https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/checklist.md (y si hay texto, también https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/checklist-verbal.md) : reportá en una línea los hex usados, el uso del lima y las fotos.

IA en Campo es una marca de programa presentada por Magoya, con manual propio (`ai-en-campo.html`): sus reglas nunca se aplican a piezas de Magoya core.
