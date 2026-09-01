# Checklist de validación — piezas, código o copy generados por IA

Diecisiete chequeos verificables. Todos tienen que dar **sí** antes de publicar. Si alguno falla, corregí y volvé a correr la lista completa.

> **Quién manda cuando dos reglas se contradicen.** La plantilla oficial gana: es una pieza real que ya funcionó. Si un chequeo de esta lista contradice a una plantilla de `ai/templates/`, el que está mal es el chequeo — reportalo, no adaptes la plantilla. El orden completo está en `ai/precedencia.json`.

| # | Chequeo | Cómo se verifica | Falla si… |
|---|---|---|---|
| 1 | **Solo hex de la paleta** | Extraé todos los colores de la pieza o del CSS y comparalos contra `tokens.json` | Aparece un hex que no está en `tokens.json` (típico: un verde "parecido", `#4CAF50`, `#2ECC71`) |
| 2 | **Cero naranja y cero amarillo** | Buscá cualquier tono con hue 20–65° | Hay naranja o amarillo del brand viejo. Excepción única: `#FFC67B`, y solo como piel de personaje |
| 3 | **Lima no es texto sobre claro** | Buscá `#A2FF00` aplicado a `color:` sobre blanco, sage, crema o papel | Hay texto lima sobre fondo claro (1.25:1). Sobre claro el verde-texto es `#009145` y solo ≥24px bold |
| 4 | **`#00DE68` como texto solo sobre oscuro** | Revisá cada uso de `#00DE68` en `color:` | Se usa como texto sobre blanco o crema en vez de `#009145` |
| 5 | **Como máximo un golpe de lima** | Contá los elementos en lima: CTA, display, motivo, ícono destacado, marca a mano. Automatizable: contar `A2FF00` por slide | Hay **dos o más** elementos lima compitiendo en la misma pieza. Cero lima es válido: 19 de las 41 plantillas oficiales no llevan lima, y el acento es un techo, no una cuota |
| 6 | **Balance 75/25** | Estimá superficie: neutros (blanco/sage/negro/crema) vs. verdes | Los verdes pasan de ~25%, o la pieza es 100% negra o 100% verde |
| 7 | **Manrope, y la jerarquía declarada** | Revisá `font-family`. Para slides, contá los `font-size` únicos y compará contra el techo del catálogo (7). Para piezas nuevas de redes o web, el techo sigue siendo 3 | Aparece otra tipografía (Inter, Poppins, system-ui suelto). O una slide pasa los 7 niveles. O una pieza nueva que no viene de plantilla pasa los 3. **Nota:** las plantillas oficiales van de 2 a 9 niveles porque cada nivel tiene un rol declarado (kicker, display, bajada, caption, dato, label, pie); el límite de 3 era para piezas escritas a mano |
| 8 | **Cero emojis** | Buscá caracteres emoji en títulos, cuerpo, bullets y labels | Hay cualquier emoji que no sea 👈 👉 👇 apuntando a un CTA, o una bandera de país |
| 9 | **Cero gradientes** | Buscá `gradient`, `blur`, `box-shadow` de brillo, glass, 3D | Hay algún gradiente que no sea el scrim verde profundo 55–86% sobre foto aérea |
| 10 | **Máximo 2 recursos gráficos** | Contá: foto aérea, foto B&N, personaje, paño de semicírculos, marca a mano, ícono. La cifra gigante y la tipografía no cuentan — son la voz | Hay 3 o más además de la tipografía, o convive un par prohibido: dos fotos, foto + personaje, foto aérea + paño, personaje + ícono (matriz completa en `resourceCoexistence` de `tokens.json`) |
| 11 | **Motivo al corte** | Mirá los bordes del paño de semicírculos | El motivo se ve cortado flotando en el aire en vez de nacer de un borde o de detrás de un objeto. Si convive con un personaje: el paño va al fondo en franja, el personaje al borde opuesto en primer plano, nunca superpuestos |
| 12 | **Personajes sin rostro y al borde** | Mirá cada personaje ilustrado | Tiene rostro, es monoline o stock, está centrado como clipart, flota entero, está sobre una foto, o usa un color fuera de `#00DE68` `#A2FF00` `#DFDFDF` `#FFC67B` `#161616` |
| 13 | **Botón vs. chip, y assets reales** | Revisá radios y logos | Un botón es pill o un chip tiene fondo sólido (botón = rect radio 10px, chip = pill outline), o hay logos de clientes inventados/placeholder, o hay un resaltador sólido detrás de texto |
| 14 | **Chips: solo texto, sin punto** | Mirá cada chip/pill de la pieza | Un chip lleva un punto/bullet (•) delante del texto, un ícono adentro, o texto en sentence case — el chip es SOLO texto uppercase; la pill ya delimita, el punto es ruido |
| 15 | **Espaciado en escala y un eje** | Extraé los margin/padding/gap y compará contra la escala base-4 de `tokens.json`; mirá el eje de alineación | Hay valores fuera de la escala (5, 10, 14, 18…), bloques a menos de 24 de aire entre sí, más de un eje de alineación en la pieza, filas cuyos elementos no comparten centro vertical, o paddings con 4 valores distintos |
| 16 | **IA, no AI** | Buscá `AI` como palabra suelta en todo el copy | Una pieza en español escribe "AI" (AI en campo, Integrar con AI, capacidades de AI) en vez de **IA**. Solo se admite "AI" en copy en inglés y en nombres propios ajenos ("Data & AI", "AI Studio") |
| 17 | **Wordmark: variante, tamaño, posición y letterforms** | Comparalo contra la plantilla: variante correcta (interiores **black**, portada y cierre **cream**), 211px de ancho, x=7.5% e y=3.2% **del ancho** del lienzo (144 y 61px sobre 1920). Y comparalo contra el asset canónico de `assets/`, no contra el nombre del archivo | La variante no corresponde al lienzo (deep en un interior), el tamaño no es 211px, la posición se midió contra el alto en vez del ancho, o las letterforms no son las del asset canónico. **Una pieza real pasó los 16 chequeos con el wordmark en variante, tamaño y posición equivocados: es el único elemento que el manual llama "LA firma de la marca" y era el único sin auditoría** |
## Extras según el formato

- **Slides**: margen interior 7% del ancho, escala 126/84/56/42pt sobre 1920px, como máximo un golpe de lima por slide (ver chequeo 5), y el lienzo que traiga la plantilla: blanco, sage `#EEF2EC`, verde profundo o foto.
- **Redes**: display y cifras al ~70% del ancho. Story 1080×1920 con zona segura de 96px arriba y abajo. Feed 1080×1080.
- **Logo**: mínimo 90px en pantalla / 24mm impreso; por debajo va el avatar "m". Clearspace = altura de la letra "m". Nunca estirado, rotado, sombreado ni en lima.
- **Copy**: sin superlativos ni frases grandilocuentes; labels de botón en sentence case; kickers en MAYÚSCULAS con tracking +0.12em.
- **Merch**: siempre foto o render real del producto, nunca ilustración ni esquema vectorial. Sin lima en textil.
- **Fotos de personas**: siempre B&N con un acento verde o lima.

## Si la pieza es de "IA en campo"

Es una **marca anexa con manual propio** (`ai-en-campo.html`), no el core. Ahí sí valen el lienzo verde digital `#00DE68` pleno, la placa negra de dato clave y los doodles del Studio (2–4 por pieza, ±5–15°). Nada de eso es válido en una pieza de Magoya core, y nada del core aplica tal cual a "IA en campo".
