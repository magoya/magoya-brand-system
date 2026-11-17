# Validación de la fusión AI ↔ brand system

Registro de las corridas del agente semanal. Protocolo:
[`agente-validacion-ia.md`](agente-validacion-ia.md). Lo más nuevo arriba.

La métrica que se sigue corrida a corrida es **la prueba a ciegas**: cuántos chequeos pasa un
contenido hecho por una AI que solo recibió un link. Todo lo demás es diagnóstico de por qué.

Las corridas anteriores al 22 de octubre de 2026 quedan en el historial de git; acá siguen solo las
decisiones que todavía aplican.

---

## 2026-11-17 · La marca se consume desde cualquier AI

**Decisión (Facu):** Integrar con AI deja de tener un único proyecto oficial. El foco es uno: la marca
se consume desde la AI que cada uno use, por link, con archivos cargados o desde un repo.

**Lo que se probó, con el fetch de Claude contra brand.magoya.com:**

- Llegan: `ai/claude.md`, `.ai/checklist.md`, `ai/assets.json`, `llms.txt`.
- No llegan: `assets/magoya-wordmark-cream.svg` y `assets/photos/field-mosaic-16x9.jpg` (el fetch
  devuelve error). Un archivo de imagen pedido por su URL no se puede consumir, aunque sea un SVG.
- Caché: `ai/claude.md` devolvió la versión 1.5 (11 de agosto). La misma URL con `?v=` devolvió la
  2.0 (22 de octubre), que es la publicada. Una AI puede estar leyendo una copia de hace meses.

**Lo que se cambió:**

- `ai/vectores.md` (generado): el código SVG de los vectores propios, como texto.
- `ai/assets.json`: clave `fotos` con la ficha de cada foto y clave `como_se_consume`.
- `.ai/presets/AGENTS.md` (generado desde el preset de Copilot) para agentes de repo.
- `ai/protocolo.md` es el protocolo de consumo: la especificación técnica que ejecuta la AI (primera
  respuesta obligatoria, modo de lectura, orden de archivos, assets por tipo, instalación por herramienta,
  fallas conocidas, contrato de entrega). `ai.html` queda mínima: un mensaje para pegar y un ZIP.
- `ai/kit.zip` (generado): los nueve archivos para cargar cuando la AI no abre links.
- Las entradas piden informar la versión leída; `ai.html` muestra la vigente, leída de `llms.txt`.
- `ai/validar.py` suma `check_consumo`: falla si un vector propio no está en `vectores.md`, si el kit
  quedó viejo o si la versión del sistema difiere entre archivos.
- Sistema a la versión 1.4.

**Prueba de estrés del mismo día. Lo que rompió y cómo quedó:**

| Prueba | Resultado | Arreglo |
|---|---|---|
| Fetch de `llms-full.txt` publicado | Llegaron 100.000 de 153.000 caracteres: lo corta | En modo link el protocolo ya no lo usa: manda a leer archivos sueltos según la tarea, todos de menos de 60 KB. `validar.py` falla si alguno pasa |
| Fetch de `.ai/presets/cursor-rule.mdc` | Llega como binario | Gemelo `cursor-rule.mdc.txt`, generado |
| `vectores.md` de un solo archivo (unos 100 KB) | Al borde del corte | Partido en `ai/vectores/logo.md`, `iconos.md` y `miscelanea.md` para link; el archivo único queda para cargar |
| Pegar inline avatares, favicon e íconos | 79 de 98 no traen ancho ni alto: sin CSS no se ven | Cada vector dice su viewBox y si necesita tamaño por CSS |
| Caché del protocolo | Una URL ya conocida puede devolver una copia vieja durante meses | Protocolo en una URL nueva (`ai/protocolo.md`) y el mensaje de `ai.html` lleva `?v=<versión>`; el protocolo pide `?v=` en cada archivo |
| Pieza en un artifact de Claude | El visor bloquea imágenes y CSS remotos | Tabla «Dónde va a vivir la pieza» (sección 4.2 del protocolo) |
| Link con `?v=` en el validador | `check_links` lo daba por roto | El validador ignora el query string |
| Texto con forma de orden al modelo | Un fetch lo trató como texto incrustado y no lo siguió | El protocolo está escrito como especificación y el mensaje de la persona es el que pide seguirlo |

Pasaron sin cambios: los 98 bloques son XML válido, idénticos a su archivo y renderizan; el ZIP abre y trae
los nueve archivos al día; todas las URLs y rutas del protocolo existen; las 9 fotos tienen ficha; el espejo
`raw.githubusercontent.com` responde; una pieza armada solo con el kit pasa `validar.py --entrega`; en
`ai.html` la versión y el link del mensaje se actualizan solos desde `llms.txt`, el botón copia el mensaje
exacto y en 390 px no hay desborde.

**Sin probar todavía, porque necesita el sitio publicado:** el protocolo leído por link (los archivos nuevos
todavía no existen en brand.magoya.com), la prueba a ciegas con una AI que no vio este trabajo, y el mismo
mensaje en ChatGPT, Gemini, Cursor y Copilot. Lo que el protocolo dice de cada herramienta sale de su
documentación, no de una corrida.

**Abierto:**

- Esta rama (`playbook-oct-es-en`) no está publicada: lo que sirve brand.magoya.com es `main`.
- `magoya-wordmark-animado.svg` tiene otra geometría que el wordmark estático (`validar.py` lo marca
  como falla desde antes de este cambio). Mientras no se resuelva, viaja también en `vectores.md`.

---

## Necesita tu decisión (abiertas al 2026-10-22)

1. **Proporciones de uso del color.** La proporción por porcentajes quedó sin efecto con el feedback
   del equipo del 22 de octubre y todavía no hay una nueva. Está declarada en
   `ai/constraints.json` (`pendiente_de_definir`).
2. **Fotos a color del equipo.** Hay tres: la de Varina Baldi y dos del equipo en el campo (26 oct 2026).
   Sumar más si el equipo elige otras.
3. **`facts.json` no tiene un campo de capacidades.** Un pedido del tipo "anunciá una capacidad
   concreta del equipo" no tiene de dónde responder qué capacidades hay: el archivo tiene empresa,
   cifras, clientes y equipo. ¿Qué capacidades se pueden anunciar?
4. **Falta el marcador de lo NO numérico.** `[PENDIENTE]` está pensado para cifras; un nombre de
   servicio, un claim de posicionamiento o una oferta comercial no tienen instrumento. ¿Se extiende
   `[PENDIENTE]` a texto, o va un marcador nuevo?
5. **"Staff Augmentation" sigue como pendiente de validación en `BRAND.md`.** ¿Se valida o se saca?
6. **La ley de precedencia no cubre los documentos que el sistema manda usar:** `ai/claude.md` (el
   punto de entrada), `ai/metodo.md` y `.ai/brand-prompt.md`.
7. **El aviso anti-resumen no alcanza.** Una herramienta de fetch que resume el archivo resume
   también el aviso que le pide no resumir. La lista plana de URLs ayuda; moverla al principio de
   las entradas es la propuesta abierta.
8. **Publicar el brand system como Agent Skill**, generada desde las mismas fuentes que
   `generate.py`. Es un target de salida más, no un rediseño. Antes de moverlo, medirlo: mismo
   pedido por URL y por skill, contando tokens y turnos.
9. **`$schema` de `tokens.json`.** DTCG pide `$value`/`$type` y cada vez más consumidores lo
   esperan; hoy `tokens.json` no los usa.
