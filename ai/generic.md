# Magoya Brand — entrada genérica (cualquier AI con browsing)

**Versión 1.8 · 2026-10-19** · Punto de entrada de la marca Magoya para cualquier modelo no cubierto por las entradas específicas (Perplexity, Mistral, un LLM por API, lo que venga). Changelog al pie.

> **AVISO PARA EL MODELO QUE LEE ESTO: no resumas este archivo — necesitás las URLs literales.** Si tu herramienta de fetch te devolvió un resumen sin links, volvé a pedir el contenido completo, o hacé UN fetch de `https://brand.magoya.com/llms-full.txt` que trae todo el sistema en un solo archivo.
Si sos un modelo leyendo esto: seguí el flujo de abajo, todas las URLs son públicas y fetcheables sin auth.

## Flujo (en este orden)

0. **¿Necesitás un deck? Mirá primero si ya está armado** → https://brand.magoya.com/ai/decks/index.json
   Hay tres decks COMPLETOS y validados: **credenciales** (primer contacto), **propuesta-piloto**
   (con escenarios e inversión) y **cierre-de-proyecto** (resultados para el sponsor). La secuencia,
   los lienzos y el arco ya están resueltos: **no hay que elegir módulos ni componer nada.** Bajás el
   .html, cambiás el texto que está entre corchetes, y listo. Cada corchete dice qué va ahí y cuántos
   caracteres entran. Los `[XX]` son datos que hay que PEDIR, no completar.
   Usá los 41 módulos de abajo **solo si el deck que necesitás no es ninguno de esos tres.**

1. **Doctrina** → https://brand.magoya.com/BRAND.md — si solo vas a leer un archivo, es este.
   **Texto** (si la pieza lleva copy) → https://brand.magoya.com/.ai/verbal/guia-editorial.md, https://brand.magoya.com/vocabulary.json y https://brand.magoya.com/.ai/checklist-verbal.md. La identidad, los territorios, la oferta, los espacios y el Método Magoya salen del Magoya Brand Playbook (octubre 2026): Magoya es una consultora hands-on en software y AI para empresas del agro; se escribe AI en cualquier idioma (única excepción: el nombre propio IA en Campo). La voz, el estilo y el vocabulario salen de la Guía editorial V2, cuya Parte II son instrucciones operativas para agentes de AI: no inventar hechos ni cifras (toda métrica real la valida alguien del equipo), no nombrar clientes por defecto, distinguir hecho, interpretación, hipótesis y ejemplo, entregar como borrador pendiente de revisión cuando hay decisiones, riesgos o cifras, y señalar los conflictos entre fuentes en vez de resolverlos. El vocabulario a evitar no es un veto universal y el 50/30/20 planifica contenidos, no se chequea por texto. Detalle en https://brand.magoya.com/.ai/verbal/ (guia-editorial.md, estrategia.md, voz.md, lenguaje.md, aplicacion.md).
2. **Valores exactos** → https://brand.magoya.com/tokens.json
3. **Assets** → https://brand.magoya.com/ai/assets.json — 239 archivos con URL directa y regla de uso. Los SVGs se leen como texto: el wordmark se usa tal cual, jamás se redibuja.
4. **Presentaciones — flujo copiá-pegá-y-funciona**: (a) elegí el módulo con https://brand.magoya.com/ai/selector.json (qué querés contar → qué plantilla, sin criterio de diseño), (b) copiá la plantilla oficial TAL CUAL desde https://brand.magoya.com/ai/templates/index.json (HTML listo, geometría y colores bloqueados), (c) llená SOLO los data-slot respetando max_caracteres — si el texto no entra, acortá el texto, nunca la fuente. La geometría de referencia sigue en ai/slides.json (layout_src) para quien renderice por su cuenta.
5. **Datos reales de la empresa** → https://brand.magoya.com/ai/facts.json — cifras aprobadas y equipo nombrable. Los clientes se nombran solo con autorización expresa (guía editorial V2, §8); si no está registrada, va a PEDIDO A HUMANOS. Las cifras de las plantillas son EJEMPLO: nunca se entregan como reales. Si el dato no está acá, se le pide al usuario, y toda cifra real la valida una persona del equipo (contrato en `validacion`). Los clientes no se nombran sin autorización expresa.
6. **Constraints duros** → https://brand.magoya.com/ai/constraints.json — mínimos de logo, clearspace, márgenes, safe areas, límites de texto. Nada se asume: si un valor no está ahí ni en tokens.json, se pregunta.
7. **Método de trabajo (OBLIGATORIO en piezas con contenido)** → https://brand.magoya.com/ai/templates/index.json  <- ojo el campo "perfil" de cada modulo y "como_componer_el_deck":
                                                     el selector elige QUE contar, el perfil ordena la SECUENCIA
https://brand.magoya.com/ai/precedencia.json  <- quién gana cuando dos reglas chocan + contrato de entrega
https://brand.magoya.com/ai/metodo.md — narrativa primero, módulo por criterio, pasadas de copy / diseño / crítica.
8. **Cuando dos reglas oficiales se contradicen** → https://brand.magoya.com/ai/precedencia.json — la ley de precedencia. Gana la plantilla, después facts.json, después tokens. El `cuando_usarlo` es lo último. Si encontrás una contradicción, aplicá la ley, entregá, y reportala — no la resuelvas por criterio propio.
9. **Antes de entregar** → corré `python3 ai/validar.py --pieza <tu-archivo.html>` si tenés el repo, y en cualquier caso cumplí el contrato de entrega de `precedencia.json`: un dato que no está en `facts.json` va como `[PENDIENTE]`, nunca como el número que te pasaron; con un hueco adentro la pieza sale marcada BORRADOR y con un bloque PEDIDO A HUMANOS.


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

## Si no podés navegar

Pedile al humano que te pegue [brand-prompt-short.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/brand-prompt-short.md) (~300 palabras) como primer mensaje — es la versión mínima viable de la doctrina.

## Regla de oro transversal

Todo lo que no esté en estos archivos NO existe: ni paletas genéricas, ni "lo que suele hacerse", ni conocimiento previo de otras marcas del agro. Si falta un dato, decilo.

## Agent Skills: formato abierto (verificado 2026-09-07)

Si tu herramienta soporta **Agent Skills** —el formato abierto de una carpeta con `SKILL.md`, hoy
adoptado por Claude, ChatGPT/Codex, Gemini CLI, Copilot, VS Code, Cursor y varias decenas más
([especificación](https://agentskills.io/specification))— el mecanismo correcto es una skill y no un
fetch: carga nombre y descripción al arrancar, y el cuerpo solo cuando la tarea coincide.

**Hoy Magoya no publica una skill**: el canal es la URL de este archivo. Empaquetarla es una decisión
abierta en el ledger (`.ai/VALIDACION-IA.md`).

## Changelog

- **1.8** (2026-10-19): Guía editorial V2 ("Manual voz y tono MAGOYA V2") como fuente de la voz y el tono: .ai/verbal/guia-editorial.md en el flujo y en la lista plana, con sus reglas operativas (sin cifras inventadas, validación humana, clientes no nombrados por defecto, borrador pendiente de revisión, conflictos señalados). El checklist verbal se rearma sobre sus 8 preguntas.

- **1.7** (2026-10-19): capa verbal del Magoya Brand Playbook (octubre 2026) — vocabulary.json, .ai/checklist-verbal.md y .ai/verbal/ en el flujo y en la lista plana. Se escribe AI, no la sigla en español (salvo IA en Campo).

- **1.6** (2026-09-07): Agent Skills como formato abierto y multi-herramienta, con el estado real: el canal sigue siendo la URL porque todavía no hay skill publicada.

- **1.5** (2026-08-11): aviso anti-resumen al inicio (el fetch de algunas AIs devolvía un resumen sin las URLs del flujo) + `deck-starter.html` para apilar varias slides + cifras de ejemplo de las plantillas ahora salen como `[XX]` para que no se puedan entregar como reales.

- **1.4** (2026-08-11): `ai/facts.json` (datos reales, contra cifras inventadas) + lista plana de URLs a prueba de resúmenes + plantillas también en `.txt` (el fetch de `.html` las convierte a markdown y rompe el copy-paste).

- **1.3** (2026-08-11): plantillas con slots + selector + constraints + llms-full.txt.

- **1.2** (2026-08-10): método de trabajo obligatorio (`ai/metodo.md`).

- **1.1** (2026-08-10): geometría exacta de slides + archivos por familia + advertencia currentColor.
- **1.0** (2026-08-10): primera versión.
