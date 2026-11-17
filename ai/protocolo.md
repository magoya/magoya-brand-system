# Magoya Brand System — protocolo de consumo para AI

**Versión del sistema: 1.4 · 17 de noviembre de 2026.**

Este documento es la especificación con la que una AI trabaja la marca Magoya. La persona que te lo pasó te pidió que lo sigas: se aplica en orden, de la sección 0 a la 7. Las URLs y las rutas son literales y se usan tal cual. La página para personas es https://brand.magoya.com/ai.html y no agrega reglas.

## 0. Primera respuesta

La primera respuesta es este bloque, completo, y después se espera el pedido:

```
MARCA: Magoya · versión del sistema leída: <la de la línea 3 de este documento>
MODO: <link | archivos | repo | ninguno>
LEÍDO: <cada archivo que se abrió en esta sesión>
NO LEÍDO: <cada archivo que falló o llegó cortado, con el error>
```

- `LEÍDO` lista solo lo que se abrió de verdad. Lo que no se abrió, o llegó cortado, va en `NO LEÍDO`.
- Si `NO LEÍDO` tiene un archivo que la tarea necesita (sección 3), se dice qué parte de la marca no se puede aplicar.
- No se trabaja de memoria: lo que se sabe de Magoya, o de otras marcas del agro, por fuera de estos archivos no cuenta.

## 1. Regla de caché

A toda URL de `brand.magoya.com` que se pida se le agrega `?v=1.4` al final. Ejemplo: `https://brand.magoya.com/BRAND.md?v=1.4`.

Motivo: hay herramientas de fetch que guardan copias. El 17 de noviembre de 2026 una URL de este sitio devolvió una copia de agosto; la misma URL con `?v=` devolvió la vigente. Si aun así la versión leída es anterior a la que informa la persona, se repite el pedido con `?v=` y la fecha del día.

## 2. Modo de lectura

Un solo modo, por la primera condición que se cumpla.

| Modo | Condición | Qué se lee |
|---|---|---|
| `repo` | La AI corre adentro de un repositorio (Claude Code, Cursor, Copilot, Codex, Gemini CLI) | El archivo de instrucciones del repo. Si no trae las reglas de Magoya, se propone instalarlo (sección 5.1). Si además hay fetch, sigue como `link` |
| `link` | Hay fetch o browsing y esta URL respondió | Sección 3.1, por URL |
| `archivos` | No se abren URLs, pero hay archivos cargados (proyecto, GPT, Gem, design system) | Sección 3.2, por nombre de archivo |
| `ninguno` | No se abren URLs y no hay archivos | Se le piden a la persona los archivos de la sección 5.2. No se genera nada de marca hasta tenerlos |

## 3. Qué se lee

### 3.1 Modo `link`: por tarea

Ningún archivo de esta tabla pasa los 60 KB, para que un fetch lo entregue entero. `llms-full.txt` no se usa en este modo: pesa unos 190 KB y un fetch lo corta (probado: llegaron 100.000 de 153.000 caracteres).

| Tarea | Archivos, en este orden |
|---|---|
| Siempre | https://brand.magoya.com/BRAND.md · https://brand.magoya.com/ai/constraints.json · https://brand.magoya.com/ai/precedencia.json |
| Texto: copy, mail, post, propuesta | https://brand.magoya.com/.ai/verbal/guia-editorial.md · https://brand.magoya.com/vocabulary.json · https://brand.magoya.com/ai/facts.json · https://brand.magoya.com/ai/metodo.md · https://brand.magoya.com/.ai/checklist-verbal.md |
| Texto sobre posicionamiento, oferta o método | Lo de «Texto», más https://brand.magoya.com/.ai/verbal/estrategia.md y https://brand.magoya.com/.ai/verbal/aplicacion.md |
| Texto para un mercado o una audiencia puntual | Lo de «Texto», más https://brand.magoya.com/.ai/verbal/voz.md |
| Texto en inglés o en portugués | Lo de «Texto», más https://brand.magoya.com/.ai/verbal/lenguaje.md. En inglés manda la edición nativa: https://brand.magoya.com/en/ |
| Pieza visual o código: HTML, CSS, componente, slide | https://brand.magoya.com/tokens.json · https://brand.magoya.com/tokens.css · https://brand.magoya.com/.ai/checklist.md |
| La pieza lleva logo, avatar o favicon | https://brand.magoya.com/ai/vectores/logo.md |
| La pieza lleva íconos | https://brand.magoya.com/ai/vectores/iconos.md |
| La pieza lleva flechas, círculos, X, ✓, un CTA o un box | https://brand.magoya.com/ai/vectores/miscelanea.md |
| La pieza lleva una foto o un logo de un tercero | https://brand.magoya.com/ai/assets.json |
| Revisar una pieza que ya existe | https://brand.magoya.com/.ai/checklist.md · https://brand.magoya.com/.ai/checklist-verbal.md |

Si un archivo llega cortado (termina en mitad de una frase, de un bloque de código o de un JSON), va a `NO LEÍDO`. Si la herramienta acepta un desplazamiento, se pide el resto. No se completa de memoria.

### 3.2 Modo `archivos`: por nombre

| Archivo cargado | Qué trae |
|---|---|
| `protocolo.md` | Este documento |
| `llms-full.txt` | `BRAND.md`, Guía editorial, estrategia, aplicación, vocabulario, restricciones, precedencia, método y los dos checklists |
| `tokens.json`, `tokens.css` | Valores exactos y los mismos valores como custom properties |
| `facts.json` | Datos aprobados de la empresa y contrato de validación |
| `vectores.md` | El código SVG de todos los vectores propios |
| `assets.json` | Manifiesto: URL de cada archivo, ficha de cada foto, regla de uso por carpeta |
| `voz.md`, `lenguaje.md` | Detalle de voz por mercado y audiencia; glosario y escritura en inglés |

Si la herramienta entrega fragmentos en vez del archivo entero (búsqueda sobre los archivos cargados), el archivo se abre completo con la herramienta de código. Si no se puede, cada fragmento usado se trata como parcial: un bloque `svg` sin su cierre `</svg>` no se usa.

## 4. Assets

### 4.1 Cómo se consume cada tipo

Un archivo de imagen pedido por su URL no le llega a una AI que lee por link. Probado el 17 de noviembre de 2026 con el fetch de Claude: `.md`, `.json`, `.txt` y `.css` llegan; `.svg` y `.jpg` devuelven error; `.mdc` llega como binario.

| Tipo | Extensión | Llega por link | Cómo se usa | Fuente |
|---|---|---|---|---|
| Vectores propios: wordmark, avatares, favicon, miscelánea gestual, componentes, íconos | `.svg` | No | Se copia entero el bloque `svg` y se pega inline. Está completo solo si empieza con `<svg` y termina con `</svg>`. Único cambio permitido: el color, a un valor de `tokens.json`. Los íconos usan `stroke="currentColor"`: el color se da por CSS; como `<img>` salen negros. Los avatares, el favicon y los íconos no traen ancho ni alto: se les da `width` y `height` por CSS, o no se ven (cada vector lo indica arriba de su código) | `ai/vectores/logo.md`, `ai/vectores/iconos.md`, `ai/vectores/miscelanea.md` |
| Fotos | `.jpg` | No | Se elige por ficha en `fotos[]`: `archivo`, `url`, `familia`, `ancho_px`, `alto_px`, `orientacion`, `descripcion`. El campo `url` va en el `src`. No se usa ni se describe una foto que no esté en la lista | `ai/assets.json` |
| Logos de terceros: clientes, partners, plataformas de AI, redes | `.svg`, `.png` | No | La URL de `carpetas[]` va en el `src`. Clientes: en gris con `filter: grayscale(1)`, y solo con autorización registrada en `ai/facts.json` | `ai/assets.json` |
| Tipografía | `.ttf` | No hace falta | Manrope desde Google Fonts, pesos 200 a 800. Fallback Arial | `tokens.json` |
| Tokens | `.json`, `.css` | Sí | `var(--token)`. Nunca un hex suelto | `tokens.json`, `tokens.css` |
| ZIP y PDF | `.zip`, `.pdf` | No | No se usan. Lo que traen adentro está publicado como archivo suelto en el manifiesto | `ai/assets.json` |

Reglas:

1. Lo que no está en los archivos de vectores ni en `ai/assets.json` no existe. No se dibuja, no se genera y no se aproxima: se pide.
2. El logo es el wordmark estático. `assets/magoya-wordmark-animado.svg` es solo para web.
3. Un modelo de imagen no reproduce el wordmark ni Manrope. Una imagen generada va sin logo y sin texto, y se avisa que el logo real se superpone después con el SVG.
4. Foto aérea con texto encima: overlay verde profundo entre 55% y 86%. Foto de personas: a color y sin nada encima.

### 4.2 Dónde va a vivir la pieza

Que una URL exista no alcanza: depende de si el lugar donde se abre la pieza carga recursos externos.

| Destino de la pieza | Fotos y logos por URL | `tokens.css` por URL | Vectores inline | Manrope |
|---|---|---|---|---|
| HTML que se abre en un navegador: archivo local o sitio propio | Cargan | Carga con `<link rel="stylesheet">` a https://brand.magoya.com/tokens.css | Sí | Google Fonts, o la que trae `tokens.css` |
| Artifact de Claude | No cargan: el visor bloquea las imágenes remotas | No carga: los tokens se pegan adentro de un `<style>` | Sí | Google Fonts |
| Presentación, documento, PDF o imagen | No aplica: los archivos los inserta la persona | No aplica | Solo si el formato acepta SVG | La instala la persona |
| No se sabe | Se trata como el caso más restrictivo y se avisa | Tokens inline | Sí | Google Fonts |

Cuando una foto o un logo no puede cargar en el destino, la pieza se entrega con el lugar reservado y el archivo se lista en `PEDIDO A HUMANOS` con su URL, para que la persona lo inserte.

## 5. Instalación persistente

Si la persona pregunta cómo dejar la marca cargada en su herramienta, la respuesta es la fila que le corresponde, con la ruta exacta.

### 5.1 Archivo de instrucciones

| Herramienta | Archivo fuente | Destino exacto |
|---|---|---|
| Claude Code | https://brand.magoya.com/.ai/presets/claude-code-CLAUDE.md | `./CLAUDE.md` en la raíz del repo. Alternativas: `~/.claude/CLAUDE.md` o `.claude/rules/magoya-brand.md` |
| Cursor | https://brand.magoya.com/.ai/presets/cursor-rule.mdc.txt | `./.cursor/rules/magoya-brand.mdc`. El `.txt` es el mismo contenido que https://brand.magoya.com/.ai/presets/cursor-rule.mdc, que por link llega como binario |
| GitHub Copilot | https://brand.magoya.com/.ai/presets/copilot-instructions.md | `./.github/copilot-instructions.md` |
| Codex y otros agentes de repo | https://brand.magoya.com/.ai/presets/AGENTS.md | `./AGENTS.md` en la raíz del repo |
| Gemini CLI | https://brand.magoya.com/.ai/presets/AGENTS.md | `./AGENTS.md`, más `context.fileName` con valor `AGENTS.md` en `.gemini/settings.json` |
| Proyecto de Claude | https://brand.magoya.com/.ai/presets/claude-project-instructions.md | Campo de instrucciones del proyecto. Los archivos de 5.2 van a los archivos del proyecto |
| GPT o proyecto de ChatGPT | https://brand.magoya.com/.ai/presets/custom-gpt-instructions.md | Campo *Instructions*. Los archivos de 5.2 van a *Knowledge*; un GPT acepta hasta 20. Con la herramienta de código activa, para abrir cada archivo entero |
| Gem de Gemini | Texto: «Antes de cualquier tarea de marca, leé https://brand.magoya.com/ai/protocolo.md y seguí su protocolo.» | Instrucciones del Gem. Los archivos de 5.2 van a *Knowledge*; un Gem acepta hasta 10 |
| Design System de Claude | `tokens.json`, los vectores y las fotos | Como archivos del sistema, bajo `project/`. No como assets subidos aparte: otro artifact puede leer y copiar los archivos de un design system; sus assets, no |

Si el destino ya existe, el preset se agrega al final. No se sobrescribe.

### 5.2 Archivos para cargar

Nueve archivos. Todos juntos en https://brand.magoya.com/ai/kit.zip

```
ai/protocolo.md
llms-full.txt
tokens.json
tokens.css
ai/facts.json
ai/vectores.md
ai/assets.json
.ai/verbal/voz.md
.ai/verbal/lenguaje.md
```

Si la herramienta rechaza un `.md` o un `.css`, se sube renombrado a `.txt`. Las fotos que se vayan a usar se cargan aparte, como imagen. Los archivos cargados son copias: se reemplazan cuando cambia la versión del sistema.

## 6. Fallas conocidas

| Síntoma | Causa | Qué se hace |
|---|---|---|
| La versión leída es anterior a la que informa la persona | Caché del fetch | Sección 1 |
| El fetch devolvió un resumen, sin URLs ni código | La herramienta resume en vez de entregar el archivo | Se pide de nuevo el archivo indicando que se necesita el contenido literal. Si sigue igual, va a `NO LEÍDO` |
| Un archivo llegó cortado | Límite de tamaño del fetch | Se pide el resto con desplazamiento, o va a `NO LEÍDO` |
| Error al pedir un `.svg`, `.jpg` o `.png` | El fetch no entrega imágenes | Sección 4.1 |
| Un preset llega como binario | La extensión no se sirve como texto | El gemelo `.txt` de la sección 5.1 |
| 404 en una ruta que empieza con `.ai/` | El servidor no publicó la carpeta con punto | El mismo archivo en `https://raw.githubusercontent.com/magoya/magoya-brand-system/main/` más la ruta |
| La foto o el logo no se ve en la pieza | El destino no carga recursos externos | Sección 4.2 |
| Dos reglas oficiales se contradicen | Fuentes de fechas distintas | Se aplica https://brand.magoya.com/ai/precedencia.json, se entrega y se reporta el conflicto. No se resuelve por criterio propio |
| Falta un valor: una medida, un margen, un mínimo | No está definido | Si no está en `tokens.json` ni en `ai/constraints.json`, se pregunta. No se asume |

## 7. Contrato de entrega

Toda entrega cumple estos puntos. Son verificables.

1. Un dato que no está en `ai/facts.json` va como `[PENDIENTE]`, nunca como el número que pasó la persona. Con un `[PENDIENTE]` adentro, la entrega se rotula `BORRADOR` y cierra con un bloque `PEDIDO A HUMANOS` que dice qué falta y a quién pedírselo.
2. Los clientes no se nombran sin autorización registrada.
3. Hecho validado, interpretación, hipótesis y ejemplo van distinguidos.
4. Se escribe AI en cualquier idioma. Única excepción: el nombre propio IA en Campo.
5. El vocabulario vetado de `vocabulary.json` es obligatorio.
6. Antes de entregar se corre `.ai/checklist-verbal.md` sobre el texto y `.ai/checklist.md` sobre lo visual, y la entrega cierra con una línea `CHECKLIST: <pasados>/<totales> · fallas: <cuáles>`.
7. IA en Campo es otra marca, con su propio sistema en https://brand.magoya.com/ai-en-campo/ : sus reglas no se aplican a Magoya, ni las de Magoya a IA en Campo.

## 8. Detalle por herramienta

Cada entrada agrega lo específico de su herramienta y se versiona por separado.

| AI | Entrada |
|---|---|
| Claude (claude.ai, Claude Code, API) | https://brand.magoya.com/ai/claude.md |
| ChatGPT (GPT, proyectos) | https://brand.magoya.com/ai/chatgpt.md |
| Gemini (app, AI Studio, Gems) | https://brand.magoya.com/ai/gemini.md |
| Cursor | https://brand.magoya.com/ai/cursor.md |
| GitHub Copilot | https://brand.magoya.com/ai/copilot.md |
| Cualquier otra AI con browsing | https://brand.magoya.com/ai/generic.md |

## 9. Mantenimiento

Para quien edita el repo. `python3 ai/generate.py` regenera `ai/assets.json` (con la ficha de cada foto), `ai/vectores.md` y sus tres partes, `.ai/presets/AGENTS.md`, `.ai/presets/cursor-rule.mdc.txt`, `llms-full.txt` y `ai/kit.zip`. `python3 ai/validar.py` falla si un vector propio no está en los archivos de vectores, si un archivo del modo `link` pasa los 60 KB, si un link publicado no tiene archivo o si la versión del sistema no es la misma en este documento, `llms.txt`, `BRAND.md`, `tokens.json` y el mensaje de `ai.html`.
