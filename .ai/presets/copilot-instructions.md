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
- `#133825` verde profundo — fondos oscuros, overlays, texto sobre claro
- `#00DE68` verde digital — identidad (wordmark, avatares, micro-acentos), ropa de personajes y data-viz. Como texto **solo sobre fondo oscuro**
- `#009145` — verde texto sobre blanco, y solo a ≥24px bold
- `#A2FF00` lima — CTA, display, motivo. **Nunca como texto sobre fondo claro.** Hover `#8BDB00`
- `#ECE3DB` crema — texto sobre verde profundo
- `#EEF2EC` sage / `#FFFFFF` — superficies claras
- `#6E756D` — captions sobre claro (mínimo accesible)

Balance por pantalla: neutros ≈75%, verdes ≈25%, un solo movimiento verde dominante. Nunca una vista 100% negra ni 100% verde. No uses colores que no estén en `tokens.json`. Cero naranja, cero amarillo (excepción única: `#FFC67B` como piel de personaje ilustrado).

## Tipografía

`font-family: "Manrope", Arial, sans-serif` — variable 200–800.
Display `font-weight:800; letter-spacing:-0.03em; line-height:1.05`. Cuerpo `400; line-height:1.55`. Kicker `800; uppercase; letter-spacing:0.12em`.
Máximo 3 niveles tipográficos por vista. Labels de botón en sentence case, nunca MAYÚSCULAS.

## Componentes

- **Botón**: `border-radius:10px`, fondo sólido. Un solo primario (lima con texto `#161616`) por pantalla; secundario verde profundo con texto crema; terciario outline.
- **Chip**: `border-radius:999px`, `background:transparent`, borde y texto del mismo color. Nunca chip sólido, nunca botón pill.
- **Focus**: `box-shadow: 0 0 0 3px rgba(0,222,104,.45)` sin blur. No dejes `outline:none` sin reemplazo.
- Radios 6/12/20/28/999px. Espaciado base 4px (4-8-12-16-24-32-48-64-96).
- Iconos SVG inline: `stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"`. Nunca rellenos sólidos ni 3D.

## No hagas

- **Sin emojis** en UI, copy, títulos ni labels. Únicas excepciones: manitos que señalan (👈 👉 👇) apuntando a un CTA, y banderas de países para geografía.
- **Sin gradientes** (`linear-gradient`, `radial-gradient`), sin glassmorphism, sin `backdrop-filter` decorativo, sin sombras de brillo, sin 3D. Único gradiente permitido: scrim verde sobre foto aérea, `linear-gradient(180deg, rgba(12,33,23,.55), rgba(12,33,23,.86))`.
- Sin bloque resaltador sólido detrás de texto — resaltá con color o subrayado lima.
- Sin logos de clientes inventados o placeholder: van los reales de `assets/logos/clients/`, en gris y grilla pareja.
- Sin la metáfora del puzzle, sin motivos de líneas (caminos concéntricos, estratos), sin personajes con rostro, monoline o stock.
- El motivo de semicírculos siempre al corte: nace de un borde del contenedor o de detrás de un objeto, nunca cortado flotando (`overflow:hidden` + posición pegada al borde).
- Máximo 2 recursos gráficos por pieza además de la tipografía; no conviven: dos fotos, foto + personaje, foto aérea + paño de semicírculos, personaje + ícono.
- El monograma "m" circular es funcional (favicon, app icon), no un sello decorativo dentro de cards.

## Copy en UI

La capa verbal sale del Magoya Brand Playbook (octubre 2026), que prevalece si algo difiere.
- Definición: consultora hands-on en software y AI para empresas del agro (*hands-on software and AI consulting firm for agribusiness*). Tagline: **Software and AI for agribusiness**.
- Territorios, por peso en los mensajes: Uso 50% · Integración 30% · Hands-on 20%.
- Rasgos, en orden: Estratega, Responsable (en inglés *Accountable*), Curiosa, Franca.
- Se escribe **AI** en cualquier idioma. Única excepción: el nombre propio **IA en Campo**.
- Vetado: agtech, digital (solo), transformación digital, custom, software factory, dev shop, agencia, tecnología (sola), ayudar, adopción como sinónimo de uso, DIPI, building blocks. "Uso" antes que "adopción".
- Pruebas, no adjetivos. Frases cortas y concretas. El inglés es el idioma principal de web, LinkedIn e Instagram.
- Detalle: https://brand.magoya.com/vocabulary.json · https://brand.magoya.com/.ai/verbal/lenguaje.md · checklist de texto: https://brand.magoya.com/.ai/checklist-verbal.md
