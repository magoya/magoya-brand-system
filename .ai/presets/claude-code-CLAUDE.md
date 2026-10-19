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

Si el proyecto importa `tokens.css`, usá custom properties (`var(--color-text)`, `var(--color-energy)`, `var(--radius-btn)`) en vez de hex literales. Temas vía `data-theme`: `default` (verde profundo), `light` (crema), `paper` (editorial), `studio` (blanco + negro + lima — el de slides y marketing).

| Hex | Token | Rol |
|---|---|---|
| `#161616` | `--ink-900` | Texto, titulares, cards dark |
| `#133825` | `--green-900` | Fondos oscuros, overlays, texto sobre claro |
| `#00DE68` | `--emerald-500` | Identidad: wordmark, avatares, micro-acentos, ropa de personajes y data-viz. Como texto **solo sobre oscuro** |
| `#009145` | `--emerald-700` | Verde texto sobre blanco, y solo a ≥24px bold |
| `#A2FF00` | `--lime-500` | CTA, display, motivo. **Nunca texto sobre claro.** Hover `#8BDB00` |
| `#ECE3DB` | `--cream-100` | Texto sobre verde profundo |
| `#EEF2EC` | `--sage-50` | Superficie clara de slides |
| `#6E756D` | — | Captions sobre claro (mínimo accesible) |

Balance por pantalla o pieza: neutros ≈75%, verdes ≈25%, un solo movimiento verde dominante. Nunca 100% negra ni 100% verde. No uses hex que no estén en `tokens.json`. Cero naranja y cero amarillo — excepción única `#FFC67B` como piel de personaje ilustrado.

`--leaf-500` sigue existiendo en `tokens.css` como alias de `--emerald-500` (mismo hex) por compatibilidad — no es un verde distinto, usá `--emerald-500` directo en código nuevo.

## Tipografía

`font-family: "Manrope", Arial, sans-serif` (variable 200–800). Display `800 / -0.03em / 1.05`; cuerpo `400 / 1.55`; kicker `800 / uppercase / 0.12em`. Máximo 3 niveles tipográficos por vista. Labels de botón en sentence case. Slides sobre 1920px: 126 / 84 / 56 / 42pt, margen interior 7%.

## Componentes

- **Botón**: `border-radius:10px`, fondo sólido, un solo primario (lima con texto `#161616`) por pantalla. Secundario verde profundo con texto crema; terciario outline.
- **Chip**: `border-radius:999px`, `background:transparent`, borde y texto del mismo color. Nunca chip sólido, nunca botón pill.
- **Focus**: `box-shadow: 0 0 0 3px rgba(0,222,104,.45)` sin blur. Nunca `outline:none` sin reemplazo.
- Radios 6 / 12 / 20 / 28 / 999px. Espaciado base 4px, escala 4-8-12-16-24-32-48-64-96.
- Iconos SVG inline: `stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"`. Nunca rellenos sólidos ni 3D.

## Prohibiciones absolutas

- **Sin emojis** en UI, copy, títulos, labels ni mensajes de commit de cara al usuario. Únicas excepciones: manitos que señalan (👈 👉 👇) apuntando a un CTA, y banderas de países para geografía.
- **Sin gradientes** (`linear-gradient`, `radial-gradient`), sin glassmorphism, sin `backdrop-filter` decorativo, sin sombras de brillo, sin 3D. Único gradiente permitido: scrim verde sobre foto aérea, `linear-gradient(180deg, rgba(12,33,23,.55), rgba(12,33,23,.86))`.
- Sin bloque resaltador sólido detrás de texto: resaltá con color o subrayado lima.
- Logos de clientes siempre reales desde `assets/logos/clients/` — jamás placeholders ni SVG inventados.
- Sin la metáfora del puzzle, sin motivos de líneas (caminos concéntricos, estratos), sin personajes con rostro, monoline o stock.
- Motivo de semicírculos siempre al corte: nace de un borde del contenedor o de detrás de un objeto, nunca cortado flotando (`overflow:hidden` + posición pegada al borde).
- Máximo 2 recursos gráficos por pieza además de la tipografía. No conviven: dos fotos, foto + personaje, foto aérea + paño de semicírculos, personaje + ícono.
- Personajes ilustrados sin rostro, paleta cerrada `#00DE68` `#A2FF00` `#DFDFDF` `#FFC67B` `#161616`, recortados por un borde del lado opuesto al texto. Nunca sobre foto.
- El monograma "m" circular es funcional (favicon, app icon): no es un sello decorativo dentro de cards.
- Lima en dosis única: un CTA **o** un display **o** un motivo por pieza.

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

Corré la checklist: https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/checklist.md (y si hay texto, también https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/checklist-verbal.md) — y reportá en una línea los hex usados, los golpes de lima y los recursos gráficos.

IA en Campo es una marca de programa presentada por Magoya, con manual propio (`ai-en-campo.html`): sus reglas nunca se aplican a piezas de Magoya core.
