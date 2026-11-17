# Magoya Brand — índice para AI

**El punto de entrada de cualquier AI es el protocolo de consumo:** https://brand.magoya.com/ai/protocolo.md

Define la primera respuesta, la regla de caché, el modo de lectura, qué archivos se leen según la tarea, cómo se consume cada tipo de asset, la instalación por herramienta, las fallas conocidas y el contrato de entrega.

La página para personas es https://brand.magoya.com/ai.html.

## Entradas por herramienta

Cada una agrega lo específico de su herramienta y se versiona por separado.

| AI | Link de entrada |
|---|---|
| ChatGPT (Custom GPT / Projects) | https://brand.magoya.com/ai/chatgpt.md |
| Claude (claude.ai / Claude Code / API) | https://brand.magoya.com/ai/claude.md |
| Gemini (app / AI Studio / Gems) | https://brand.magoya.com/ai/gemini.md |
| Cursor | https://brand.magoya.com/ai/cursor.md |
| GitHub Copilot | https://brand.magoya.com/ai/copilot.md |
| Codex, Gemini CLI y otros agentes de repo | https://brand.magoya.com/.ai/presets/AGENTS.md (preset `AGENTS.md`) |
| Cualquier otra AI con browsing | https://brand.magoya.com/ai/generic.md |

## Cómo se regenera

`python3 ai/generate.py` desde la raíz del repo, después de cualquier cambio de assets o de los documentos que entran en `llms-full.txt`. `python3 ai/validar.py` lo valida.
