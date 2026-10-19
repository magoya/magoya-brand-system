# Magoya Brand — entradas por AI

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
- `vocabulary.json` y `.ai/verbal/` (estrategia, voz, lenguaje, aplicación) — capa verbal del Magoya Brand Playbook (octubre 2026), que prevalece si algo difiere. Páginas: `estrategia.html`, `voz.html`, `lenguaje.html`, `aplicacion.html`.
- `tokens.json` / `tokens.css` — valores exactos con roles.
- `ai/assets.json` — manifiesto de los 247 assets con URL directa y regla de uso (incluye los 58 íconos del sistema como SVGs individuales en `assets/icons/`).
- `ai/slides.json` — los 41 módulos de presentación, machine-readable.
- `ai/metodo.md` — método de trabajo obligatorio: narrativa primero, módulos por criterio, agentes de copy/diseño/crítica.
- `.ai/checklist.md` — 17 chequeos visuales antes de entregar.
- `.ai/checklist-verbal.md` — chequeos de texto, cada uno con la slide del playbook de la que sale.

## Cómo se regenera la capa compartida

`python3 ai/generate.py` desde la raíz del repo — re-exporta los 58 íconos desde `icons.html` y regenera `assets.json` y `slides.json` desde el árbol real. Correrlo después de cualquier cambio de assets o slides.
