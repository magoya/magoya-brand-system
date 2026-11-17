# Magoya Brand — entrada para Cursor

> **La marca de Magoya se consume desde cualquier AI.** Esta es una de las entradas y todas leen la misma fuente. El protocolo común (primera respuesta, modo de lectura, assets, instalación, fallas conocidas, contrato de entrega) es https://brand.magoya.com/ai/protocolo.md

> **Si sos una AI:** decile a la persona qué versión y qué fecha de esta entrada leíste. Algunos fetch devuelven una copia vieja guardada en caché: si no es la última del changelog publicado, pedí esta misma URL agregándole `?v=` y la fecha de hoy.

**Versión 1.4 · 2026-11-17** · Punto de entrada de la marca Magoya para Cursor. Se versiona por separado de las otras AIs (changelog al pie).

## Flujo (en este orden)

1. **Regla del proyecto**: guardá [cursor-rule.mdc](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/presets/cursor-rule.mdc) como `.cursor/rules/magoya-brand.mdc` — es la doctrina condensada que el agente aplica en cada edición.
2. **Tokens en el código**: bajá https://brand.magoya.com/tokens.css al proyecto y usá SIEMPRE las custom properties (`var(--color-energy)`), nunca hex sueltos.
3. **Doctrina completa** (cuando el agente necesite contexto): https://brand.magoya.com/BRAND.md
4. **Assets** → https://brand.magoya.com/ai/assets.json — URL directa de cada SVG/foto para embeber o bajar al repo. Los vectores propios también están como texto en https://brand.magoya.com/ai/vectores.md, por si el agente no puede abrir un `.svg` por URL.
5. **Antes de mergear UI nueva** → https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/checklist.md
6. **Copy de la UI** → https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/verbal/guia-editorial.md, https://brand.magoya.com/vocabulary.json y https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/checklist-verbal.md — la voz y el vocabulario salen de la Guía editorial V2 (sin cifras ni clientes inventados); la definición, el vocabulario vetado (obligatorio), AI en cualquier idioma (salvo el nombre propio IA en Campo) y el glosario ES/EN/PT, del Magoya Brand Voice Playbook (octubre de 2026). Copy en inglés: edición en inglés del playbook, https://brand.magoya.com/en/ (se escribe nativo, nunca traducido).

## Qué podés hacer al pie de la letra (hoy)

- **Componentes y páginas**: fidelidad total — tokens.css + SVGs reales del manifiesto. Verificación rápida: un card oscuro tiene que salir `#133825` o `#161616`, sin gradientes.
- El agente de Cursor puede fetchear las URLs de arriba en vivo (@web o fetch del agente) — preferí eso a copiar valores a mano.
- **`AGENTS.md`**: si el repo ya trabaja con ese archivo (lo leen Codex, Cursor, Copilot, Gemini CLI y otros agentes), el preset es https://brand.magoya.com/.ai/presets/AGENTS.md

## Changelog

- **1.4** (2026-11-17): la marca se consume desde cualquier AI: se retira «el proyecto de Claude es el único camino». Los vectores propios (wordmark, avatares, miscelánea, íconos) pasan a leerse como texto en `ai/vectores.md`, porque un `.svg` pedido por URL no le llega a una AI, y cada foto tiene su ficha en `ai/assets.json`. La entrada pide informar la versión leída: hay fetch que devuelven copias viejas.

- **1.3** (2026-10-29): Magoya Brand Voice Playbook (octubre de 2026, ediciones en español y en inglés): el vocabulario vetado pasa a obligatorio, como lo marca el playbook (la contradicción con la Guía V2 queda como nota para mantenedores en `precedencia.json`), y se suma la edición en inglés del sitio (https://brand.magoya.com/en/) para el copy en inglés.

- **1.2** (2026-10-19): Guía editorial V2 ("Manual voz y tono MAGOYA V2") como fuente de la voz y el tono: .ai/verbal/guia-editorial.md en el flujo y en la lista plana, con sus reglas operativas (sin cifras inventadas, validación humana, clientes no nombrados por defecto, borrador pendiente de revisión, conflictos señalados). El checklist verbal se rearma sobre sus 8 preguntas.

- **1.1** (2026-10-19): capa verbal del Magoya Brand Playbook (octubre 2026) — vocabulary.json, .ai/checklist-verbal.md y .ai/verbal/ en el flujo y en la lista plana. Se escribe AI, no la sigla en español (salvo IA en Campo).

- **1.0** (2026-08-10): primera versión.
