# Magoya Brand — entrada para Claude (claude.ai / Claude Code / API)

**Versión 2.2 · 2026-11-17** · Punto de entrada de la marca Magoya para Claude. Se versiona por separado de las otras AIs: cuando Claude gane capacidades nuevas, esta entrada se actualiza sin tocar las demás (changelog al pie).

> **La marca de Magoya se consume desde cualquier AI.** Esta es una de las entradas y todas leen la misma fuente. El protocolo común (primera respuesta, modo de lectura, assets, instalación, fallas conocidas, contrato de entrega) es https://brand.magoya.com/ai/protocolo.md

> **Si sos una AI:** decile a la persona qué versión y qué fecha de esta entrada leíste. Algunos fetch devuelven una copia vieja guardada en caché: si no es la última del changelog publicado, pedí esta misma URL agregándole `?v=` y la fecha de hoy.

> **AVISO PARA EL MODELO QUE LEE ESTO: no resumas este archivo — necesitás las URLs literales.** Si tu herramienta de fetch te devolvió un resumen sin links, volvé a pedir el contenido completo, o hacé UN fetch de `https://brand.magoya.com/llms-full.txt` que trae todo el sistema en un solo archivo.
Si sos Claude leyendo esto: seguí el flujo de abajo, todas las URLs son públicas y fetcheables sin auth.

## Flujo (en este orden)

1. **Doctrina** → https://brand.magoya.com/BRAND.md · todas las reglas de la marca. Si solo vas a leer un archivo, es este.
   **Texto** (si hay copy) → https://brand.magoya.com/.ai/verbal/guia-editorial.md, https://brand.magoya.com/vocabulary.json y https://brand.magoya.com/.ai/checklist-verbal.md. La identidad, los territorios, la oferta, los espacios y el Método Magoya salen del Magoya Brand Voice Playbook (octubre de 2026): Magoya es una consultora hands-on en software y AI para empresas del agro; se escribe AI en cualquier idioma (única excepción: el nombre propio IA en Campo). La voz, el estilo y el vocabulario salen de la Guía editorial V2, cuya Parte II son instrucciones operativas para agentes de AI: no inventar hechos ni cifras (toda métrica real la valida alguien del equipo), no nombrar clientes por defecto, distinguir hecho, interpretación, hipótesis y ejemplo, entregar como borrador pendiente de revisión cuando hay decisiones, riesgos o cifras, y señalar los conflictos entre fuentes en vez de resolverlos. El vocabulario vetado del playbook es obligatorio (pp. 45–46) y el 50/30/20 planifica contenidos, no se chequea por texto. Para textos en inglés manda la edición en inglés del playbook, redactada de forma nativa (nunca se traduce desde el español): https://brand.magoya.com/en/. Detalle en https://brand.magoya.com/.ai/verbal/ (guia-editorial.md, estrategia.md, voz.md, lenguaje.md, aplicacion.md).
2. **Valores exactos** → https://brand.magoya.com/tokens.json · paleta con roles, regla de uso del color, escala tipográfica, espaciado, radios y accesibilidad.
3. **Tokens CSS** (si vas a escribir código) → https://brand.magoya.com/tokens.css · usá las custom properties, nunca hex sueltos.
4. **Assets** → https://brand.magoya.com/ai/assets.json · manifiesto de TODOS los archivos (230): wordmarks, avatares, 58 íconos, fotos, logos reales de clientes; cada uno con URL directa y su regla de uso. Los vectores propios (wordmark, avatares, miscelánea gestual, íconos) están como texto en https://brand.magoya.com/ai/vectores.md (un `.svg` pedido por su URL puede no llegarte; ese archivo sí). El código se pega tal cual, jamás se redibuja. Las fotos no se leen por link: elegilas por su ficha (clave `fotos` del manifiesto) y referencialas por URL.
5. **Datos reales de la empresa** → https://brand.magoya.com/ai/facts.json · cifras aprobadas y equipo nombrable. Los clientes se nombran solo con autorización expresa (guía editorial V2, §8); si no está registrada, va a PEDIDO A HUMANOS. Si el dato no está acá, se le pide al usuario, y toda cifra real la valida una persona del equipo (contrato en `validacion`).
6. **Constraints duros** → https://brand.magoya.com/ai/constraints.json · mínimos de logo, clearspace, safe areas, límites de texto. Nada se asume: si un valor no está ahí ni en tokens.json, se pregunta.
7. **Método de trabajo** → https://brand.magoya.com/ai/metodo.md · la idea antes del texto, títulos-aserción, y pasadas de copy, diseño y crítica antes de entregar (secuenciales si no tenés subagentes).
8. **Cuando dos reglas oficiales se contradicen** → https://brand.magoya.com/ai/precedencia.json · la ley de precedencia. Para cifras y hechos manda siempre facts.json; tokens.json fija los valores exactos. Para identidad y oferta manda el playbook, y para voz y estilo la Guía editorial V2. Si encontrás una contradicción, aplicá la ley, entregá, y reportala: no la resuelvas por criterio propio.
9. **Antes de entregar** → `.ai/checklist-verbal.md` para el texto y `.ai/checklist.md` si hay algo visual. Si tenés el repo, corré `python3 ai/validar.py --entrega <tu-archivo>`. En cualquier caso cumplí el contrato de entrega de `precedencia.json`: un dato que no está en `facts.json` va como `[PENDIENTE]`, nunca como el número que te pasaron; con un hueco adentro el entregable sale marcado BORRADOR y con un bloque PEDIDO A HUMANOS.


## URLs del flujo (lista plana: si tu fetch resumió lo de arriba, usá esta)

```
https://brand.magoya.com/llms-full.txt        <- casi todo en un archivo, para CARGAR: por link un fetch lo corta (unos 190 KB)
https://brand.magoya.com/BRAND.md             <- doctrina
https://brand.magoya.com/tokens.json          <- valores exactos
https://brand.magoya.com/tokens.css           <- tokens como CSS custom properties
https://brand.magoya.com/ai/facts.json        <- datos REALES de la empresa (cifras, clientes, equipo)
https://brand.magoya.com/ai/constraints.json  <- mínimos, clearspace, safe areas
https://brand.magoya.com/ai/assets.json       <- los 230 assets con URL directa + la ficha de cada foto
https://brand.magoya.com/ai/vectores.md       <- wordmark, avatares, miscelánea e íconos como TEXTO (un .svg por URL puede no llegar)
https://brand.magoya.com/ai/metodo.md         <- método de trabajo (idea, títulos, pasadas)
https://brand.magoya.com/ai/precedencia.json  <- quién gana cuando dos reglas chocan + contrato de entrega
https://brand.magoya.com/.ai/checklist.md     <- chequeos visuales
https://brand.magoya.com/.ai/verbal/guia-editorial.md <- voz y tono + instrucciones operativas para AI (Guía editorial V2)
https://brand.magoya.com/vocabulary.json     <- vocabulario vetado (obligatorio), frases, regla AI, glosario ES/EN/PT
https://brand.magoya.com/.ai/checklist-verbal.md  <- checklist de texto: las 8 preguntas de la guía + chequeos del playbook
https://brand.magoya.com/.ai/verbal/estrategia.md <- definición, territorios, razones para creer, tagline
https://brand.magoya.com/.ai/verbal/voz.md        <- rasgos, diales por país, énfasis por audiencia
https://brand.magoya.com/.ai/verbal/lenguaje.md   <- expresión verbal, vocabulario vetado, regla AI, glosario, writing in English
https://brand.magoya.com/.ai/verbal/aplicacion.md <- voceros, canales, idioma, reglas de evidencia, instrucciones para agentes
```

**Las dos reglas que más se rompen en este flujo:** (1) los datos reales están en `facts.json` y lo que no esté ahí se pide, nunca se inventa; (2) el wordmark y los íconos se usan tal cual desde `assets.json`, nunca se redibujan.

## Qué podés hacer al pie de la letra (hoy)

- **Artifacts / HTML / componentes**: fidelidad total — embebé los SVGs reales inline, tomados de `ai/vectores.md` y cargá Manrope desde Google Fonts.
- **Claude Code**: cloná o fetcheá el repo directamente (`github.com/magoya/magoya-brand-system`) — ahí está todo el árbol de assets sin manifiesto de por medio. Preset listo: [claude-code-CLAUDE.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/presets/claude-code-CLAUDE.md).
- **Imágenes**: Claude no genera fotos; arma diagramas y visuales en HTML y SVG ([ayuda de Claude](https://support.claude.com/en/articles/9002504)). Para piezas visuales la salida correcta es HTML/SVG con los assets reales, que es justamente donde la fidelidad es total.

## Setup (una sola vez, para humanos)

- **Un chat cualquiera**: pegá el link de esta entrada y pedile que siga el flujo. Con Web search activo lee todo desde el sitio.
- **Un proyecto de Claude** (uno propio, o el del equipo: "Magoya · Marca"): las instrucciones y los archivos quedan cargados, así no depende del fetch. Es una opción, no el único camino.
- **Design System de Claude**: los logos, los íconos y las fotos van como archivos del sistema, no como assets subidos aparte. Otro artifact puede leer y copiar los archivos de un design system; sus assets, no.
- **Quien administra el proyecto**: las instrucciones del proyecto son el preset [claude-project-instructions.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/presets/claude-project-instructions.md) (lo que está debajo del separador) y el knowledge son los archivos que lista ese preset. Cuando cambia la marca, se reemplazan los archivos que cambiaron. Con Web search activo, Claude además puede leer esta entrada y el resto del sitio por URL.

## Agent Skills: el canal que le gana a la URL

Una **skill** es una carpeta con un `SKILL.md` (metadata + instrucciones) que el agente carga en tres
etapas: al arrancar solo lee nombre y descripción, el cuerpo entra cuando la tarea coincide, y los
archivos referenciados recién cuando los necesita. Eso es lo contrario de `llms-full.txt`, que entra
entero en cada conversación.

- **Claude Code**: skills en `.claude/skills/` del proyecto o `~/.claude/skills/`
  ([docs](https://code.claude.com/docs/en/skills)). En claude.ai, las skills se suben y se activan
  desde la configuración de la cuenta, no desde una carpeta. La distribución soportada es un **plugin
  marketplace**, que es un repo de git: `/plugin marketplace add <owner/repo>` y después
  `/plugin install <nombre>@<marketplace>`. Este brand system YA es un repo, así que el canal existe.
- **Hoy Magoya no publica una skill.** El canal sigue siendo la URL de arriba. Empaquetarla es una
  decisión abierta en el ledger (`.ai/VALIDACION-IA.md`), no la tomes por tu cuenta.

## Changelog

- **2.2** (2026-11-17): la marca se consume desde cualquier AI: se retira «el proyecto de Claude es el único camino». Los vectores propios (wordmark, avatares, miscelánea, íconos) pasan a leerse como texto en `ai/vectores.md`, porque un `.svg` pedido por URL no le llega a una AI, y cada foto tiene su ficha en `ai/assets.json`. La entrada pide informar la versión leída: hay fetch que devuelven copias viejas.

- **2.1** (2026-10-29): Magoya Brand Voice Playbook (octubre de 2026, ediciones en español y en inglés): el vocabulario vetado pasa a obligatorio, como lo marca el playbook (la contradicción con la Guía V2 queda como nota para mantenedores en `precedencia.json`); se suma la edición en inglés del sitio (https://brand.magoya.com/en/) para textos en inglés; el manifiesto tiene 230 assets.

- **2.0** (2026-10-22): el flujo queda para escribir y revisar contenido con las reglas y los recursos de la marca. La capa visual sigue el feedback del 22 de octubre: el Verde Magoya #133825 es el verde protagonista, el lima es solo para acentos, detalles, resaltar o CTA, las proporciones de uso quedan pendientes de definir, las personas van siempre a color y sin detalle encima, y no hay ilustración. El validador pasa a `validar.py --entrega`.

- **1.9** (2026-10-19): el equipo de Magoya trabaja la marca en el proyecto oficial de Claude "Magoya · Marca"; el setup para humanos pasa a ser acceso al proyecto, sin configuración individual. Se corrigen la línea de imágenes (Claude no genera fotos, sí HTML/SVG) y la de skills en claude.ai, y se quita la fecha de verificación que no tenía fuente.

- **1.8** (2026-10-19): Guía editorial V2 ("Manual voz y tono MAGOYA V2") como fuente de la voz y el tono: .ai/verbal/guia-editorial.md en el flujo y en la lista plana, con sus reglas operativas (sin cifras inventadas, validación humana, clientes no nombrados por defecto, borrador pendiente de revisión, conflictos señalados). El checklist verbal se rearma sobre sus 8 preguntas.

- **1.7** (2026-10-19): capa verbal del Magoya Brand Playbook (octubre 2026) — vocabulary.json, .ai/checklist-verbal.md y .ai/verbal/ en el flujo y en la lista plana. Se escribe AI, no la sigla en español (salvo IA en Campo).

- **1.6** (2026-09-07): Agent Skills documentado como mecanismo (progressive disclosure + plugin marketplace como canal de distribución). Todavía no hay skill publicada: el canal sigue siendo la URL.

- **1.4** (2026-08-11): `ai/facts.json` (datos reales, contra cifras inventadas) + lista plana de URLs a prueba de resúmenes.

- **1.2** (2026-08-10): método de trabajo obligatorio (`ai/metodo.md`).

- **1.0** (2026-08-10): primera versión. Fetch directo como canal principal; artifacts como salida recomendada para piezas visuales.
