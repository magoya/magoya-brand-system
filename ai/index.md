# Magoya Brand — entradas por AI

**Equipo de Magoya:** el trabajo de marca con AI se hace en el proyecto oficial de Claude **"Magoya · Marca"** (organización de Magoya en claude.ai), con las instrucciones y los archivos ya cargados. Nadie configura su propia herramienta, y las otras herramientas no están soportadas para el trabajo del equipo con la marca. Detalle en https://brand.magoya.com/ai.html. Las entradas de abajo son puntos de lectura para cualquier AI que lea el sistema.

Un link por herramienta. Cada entrada se versiona por separado: cuando una AI gana capacidades, se actualiza SU archivo (con changelog) sin tocar los demás.

| AI | Link de entrada |
|---|---|
| ChatGPT (Custom GPT / Projects) | https://brand.magoya.com/ai/chatgpt.md |
| Claude (claude.ai / Claude Code / API) | https://brand.magoya.com/ai/claude.md |
| Gemini (app / AI Studio / Gems) | https://brand.magoya.com/ai/gemini.md |
| Cursor | https://brand.magoya.com/ai/cursor.md |
| GitHub Copilot | https://brand.magoya.com/ai/copilot.md |
| Cualquier otra AI con browsing | https://brand.magoya.com/ai/generic.md |

## Capa compartida (lo que todas las entradas apuntan)

- `BRAND.md` — doctrina completa: resumen de la capa verbal y la capa visual.
- `.ai/verbal/guia-editorial.md` — Guía editorial V2 ("Manual voz y tono MAGOYA V2", octubre 2026): fuente de la voz, el estilo, el vocabulario y la adaptación editorial. Su Parte II son las instrucciones operativas para agentes de AI (fuentes, generación, validación humana, control antes de entregar).
- `vocabulary.json` y `.ai/verbal/` (estrategia, voz, lenguaje, aplicación) — capa verbal del Magoya Brand Playbook (octubre 2026), fuente de la identidad, el posicionamiento, la oferta, los espacios y el Método Magoya. Páginas: `estrategia.html`, `voz.html`, `lenguaje.html`, `aplicacion.html`.
- `tokens.json` / `tokens.css` — valores exactos con roles.
- `ai/assets.json` — manifiesto de los 202 assets con URL directa y regla de uso (incluye los 58 íconos del sistema como SVGs individuales en `assets/icons/`).
- `ai/facts.json` — datos reales y aprobados de la empresa.
- `ai/metodo.md` — método de trabajo para escribir y revisar contenido: la idea antes del texto, títulos-aserción, pasadas de copy, diseño y crítica.
- `.ai/checklist.md` — chequeos visuales antes de entregar.
- `.ai/checklist-verbal.md` — chequeos de texto: las 8 preguntas del control antes de entregar de la guía editorial (§9) y los chequeos del playbook que siguen vigentes, cada uno con su fuente.

## Cómo se regenera la capa compartida

`python3 ai/generate.py` desde la raíz del repo: re-exporta los 58 íconos desde `icons.html`, regenera `assets.json` desde el árbol real y arma `llms-full.txt`. Correrlo después de cualquier cambio de assets o de los documentos que entran en `llms-full.txt`.
