# Magoya Brand System · Roadmap maestro

> Única lista de pendientes y decisiones del sistema. Si algo no está acá, no existe.
> **Última actualización:** 2026-10-22 (feedback del equipo "Brand System Online - Magoya") · **Live:** https://brand.magoya.com/ · **Repo:** `magoya/magoya-brand-system` (público)
> **Proyecto hermano:** Magoya Studio → facundo-web.github.io/magoya-studio (produce las piezas de IA en Campo)
> El detalle de cada pedido de feedback, con su evidencia, vive en [`AUDITORIA-FEEDBACK.md`](AUDITORIA-FEEDBACK.md).

---

## Principio fundacional: el manual enseña, no solo dicta

> **Regla del dueño (2026-08-04):** *"lo que importa es CÓMO aplicamos el contenido y cómo la gente lo puede llegar a usar, porque muchos son literales con los criterios o las ideas pueden no aparecer. Este brand tiene que lograr eso educando, enseñando y compartiendo desde el mismo brand."*

Criterio de aceptación transversal: ninguna sección se considera terminada si solo enuncia una regla. Cada una cumple cuatro capas: **la regla** (verificable), **el ejemplo aplicado**, **el contraste** (hacer / evitar) y **el recurso listo** (el archivo o el bloque para ejecutarla ya).

- Todo asset que se puede usar tiene su ficha en el manual: qué es, cuándo se usa, cuándo no, y de dónde se baja.
- Preferir *mostrar* antes que *explicar*.
- Escribir para el lector literal: nada de "usá la identidad de Magoya"; sí "display 800, tracking −3%".
- Todo lo que una persona podría necesitar copiar (prompt, token, snippet, archivo) está a un click.

---

## 1. Qué cambió el 22 de octubre de 2026

Fuente: presentación de feedback del equipo y respuestas de Facu.

- **Navegación única** en todas las páginas: Inicio · Conocer la marca (Estrategia, Voz, Lenguaje, Aplicación, Identidad visual) · Recursos · Integrar con AI · IA en Campo.
- **Se retiraron del sistema** las piezas editables y todo lo que servía para armarlas (páginas, plantillas, módulos, generadores y validadores asociados). Se descarga solo lo que está en Recursos.
- **Recursos** (`library.html`): logo kit, Manrope, paleta (tokens), íconos, logos de clientes, membrete de documentos, fotos aéreas cenitales y el kit de IA en Campo.
- **Color:** el Verde Magoya `#133825` es el verde protagonista; el lima `#A2FF00` es solo para acentos, detalles, resaltar o CTA. La proporción por porcentajes quedó sin efecto.
- **Fotografía:** aérea de campo en color natural, con overlay verde profundo para fondos con texto, siempre cenital. Personas siempre a color, sin ningún detalle encima, mejor en espacios abiertos.
- **Sin ilustración.** Para resaltar una palabra: círculo o flechas, nunca subrayado.

---

## 2. Backlog

**Desbloquea**: quién tiene que producir algo o decidir para que el ítem avance. **nadie** = se puede hacer ya.

| # | Qué | Desbloquea |
|---|---|---|
| **B1** | Definir las **proporciones de uso del color** con el Verde Magoya como protagonista. Hasta entonces, la regla es cualitativa y ningún archivo publica porcentajes | **Varu** + diseño |
| **B2** | Fotos **a color** del equipo, en espacios abiertos. Hoy la única es la de Varu (`assets/photos/varu-ceo-color.jpg`) | **Facu** (sesión de fotos) |
| **B3** | Sumar, cuando estén listos, el **estilo de feed-placas** y el **Deck**. No se suman ahora | **equipo** |
| **B4** | Conseguir en vector los logos de clientes faltantes: **ProducePay**, **HabiTerre**, **IntelinAir** | **Facu** (pedir a los clientes o al diseñador) |
| **B5** | Unificar el contacto (hoy conviven `people@magoya.com` e `info@magoya.com`) | **Varu** |
| **B6** | Rol vigente de Camila López Colmano ("AgTech Expert" está a confirmar) | **Facu** |
| **B7** | Validar si **Staff Augmentation** sigue en la oferta | **Varu** |
| **B8** | Recibir y triagear el **listado de mejoras de Aye para Magoya Studio** | **Aye** |
| **B9** | Alivianar el repo: comprimir fotos, regenerar ZIPs, evaluar si los ZIPs se versionan o se generan en release | nadie |
| **B10** | Definir **gobernanza**: quién aprueba un cambio de marca, cómo se versiona, dónde se registran las decisiones | **Varu** (owner de marca) |
| **B11** | Resolver la **duplicación de assets** entre `brand-system/assets/studio/` y `magoya-studio/`: cuál es la fuente y cómo se sincroniza | nadie (decisión técnica) |
| **B12** | Backup del material fuente del diseñador: `assets/refs/` está gitignored y existe solo en la máquina de Facu | **Facu** |

Las decisiones abiertas de la capa para AI (capacidades en `facts.json`, marcador de lo no numérico, Agent Skill, `$schema` de `tokens.json`) están en [`.ai/VALIDACION-IA.md`](.ai/VALIDACION-IA.md).

---

## 3. Decisiones tomadas (no re-litigar)

### Identidad

| Decisión | Detalle |
|---|---|
| Tipografía | **Manrope** variable 200–800, self-hosted, OFL. Fallback **Arial**. Una sola familia |
| Wordmark | Redondeado, 4 versiones (verde digital sobre blanco · crema sobre verde profundo · negro sobre blanco · verde profundo sobre crema). Nunca reconstruir ni alterar espaciado. Aire mínimo = altura de la "m". Mínimo 90px pantalla / 24mm print |
| Avatares | Círculo `#00DE68` + marca blanca, 4 variantes. **cara** = redes de comunidad · **m** = monograma funcional (favicon, app icon, corporativo). No recolorear |
| Documentos | En documentos va **el wordmark**, no la cara |

### Color

| Rol | HEX | Regla |
|---|---|---|
| Verde Magoya | `#133825` | **El verde protagonista de Magoya**: fondos oscuros, overlays, texto sobre claro |
| Verde digital | `#00DE68` | Identidad (logo/avatares) y data-viz. Como texto **solo sobre oscuro** |
| Lima | `#A2FF00` | **Solo acentos, detalles, resaltar o CTA.** Nunca texto sobre blanco (1.25:1) |
| Crema Magoya | `#ECE3DB` | Neutro cálido; texto sobre verde profundo |
| Sage | `#EEF2EC` | Superficie clara |
| Negro Magoya | `#161616` | Texto, titulares, cards dark |

- **Proporciones de uso: pendientes de definir** (B1). No se aplican porcentajes.
- Verde sobre blanco como texto = `#009145` y solo ≥24px bold. Captions sobre claro: mínimo `#6E756D`. **Accesibilidad no negociable.**
- Lima ≠ logo. El wordmark usa una de sus cuatro variantes (verde, crema, negro, verde profundo) según el fondo.

### Recursos visuales

| Decisión | Detalle |
|---|---|
| Fotografía | Aérea de campo en color natural, con **overlay verde profundo 55–86%** cuando lleva texto (el único gradiente permitido), **siempre cenital**. **Personas siempre a color**, sin ningún detalle encima, mejor en espacios abiertos |
| Ilustración | **No hay.** Magoya no usa ilustración |
| Resaltar | Un **círculo** que rodea la palabra o **flechas** que la señalan. Verde digital sobre claro / lima sobre oscuro, nunca negro. **Nunca subrayado** y **nunca** bloque resaltador sólido detrás de palabras |
| Iconografía | Línea 2px, terminaciones y esquinas redondeadas, grid 24×24, `currentColor`. Lima solo en el ícono destacado (uno por pieza). Nunca relleno sólido ni 3D. Completar volumen con Lucide |
| Botón ≠ chip | **Botón** = rectángulo radio 10px, fondo sólido. **Chip** = pill outline (borde y texto del mismo color, fondo transparente). Nunca chip sólido ni botón pill |
| Tipografía en pieza | Máximo **3 niveles por pieza**. El peso hace la jerarquía |
| Logos de clientes | **SIEMPRE reales**, en gris, grilla pareja. Jamás placeholders |
| Estética | **Que no se vea hecho por AI**: sin gradientes, 3D, glossy ni simetría perfecta |

### Arquitectura del sistema

| Decisión | Detalle |
|---|---|
| Dos marcas, dos manuales | El core (`brand-book.html`) y **IA en Campo** (`ai-en-campo.html`) son **marcas separadas**. IA en Campo rompe 3 reglas del core **a propósito** (fondo verde digital pleno · placa negra con crema para el dato clave · ruido controlado de 2–4 doodles ±5–15°). **Nada de eso vuelve al core** |
| Producción de IA en Campo | Sus piezas se producen en Magoya Studio y la receta queda en un `.magoya.json`: esa es la fuente para reproducir una pieza, no el ojo |
| Capa para AI | `BRAND.md` (doctrina) + `tokens.json` (valores) + `tokens.css` (4 temas) + `llms.txt` / `llms-full.txt`. El equipo trabaja la marca en el proyecto de Claude "Magoya · Marca" (`ai.html`) |
| Material fuente | `assets/refs/` (25 MB del diseñador) **excluido del repo** vía `.gitignore` |

---

## 4. Descartado y por qué

| Descartado | Por qué |
|---|---|
| **Piezas editables** | Decisión del equipo (22 oct 2026): se descargan tipografías, elementos y paleta, no piezas hechas o para editar |
| **Ilustración** | "Ilustración no tenemos" (feedback del 22 oct 2026) |
| **Motivos gráficos decorativos** | Retirados con la ilustración |
| **Fotos de personas en blanco y negro o con acento de color encima** | Las personas van siempre a color y sin detalle |
| **Proporción de color por porcentajes** | Quedó sin efecto con el Verde Magoya como protagonista; la nueva está pendiente (B1) |
| **Regla de máximo dos recursos gráficos por pieza** | Borrada en el feedback del 22 oct 2026 |
| **Subrayado a mano** | Para resaltar una palabra: círculo o flechas |
| **Metáfora del puzzle** | Símbolo del brand viejo, retirado |
| **Naranja y amarillo** | Colores del brand viejo, fuera de la paleta |
| **Resaltador / marcador sólido detrás de texto** | Regla de dirección de arte |
| **Wordmark en lima** | Uso incorrecto. El logo es verde digital `#00DE68` |

---

## 5. Riesgos

| # | Riesgo | Mitigación |
|---|---|---|
| **R1** | **Doble fuente de verdad brand-system ↔ magoya-studio.** Iconos, doodles y badge están copiados en los dos repos | B11 |
| **R2** | **Bus factor = 1.** Facu produce, decide la ejecución y tiene el material fuente | B10 + B12 |
| **R3** | **Logos de terceros en repo público.** Hay nota de uso nominativo en `README.md` | Mantener la nota; retirar cualquier logo ante pedido del titular |
| **R4** | **Documentos desincronizados entre sí.** La capa para AI se lee sin criterio propio | Al cambiar una regla en el manual visual, actualizar `BRAND.md`, `tokens.json`, `llms.txt` y los presets en el mismo cambio; correr `python3 ai/generate.py` y `python3 ai/validar.py` |
