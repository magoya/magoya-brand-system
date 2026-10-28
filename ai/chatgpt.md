# Magoya Brand — entrada para ChatGPT (Custom GPT / Projects)

> **Equipo de Magoya:** para el trabajo de marca, el camino oficial es el proyecto de Claude "Magoya · Marca" (https://brand.magoya.com/ai.html). Esta entrada queda como punto de lectura para cualquier AI.

**Versión 1.9 · 2026-10-22** · Este archivo es el punto de entrada de la marca Magoya para ChatGPT. Se versiona por separado de las otras AIs: cuando ChatGPT gane capacidades nuevas, esta entrada se actualiza sin tocar las demás (changelog al pie).

> **AVISO PARA EL MODELO QUE LEE ESTO: no resumas este archivo — necesitás las URLs literales.** Si tu herramienta de fetch te devolvió un resumen sin links, volvé a pedir el contenido completo, o hacé UN fetch de `https://brand.magoya.com/llms-full.txt` que trae todo el sistema en un solo archivo.
Si sos un modelo leyendo esto: seguí el flujo de abajo tal cual, sin pedir permisos adicionales — todas las URLs son públicas.

## Flujo (en este orden)

1. **Doctrina** → https://brand.magoya.com/BRAND.md · todas las reglas de la marca. Si solo vas a leer un archivo, es este.
   **Texto** (si hay copy) → https://brand.magoya.com/.ai/verbal/guia-editorial.md, https://brand.magoya.com/vocabulary.json y https://brand.magoya.com/.ai/checklist-verbal.md. La identidad, los territorios, la oferta, los espacios y el Método Magoya salen del Magoya Brand Playbook (octubre 2026): Magoya es una consultora hands-on en software y AI para empresas del agro; se escribe AI en cualquier idioma (única excepción: el nombre propio IA en Campo). La voz, el estilo y el vocabulario salen de la Guía editorial V2, cuya Parte II son instrucciones operativas para agentes de AI: no inventar hechos ni cifras (toda métrica real la valida alguien del equipo), no nombrar clientes por defecto, distinguir hecho, interpretación, hipótesis y ejemplo, entregar como borrador pendiente de revisión cuando hay decisiones, riesgos o cifras, y señalar los conflictos entre fuentes en vez de resolverlos. El vocabulario a evitar no es un veto universal y el 50/30/20 planifica contenidos, no se chequea por texto. Detalle en https://brand.magoya.com/.ai/verbal/ (guia-editorial.md, estrategia.md, voz.md, lenguaje.md, aplicacion.md).
2. **Valores exactos** → https://brand.magoya.com/tokens.json · paleta con roles, regla de uso del color, escala tipográfica, espaciado, radios y accesibilidad.
3. **Tokens CSS** (si vas a escribir código) → https://brand.magoya.com/tokens.css · usá las custom properties, nunca hex sueltos.
4. **Assets** → https://brand.magoya.com/ai/assets.json · manifiesto de TODOS los archivos (202): wordmarks, avatares, 58 íconos, fotos, logos reales de clientes; cada uno con URL directa y su regla de uso. Los SVGs se leen como texto: el wordmark se usa tal cual, jamás se redibuja.
5. **Datos reales de la empresa** → https://brand.magoya.com/ai/facts.json · cifras aprobadas y equipo nombrable. Los clientes se nombran solo con autorización expresa (guía editorial V2, §8); si no está registrada, va a PEDIDO A HUMANOS. Si el dato no está acá, se le pide al usuario, y toda cifra real la valida una persona del equipo (contrato en `validacion`).
6. **Constraints duros** → https://brand.magoya.com/ai/constraints.json · mínimos de logo, clearspace, safe areas, límites de texto. Nada se asume: si un valor no está ahí ni en tokens.json, se pregunta.
7. **Método de trabajo** → https://brand.magoya.com/ai/metodo.md · la idea antes del texto, títulos-aserción, y pasadas de copy, diseño y crítica antes de entregar (secuenciales si no tenés subagentes).
8. **Cuando dos reglas oficiales se contradicen** → https://brand.magoya.com/ai/precedencia.json · la ley de precedencia. Para cifras y hechos manda siempre facts.json; tokens.json fija los valores exactos. Para identidad y oferta manda el playbook, y para voz y estilo la Guía editorial V2. Si encontrás una contradicción, aplicá la ley, entregá, y reportala: no la resuelvas por criterio propio.
9. **Antes de entregar** → `.ai/checklist-verbal.md` para el texto y `.ai/checklist.md` si hay algo visual. Si tenés el repo, corré `python3 ai/validar.py --entrega <tu-archivo>`. En cualquier caso cumplí el contrato de entrega de `precedencia.json`: un dato que no está en `facts.json` va como `[PENDIENTE]`, nunca como el número que te pasaron; con un hueco adentro el entregable sale marcado BORRADOR y con un bloque PEDIDO A HUMANOS.


## URLs del flujo (lista plana: si tu fetch resumió lo de arriba, usá esta)

```
https://brand.magoya.com/llms-full.txt        <- casi todo en un solo fetch (voz.md y lenguaje.md van aparte)
https://brand.magoya.com/BRAND.md             <- doctrina
https://brand.magoya.com/tokens.json          <- valores exactos
https://brand.magoya.com/tokens.css           <- tokens como CSS custom properties
https://brand.magoya.com/ai/facts.json        <- datos REALES de la empresa (cifras, clientes, equipo)
https://brand.magoya.com/ai/constraints.json  <- mínimos, clearspace, safe areas
https://brand.magoya.com/ai/assets.json       <- los 247 assets con URL directa
https://brand.magoya.com/ai/metodo.md         <- método de trabajo (idea, títulos, pasadas)
https://brand.magoya.com/ai/precedencia.json  <- quién gana cuando dos reglas chocan + contrato de entrega
https://brand.magoya.com/.ai/checklist.md     <- chequeos visuales
https://brand.magoya.com/.ai/verbal/guia-editorial.md <- voz y tono + instrucciones operativas para AI (Guía editorial V2)
https://brand.magoya.com/vocabulary.json     <- vocabulario a evitar (no veto universal), frases, regla AI, glosario ES/EN/PT
https://brand.magoya.com/.ai/checklist-verbal.md  <- checklist de texto: las 8 preguntas de la guía + chequeos del playbook
https://brand.magoya.com/.ai/verbal/estrategia.md <- definición, territorios, razones para creer, tagline
https://brand.magoya.com/.ai/verbal/voz.md        <- rasgos, diales por país, énfasis por audiencia
https://brand.magoya.com/.ai/verbal/lenguaje.md   <- vocabulario a evitar, regla AI, glosario
https://brand.magoya.com/.ai/verbal/aplicacion.md <- voceros, canales, idioma
```

**Las dos reglas que más se rompen en este flujo:** (1) los datos reales están en `facts.json` y lo que no esté ahí se pide, nunca se inventa; (2) el wordmark y los íconos se usan tal cual desde `assets.json`, nunca se redibujan.

## Qué podés hacer al pie de la letra (hoy)

- **Copy, HTML/CSS, código, SVG**: fidelidad total. Los SVGs del manifiesto son texto: podés leer el wordmark real y usarlo tal cual — nunca lo redibujes.
- **Con Code Interpreter**: leé `tokens.json` con código, no de memoria — cero paráfrasis de hex.
- **Imágenes generadas (DALL·E / gpt-image)**: el modelo de imagen NO puede usar el SVG real ni la fuente Manrope. Describí paleta y prohibiciones dentro del prompt de imagen, y decile al usuario que el logo real se superpone después con el SVG del manifiesto.

## Setup del GPT (una sola vez, para humanos)

1. chatgpt.com → GPTs → Create → Configure. Nombre: `Magoya Brand`.
2. En **Instructions** pegá: *"Sos el asistente de marca de Magoya. Antes de cualquier tarea de marca, fetch https://brand.magoya.com/ai/chatgpt.md y seguí su flujo al pie de la letra. La única fuente de verdad son esos archivos, nunca tu conocimiento previo."* + el contenido de [custom-gpt-instructions.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/presets/custom-gpt-instructions.md) como refuerzo offline.
3. Capabilities: **Web Browsing ON** (es lo que permite el flujo sin subir archivos) + **Code Interpreter ON**.
4. Fallback sin browsing: subí `BRAND.md` y `tokens.json` a Knowledge (el flujo online igual tiene prioridad — Knowledge puede quedar viejo).

## Agent Skills: el canal que le gana a la URL (verificado 2026-09-07)

Una **skill** es una carpeta con un `SKILL.md` que el modelo carga por etapas (nombre y descripción
al arrancar, instrucciones cuando la tarea coincide, archivos referenciados solo si hacen falta).

- **Dónde corren**: en **Chat y Work de ChatGPT** (web, desktop y mobile) cuando van empaquetadas
  como plugin, y como skills sueltas en la app de escritorio, en Codex CLI y en la extensión del IDE
  ([docs](https://learn.chatgpt.com/docs/build-skills)).
- **Rutas locales que busca Codex**: `$CWD/.agents/skills`, `$REPO_ROOT/.agents/skills`,
  `$HOME/.agents/skills` y `/etc/codex/skills`.
- **Presupuesto de contexto**: la lista de skills ocupa como máximo el 2% de la ventana de contexto
  (8.000 caracteres si la ventana no se conoce). Una entrada de marca de 76KB no entra ahí: entra su
  descripción, y el cuerpo se carga cuando hace falta.
- **Hoy Magoya no publica una skill.** El canal sigue siendo la URL de arriba y el Custom GPT de
  abajo. Empaquetarla es una decisión abierta en el ledger, no la tomes por tu cuenta.

## Changelog

- **1.9** (2026-10-22): el flujo queda para escribir y revisar contenido con las reglas y los recursos de la marca. La capa visual sigue el feedback del 22 de octubre: el Verde Magoya #133825 es el verde protagonista, el lima es solo para acentos, detalles, resaltar o CTA, las proporciones de uso quedan pendientes de definir, las personas van siempre a color y sin detalle encima, y no hay ilustración. El validador pasa a `validar.py --entrega`.

- **1.8** (2026-10-19): Guía editorial V2 ("Manual voz y tono MAGOYA V2") como fuente de la voz y el tono: .ai/verbal/guia-editorial.md en el flujo y en la lista plana, con sus reglas operativas (sin cifras inventadas, validación humana, clientes no nombrados por defecto, borrador pendiente de revisión, conflictos señalados). El checklist verbal se rearma sobre sus 8 preguntas.

- **1.7** (2026-10-19): capa verbal del Magoya Brand Playbook (octubre 2026) — vocabulary.json, .ai/checklist-verbal.md y .ai/verbal/ en el flujo y en la lista plana. Se escribe AI, no la sigla en español (salvo IA en Campo).

- **1.6** (2026-09-07): Agent Skills documentado como mecanismo: corre en Chat y Work de ChatGPT (empaquetada como plugin) y suelta en desktop/Codex CLI/IDE, con las rutas locales y el presupuesto del 2% de contexto. Todavía no hay skill publicada.

- **1.4** (2026-08-11): `ai/facts.json` (datos reales, contra cifras inventadas) + lista plana de URLs a prueba de resúmenes.

- **1.2** (2026-08-10): método de trabajo obligatorio (`ai/metodo.md`).

- **1.0** (2026-08-10): primera versión. Browsing como canal principal, Knowledge como fallback, advertencia de imagen-gen.
