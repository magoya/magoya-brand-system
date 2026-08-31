# Magoya Brand — entrada para Gemini (gemini.google.com / AI Studio / Gems)

**Versión 1.5 · 2026-08-11** · Punto de entrada de la marca Magoya para Gemini. Se versiona por separado de las otras AIs (changelog al pie).

> **AVISO PARA EL MODELO QUE LEE ESTO: no resumas este archivo — necesitás las URLs literales.** Si tu herramienta de fetch te devolvió un resumen sin links, volvé a pedir el contenido completo, o hacé UN fetch de `https://brand.magoya.com/llms-full.txt` que trae todo el sistema en un solo archivo.
Si sos un modelo leyendo esto: seguí el flujo de abajo, todas las URLs son públicas.

## Flujo (en este orden)

1. **Doctrina** → https://brand.magoya.com/BRAND.md
2. **Valores exactos** → https://brand.magoya.com/tokens.json
3. **Assets** → https://brand.magoya.com/ai/assets.json — 239 archivos con URL directa y regla de uso.
4. **Presentaciones — flujo copiá-pegá-y-funciona**: (a) elegí el módulo con https://brand.magoya.com/ai/selector.json (qué querés contar → qué plantilla, sin criterio de diseño), (b) copiá la plantilla oficial TAL CUAL desde https://brand.magoya.com/ai/templates/index.json (HTML listo, geometría y colores bloqueados), (c) llená SOLO los data-slot respetando max_caracteres — si el texto no entra, acortá el texto, nunca la fuente. La geometría de referencia sigue en ai/slides.json (layout_src) para quien renderice por su cuenta.
5. **Datos reales de la empresa** → https://brand.magoya.com/ai/facts.json — cifras aprobadas, clientes y equipo nombrables. Las cifras de las plantillas son EJEMPLO: nunca se entregan como reales. Si el dato no está acá, se le pide al usuario.
6. **Constraints duros** → https://brand.magoya.com/ai/constraints.json — mínimos de logo, clearspace, márgenes, safe areas, límites de texto. Nada se asume: si un valor no está ahí ni en tokens.json, se pregunta.
7. **Método de trabajo (OBLIGATORIO en piezas con contenido)** → https://brand.magoya.com/ai/templates/index.json  <- ojo el campo "perfil" de cada modulo y "como_componer_el_deck":
                                                     el selector elige QUE contar, el perfil ordena la SECUENCIA
https://brand.magoya.com/ai/precedencia.json  <- quién gana cuando dos reglas chocan + contrato de entrega
https://brand.magoya.com/ai/metodo.md — narrativa primero, módulo por criterio, pasadas de copy / diseño / crítica.
8. **Cuando dos reglas oficiales se contradicen** → https://brand.magoya.com/ai/precedencia.json — la ley de precedencia. Gana la plantilla, después facts.json, después tokens. El `cuando_usarlo` es lo último. Si encontrás una contradicción, aplicá la ley, entregá, y reportala — no la resuelvas por criterio propio.
9. **Antes de entregar** → corré `python3 ai/validar.py --pieza <tu-archivo.html>` si tenés el repo, y en cualquier caso cumplí el contrato de entrega de `precedencia.json`: un dato que no está en `facts.json` va como `[PENDIENTE]`, nunca como el número que te pasaron; con un hueco adentro la pieza sale marcada BORRADOR y con un bloque PEDIDO A HUMANOS.


## URLs del flujo (lista plana — si tu fetch resumió lo de arriba, usá esta)

```
https://brand.magoya.com/llms-full.txt        <- TODO en un solo fetch (empezá acá si dudás)
https://brand.magoya.com/BRAND.md             <- doctrina
https://brand.magoya.com/tokens.json          <- valores exactos
https://brand.magoya.com/ai/facts.json        <- datos REALES de la empresa (cifras, clientes, equipo)
https://brand.magoya.com/ai/selector.json     <- qué querés contar -> qué plantilla
https://brand.magoya.com/ai/templates/index.json  <- las 41 plantillas + slots + max_caracteres
https://brand.magoya.com/ai/templates/<ID>.txt    <- la plantilla como TEXTO PLANO (usá .txt, no .html:
                                                     muchos fetch convierten el .html a markdown y rompen el copy-paste)
https://brand.magoya.com/ai/constraints.json  <- mínimos, clearspace, márgenes, safe areas
https://brand.magoya.com/ai/assets.json       <- los 239 assets con URL directa
https://brand.magoya.com/ai/metodo.md         <- método obligatorio (narrativa + agentes)
https://brand.magoya.com/.ai/checklist.md  <- 16 chequeos
```

**Las dos reglas que más se rompen en este flujo:** (1) la plantilla se copia TAL CUAL — solo cambia el texto de los `data-slot`; (2) las cifras y textos de las plantillas son EJEMPLO: los datos reales están en `facts.json` y lo que no esté ahí se pide, nunca se inventa.

## Qué podés hacer al pie de la letra (hoy)

- **Copy, HTML/CSS, código, SVG**: fidelidad total leyendo los archivos de arriba. Los SVGs son texto — el wordmark se usa tal cual, nunca se redibuja.
- **Con URL context / browsing**: fetcheá los archivos en vivo; no respondas de memoria.
- **Imagen (Imagen/gemini image)**: el generador no puede usar el SVG real ni Manrope — describí paleta y prohibiciones en el prompt y aclarale al usuario que el logo real se superpone después.

## Setup (una sola vez, para humanos)

- **Gem**: creá un Gem "Magoya Brand" con la instrucción: *"Antes de cualquier tarea de marca, leé https://brand.magoya.com/ai/gemini.md y seguí su flujo al pie de la letra. Esos archivos son la única fuente de verdad."*
- **AI Studio / API**: mismo texto como system instruction; si tu integración tiene URL context tool, dale esta URL directamente.

## Changelog

- **1.5** (2026-08-11): aviso anti-resumen al inicio (el fetch de algunas AIs devolvía un resumen sin las URLs del flujo) + `deck-starter.html` para apilar varias slides + cifras de ejemplo de las plantillas ahora salen como `[XX]` para que no se puedan entregar como reales.

- **1.4** (2026-08-11): `ai/facts.json` (datos reales, contra cifras inventadas) + lista plana de URLs a prueba de resúmenes + plantillas también en `.txt` (el fetch de `.html` las convierte a markdown y rompe el copy-paste).

- **1.3** (2026-08-11): plantillas con slots + selector + constraints + llms-full.txt (un solo fetch con todo).

- **1.2** (2026-08-10): método de trabajo obligatorio (`ai/metodo.md`).

- **1.1** (2026-08-10): geometría exacta de slides + archivos por familia + advertencia currentColor.
- **1.0** (2026-08-10): primera versión.
