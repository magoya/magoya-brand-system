# Magoya Brand — entrada para GitHub Copilot

**Versión 1.1 · 2026-08-31** · Punto de entrada de la marca Magoya para Copilot. Se versiona por separado de las otras AIs (changelog al pie).

## Flujo (en este orden)

1. **Instrucciones del repo**: guardá [copilot-instructions.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/presets/copilot-instructions.md) como `.github/copilot-instructions.md` en el proyecto donde trabajás. Si el repo ya tiene un `AGENTS.md` (Copilot lo lee desde agosto de 2025, igual que `CLAUDE.md`), pegá el preset ahí y no dupliques: un solo archivo de instrucciones, el que ya exista.
2. **Tokens en el código**: bajá https://brand.magoya.com/tokens.css al proyecto — Copilot autocompleta con las custom properties que ve en el árbol.
3. **Doctrina completa**: https://brand.magoya.com/BRAND.md (Copilot Chat puede leerla si se la pegás o si está en el workspace).
4. **Assets**: https://brand.magoya.com/ai/assets.json — bajá al repo los SVGs que la UI necesite.

## Qué podés hacer al pie de la letra (hoy)

- **Autocompletado on-brand**: depende de que tokens.css y los assets estén EN el workspace — Copilot no navega URLs por sí solo. Poner una URL en el archivo de instrucciones **no** la hace leer: el texto entra al contexto, el link no se sigue. Por eso el flujo acá es "bajar al repo" en vez de "fetch en vivo", y es la diferencia con la entrada de Claude.
- Verificación rápida: pedí un card oscuro en Copilot Chat — tiene que salir `#133825` o `#161616`, sin gradiente.

## Changelog

- **1.1** (2026-08-31): `AGENTS.md` como ubicación alternativa del preset (Copilot lo soporta junto a `copilot-instructions.md` y `CLAUDE.md`) + queda dicho explícito que una URL escrita en el archivo de instrucciones no se fetchea sola, que es el error más caro de este flujo.

- **1.0** (2026-08-10): primera versión.
