# Checklist de validación visual: piezas, código o copy generados por AI

Diecisiete chequeos verificables. Todos tienen que dar **sí** antes de publicar. Si alguno falla, corregí y volvé a correr la lista completa. **Si hay texto, corré también `.ai/checklist-verbal.md`** (capa verbal del Brand Playbook y la Guía editorial V2, oct 2026).

> **Quién manda cuando dos reglas se contradicen.** Si un chequeo de esta lista contradice a `tokens.json` o a `BRAND.md`, el que está mal es el chequeo: reportalo, no fuerces la pieza. El orden completo está en `ai/precedencia.json`.

| # | Chequeo | Cómo se verifica | Falla si… |
|---|---|---|---|
| 1 | **Solo hex de la paleta** | Extraé todos los colores de la pieza o del CSS y comparalos contra `tokens.json` | Aparece un hex que no está en `tokens.json` (típico: un verde "parecido", `#4CAF50`, `#2ECC71`) |
| 2 | **Cero naranja y cero amarillo** | Buscá cualquier tono con hue 20–65° **y saturación > 40%**. El piso de saturación no es opcional: sin él, colores oficiales de `tokens.json` caen en el rango (`#ECE3DB` 28°, `#DCD0C4` 30°, `#C4B5A6` 30°, `#F6F1EB` 33°, `#F1EDE7` 36°, `#E0A33A` 38°, `#E6E1D8` 39°) y toda la familia crema de la marca da "naranja". Es el mismo calificador que usa `ai/validar.py` | Hay naranja o amarillo del brand viejo: hue 20–65° **con saturación alta** |
| 3 | **Lima no es texto sobre claro** | Buscá `#A2FF00` aplicado a `color:` sobre blanco, sage, crema o papel | Hay texto lima sobre fondo claro (1.25:1). Sobre claro el verde-texto es `#009145` y solo ≥24px bold |
| 4 | **`#00DE68` como texto solo sobre oscuro** | Revisá cada uso de `#00DE68` en `color:` | Se usa como texto sobre blanco o crema en vez de `#009145` |
| 5 | **Lima solo como acento** | Mirá cada elemento en lima | El lima se usa para algo que no es un acento, un detalle, un resaltado o un CTA, o cubre una superficie grande (por ejemplo un box) |
| 6 | **Verde Magoya protagonista** | Mirá qué verde manda en la pieza | El verde protagonista no es el Verde Magoya `#133825`. Las proporciones de uso entre colores están pendientes de definir: este chequeo no mide porcentajes |
| 7 | **Manrope y tres niveles** | Revisá `font-family` y contá los niveles tipográficos | Aparece otra tipografía (Inter, Poppins, system-ui suelto), o la pieza pasa los 3 niveles tipográficos |
| 8 | **Cero emojis** | Buscá caracteres emoji en títulos, cuerpo, bullets y labels | Hay cualquier emoji que no sea 👈 👉 👇 apuntando a un CTA, o una bandera de país |
| 9 | **Cero gradientes** | Buscá `gradient`, `blur`, `box-shadow` de brillo, glass, 3D sobre elementos de la pieza | Hay algún gradiente que no sea el overlay verde profundo 55–86% sobre foto aérea, o una sombra de brillo sobre un elemento de la pieza |
| 10 | **Fotografía aérea** | Mirá cada foto de campo | No es cenital, no está en color natural, o lleva texto encima sin el overlay verde profundo |
| 11 | **Fotografía de personas** | Mirá cada foto de personas | Está en blanco y negro, o lleva un detalle encima (barra, acento verde, overlay). Las personas van siempre a color y, mejor, en espacios abiertos |
| 12 | **Sin ilustración** | Mirá los recursos gráficos de la pieza | Hay ilustración: Magoya no la usa |
| 13 | **Resaltar con círculo o flechas** | Mirá cómo se destaca cada palabra o dato | Una palabra se resalta con subrayado o con un bloque resaltador sólido detrás. Vale el color (Verde digital #00DE68 sobre oscuro) o el círculo gestual nuevo (`assets/marks/`); flechas, círculos, X y ✓ en lima, Verde digital o Verde Magoya según el fondo |
| 14 | **Botón vs. chip, y logos reales** | Revisá radios y logos | Un botón secundario es pill, un CTA no es pill Verde digital o lima de radio 44px, un box es lima, o un chip tiene fondo sólido, o hay logos de clientes inventados o placeholder |
| 15 | **Chips: solo texto, sin punto** | Mirá cada chip/pill de la pieza | Un chip lleva un punto/bullet (•) delante del texto, un ícono adentro, o texto en sentence case: el chip es SOLO texto uppercase; la pill ya delimita, el punto es ruido |
| 16 | **Espaciado en escala y un eje** | Extraé los margin/padding/gap y compará contra la escala base-4 de `tokens.json`; mirá el eje de alineación | Hay valores fuera de la escala (5, 10, 14, 18…), bloques a menos de 24 de aire entre sí, más de un eje de alineación, filas cuyos elementos no comparten centro vertical, o paddings con 4 valores distintos |
| 17 | **AI, en cualquier idioma** | Buscá la sigla de inteligencia artificial en todo el copy. La regla verbal completa está en `.ai/checklist-verbal.md` (chequeo 2) | El copy no escribe **AI** para nombrar la inteligencia artificial, en cualquier idioma del texto. Única excepción: el nombre propio **IA en Campo**, que se escribe siempre así (nunca "AI en Campo"). Regla del Brand Playbook, oct 2026, slide 50 |

## Extras según el formato

- **Logo**: el wordmark sale del asset canónico de `assets/`, nunca redibujado, en la variante que corresponde al fondo (cream sobre oscuro; green, black o deep sobre claro, ver `BRAND.md` §2). Mínimo 90px en pantalla / 24mm impreso; por debajo va el avatar "m". Clearspace = altura de la letra "m". Nunca estirado, rotado, sombreado ni en lima.
- **Copy**: labels de botón en sentence case; kickers en MAYÚSCULAS con tracking +0.12em. Todo lo demás del texto (definición, vocabulario de marca, frases prohibidas, AI, datos validados, clientes con permiso) se valida con `.ai/checklist-verbal.md`.

## Si la pieza es de "IA en Campo"

Es una **marca de programa presentada por Magoya, con manual propio** (`ai-en-campo.html`), no el core. Ahí sí valen el lienzo verde digital `#00DE68` pleno, la placa negra de dato clave y los doodles del Studio (2–4 por pieza, ±5–15°). Nada de eso es válido en una pieza de Magoya core, y nada del core aplica tal cual a IA en Campo.
