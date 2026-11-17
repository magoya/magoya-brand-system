# Magoya Brand — entrada para GitHub Copilot

> **La marca de Magoya se consume desde cualquier AI.** Esta es una de las entradas y todas leen la misma fuente. El protocolo común (primera respuesta, modo de lectura, assets, instalación, fallas conocidas, contrato de entrega) es https://brand.magoya.com/ai/protocolo.md

> **Si sos una AI:** decile a la persona qué versión y qué fecha de esta entrada leíste. Algunos fetch devuelven una copia vieja guardada en caché: si no es la última del changelog publicado, pedí esta misma URL agregándole `?v=` y la fecha de hoy.

**Versión 1.6 · 2026-11-17** · Punto de entrada de la marca Magoya para Copilot. Se versiona por separado de las otras AIs (changelog al pie).

## Flujo (en este orden)

1. **Instrucciones del repo**: guardá [copilot-instructions.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/presets/copilot-instructions.md) como `.github/copilot-instructions.md` en el proyecto donde trabajás. Si el repo ya tiene un `AGENTS.md` (Copilot lo lee desde agosto de 2025, igual que `CLAUDE.md`), pegá el preset ahí y no dupliques: un solo archivo de instrucciones, el que ya exista.
2. **Tokens en el código**: bajá https://brand.magoya.com/tokens.css al proyecto — Copilot autocompleta con las custom properties que ve en el árbol.
3. **Doctrina completa**: https://brand.magoya.com/BRAND.md (Copilot Chat puede leerla si se la pegás o si está en el workspace).
4. **Assets**: https://brand.magoya.com/ai/assets.json — bajá al repo los SVGs que la UI necesite. Si solo podés pegar texto, el código de cada vector propio está en https://brand.magoya.com/ai/vectores.md.
5. **Copy de la UI**: bajá al repo [guia-editorial.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/verbal/guia-editorial.md), https://brand.magoya.com/vocabulary.json y [checklist-verbal.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/checklist-verbal.md) — la voz y el vocabulario salen de la Guía editorial V2 (sin cifras ni clientes inventados); la definición, el vocabulario vetado (obligatorio), AI en cualquier idioma (salvo el nombre propio IA en Campo) y el glosario ES/EN/PT, del Magoya Brand Voice Playbook (octubre de 2026). Copy en inglés: edición en inglés del playbook, https://brand.magoya.com/en/ (se escribe nativo, nunca traducido). El preset del punto 1 ya trae lo esencial.

## Qué podés hacer al pie de la letra (hoy)

- **Autocompletado on-brand**: depende de que tokens.css y los assets estén EN el workspace — Copilot no navega URLs por sí solo. Poner una URL en el archivo de instrucciones **no** la hace leer: el texto entra al contexto, el link no se sigue. Por eso el flujo acá es "bajar al repo" en vez de "fetch en vivo", y es la diferencia con la entrada de Claude.
- Verificación rápida: pedí un card oscuro en Copilot Chat — tiene que salir `#133825` o `#161616`, sin gradiente.
- **`AGENTS.md`**: si el repo ya trabaja con ese archivo (lo leen Codex, Cursor, Copilot, Gemini CLI y otros agentes), el preset es https://brand.magoya.com/.ai/presets/AGENTS.md

## Agent Skills (verificado 2026-09-07)

Copilot lee **skills** —carpetas con instrucciones, scripts y recursos— desde `.github/skills`,
`.claude/skills` o `.agents/skills` del repo, y desde `~/.copilot/skills` o `~/.agents/skills` para
las personales ([docs](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)).
Funcionan en el agente en la nube, en code review, en la CLI, en la app y en modo agente de VS Code
y de los IDEs de JetBrains.

Sirve para lo mismo que el preset de instrucciones, pero cargado por etapas en vez de entero. **Hoy
Magoya no publica una skill**: el canal sigue siendo el preset de instrucciones del punto 1. Y vale
la advertencia de siempre: una URL escrita en un archivo de instrucciones **no se fetchea sola**.

## Changelog

- **1.6** (2026-11-17): la marca se consume desde cualquier AI: se retira «el proyecto de Claude es el único camino». Los vectores propios (wordmark, avatares, miscelánea, íconos) pasan a leerse como texto en `ai/vectores.md`, porque un `.svg` pedido por URL no le llega a una AI, y cada foto tiene su ficha en `ai/assets.json`. La entrada pide informar la versión leída: hay fetch que devuelven copias viejas.

- **1.5** (2026-10-29): Magoya Brand Voice Playbook (octubre de 2026, ediciones en español y en inglés): el vocabulario vetado pasa a obligatorio, como lo marca el playbook (la contradicción con la Guía V2 queda como nota para mantenedores en `precedencia.json`), y se suma la edición en inglés del sitio (https://brand.magoya.com/en/) para el copy en inglés.

- **1.4** (2026-10-19): Guía editorial V2 ("Manual voz y tono MAGOYA V2") como fuente de la voz y el tono: .ai/verbal/guia-editorial.md en el flujo y en la lista plana, con sus reglas operativas (sin cifras inventadas, validación humana, clientes no nombrados por defecto, borrador pendiente de revisión, conflictos señalados). El checklist verbal se rearma sobre sus 8 preguntas.

- **1.3** (2026-10-19): capa verbal del Magoya Brand Playbook (octubre 2026) — vocabulary.json, .ai/checklist-verbal.md y .ai/verbal/ en el flujo y en la lista plana. Se escribe AI, no la sigla en español (salvo IA en Campo).

- **1.2** (2026-09-07): Agent Skills como ubicación soportada (`.github/skills`, `.claude/skills`, `.agents/skills` y las personales), con las superficies donde corren. Todavía no hay skill publicada: el canal sigue siendo el preset.

- **1.1** (2026-08-31): `AGENTS.md` como ubicación alternativa del preset (Copilot lo soporta junto a `copilot-instructions.md` y `CLAUDE.md`) + queda dicho explícito que una URL escrita en el archivo de instrucciones no se fetchea sola, que es el error más caro de este flujo.

- **1.0** (2026-08-10): primera versión.
