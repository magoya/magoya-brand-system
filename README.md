# Magoya Brand System

Sistema de marca oficial de **Magoya**, consultora hands-on en software y AI para empresas del agro. Una sola fuente de verdad, consumible por personas y por AIs.

**v2.0 (octubre de 2026):** la estructura sale del Magoya Brand Playbook. Las partes A–D (estrategia, voz, lenguaje, aplicación) salen del playbook; desde la v2.1, la voz y el tono aplicados salen de la Guía editorial de voz y tono V2 (`.ai/verbal/guia-editorial.md`). La identidad visual se actualizó con el feedback del equipo del 22 de octubre de 2026.

**Live:** https://brand.magoya.com/

**Regla madre:** todo asset que se puede usar tiene que estar en el brand, con su ficha: qué es, cuándo se usa, cuándo no, y de dónde se baja.

## Para personas

Todas las páginas comparten la misma barra de navegación (`nav.css` + `nav.js`): Inicio · Conocer la marca (Estrategia, Voz, Lenguaje, Aplicación, Identidad visual) · Recursos · Integrar con AI · IA en Campo.

| Sección | Página | Qué hay |
|---|---|---|
| Inicio | [`index.html`](index.html) | Qué es Magoya en una línea, mapa del sistema, qué documento manda, versiones, entrada para AI |
| Estrategia | [`estrategia.html`](estrategia.html) | Quiénes somos, propósito, diferenciales, propuesta de valor, oferta, boilerplate, territorios y Usage Loop, audiencias, razones para creer, Método Magoya, valores, pilares, promesa, personalidad, arquitectura, tagline |
| Voz | [`voz.html`](voz.html) | Desde la Guía editorial V2: la voz en la práctica, personalidad, ejes, cómo construimos mensajes, adaptación por audiencia, mercado, canal y vocero, ejemplos. Del playbook: qué se construye primero, objetivos por mercado, postura, contra qué lucha, lo que no dice |
| Lenguaje | [`lenguaje.html`](lenguaje.html) | Estilo y lenguaje, expresión verbal (los siete principios), vocabulario de marca, AI (no IA), glosario ES/EN/PT, cómo suena Magoya, reglas de oro verbales |
| Aplicación | [`aplicacion.html`](aplicacion.html) | Capas de la marca, voceros y territorios, canales e idioma, focos de contenido y producción |
| Identidad visual | [`brand-book.html`](brand-book.html) · [`icons.html`](icons.html) | Logo, color, tipografía, fotografía, iconografía, componentes, reglas de oro visuales · librería de 58 íconos |
| Recursos | [`library.html`](library.html) · [`logos.html`](logos.html) | Lo que se descarga: logo kit, Manrope, paleta (tokens), íconos, logos de clientes, membrete de documentos, fotos aéreas cenitales y de personas, posteos de redes y el deck base (referencias en PNG y PDF) y el kit anterior de IA en Campo |
| IA en Campo | [`ai-en-campo/`](ai-en-campo/) | Sistema de marca propio del programa presentado por Magoya (sitio aparte, octubre 2026): esencia, logo, paleta, tipografía, imágenes, íconos, piezas, YouTube, personaje, componentes y recursos. `ai-en-campo.html` redirige ahí |
| Integrar con AI | [`ai.html`](ai.html) | El proyecto de Claude "Magoya · Marca": cómo se usa, cómo se valida lo que devuelve y cómo se administra |

Estilos compartidos: `manual.css` (base del manual, extraída del brand book), `playbook.css` (componentes de la capa verbal), `nav.css` y `nav.js` (navegación). `manual.js` maneja el índice lateral y el alto del topbar.

## Para AIs

Si sos una AI escribiendo o revisando contenido para Magoya, leé **en este orden**:

1. [`BRAND.md`](BRAND.md) — la doctrina completa en Markdown (reglas, roles de color, prohibiciones). Sus reglas visuales espejan las del brand book visual.
2. [`tokens.json`](tokens.json) — todos los valores exactos: paleta con roles y reglas de accesibilidad, regla de uso del color, tipografía, espaciado, radios, layouts de export y rutas de assets.
3. [`tokens.css`](tokens.css) — los mismos tokens como custom properties CSS con 4 temas (`default` verde profundo, `light`, `paper`, `studio`).
4. [`llms.txt`](llms.txt) — el resumen corto y estable de la marca para agentes.
5. [`.ai/`](.ai) — prompts listos para pegar (`brand-prompt.md`, `brand-prompt-short.md`), los checklists de validación (`checklist.md` visual, `checklist-verbal.md` de texto) y presets por herramienta (`.ai/presets/`). La guía de uso está en [`ai.html`](ai.html).

Reglas mínimas si solo vas a leer una cosa: Manrope; el Verde Magoya `#133825` es el verde protagonista; lima `#A2FF00` en poca superficie: acentos, detalles, CTA o resaltar una palabra (la frase clave sobre oscuro va en Verde digital #00DE68), y nunca como texto sobre blanco; el Verde Magoya ocupa la mayor superficie y el lima mucha menos (sin porcentajes definidos); logo/avatares = `#00DE68`; fotos aéreas cenitales con overlay verde profundo si llevan texto; personas siempre a color, sin ningún detalle encima; no hay ilustración; para resaltar, color o el círculo gestual nuevo, nunca subrayado; emojis prohibidos salvo manitos que señalan y banderas; el monograma "m" no va en cards; nada de gradientes glossy, puzzle, naranja ni amarillo.

## Assets

```
assets/
├── magoya-wordmark-{green,cream,black,deep}.svg
├── magoya-wordmark-animado.svg   # versión animada para web
├── avatars/          # go · o · cara · m (vectoriales)
├── favicon/          # favicon.svg + favicon-{16,32,180,512}.png
├── marks/            # miscelánea gestual: 6 flechas, 2 círculos, 2 X y 2 ✓
├── components/       # CTA (pill 44px) y box (radio 12px)
├── icons/            # los 58 íconos del sistema (export de icons.html)
├── photos/           # aéreas cenitales + personas a color
├── social/           # posteos de redes de referencia (PNG 1080×1350)
├── deck/             # deck base institucional (PDF + previews)
├── logos/clients/    # clientes reales
├── logos/partners/   # partners tecnológicos
├── logos/*.svg       # logos de cuentas objetivo
├── studio/icons/     # espejo de Magoya Studio: iconos agro, logos de AI y de redes
├── downloads/        # ZIPs por sección + doc-header/footer (membrete)
├── refs/             # MATERIAL FUENTE — no publicable, ver abajo
└── font/manrope/     # Manrope variable 200–800 (OFL)
```

La lista completa y vigente, con URL directa y regla de uso por carpeta, está en [`ai/assets.json`](ai/assets.json) (lo regenera `python3 ai/generate.py`).

**`assets/refs/` es material fuente, no un asset del sistema.** Son los exports originales del diseñador (~25 MB) que sirvieron de referencia de trazado. No se enlazan desde ninguna página, no se distribuyen y no tienen ficha en `library.html`. Si algo de ahí tiene que poder usarse, primero se produce como asset aprobado y se le hace su ficha.

**IA en Campo** tiene su propio sistema de marca y sus propios archivos en `ai-en-campo/` (fuera de `assets/`). Los archivos de su identidad anterior (doodles, piezas, silueta, kit .zip) se retiraron el 29 oct 2026.

## Documentos de trabajo

No son parte del manual — son el registro de por qué el manual dice lo que dice.

| Archivo | Qué es |
|---|---|
| [`AUDITORIA-FEEDBACK.md`](AUDITORIA-FEEDBACK.md) | Cada pedido de feedback con su estado verificado, la evidencia (archivo:línea) y el criterio de aceptación. Incluye el roadmap por olas y las contradicciones abiertas |
| [`ROADMAP.md`](ROADMAP.md) | Roadmap maestro y decisiones tomadas que no se re-litigan |

## Desarrollo

Sitio estático — no hay build. Servir la carpeta con cualquier server:

```bash
python3 -m http.server 5501 --directory .
```

`python3 ai/generate.py` regenera la capa para AI (íconos, `ai/assets.json`, `llms-full.txt`) y `python3 ai/validar.py` la valida.

---

Manrope © The Manrope Project (OFL). Logos de clientes/partners: marcas registradas de sus dueños, uso nominativo.
