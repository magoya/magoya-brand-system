# Magoya Brand — entrada para Claude (claude.ai / Claude Code / API)

**Versión 1.8 · 2026-10-19** · Punto de entrada de la marca Magoya para Claude. Se versiona por separado de las otras AIs: cuando Claude gane capacidades nuevas, esta entrada se actualiza sin tocar las demás (changelog al pie).

> **AVISO PARA EL MODELO QUE LEE ESTO: no resumas este archivo — necesitás las URLs literales.** Si tu herramienta de fetch te devolvió un resumen sin links, volvé a pedir el contenido completo, o hacé UN fetch de `https://brand.magoya.com/llms-full.txt` que trae todo el sistema en un solo archivo.
Si sos Claude leyendo esto: seguí el flujo de abajo, todas las URLs son públicas y fetcheables sin auth.

## Flujo (en este orden)

0. **¿Necesitás un deck? Mirá primero si ya está armado** → https://brand.magoya.com/ai/decks/index.json
   Hay tres decks COMPLETOS y validados: **credenciales** (primer contacto), **propuesta-piloto**
   (con escenarios e inversión) y **cierre-de-proyecto** (resultados para el sponsor). La secuencia,
   los lienzos y el arco ya están resueltos: **no hay que elegir módulos ni componer nada.** Bajás el
   .html, cambiás el texto que está entre corchetes, y listo. Cada corchete dice qué va ahí y cuántos
   caracteres entran. Los `[XX]` son datos que hay que PEDIR, no completar.
   Usá los 41 módulos de abajo **solo si el deck que necesitás no es ninguno de esos tres.**

1. **Doctrina** → https://brand.magoya.com/BRAND.md
   **Texto** (si la pieza lleva copy) → https://brand.magoya.com/.ai/verbal/guia-editorial.md, https://brand.magoya.com/vocabulary.json y https://brand.magoya.com/.ai/checklist-verbal.md. La identidad, los territorios, la oferta, los espacios y el Método Magoya salen del Magoya Brand Playbook (octubre 2026): Magoya es una consultora hands-on en software y AI para empresas del agro; se escribe AI en cualquier idioma (única excepción: el nombre propio IA en Campo). La voz, el estilo y el vocabulario salen de la Guía editorial V2, cuya Parte II son instrucciones operativas para agentes de AI: no inventar hechos ni cifras (toda métrica real la valida alguien del equipo), no nombrar clientes por defecto, distinguir hecho, interpretación, hipótesis y ejemplo, entregar como borrador pendiente de revisión cuando hay decisiones, riesgos o cifras, y señalar los conflictos entre fuentes en vez de resolverlos. El vocabulario a evitar no es un veto universal y el 50/30/20 planifica contenidos, no se chequea por texto. Detalle en https://brand.magoya.com/.ai/verbal/ (guia-editorial.md, estrategia.md, voz.md, lenguaje.md, aplicacion.md).
2. **Valores exactos** → https://brand.magoya.com/tokens.json
3. **Tokens CSS** (si vas a escribir código) → https://brand.magoya.com/tokens.css — usá las custom properties, nunca hex sueltos.
4. **Assets** → https://brand.magoya.com/ai/assets.json — 239 archivos con URL directa y regla de uso. Los SVGs se leen como texto: el wordmark se usa tal cual, jamás se redibuja.
5. **Datos reales de la empresa** → https://brand.magoya.com/ai/facts.json — cifras aprobadas y equipo nombrable. Los clientes se nombran solo con autorización expresa (guía editorial V2, §8); si no está registrada, va a PEDIDO A HUMANOS. Las cifras de las plantillas son EJEMPLO: nunca se entregan como reales. Si el dato no está acá, se le pide al usuario, y toda cifra real la valida una persona del equipo (contrato en `validacion`). Los clientes no se nombran sin autorización expresa.
6. **Presentaciones — flujo copiá-pegá-y-funciona**: (a) elegí el módulo con https://brand.magoya.com/ai/selector.json (qué querés contar → qué plantilla, sin criterio de diseño), (b) copiá la plantilla oficial TAL CUAL desde https://brand.magoya.com/ai/templates/index.json (HTML listo, geometría y colores bloqueados), (c) llená SOLO los data-slot respetando max_caracteres — si el texto no entra, acortá el texto, nunca la fuente. La geometría de referencia sigue en ai/slides.json (layout_src) para quien renderice por su cuenta.
7. **Constraints duros** → https://brand.magoya.com/ai/constraints.json — mínimos de logo, clearspace, márgenes, safe areas, límites de texto. Nada se asume: si un valor no está ahí ni en tokens.json, se pregunta.
8. **Método de trabajo (OBLIGATORIO en piezas con contenido)** → https://brand.magoya.com/ai/metodo.md — el ghost deck antes de elegir módulos, el módulo por criterio y no por defecto, y las pasadas de títulos / copy / diseño / crítica antes de entregar. Si tu plataforma soporta subagentes, desplegalos; si no, hacé las pasadas por rol.
   La SECUENCIA del deck se gobierna con el campo `perfil.beat` de cada módulo y las cuatro reglas de `como_componer_el_deck`, los dos en https://brand.magoya.com/ai/templates/index.json — el selector elige QUÉ contar, el beat ordena en qué orden.
9. **Cuando dos reglas oficiales se contradicen** → https://brand.magoya.com/ai/precedencia.json — la ley de precedencia. Gana la plantilla, después facts.json, después tokens. El `cuando_usarlo` es lo último. Si encontrás una contradicción, aplicá la ley, entregá, y reportala — no la resuelvas por criterio propio.
10. **Antes de entregar** → corré `python3 ai/validar.py --pieza <tu-archivo.html>` si tenés el repo, y en cualquier caso cumplí el contrato de entrega de `precedencia.json`: un dato que no está en `facts.json` va como `[PENDIENTE]`, nunca como el número que te pasaron; con un hueco adentro la pieza sale marcada BORRADOR y con un bloque PEDIDO A HUMANOS.


## URLs del flujo (lista plana — si tu fetch resumió lo de arriba, usá esta)

```
https://brand.magoya.com/ai/decks/index.json  <- TRES DECKS YA ARMADOS: empezá acá si es un deck
https://brand.magoya.com/llms-full.txt        <- casi todo en un solo fetch (voz.md y lenguaje.md van aparte)
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
https://brand.magoya.com/.ai/checklist.md  <- 17 chequeos
https://brand.magoya.com/.ai/verbal/guia-editorial.md <- voz y tono + instrucciones operativas para AI (Guía editorial V2)
https://brand.magoya.com/vocabulary.json     <- vocabulario a evitar (no veto universal), frases, regla AI, glosario ES/EN/PT
https://brand.magoya.com/.ai/checklist-verbal.md  <- checklist de texto: las 8 preguntas de la guía + chequeos del playbook
https://brand.magoya.com/.ai/verbal/estrategia.md <- definición, territorios, razones para creer, tagline
https://brand.magoya.com/.ai/verbal/voz.md        <- rasgos, diales por país, énfasis por audiencia
https://brand.magoya.com/.ai/verbal/lenguaje.md   <- vocabulario a evitar, regla AI, glosario
https://brand.magoya.com/.ai/verbal/aplicacion.md <- voceros, canales, idioma
```

**Las dos reglas que más se rompen en este flujo:** (1) la plantilla se copia TAL CUAL — solo cambia el texto de los `data-slot`; (2) las cifras y textos de las plantillas son EJEMPLO: los datos reales están en `facts.json` y lo que no esté ahí se pide, nunca se inventa.

## Qué podés hacer al pie de la letra (hoy)

- **Artifacts / HTML / componentes**: fidelidad total — embebé los SVGs reales (fetch + inline) y cargá Manrope desde Google Fonts.
- **Claude Code**: cloná o fetcheá el repo directamente (`github.com/magoya/magoya-brand-system`) — ahí está todo el árbol de assets sin manifiesto de por medio. Preset listo: [claude-code-CLAUDE.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/presets/claude-code-CLAUDE.md).
- **Imágenes**: Claude no genera raster — para piezas visuales la salida correcta es HTML/SVG con los assets reales, que es justamente donde la fidelidad es total.

## Setup (una sola vez, para humanos)

- **claude.ai Projects**: pegá en las instrucciones del proyecto: *"Antes de cualquier tarea de marca, fetch https://brand.magoya.com/ai/claude.md y seguí su flujo."* + el preset [claude-project-instructions.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/presets/claude-project-instructions.md) como refuerzo. Knowledge opcional como fallback offline: BRAND.md, tokens.json, tokens.css.
- **Claude Code**: copiá el preset a `CLAUDE.md` del proyecto.

## Agent Skills: el canal que le gana a la URL (verificado 2026-09-07)

Una **skill** es una carpeta con un `SKILL.md` (metadata + instrucciones) que el agente carga en tres
etapas: al arrancar solo lee nombre y descripción, el cuerpo entra cuando la tarea coincide, y los
archivos referenciados recién cuando los necesita. Eso es lo contrario de `llms-full.txt`, que entra
entero en cada conversación.

- **Claude Code / claude.ai**: skills en `.claude/skills/` del proyecto o `~/.claude/skills/`
  ([docs](https://code.claude.com/docs/en/skills)). La distribución soportada es un **plugin
  marketplace**, que es un repo de git: `/plugin marketplace add <owner/repo>` y después
  `/plugin install <nombre>@<marketplace>`. Este brand system YA es un repo, así que el canal existe.
- **Hoy Magoya no publica una skill.** El canal sigue siendo la URL de arriba. Empaquetarla es una
  decisión abierta en el ledger (`.ai/VALIDACION-IA.md`), no la tomes por tu cuenta.

## Changelog

- **1.8** (2026-10-19): Guía editorial V2 ("Manual voz y tono MAGOYA V2") como fuente de la voz y el tono: .ai/verbal/guia-editorial.md en el flujo y en la lista plana, con sus reglas operativas (sin cifras inventadas, validación humana, clientes no nombrados por defecto, borrador pendiente de revisión, conflictos señalados). El checklist verbal se rearma sobre sus 8 preguntas.

- **1.7** (2026-10-19): capa verbal del Magoya Brand Playbook (octubre 2026) — vocabulary.json, .ai/checklist-verbal.md y .ai/verbal/ en el flujo y en la lista plana. Se escribe AI, no la sigla en español (salvo IA en Campo).

- **1.6** (2026-09-07): Agent Skills documentado como mecanismo (progressive disclosure + plugin marketplace como canal de distribución). Todavía no hay skill publicada: el canal sigue siendo la URL.

- **1.5** (2026-08-11): aviso anti-resumen al inicio (el fetch de algunas AIs devolvía un resumen sin las URLs del flujo) + `deck-starter.html` para apilar varias slides + cifras de ejemplo de las plantillas ahora salen como `[XX]` para que no se puedan entregar como reales.

- **1.4** (2026-08-11): `ai/facts.json` (datos reales, contra cifras inventadas) + lista plana de URLs a prueba de resúmenes + plantillas también en `.txt` (el fetch de `.html` las convierte a markdown y rompe el copy-paste).

- **1.3** (2026-08-11): flujo copiá-pegá-y-funciona — 41 plantillas HTML con slots (`ai/templates/`), selector de módulos (`ai/selector.json`), constraints duros (`ai/constraints.json`) y `llms-full.txt` (todo en un fetch). El LLM ya no interpreta geometría: llena slots.

- **1.2** (2026-08-10): método de trabajo obligatorio (`ai/metodo.md`): narrativa primero, módulos por criterio, agentes de copy/diseño/crítica.

- **1.1** (2026-08-10): slides.json ahora trae la geometría exacta de los 41 módulos (`layout_src`) + archivos por familia contra truncamiento de fetch + advertencia currentColor en íconos.
- **1.0** (2026-08-10): primera versión. Fetch directo como canal principal; artifacts como salida recomendada para piezas visuales.
