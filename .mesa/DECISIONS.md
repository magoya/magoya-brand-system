# Decisiones

## D1 · 2026-08-19 · G0: el problema se reencuadra aguas arriba

**Decisión.** La iniciativa deja de ser "mejorar el análisis de copy" y pasa a ser **"de material
crudo a narrativa, declarando los huecos"**. Dos cambios de mandato que se derivan directo de la
evidencia:

1. El agente de copy **no reescribe**: marca qué falta, qué no cierra y a quién pedírselo. El texto
   entra bloqueado y aprobado (E1); reescribirlo es trabajo que nadie pidió y que después hay que
   revertir.
2. La capa arranca **antes** de la Fase 1 actual. Hoy metodo.md pide "escribí LA idea" como insumo;
   eso es precisamente lo que el equipo no produce (E5). El insumo real es un transcript o un doc.

**Fundamento.** E1–E5 y E8: el costo medido está en las vueltas de reconciliación, no en redactar ni
en maquetar. La mitigación del copy inventado ya existe (E9).

**Disidencia registrada (negocio).** No firma la inversión sin los tres números de E14, y sostiene un
escenario alternativo que hay que tomar en serio: *si la prueba a ciegas sale bien, la capa ya
alcanza y la inversión correcta es cerrar A5/A6 y el pase de inglés* (E13), que pegan directo en
cuentas que facturan y están frenados por una decisión de personas, no por sistema. No se promedia:
se resuelve con el dato de G1.

**Disidencia registrada (negocio, 2).** Construir "para cualquier IA" es invertir contra un usuario
que todavía no apareció (E11); el que absorbe el retrabajo es Facu en Claude Code, que ya tiene el
repo. Son dos productos distintos. Queda para G2 como eje de las tres direcciones.

## D2 · 2026-08-19 · G1: el problema no es el criterio de la IA, es que el spec se contradice

**El dato que cierra el gate.** `validar.py` da **0 fallas** y las dos pruebas a ciegas encontraron
**16 contradicciones verificadas** del spec. No es una discrepancia de opinión: las verifiqué una por
una con grep y con cuentas. El validador cruza *estructura* (¿resuelven los links, tienen límite los
slots) y no **consistencia entre reglas en prosa de distintos documentos**. Ese es el agujero.

**Y hay un patrón, no una lista.** Las 16 caen en tres familias:

1. **Regla que la plantilla oficial no puede cumplir** (39, 43, 54, 55, 60, 61): un golpe de lima por
   slide cuando 6 plantillas tienen cero; 3 niveles tipográficos cuando M3 tiene 7; 75/25 cuando la
   portada oficial es 70% verde; chip en mayúsculas cuando el ejemplo oficial va en sentence case.
   **El checklist audita a las plantillas y las plantillas lo fallan de fábrica.**
2. **Instrucción que promete control que la geometría bloqueada niega** (47, 56, 62): "la frase que
   carga el sentido va en lima" en un módulo sin lima; "el ícono en lima marca el modelo que estás
   proponiendo" cuando está `data-locked` en la card del medio; slots dimensionados para un copy que
   la voz de marca prohíbe escribir. Son textos escritos para un sistema flexible, aplicados a uno
   bloqueado.
3. **Dos documentos que dicen números distintos** (40, 42, 57, 63, 65): M3 tres pasos vs. cuatro,
   239 assets vs. 247, 15 chequeos vs. 16 (con la fila 16 fuera de la tabla), un `cuando_usarlo`
   cortado a la mitad.

**Decisión.** G2 no diseña una capa de análisis de copy nueva. G2 tiene que resolver, en este orden:

1. **La contradicción es el bug principal.** Cada una obliga a la IA a elegir entre dos reglas
   oficiales — exactamente lo que el sistema promete eliminar ("que nadie tenga que adaptar ni
   asumir"). Mientras existan, cualquier capa nueva hereda el problema.
2. **La detección tiene que separarse de la contención** (68). La prueba B declaró los huecos con
   precisión y publicó el dato igual. Declarar no alcanza: hace falta una regla de qué se puede
   entregar con un hueco adentro y qué no sale.
3. **El selector necesita un eje que se pueda verificar.** El mercado indexa por forma del dato (24,
   25); Magoya por intención retórica. Y no hay fila para "no tengo el dato" (33).

**Lo que NO se toca**, porque la evidencia dice que funciona: el flujo copiá-pegá (35), los
`max_caracteres` como assert (35), los `[XX]` (37), y el aviso anti-resumen, que se activó de verdad
en las dos corridas (36).

**Disidencia de negocio, actualizada.** Su escenario alternativo era "si la prueba a ciegas sale bien,
la capa ya alcanza". Salió mixta: el mecanismo funciona y el spec se contradice. Eso **no** valida
construir una capa nueva, y **sí** valida arreglar el spec — que es más barato. La disidencia sobre los
tres números de ROI sigue abierta y sin resolver con dato.

## D3 · 2026-08-19 · La plantilla es dueña de la regla, y el concepto 2 se ejecutó

**Decisión de Facu en el checkpoint de G2:** cuando un chequeo y una plantilla oficial se
contradicen, **gana la plantilla**. El catálogo es una pieza real que ya funcionó; el checklist es un
gate de salida, no la fuente. Consecuencia: el techo tipográfico pasa de 3 a lo que declara el
catálogo (7) y "exactamente un golpe de lima" pasa a "como máximo uno" — cero es válido, porque 19 de
las 41 plantillas no llevan lima.

**Alcance ejecutado:** el concepto 2 completo.

| Qué | Dónde | Resultado verificado |
|---|---|---|
| El regex que cortaba el `cuando_usarlo` en el primer tag inline | `ai/generate.py` | **de 9 truncados a 0**. L1 recuperó "logos siempre reales y en gris, grilla pareja de 6×2, jamás placeholders" |
| El bug que barría `usa` y `alternativa` juntos y ocultaba el hallazgo 31 | `ai/validar.py` | el hueco aparece solo: **10 módulos** solo alcanzables por criterio de diseño |
| Ley de precedencia | `ai/precedencia.json` (nuevo) | 7 niveles, del que gana al que pierde. Publicada en las 4 entradas por herramienta y en `llms.txt` |
| Contrato de entrega | `validar.py --pieza` | **discrimina**: el deck de la auditoría que publicó las cifras de la CEO da 4 fallas; el que declaró no haber inventado nada da 0 |
| Los tres chequeos que ya eran auditables | `ai/validar.py` | lima por atributo, niveles por `font-size` único, y el hue con el calificador de saturación que faltaba |
| El tercer estado para la familia F2 | `data-accent="lima"` en `ai/templates.py` | **19 plantillas** con acento marcado, ninguna con más de uno. La instrucción "el destacado va en lima" pasa de inejecutable a ejecutable |
| El método, reescrito con la evidencia | `ai/metodo.md` v2.0 | Fase 0 nueva (material crudo → narrativa), el agente de copy marca en vez de reescribir, agente de títulos con umbral medido |
| La unidad del 75/25, que era la asunción más grande de la auditoría | `ai/constraints.json` | queda definida: **el deck**, no la slide |
| El defecto de mi diseño de prueba | `.ai/agente-validacion-ia.md` | los agentes a ciegas pasan a `isolation: worktree` |

**Lo que queda declarado como falla y NO se tocó, a propósito:** E4 (2 acentos, 9 niveles) y G1
(8 niveles) son los dos únicos outliers del catálogo contra su propio techo. Colapsar niveles en E4 es
decidir qué jerarquía se pierde — es una decisión de diseño, no un bug, y no la toma el panel.

**Lo que NO se hizo, y hay que decirlo:** **G3 (Challenge) no corrió.** Normalmente va antes de
construir. De los ocho cambios, seis son arreglos de bugs verificados o aritmética sobre reglas que ya
existían; los dos con superficie de diseño real son el techo tipográfico nuevo y `data-accent`. Esos
dos son los que se beneficiarían de pasar por red-team y usuario-no-adopta.

## D4 · 2026-08-19 · La composición del deck es un paso, y se mide

**Origen:** feedback de campo de Pato en el primer uso real de la capa (hallazgos 69-74).

**El diagnóstico.** No era que la IA eligiera mal los módulos: era que **nada gobernaba la
secuencia.** El selector resuelve "qué módulo para este contenido" fila por fila; el ritmo del deck no
tenía dueño. Y la única regla que existía —"nunca dos slides seguidas del mismo módulo"— el deck la
cumplía. Es exactamente la misma clase de defecto que documentamos en D2: una regla escrita en prosa,
enterrada en un bullet, sin nada que la verifique.

**Lo que se hizo.**

1. **Cada módulo publica su `perfil`**, derivado de la plantilla real y no escrito a mano: `lienzo`
   (blanco/sage/verde-profundo/foto), `peso` (visual/mixto/texto), presupuesto de texto y recursos
   visuales. Es el eje que le faltaba a la IA para componer.
2. **`como_componer_el_deck` en `index.json`**, con cinco reglas verificables: nunca 3 seguidas de
   peso texto, el lienzo cambia cada 3, 1 de cada 3 visual, apertura y cierre oscuros, y la de módulo
   repetido que ya existía.
3. **Fase 1b nueva en `metodo.md`** — componer la secuencia es un paso, no un subproducto de elegir
   módulos.
4. **La regla anti-adorno, que ataca la segunda falla:** *si te queda soso, cambiá de módulo, no
   agregues adorno.* Está en `metodo.md` como bloque destacado, en `selector.json` y en
   `como_componer_el_deck`. Era el hueco por el que la IA se fue a inventar carátulas.
5. **El instrumento:** `validar.py --pieza` mide la secuencia de lienzos y pesos desde los
   `data-modulo` del HTML entregado. **Validado contra los dos decks de la auditoría: falla el que se
   lee soso, pasa el otro.** Sin esto sería otra regla en prosa sin verificar, que es la clase de
   fallo que este proyecto ya documentó.

**Lo que este hallazgo dice del método de la Mesa.** Las dos pruebas a ciegas encontraron 16
contradicciones y **ninguna encontró esto**, porque las dos evaluaban *conformidad* (¿cumple las
reglas?) y no *calidad* (¿está bien contado?). El crítico del protocolo semanal puntúa contra el
checklist, y el checklist no tenía nada de ritmo. **Un panel que solo mide conformidad no detecta lo
soso.** El bloque 2 del protocolo semanal necesita una pregunta más: *¿esta pieza te daría vergüenza
mandarla?* — y el chequeo de composición ahora la vuelve parcialmente objetiva.

## D5 · 2026-08-19 · G3: se retira el gate de composición y cambia el eje

**Las cuatro voces convergieron desde ángulos distintos, y todas contra D4.** Verifiqué cada traza
corriéndola; ninguna quedó en opinión.

**La decisión inmediata, ya ejecutada.** El chequeo de ritmo **deja de ser un gate** y pasa a ser un
diagnóstico que imprime la composición y declara explícitamente qué NO mide. Tres razones, todas
verificadas:

1. **Es insatisfacible para una clase real de deck.** 0 de 362.860 órdenes del deck de producto
   canónico pasaban las cinco reglas (H87), porque el catálogo no tiene un módulo visual que cargue
   un método, un journey ni un caso (H88).
2. **Daba verde sobre secuencias peores que la que hizo abandonar al primer usuario** (H75).
3. **Yo mismo lo cerré afirmando "cinco reglas verificables" y eran cuatro** — y el deck que usé como
   prueba de que la medición coincidía con el juicio humano viola la quinta y sale `[OK]` (H98).

Una métrica que da verde sobre el deck que hizo abandonar es peor que no tener métrica. Retirarla no
es un paso atrás: es sacar una afirmación falsa de circulación.

**El eje era el equivocado, y esto es el hallazgo central del gate.** El mercado —Sequoia, Storydoc,
el ghost deck de McKinsey— gobierna la secuencia por **rol narrativo**; nosotros elegimos **textura**
(lienzo y peso visual). Solapamiento cero. Textura es consecuencia; argumento es causa. Y nuestro
propio umbral ("1 de cada 3 visual") es **más bajo que la fuente que citamos** para justificarlo:
Garner & Alley pide aserción + evidencia visual en cada slide (H102).

**Lo que queda decidido como dirección** (el alcance lo elige Facu, no el panel):

| # | Qué | Por qué, con el hallazgo |
|---|---|---|
| 1 | **`beat` por módulo** (contexto / tensión / propuesta / evidencia / pedido) como eje primario, y `selector.json` gana la columna de rol que hoy no tiene | H97: es el eje que gobierna el mercado, y es verificable porque el tag vive en las 41 filas del catálogo, no en el copy |
| 2 | **El ghost deck va ANTES de elegir módulos**: los títulos solos tienen que sostener el argumento y eso se aprueba primero | H100: el deck aprobado tiene 1 de 5 títulos con verbo. La Fase 1b compone ritmo sobre un orden cuyo argumento nunca se testeó |
| 3 | **El adorno se mide**: contenedores de slide contra slides con `data-modulo`, y nodos fuera de los slots declarados | H104: hoy el chequeo es ciego a la peor falla y encima la saca del denominador. Base empírica en H103 |
| 4 | **`peso` tiene que mirar el texto**, y la densidad entregada se mide sobre la pieza, no sobre el presupuesto | H76: K2 con 1.853 caracteres está etiquetado `visual` por 4 íconos |
| 5 | **El veredicto lo da la IA en el chat, antes de renderizar** — la secuencia propuesta con módulo, rol, y de dónde sale cada dato | H86, textual del que no adopta: *"si para saber si la pieza sirve tengo que clonar un repo y abrir una terminal, no lo voy a saber nunca"* |
| 6 | **La audiencia entra como variable de primer nivel**, codificando la matriz que ya existe | H92: `VOICE-RESEARCH §4.2` la tiene escrita y admite que los aciertos son "por intuición del autor, no regla del sistema". En todo el spec la palabra aparece una vez |
| 7 | **Se mide el archivo entregado, no el master** | H90: `build_pdf.py` saca la slide de inversión completa en una variante, y el PDF es la pieza que el prospecto se queda |
| 8 | **El contrato de entrega se afloja**: distinguir "falta el dato" de "el dato contradice". Lo segundo bloquea; lo primero marca sin sellar la pieza entera | H85: un deck con quince `[PENDIENTE]` sellado BORRADOR no lo manda nadie, y eso hace abandonar más rápido que lo soso |
| 9 | **El catálogo le debe módulos al sistema**: portadores visuales de método, journey y caso; cierres para los otros 3 momentos comerciales; una fila para el calendario del cliente | H88, H93, H94. Es trabajo de diseño en `slides.html`, no del panel |
| 10 | **Léxico por cuenta en `facts.json`** | H95: Doug barrió *adoption → utilization* en dos commits y el sistema no tiene dónde guardar eso |

**Disidencia registrada (usuario-no-adopta), y es la que más me preocupa.** Sostiene que el problema
es **exceso de reglas, no falta**: el camino obligatorio ya son 12 archivos y ~5.000 líneas, y D4
agregó cinco reglas al fondo de un JSON de 3.171 líneas. Si los puntos 1 a 10 se ejecutan sumando
archivos, la próxima IA tampoco los va a leer. **No se promedia:** cualquier implementación tiene que
salir con una cuenta neta de reglas y de archivos igual o menor. Empezando por deshacer lo que ya
detecté como mío: `BRAND.md:121` y `.ai/checklist.md:27` siguen diciendo lo viejo (H83), `llms-full.txt`
trae la regla sin el dato (H82), y `selector.json` tiene un bullet que dice "esa regla NO alcanza"
sobre el anterior (H84).
