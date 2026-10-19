# Magoya Brand — entrada para GitHub Copilot

**Versión 1.3 · 2026-10-19** · Punto de entrada de la marca Magoya para Copilot. Se versiona por separado de las otras AIs (changelog al pie).

## Flujo (en este orden)

1. **Instrucciones del repo**: guardá [copilot-instructions.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/presets/copilot-instructions.md) como `.github/copilot-instructions.md` en el proyecto donde trabajás. Si el repo ya tiene un `AGENTS.md` (Copilot lo lee desde agosto de 2025, igual que `CLAUDE.md`), pegá el preset ahí y no dupliques: un solo archivo de instrucciones, el que ya exista.
2. **Tokens en el código**: bajá https://brand.magoya.com/tokens.css al proyecto — Copilot autocompleta con las custom properties que ve en el árbol.
3. **Doctrina completa**: https://brand.magoya.com/BRAND.md (Copilot Chat puede leerla si se la pegás o si está en el workspace).
4. **Assets**: https://brand.magoya.com/ai/assets.json — bajá al repo los SVGs que la UI necesite.
5. **Copy de la UI**: bajá al repo https://brand.magoya.com/vocabulary.json y [checklist-verbal.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/checklist-verbal.md) — capa verbal del Magoya Brand Playbook (octubre 2026): definición, AI en cualquier idioma (salvo el nombre propio IA en Campo), vocabulario vetado, glosario ES/EN/PT. El preset del punto 1 ya trae lo esencial.

## Qué podés hacer al pie de la letra (hoy)

- **Autocompletado on-brand**: depende de que tokens.css y los assets estén EN el workspace — Copilot no navega URLs por sí solo. Poner una URL en el archivo de instrucciones **no** la hace leer: el texto entra al contexto, el link no se sigue. Por eso el flujo acá es "bajar al repo" en vez de "fetch en vivo", y es la diferencia con la entrada de Claude.
- Verificación rápida: pedí un card oscuro en Copilot Chat — tiene que salir `#133825` o `#161616`, sin gradiente.

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

- **1.3** (2026-10-19): capa verbal del Magoya Brand Playbook (octubre 2026) — vocabulary.json, .ai/checklist-verbal.md y .ai/verbal/ en el flujo y en la lista plana. Se escribe AI, no la sigla en español (salvo IA en Campo).

- **1.2** (2026-09-07): Agent Skills como ubicación soportada (`.github/skills`, `.claude/skills`, `.agents/skills` y las personales), con las superficies donde corren. Todavía no hay skill publicada: el canal sigue siendo el preset.

- **1.1** (2026-08-31): `AGENTS.md` como ubicación alternativa del preset (Copilot lo soporta junto a `copilot-instructions.md` y `CLAUDE.md`) + queda dicho explícito que una URL escrita en el archivo de instrucciones no se fetchea sola, que es el error más caro de este flujo.

- **1.0** (2026-08-10): primera versión.
