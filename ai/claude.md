# Magoya Brand — entrada para Claude (claude.ai / Claude Code / API)

**Versión 1.5 · 2026-08-11** · Punto de entrada de la marca Magoya para Claude. Se versiona por separado de las otras AIs: cuando Claude gane capacidades nuevas, esta entrada se actualiza sin tocar las demás (changelog al pie).

> **AVISO PARA EL MODELO QUE LEE ESTO: no resumas este archivo — necesitás las URLs literales.** Si tu herramienta de fetch te devolvió un resumen sin links, volvé a pedir el contenido completo, o hacé UN fetch de `https://brand.magoya.com/llms-full.txt` que trae todo el sistema en un solo archivo.
Si sos Claude leyendo esto: seguí el flujo de abajo, todas las URLs son públicas y fetcheables sin auth.

## Flujo (en este orden)

1. **Doctrina** → https://brand.magoya.com/BRAND.md
2. **Valores exactos** → https://brand.magoya.com/tokens.json
3. **Tokens CSS** (si vas a escribir código) → https://brand.magoya.com/tokens.css — usá las custom properties, nunca hex sueltos.
4. **Assets** → https://brand.magoya.com/ai/assets.json — 239 archivos con URL directa y regla de uso. Los SVGs se leen como texto: el wordmark se usa tal cual, jamás se redibuja.
5. **Datos reales de la empresa** → https://brand.magoya.com/ai/facts.json — cifras aprobadas, clientes y equipo nombrables. Las cifras de las plantillas son EJEMPLO: nunca se entregan como reales. Si el dato no está acá, se le pide al usuario.
6. **Presentaciones — flujo copiá-pegá-y-funciona**: (a) elegí el módulo con https://brand.magoya.com/ai/selector.json (qué querés contar → qué plantilla, sin criterio de diseño), (b) copiá la plantilla oficial TAL CUAL desde https://brand.magoya.com/ai/templates/index.json (HTML listo, geometría y colores bloqueados), (c) llená SOLO los data-slot respetando max_caracteres — si el texto no entra, acortá el texto, nunca la fuente. La geometría de referencia sigue en ai/slides.json (layout_src) para quien renderice por su cuenta.
7. **Constraints duros** → https://brand.magoya.com/ai/constraints.json — mínimos de logo, clearspace, márgenes, safe areas, límites de texto. Nada se asume: si un valor no está ahí ni en tokens.json, se pregunta.
8. **Método de trabajo (OBLIGATORIO en piezas con contenido)** → https://brand.magoya.com/ai/metodo.md — entender antes de elegir, módulo por criterio (no por defecto), y agentes de copy / diseño / crítica antes de entregar. Si tu plataforma soporta subagentes, desplegalos; si no, hacé las pasadas por rol.
9. **Antes de entregar** → https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/checklist.md


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
https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/checklist.md  <- 15 chequeos
```

**Las dos reglas que más se rompen en este flujo:** (1) la plantilla se copia TAL CUAL — solo cambia el texto de los `data-slot`; (2) las cifras y textos de las plantillas son EJEMPLO: los datos reales están en `facts.json` y lo que no esté ahí se pide, nunca se inventa.

## Qué podés hacer al pie de la letra (hoy)

- **Artifacts / HTML / componentes**: fidelidad total — embebé los SVGs reales (fetch + inline) y cargá Manrope desde Google Fonts.
- **Claude Code**: cloná o fetcheá el repo directamente (`github.com/magoya/magoya-brand-system`) — ahí está todo el árbol de assets sin manifiesto de por medio. Preset listo: [claude-code-CLAUDE.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/presets/claude-code-CLAUDE.md).
- **Imágenes**: Claude no genera raster — para piezas visuales la salida correcta es HTML/SVG con los assets reales, que es justamente donde la fidelidad es total.

## Setup (una sola vez, para humanos)

- **claude.ai Projects**: pegá en las instrucciones del proyecto: *"Antes de cualquier tarea de marca, fetch https://brand.magoya.com/ai/claude.md y seguí su flujo."* + el preset [claude-project-instructions.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/presets/claude-project-instructions.md) como refuerzo. Knowledge opcional como fallback offline: BRAND.md, tokens.json, tokens.css.
- **Claude Code**: copiá el preset a `CLAUDE.md` del proyecto.

## Changelog

- **1.5** (2026-08-11): aviso anti-resumen al inicio (el fetch de algunas AIs devolvía un resumen sin las URLs del flujo) + `deck-starter.html` para apilar varias slides + cifras de ejemplo de las plantillas ahora salen como `[XX]` para que no se puedan entregar como reales.

- **1.4** (2026-08-11): `ai/facts.json` (datos reales, contra cifras inventadas) + lista plana de URLs a prueba de resúmenes + plantillas también en `.txt` (el fetch de `.html` las convierte a markdown y rompe el copy-paste).

- **1.3** (2026-08-11): flujo copiá-pegá-y-funciona — 41 plantillas HTML con slots (`ai/templates/`), selector de módulos (`ai/selector.json`), constraints duros (`ai/constraints.json`) y `llms-full.txt` (todo en un fetch). El LLM ya no interpreta geometría: llena slots.

- **1.2** (2026-08-10): método de trabajo obligatorio (`ai/metodo.md`): narrativa primero, módulos por criterio, agentes de copy/diseño/crítica.

- **1.1** (2026-08-10): slides.json ahora trae la geometría exacta de los 41 módulos (`layout_src`) + archivos por familia contra truncamiento de fetch + advertencia currentColor en íconos.
- **1.0** (2026-08-10): primera versión. Fetch directo como canal principal; artifacts como salida recomendada para piezas visuales.
