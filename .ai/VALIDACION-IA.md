# Validación de la fusión IA ↔ brand system

Registro de las corridas del agente semanal. Protocolo:
[`agente-validacion-ia.md`](agente-validacion-ia.md). Lo más nuevo arriba.

La métrica que se sigue corrida a corrida es **la prueba a ciegas**: cuántos de los 16 chequeos
pasa una pieza hecha por una IA que solo recibió un link. Todo lo demás es diagnóstico de por qué.

---

## 2026-08-31

**Validador:** 2 fallas · 6 huecos · 7 ok. Empezó en 3 fallas: la tercera era un falso positivo
que reportaba **353 URLs caídas con el sitio en 200**.

**Prueba a ciegas:** one-pager A4 — **13/16** · landing — **15/16** · carrusel 4:5 — **13/16**.
Métrica de títulos-aserción: **9% · 71% · 50%** (45% agregado). Línea de base 17%, objetivo 80%.
El promedio miente: la landing sola llega a 71% y el one-pager queda **por debajo de la línea de
base**, porque su título es fijo de la plantilla y son todas etiquetas de tema.

**Dos advertencias sobre la medición, antes de creerle a los puntajes.**

1. **El piso se movió durante la corrida.** Otra sesión pusheó `37f06a9` a las 17:29 y Pages
   rebuildeó a las 17:36, con las tres pruebas en el aire. La 1 terminó antes y midió un estado
   entero; la 2 y la 3 pudieron leer una mezcla de dos versiones. No invalida los hallazgos
   estructurales (los verifiqué después contra lo publicado), sí invalida comparar 13/16 contra
   una corrida futura como si fueran la misma vara.
2. **La ceguera por worktree no alcanza.** El worktree aísla el filesystem, no el contexto: a la
   prueba 2 el harness le inyectó el `MEMORY.md` del usuario como system-reminder, y la 3 vio el
   `h1` de la pieza de la 2 a través del panel de browser compartido y corrió un `ls` sobre el
   worktree. Las tres lo declararon solas, que es lo que la instrucción pedía. Ninguna abrió el repo.

**Por qué falló cada chequeo — que es el producto real del bloque.** De las 6 fallas de checklist:
**4 por (C) la regla estaba clara y la pieza la ignoró**, **1 por (B) estaba escrita pero enterrada**,
**0 por (A) no estaba escrita**. Eso da vuelta el diagnóstico de la corrida anterior: el sistema
está mejor escrito de lo que estas piezas lo cumplieron. El problema ya no es el spec mudo.

Pero el crítico encontró **5 contradicciones del sistema que las tres piezas tenían que reportar
por contrato y ninguna reportó**. Y la más cara explica la falla más grave de la corrida: la pieza 1
invocó la ley de precedencia para publicar el texto de la plantilla por encima de `facts.json`, y
**esa protección no existe** — la regla 1 dice "la plantilla oficial de `ai/templates/`", que son 41
módulos de slide, y T1 vive en `pieces.html`, que no tiene rango en la ley.

**Lo más peligroso de la corrida no es la pieza que se ve rota.** El carrusel es el que más lejos
está de entregarse, pero se nota. El one-pager sale visualmente impecable —assets reales
verificados por hash, wordmark oficial, geometría de la plantilla madre— **y publica tres datos
que `facts.json` no autoriza** (mercados activos, `info@magoya.com`, "100% on Ag"), los declara
en su propia hoja de estado y los deja escritos igual. Es palabra por palabra el modo de falla que
`precedencia.json` dice haber resuelto. La landing tiene el mismo hueco de email y lo resuelve al
revés, con `[PENDIENTE]` visible: mismo sistema, mismo dato, decisión opuesta.

**Arreglado y commiteado:**

- **El validador daba 353 links rotos con el sitio arriba** (`6ba57e1`). `--red` usaba urllib sin
  bundle de CA: todas fallaban con `CERTIFICATE_VERIFY_FAILED` y se contaban como links rotos. Un
  falso positivo de ese tamaño tapa uno de verdad. Ahora busca el bundle, separa "no pude medir" de
  "link roto" y va en paralelo (18s). Verificado: 354/354 en 200.
- **`tokens.css` reprobaba el checklist oficial** (`b797b59`). Declaraba `"Manrope", system-ui,
  sans-serif` mientras BRAND.md y `tokens.json` dicen Arial y el chequeo 7 marca "system-ui suelto"
  como falla. Usar la variable oficial te reprobaba el control oficial. Mismo bug en 5 elementos de
  `assets/pieces/fecha-marcada-ig-portrait.svg`.
- **`constraints.json` mentía sobre lo que existe** (`b797b59`). Justificaba el hueco de tipografía
  web con "hoy solo existe la escala de slides", y `tokens.json` tiene `typography.scale` en rem
  (xs→7xl) más `slideScale` aparte. La prueba 2 desconfió del archivo y usó la escala rem: acertó.
  El hueco sigue abierto (falta el piso en px por nivel), pero ya no afirma algo falso.
- **D3 no se había propagado a la doctrina** (`b797b59`). El checklist decía "como máximo un golpe
  de lima" y techo 7 en slides; BRAND.md seguía con "máximo 3 niveles por pieza" plano y "un golpe
  de lima por slide". BRAND.md es el **paso 1** del flujo de las cuatro entradas: la IA leía la
  regla vieja primero. Y el checklist se contradecía entre su fila 5 y sus Extras.
- **La pieza patrón del 4:5 decía "AI EN CAMPO"** (`96e9449`). El repo tiene un commit entero
  dedicado a corregir eso y el único archivo con los números reales de la sub-marca lo publicaba
  mal. No lo vio nadie en tres corridas porque `check_nomenclatura` no barría los SVG de
  `assets/pieces/`, que son justo los que llevan copy visible. Ahora sí.
- **Las cuatro entradas mandaban a la IA fuera del dominio** (`96e9449`) a leer los 16 chequeos en
  raw.githubusercontent.com. `brand.magoya.com/.ai/checklist.md` responde 200. Dos de las tres
  pruebas se toparon con esto; una directamente no lo abrió.
- **`ai/copilot.md` a 1.1** y numeración del flujo (saltaba del 7 al 9) en gemini/chatgpt/generic.
  Quedaron dentro de `37f06a9` porque la otra sesión commiteó el árbol entero.

**Necesita tu decisión** (ninguna se inventa acá):

1. **`precedencia.json` no rankea `pieces.html` ni `ai-en-campo.html`** — 2 de las 8 páginas del
   sistema no tienen rango. Es la causa raíz de la falla más grave de la corrida. ¿Dónde entran?
   ¿Arriba o abajo de `facts.json`? Mientras no tengan rango, cualquier IA que use el one-pager o
   la sub-marca decide sola.
2. **El techo de 3 niveles tipográficos es inalcanzable en web, y no por descuido:**
   `tokens.components` fija chip 12,5px y botón 15px, así que una pieza web con un chip y un botón
   ya gastó 2 de sus 3 niveles antes de escribir una palabra. Las tres piezas fallaron el chequeo 7.
   ¿Se sube el techo para web como se subió para slides, o los componentes no cuentan?
3. **Misma familia, en espaciado:** `tokens.spacing.rules` dice "nunca valores fuera de la escala
   (ni 5, ni 10, ni 14)" y `tokens.components` fija `13px 26px`, `6px 15px`. BRAND.md los llama
   "paddings canónicos" pero la excepción no está escrita en la regla. Dos pruebas independientes
   chocaron con esto.
4. **`colorProportion` no se puede cumplir como está escrito.** Exige 8% de lima y 4% de verde
   digital **por área**, declarado "regla obligatoria, no una guía aproximada" — contra "lima en
   dosis única" (un CTA es ~0,1% del área) y contra el rol del verde digital, que es micro-acento.
   Y el mismo `tokens.json` lo declara dos veces: una como regla obligatoria y otra, en
   `usageRatio`, como "Guía por pieza". ¿Cuál de las dos vale?
5. **La plantilla madre del one-pager falla tres chequeos del sistema.** T1 tiene dos golpes de
   lima, **48,3% de verde medido contra un techo de ~25%** y 9 niveles tipográficos. Y `pieces.html`
   publica **6 placeholders "Nombre Apellido"** y usa una foto aérea de paisaje como foto de
   persona, las dos cosas prohibidas por BRAND.md. ¿Se corrige la plantilla o se declara la
   excepción?
6. **No hay ninguna ruta a una pieza que no sea slide.** `selector.json` tiene 31 filas y cero para
   one-pager, flyer, carrusel, post, banner o landing; ningún archivo de `ai/` nombra `pieces.html`.
   La prueba 1 encontró la plantilla recién en un paréntesis de BRAND.md §10, después de recorrer
   los 10 pasos. Y cuando la encontró, `pieces.html` es catálogo para humanos: sin `data-slot`, sin
   `max_caracteres`, sin `.txt`.
7. **El sub-manual manda producir desde plantillas del Studio que no están publicadas.**
   `impacto-pregunta`, `carrusel-cierre`, `impacto-cifra` y `contraste` dan 404. El manual dice
   "arrancar en blanco es donde se rompe la marca" y no hay otra opción. ¿Se publican o se dice que
   esa línea no se produce fuera del Studio?
8. **`font-mono` se exige y no se define.** BRAND.md §14 obliga a la firma "por Magoya" en
   `font-mono`; `tokens.json` no define ninguna familia mono y `tokens.css` la resuelve con un stack
   del sistema. La firma de la sub-marca se renderiza distinta en cada máquina que exporte.
9. **El contrato de entrega exige marcar `[PENDIENTE]` y el sistema no lo dibuja.** No hay
   componente ni ficha. Las tres piezas lo inventaron distinto.
10. **`#0A5C31` en la pieza patrón del 4:5 no está en `tokens.json`** — falla el chequeo 1. Elegir
    el reemplazo es decisión de diseño.
11. **`tokens.json` declara `$schema` de DTCG y no es DTCG.** La spec estable (2025.10) exige
    `$value`/`$type`; el archivo usa `value`/`role`, y el `$schema` apunta a una página HTML.
    Migrar rompe todos los consumidores. O se migra, o se saca la declaración.
12. Siguen abiertos de la corrida anterior: E4 (2 acentos, 9 niveles) y G1 (8 niveles) como los dos
    outliers declarados a propósito en D3; los 10 módulos alcanzables solo por criterio; `E3/tabla3`;
    `#E0A33A` (hue 38°, sat 73%); los 3 datos de `facts.json` sin aprobar; y los mínimos en px,
    el clearspace de avatares y el margen en mm de impresos.

**Del mundo afuera** (solo lo que cambia una decisión):

- **Atlassian midió el markdown "todo junto" contra su MCP y publicó los números**: DESIGN.md gastó
  **92% más tokens** que el MCP on-demand para la misma tarea (7,21M vs 3,75M, 45,3 vs 35,1 turnos),
  porque carga todo de una en vez de traer lo que hace falta. Es exactamente la arquitectura de
  `llms-full.txt`, que las cuatro entradas ofrecen como "empezá acá si dudás".
  [Fuente](https://www.atlassian.com/blog/how-we-build/atlassians-design-md-is-here-what-we-learned-testing-portable-design-context-in-practice)
- **El mecanismo que le gana a una URL apareció y es MCP.** Atlassian hostea el ADS MCP público en
  `https://mcp.atlassian.com/v1/ads/public/mcp`; Carbon publicó `carbon-mcp` en preview. Dejó de ser
  una idea: dos design systems grandes ya publican así.
- **Copilot**: confirmado que una URL escrita en un archivo de instrucciones **no se fetchea sola**
  — el texto entra al contexto, el link no se sigue. La entrada ya lo decía; ahora lo dice explícito.
  Novedad real: `AGENTS.md` es ubicación soportada junto a `copilot-instructions.md` y `CLAUDE.md`.
- **`llms.txt`: los crawlers lo ignoran** y Google confirmó que no tiene efecto en Search ni en AI
  Overviews. **No cambia nada acá**: el `llms.txt` de este sistema no es SEO, es un destino para
  pegar en un chat. Lo anoto para no volver a investigarlo el mes que viene.
- **DTCG llegó a su primera versión estable** (2025.10, `$value`/`$type`). Es lo que convierte el
  `$schema` de `tokens.json` en una afirmación falsa (punto 11).

**Propuesta para la próxima** (3, por impacto):

1. **Cerrar los puntos 1, 2 y 3 juntos: son una sola cosa.** Rankear las 8 páginas en
   `precedencia.json` y escribir la excepción de componentes en el techo tipográfico y en la escala
   de espaciado. Eso solo elimina 4 de las 6 fallas de checklist de esta corrida y le saca a
   cualquier IA la excusa de "elegí entre dos reglas oficiales".
2. **Una fila del selector para lo que no es slide, aunque sea para declarar el hueco.** Hoy el
   sistema no dice "no tengo plantilla para esto": deja que la IA lo descubra a los 10 pasos. Una
   fila honesta que rutee a `pieces.html` / `ai-en-campo.html` y avise que ahí no hay slots ni
   `max_caracteres` vale más que el silencio.
3. **Medir la hipótesis de Atlassian en casa antes de mover nada.** Misma pieza, dos entregas: por
   URL como hoy, y empaquetada como Skill local. Contar tokens y turnos. Si el gap se parece al 92%,
   la decisión de publicar por MCP deja de ser teórica. Si no, se archiva con dato y no se vuelve a
   discutir.

**Cambio al protocolo, para que la próxima corrida mida algo comparable:** congelar el push
mientras las pruebas a ciegas están en el aire, y pedirle a cada agente que registre la hora de cada
fetch. Esta corrida no se puede comparar con la siguiente porque el sitio se republicó en el medio.

---

## 2026-08-19 · línea de base

**Validador:** 0 fallas · 3 huecos · 7 ok — primera corrida, con los arreglos de abajo ya aplicados.

**Prueba a ciegas:** pendiente — la corre el agente en su primera pasada (2026-08-24).

**Arreglado en esta pasada:**

- `ai/assets.json` publicaba 8 URLs a `assets/refs/`, que está **gitignored**: eran 404 servidos a
  cualquier IA que leyera el manifiesto. `BRAND.md` ya decía que esa carpeta no se publica ni se
  enlaza, así que el manifiesto contradecía la doctrina. `generate.py` ahora la excluye del walk.
- Las cifras de ejemplo se convertían en `[XX]` solo si el texto era grande (≥2.4cqw). Los captions
  de D4 mostraban `68%`, `44%`, `31%` en tamaño chico: una IA podía entregarlas como datos reales.
  Ahora **toda cifra con unidad** (`%`, `x`, `k`, `M`, `+`, `hs`, `min`) va a `[XX]` sin importar el
  tamaño. La numeración de pasos (`1`, `01`) se deja, que no es un dato.

**Necesita tu decisión** (el validador las detecta y no las inventa):

1. `constraints.json` declara 3 definiciones pendientes: mínimos tipográficos para web/app en px
   (hoy solo existe la escala de slides), clearspace numérico de los avatares (hoy solo lo tiene el
   wordmark) y margen mínimo en mm para piezas impresas. Mientras estén pendientes, una IA que arme
   una landing o un one-pager tiene que asumir.
2. `facts.json` tiene 3 datos sin aprobar (retención, la métrica de un caso puntual, y volumen de
   proyectos/equipo/mercados). Hasta que los confirmes no se publican, así que una IA que necesite
   una cifra de escala se queda sin dato.
3. El slot `E3/tabla3` no dice qué va adentro de la tabla. Los demás slots de gráfico sí lo dicen.

**Estado de la capa:** 352 URLs publicadas y todas con archivo en el repo · 344 slots y todos con
límite de texto · 31 filas de selector y todos los módulos citados existen · `llms-full.txt` 56KB
(lejos del techo donde las IA truncan) · regenerar no cambia nada · ningún "AI" en copy español.
