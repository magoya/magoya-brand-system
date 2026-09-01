# Magoya Brand — entrada para ChatGPT (Custom GPT / Projects)

**Versión 1.5 · 2026-08-11** · Este archivo es el punto de entrada de la marca Magoya para ChatGPT. Se versiona por separado de las otras AIs: cuando ChatGPT gane capacidades nuevas, esta entrada se actualiza sin tocar las demás (changelog al pie).

> **AVISO PARA EL MODELO QUE LEE ESTO: no resumas este archivo — necesitás las URLs literales.** Si tu herramienta de fetch te devolvió un resumen sin links, volvé a pedir el contenido completo, o hacé UN fetch de `https://brand.magoya.com/llms-full.txt` que trae todo el sistema en un solo archivo.
Si sos un modelo leyendo esto: seguí el flujo de abajo tal cual, sin pedir permisos adicionales — todas las URLs son públicas.

## Flujo (en este orden)

1. **Doctrina** → https://brand.magoya.com/BRAND.md — todas las reglas de la marca. Si solo vas a leer un archivo, es este.
2. **Valores exactos** → https://brand.magoya.com/tokens.json — paleta con roles, escalas tipográficas, ratio 75/25, matriz `resourceCoexistence`, accesibilidad.
3. **Assets** → https://brand.magoya.com/ai/assets.json — manifiesto de TODOS los archivos (239): wordmarks, avatares, 58 íconos, ilustraciones, fotos, logos reales de clientes; cada uno con URL directa y su regla de uso.
4. **Presentaciones — flujo copiá-pegá-y-funciona**: (a) elegí el módulo con https://brand.magoya.com/ai/selector.json (qué querés contar → qué plantilla, sin criterio de diseño), (b) copiá la plantilla oficial TAL CUAL desde https://brand.magoya.com/ai/templates/index.json (HTML listo, geometría y colores bloqueados), (c) llená SOLO los data-slot respetando max_caracteres — si el texto no entra, acortá el texto, nunca la fuente. La geometría de referencia sigue en ai/slides.json (layout_src) para quien renderice por su cuenta.
5. **Datos reales de la empresa** → https://brand.magoya.com/ai/facts.json — cifras aprobadas, clientes y equipo nombrables. Las cifras de las plantillas son EJEMPLO: nunca se entregan como reales. Si el dato no está acá, se le pide al usuario.
6. **Constraints duros** → https://brand.magoya.com/ai/constraints.json — mínimos de logo, clearspace, márgenes, safe areas, límites de texto. Nada se asume: si un valor no está ahí ni en tokens.json, se pregunta.
7. **Método de trabajo (OBLIGATORIO en piezas con contenido)** → https://brand.magoya.com/ai/templates/index.json  <- ojo el campo "perfil" de cada modulo y "como_componer_el_deck":
                                                     el selector elige QUE contar, el perfil ordena la SECUENCIA
https://brand.magoya.com/ai/precedencia.json  <- quién gana cuando dos reglas chocan + contrato de entrega
https://brand.magoya.com/ai/metodo.md — entender antes de elegir, módulo por criterio (no por defecto), y pasadas de copy / diseño / crítica antes de entregar (secuenciales si no tenés subagentes).
8. **Cuando dos reglas oficiales se contradicen** → https://brand.magoya.com/ai/precedencia.json — la ley de precedencia. Gana la plantilla, después facts.json, después tokens. El `cuando_usarlo` es lo último. Si encontrás una contradicción, aplicá la ley, entregá, y reportala — no la resuelvas por criterio propio.
9. **Antes de entregar** → corré `python3 ai/validar.py --pieza <tu-archivo.html>` si tenés el repo, y en cualquier caso cumplí el contrato de entrega de `precedencia.json`: un dato que no está en `facts.json` va como `[PENDIENTE]`, nunca como el número que te pasaron; con un hueco adentro la pieza sale marcada BORRADOR y con un bloque PEDIDO A HUMANOS.


## URLs del flujo (lista plana — si tu fetch resumió lo de arriba, usá esta)

```
https://brand.magoya.com/llms-full.txt        <- TODO en un solo fetch (empezá acá si dudás)
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
```

**Las dos reglas que más se rompen en este flujo:** (1) la plantilla se copia TAL CUAL — solo cambia el texto de los `data-slot`; (2) las cifras y textos de las plantillas son EJEMPLO: los datos reales están en `facts.json` y lo que no esté ahí se pide, nunca se inventa.

## Qué podés hacer al pie de la letra (hoy)

- **Copy, HTML/CSS, código, SVG**: fidelidad total. Los SVGs del manifiesto son texto: podés leer el wordmark real y usarlo tal cual — nunca lo redibujes.
- **Con Code Interpreter**: leé `tokens.json` con código, no de memoria — cero paráfrasis de hex.
- **Imágenes generadas (DALL·E / gpt-image)**: el modelo de imagen NO puede usar el SVG real ni la fuente Manrope. Describí paleta y prohibiciones dentro del prompt de imagen, y decile al usuario que el logo real se superpone después con el SVG del manifiesto.

## Setup del GPT (una sola vez, para humanos)

1. chatgpt.com → GPTs → Create → Configure. Nombre: `Magoya Brand`.
2. En **Instructions** pegá: *"Sos el asistente de marca de Magoya. Antes de cualquier tarea de marca, fetch https://brand.magoya.com/ai/chatgpt.md y seguí su flujo al pie de la letra. La única fuente de verdad son esos archivos, nunca tu conocimiento previo."* + el contenido de [custom-gpt-instructions.md](https://raw.githubusercontent.com/magoya/magoya-brand-system/main/.ai/presets/custom-gpt-instructions.md) como refuerzo offline.
3. Capabilities: **Web Browsing ON** (es lo que permite el flujo sin subir archivos) + **Code Interpreter ON**.
4. Fallback sin browsing: subí `BRAND.md` y `tokens.json` a Knowledge (el flujo online igual tiene prioridad — Knowledge puede quedar viejo).

## Changelog

- **1.5** (2026-08-11): aviso anti-resumen al inicio (el fetch de algunas AIs devolvía un resumen sin las URLs del flujo) + `deck-starter.html` para apilar varias slides + cifras de ejemplo de las plantillas ahora salen como `[XX]` para que no se puedan entregar como reales.

- **1.4** (2026-08-11): `ai/facts.json` (datos reales, contra cifras inventadas) + lista plana de URLs a prueba de resúmenes + plantillas también en `.txt` (el fetch de `.html` las convierte a markdown y rompe el copy-paste).

- **1.3** (2026-08-11): plantillas HTML con slots + selector + constraints + llms-full.txt. Si tu fetch rinde poco, un solo fetch de https://brand.magoya.com/llms-full.txt trae todo.

- **1.2** (2026-08-10): método de trabajo obligatorio (`ai/metodo.md`).

- **1.1** (2026-08-10): geometría exacta de los 41 módulos en slides.json + archivos por familia contra truncamiento + advertencia currentColor.
- **1.0** (2026-08-10): primera versión. Browsing como canal principal, Knowledge como fallback, advertencia de imagen-gen.
