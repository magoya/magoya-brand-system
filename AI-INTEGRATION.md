# Cómo darle el manual de Magoya a una AI

> **Equipo de Magoya:** esta guía por herramienta quedó como referencia técnica. El trabajo de marca del equipo se hace en el proyecto oficial de Claude "Magoya · Marca"; nadie configura su propia herramienta. Ver [ai.html](ai.html).

Guía de setup, herramienta por herramienta. El objetivo es que cualquier AI que use el equipo respete el manual sin que haya que recordárselo en cada prompt.

**Fuente de verdad:** [`BRAND.md`](BRAND.md) (doctrina) · [`tokens.json`](tokens.json) (valores exactos con roles) · [`tokens.css`](tokens.css) (custom properties, 4 temas). Todo lo demás de este repo es presentación.

**Capa para IAs:**

| Archivo | Qué es | Cuándo se usa |
|---|---|---|
| [`llms.txt`](llms.txt) | Índice según la convención [llmstxt.org](https://llmstxt.org/): resumen del sistema, las 10 reglas que más se rompen, y links absolutos a cada recurso con una línea de descripción | Cuando la AI puede navegar. Le pegás una URL y entiende el sistema entero |
| [`.ai/brand-prompt.md`](.ai/brand-prompt.md) | Prompt de sistema canónico, autocontenido (~500 palabras) | Cuando la AI **no** puede navegar ni leer archivos: lo pegás y ya |
| [`.ai/brand-prompt-short.md`](.ai/brand-prompt-short.md) | Versión de ~120 palabras | Chat suelto, un solo pedido |
| [`.ai/checklist.md`](.ai/checklist.md) | 17 chequeos verificables (visuales) | Antes de publicar cualquier cosa que devolvió una AI |
| [`.ai/presets/`](.ai/presets/) | Un archivo por herramienta, listo para copiar sin editar | Setup inicial |

---

## Tabla comparativa

| Herramienta | Qué le doy | Dónde lo pego / subo | Cómo lo verifico |
|---|---|---|---|
| **Claude Projects** (claude.ai) | `.ai/presets/claude-project-instructions.md` como project instructions + `BRAND.md`, `tokens.json`, `tokens.css` en Project knowledge | Project settings → instructions; "Add content" → files | Preguntá *"¿qué hex uso para un CTA sobre fondo blanco y por qué no el lima?"* → tiene que responder lima `#A2FF00` de fondo con texto `#161616`, y explicar que el lima como **texto** sobre claro está prohibido (1.25:1) |
| **Claude Code** | `.ai/presets/claude-code-CLAUDE.md` como `CLAUDE.md` del repo (o `~/.claude/CLAUDE.md`, o `.claude/rules/magoya-brand.md` con `paths:`) | Raíz del repo | Corré `/context` y confirmá que aparece bajo **Memory files**. Después pedí un botón: tiene que salir `border-radius:10px`, nunca pill |
| **Claude Design** (claude.ai/design) | El repo `magoya/magoya-brand-system` como fuente del design system, o `/design-sync` desde Claude Code apuntando a esta carpeta | Onboarding de Claude Design → "Link a code repository"; o `/design-sync` | Pedí una landing y revisá que use Manrope y los hex de `tokens.css`. Claude Design chequea su propio output contra el design system importado |
| **Custom GPT** (ChatGPT) | `.ai/presets/custom-gpt-instructions.md` en Instructions + `BRAND.md` y `tokens.json` en Knowledge | GPTs → Create → Configure | Pedí un carrusel y contá emojis: tienen que ser cero (salvo manitos hacia un CTA o banderas) |
| **ChatGPT Projects** | Mismo texto en Project instructions + los mismos archivos como referencia | Project settings (los tres puntos arriba a la derecha) | Igual que arriba |
| **Cursor** | `.ai/presets/cursor-rule.mdc` como `.cursor/rules/magoya-brand.mdc` (o `.cursorrules` legacy) | Raíz del repo | Escribí un componente y mirá si usa `var(--color-energy)` o hex sueltos random |
| **GitHub Copilot** | `.ai/presets/copilot-instructions.md` como `.github/copilot-instructions.md` | Carpeta `.github/` del repo | En Copilot Chat pedí un card oscuro: tiene que salir `#133825` o `#161616`, sin gradiente |
| **Chat genérico** (Gemini, Perplexity, un LLM por API, un chat nuevo de cualquier cosa) | `.ai/brand-prompt-short.md` pegado como primer mensaje. Si la herramienta navega, agregá la URL de `llms.txt` | Primer mensaje del chat | Pedí que repita las tres reglas de color antes de generar |

---

## Setup detallado

### 1. Claude Projects (claude.ai)

El camino más rentable para el equipo no técnico: se configura una vez y todos los chats del proyecto heredan la marca.

1. claude.ai → **Projects** → *New project*. Nombre: `Magoya — Marca`.
2. Abrí **Set project instructions** y pegá el contenido de [`.ai/presets/claude-project-instructions.md`](.ai/presets/claude-project-instructions.md) (todo lo que está debajo del separador `---`).
3. En **Project knowledge** → *Add content* subí `BRAND.md`, `tokens.json` y `tokens.css`. Projects acepta `.md`, `.txt`, `.json`, `.csv`, `.html`, `.pdf`, `.docx` y otros, hasta 30MB por archivo; la cantidad de archivos está limitada por el context window, y en planes pagos hay recuperación por RAG sobre el knowledge.
4. Cuando cambie el manual, **volvé a subir los tres archivos** — el knowledge no se sincroniza solo con el repo.

Qué esperar: responde preguntas de marca citando los archivos, y las piezas y el copy salen on-brand sin recordatorios. No genera imágenes: para piezas visuales usá Claude Design o el Magoya Studio.

### 2. Claude Code

1. Copiá [`.ai/presets/claude-code-CLAUDE.md`](.ai/presets/claude-code-CLAUDE.md) a la raíz del repo como `CLAUDE.md`. Si ya existe uno, pegá la sección al final en vez de sobrescribir.
2. Alternativas según el caso:
   - Para **todos** tus proyectos: `~/.claude/CLAUDE.md`.
   - Para un repo grande donde solo el front toca la marca: `.claude/rules/magoya-brand.md` con frontmatter `paths: ["**/*.{css,scss,html,jsx,tsx,vue,svelte,svg}"]`, así carga solo cuando Claude abre esos archivos.
   - Si el repo ya usa `AGENTS.md` para otras herramientas: Claude Code **no** lee `AGENTS.md`, así que dejá un `CLAUDE.md` con `@AGENTS.md` en la primera línea y la sección de marca debajo.
3. Verificá con `/context`: tiene que aparecer bajo **Memory files**.

Qué esperar: el CLAUDE.md es contexto, no configuración forzada — Claude lo sigue con mucha más consistencia si las reglas son concretas y verificables, que es exactamente cómo está escrito el preset. Apuntá a mantenerlo bajo 200 líneas.

### 3. Claude Design (claude.ai/design)

Claude Design construye un design system para el equipo leyendo tu código y tus archivos de diseño durante el onboarding, y después cada proyecto hereda automáticamente colores, tipografía y componentes.

Dos caminos, en orden de preferencia:

- **Repo de GitHub**: en el onboarding, linkeá `magoya/magoya-brand-system`. Lo que hace que esto funcione bien es `tokens.css`: dos capas de custom properties con roles explícitos y 4 temas. Claude Design extrae de ahí la paleta, la tipografía y los patrones de componentes.
- **`/design-sync` desde Claude Code**: parado en esta carpeta, corré `/design-sync`. Trae el design system local al proyecto de Claude Design.

Al generar, Claude Design construye con los componentes del design system real y **chequea su propio output contra él antes de mostrártelo**. Si el equipo es Enterprise, un admin tiene que habilitarlo en Organization settings (viene apagado), y el rol *Claude Design Admin* permite aprobar un sistema estándar y bloquear ediciones.

Advertencia de la documentación oficial: *"Design system import is only as good as its source"* — si el `tokens.css` estuviera desordenado, eso aparece en el output. Está ordenado, mantenelo así.

Si el import no toma bien algo, el camino de rescate es genérico y siempre funciona: adjuntá `BRAND.md` como primer mensaje de la sesión y pedí que sea la fuente de verdad de todas las decisiones de diseño de esa sesión.

### 4. Custom GPT (ChatGPT)

1. chatgpt.com → **GPTs** → *Create* → pestaña **Configure**.
2. Nombre: `Magoya Brand`. En **Instructions** pegá [`.ai/presets/custom-gpt-instructions.md`](.ai/presets/custom-gpt-instructions.md) (lo que está debajo del separador). Entra con margen en el límite de 8.000 caracteres del campo.
3. En **Knowledge** subí `BRAND.md` y `tokens.json`. Máximo 20 archivos por GPT. Si el uploader rechaza `tokens.css`, renombralo a `tokens-css.txt` y subilo así.
4. Dejá **Code Interpreter** activado: es lo que le permite leer el JSON con precisión en vez de parafrasearlo.

Para un uso más liviano, **ChatGPT Projects** acepta el mismo texto en *Project settings → instructions* y los mismos archivos como referencia, sin tener que publicar un GPT.

Qué esperar: buen copy y buen HTML/CSS. Si generás imágenes, el modelo de imagen **no** lee el Knowledge: describí la paleta y las prohibiciones dentro del prompt de imagen.

### 5. Cursor

1. Guardá [`.ai/presets/cursor-rule.mdc`](.ai/presets/cursor-rule.mdc) como `.cursor/rules/magoya-brand.mdc`, con el bloque de frontmatter que viene incluido.
2. `.cursorrules` (archivo único en la raíz) sigue funcionando pero está deprecado, y **se ignora en modo Agent**. Si las reglas "dejaron de aplicarse", esto es casi siempre la causa: migrá al `.mdc`.
3. El preset viene con `alwaysApply: true` y un `globs` de archivos de front. Si el repo tiene mucho backend, poné `alwaysApply: false` y dejá que el glob decida.

### 6. GitHub Copilot

1. Guardá [`.ai/presets/copilot-instructions.md`](.ai/presets/copilot-instructions.md) como `.github/copilot-instructions.md`. Se lee en cada request de Copilot Chat y de los agentes, en el IDE y en github.com.
2. Si querés limitarlo al front, movelo a `.github/instructions/magoya-brand.instructions.md` y agregale frontmatter `applyTo: "**/*.{css,scss,html,jsx,tsx,vue,svelte,svg}"`.
3. No metas el manual completo ahí: instrucciones cortas y concretas rinden más que volcar contexto.

### 7. Chat genérico (Gemini, Perplexity, un LLM por API, un chat nuevo)

- **Si la herramienta navega**: primer mensaje →
  > Leé https://brand.magoya.com/llms.txt y seguí ese sistema de diseño en todo lo que generes en esta conversación. Empezá confirmando las tres reglas de color.
- **Si no navega**: pegá [`.ai/brand-prompt-short.md`](.ai/brand-prompt-short.md) (120 palabras) o [`.ai/brand-prompt.md`](.ai/brand-prompt.md) (~500 palabras, todas las prohibiciones) como primer mensaje.
- **Por API**: `.ai/brand-prompt.md` va como `system`. Es autocontenido a propósito: no depende de ningún adjunto.

### 8. Un servidor MCP para el brand system (a evaluar, no implementado)

Tiene sentido, y el diseño sería directo con los tres primitivos de MCP:

- **Resources** (contexto read-only direccionable por URI): `magoya://brand/doctrine` → `BRAND.md`, `magoya://tokens` → `tokens.json`, `magoya://tokens/css` → `tokens.css`, `magoya://assets/{nombre}` → los SVG de wordmarks, avatares e íconos.
- **Tools**: `validate_piece(html_or_svg)` que corra la checklist programáticamente (hex fuera de paleta, uso del lima, emojis, gradientes) y devuelva las violaciones; `get_token(path)` para consultas puntuales; `list_client_logos()` para que ninguna AI vuelva a inventar un logo.
- **Prompts**: `magoya_system_prompt` (el contenido de `.ai/brand-prompt.md`) y `review_piece` (la checklist como plantilla de revisión).

**Cuándo vale la pena:** cuando el equipo empiece a generar piezas en volumen y la validación manual sea el cuello de botella — el valor real está en `validate_piece`, que convierte la checklist en algo determinístico. Hasta entonces, `llms.txt` + los presets cubren el 90% con cero mantenimiento.

---

## Troubleshooting

### La AI inventa colores

Síntoma: aparece un verde "parecido" (`#2ECC71`, `#4CAF50`), un naranja, o un hex que no está en `tokens.json`.

1. Confirmá que el knowledge / el archivo de reglas está realmente cargado — no que está subido, que está **cargado en la sesión**. En Claude Code: `/context` → *Memory files*. En Claude Projects: preguntá *"¿qué archivos tenés en el knowledge?"*.
2. Pedí la paleta antes de pedir la pieza: *"listame los 7 hex oficiales con su rol"*. Si no los sabe, el problema es el setup, no el prompt.
3. En código, exigí tokens en vez de hex: *"usá solo `var(--…)` de `tokens.css`; si no hay token para algo, decímelo"*.
4. Corré el punto 1 de [`.ai/checklist.md`](.ai/checklist.md): extraé todos los hex de la salida y comparalos contra `tokens.json`.

### La AI mete emojis

Es el fallo más terco: los modelos los usan por defecto en bullets, títulos y labels.

1. La regla completa es: **cero emojis**, salvo manitos que señalan (👈 👉 👇) apuntando a un CTA y banderas de países para geografía.
2. Si insiste, agregá una instrucción de salida explícita: *"antes de responder, revisá tu texto y borrá todo emoji que no sea 👈 👉 👇 apuntando a un CTA o una bandera de país"*. Los modelos cumplen mucho mejor una instrucción de auto-revisión que una prohibición suelta.
3. En Claude Code, si tiene que ser inviolable, un [hook `PreToolUse`](https://code.claude.com/docs/en/hooks-guide) que rechace escrituras con emojis es enforcement real; el archivo de instrucciones es solo contexto.

### La AI mete gradientes, glass o 3D

Es el default estético de casi todos los modelos entrenados con landings genéricas.

1. Nombrá la prohibición en positivo: *"color plano; el único gradiente permitido en toda la marca es el overlay verde profundo sobre foto aérea: `linear-gradient(180deg, rgba(12,33,23,.55), rgba(12,33,23,.86))`"*.
2. En código, pedí un grep de la salida: *"buscá `gradient`, `backdrop-filter` y `box-shadow` con brillo en lo que escribiste y quitalos"*.

### La AI vuelve a recursos retirados

Síntoma: aparece el **puzzle**, naranja o amarillo, ilustración, o una foto de persona en blanco y negro.

1. Es memoria del brand viejo, no del manual: alguien la alimentó con material 2017-2024 o con la web anterior. Revisá qué archivos hay en el knowledge y borrá lo viejo.
2. Enunciá el reemplazo, no solo la prohibición: los acentos son lima o verde, nunca naranja ni amarillo; las personas van siempre a color; Magoya no usa ilustración.
3. Si es una pieza heredada que hay que actualizar, decilo de entrada: *"esta pieza es del brand viejo; rehacela con el manual actual"*.
4. Cuidado especial con las **fotos y los logos de clientes**: la regla es foto real y logos reales de `assets/logos/clients/`. Si falta el asset, la AI tiene que decirlo, no dibujarlo.

### La AI mezcla "IA en Campo" con el core

`ai-en-campo/` es una **marca anexa con sistema de marca propio**: paleta propia (verde profundo #003922, lima #80FF00, violeta eléctrico #B700FF, blanco, negro), Plus Jakarta Sans + Helvetica, íconos pixelados, personaje y componentes con esquinas cortadas. Si aparece violeta, Plus Jakarta Sans o una esquina cortada en una pieza institucional, la AI cruzó los manuales. Decile explícitamente en qué marca estás trabajando antes de pedir la pieza.

### La AI cumple al principio y se olvida a los 20 mensajes

1. En conversaciones largas, las instrucciones de sistema pesan menos que los últimos mensajes. Volvé a pegar [`.ai/brand-prompt-short.md`](.ai/brand-prompt-short.md) o pedí *"corré la checklist sobre esto"*.
2. En Claude Code, el `CLAUDE.md` de la raíz del proyecto se re-inyecta después de `/compact`; las instrucciones dadas solo en el chat, no. Si una corrección importa, va al archivo.
3. Para sesiones largas de producción, arrancá una conversación nueva por pieza.

### Notas de publicación

- Las URLs de `llms.txt` que apuntan a `.ai/…` usan `raw.githubusercontent.com` a propósito: GitHub Pages está sirviendo este repo con el build **legacy (Jekyll)**, que ignora archivos y carpetas que empiezan con punto, así que `…github.io/magoya-brand-system/.ai/brand-prompt.md` devuelve 404. Si querés que la carpeta `.ai/` también se sirva desde el dominio de Pages, agregá un archivo vacío `.nojekyll` en la raíz del repo y volvé a publicar.
- Cuando cambie `BRAND.md` o `tokens.json`, actualizá también `.ai/brand-prompt.md` y `.ai/checklist.md`: son copias deliberadas, pensadas para funcionar sin conexión al repo.
