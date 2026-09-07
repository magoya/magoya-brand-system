# Validación de la fusión IA ↔ brand system

Registro de las corridas del agente semanal. Protocolo:
[`agente-validacion-ia.md`](agente-validacion-ia.md). Lo más nuevo arriba.

La métrica que se sigue corrida a corrida es **la prueba a ciegas**: cuántos de los 16 chequeos
pasa una pieza hecha por una IA que solo recibió un link. Todo lo demás es diagnóstico de por qué.

---

## 2026-09-07

**Validador:** 4 fallas · 5 huecos · 8 ok al abrir; **3 fallas · 5 huecos · 8 ok al cerrar.** La
única falla mecánica era el drift, y era **un falso positivo que iba a repetirse todos los días**:
`ai/decks/index.json` estampaba `date.today()`, así que regenerar cambiaba el archivo aunque nada
hubiera cambiado. Las otras tres (E4 con dos acentos, E4=9 y G1=8 niveles, los tres wordmarks
distintos) están declaradas a propósito en `.mesa/DECISIONS.md` y esperan una persona.

**Prueba a ciegas:** deck de 5 slides — **11/13 (3 N/A)** · post de LinkedIn — **3/3 (13 N/A)** ·
tabla de precios — **12/12 (4 N/A)**. Títulos-aserción: **60% · n/a (100% por analogía) · 100%**
(base 17%, objetivo 80%). Pedidos rotados: el post y la tabla de precios son nuevos; el deck se
repitió a propósito porque `ai/decks/` es de hace cinco días y nunca se había probado a ciegas.

**Los puntajes no se comparan con los de la corrida anterior y hay que decirlo**: los N/A cambian el
denominador según el formato. Un post de texto plano deja 13 de los 16 chequeos sin aplicar, y saca
3/3 publicando una afirmación de capacidad sin ningún respaldo. Ese es el hallazgo, no el puntaje.

**Lo que la corrida dice del sistema, y es lo que importa:**

1. **El checklist es visual y el riesgo es textual.** De 16 chequeos, uno solo mira el copy, y mira
   ortografía. Las dos piezas que publicaron algo que no debían sacaron puntaje perfecto.
2. **El contrato de entrega solo sabe contar cifras.** Dice "un **dato** que no está en `facts.json`
   no se escribe", y toda su maquinaria es numérica: `[XX]` está definido como marcador de cifras y
   el pedido a humanos enumera "N cifra(s)". **Dos IAs independientes leyeron el mismo párrafo igual
   y las dos entregaron "Staff Augmentation"**, que `BRAND.md` marca pendiente de validación. Cuando
   dos agentes que no se hablaron leen igual un texto, el que está mal es el texto.
3. **El camino corto esconde reglas.** La regla 3b —mover el acento lima— está en las 41 plantillas
   y no estaba en el deck armado, que es adonde `claude.md` paso 0 manda primero. La prueba del deck
   razonó al revés por eso; la que leyó la plantilla suelta lo hizo bien.
4. **La pieza más obediente no es la más segura.** Ver abajo.

**La más peligrosa es el deck, y no es la que se ve rota.** Es un recorte literal del deck oficial:
geometría idéntica tag por tag, 19 assets reales en 200, wordmark correcto, un golpe de lima por
slide, arco verificado. **Pasa cualquier revisión visual que le haga un humano.** Tiene un solo
corchete —el nombre del cliente— y el bloque de entrega dice "cuando no quede ningún corchete, borrá
este bloque y el deck sale como final". Lo que sale sin corchete es **una oferta comercial que nadie
aprobó**: noventa minutos con el equipo de producto y agronomía, entregable escrito, "trabajemos
juntos o no", más un cronograma de cuatro semanas. No está en `facts.json`, ni en `BRAND.md`, ni en
el `texto_ejemplo` de M3 (que ofrece otra cosa: un discovery pago de seis semanas). Y el pedido a
humanos **no lo lista entre sus cinco huecos**. La tabla de precios comete el mismo error de fondo y
es inofensiva, porque le faltan los tres números que son el objeto de la pieza.

**Por qué falló cada chequeo.** Solo tres fallas duras, las tres en el deck y las tres en el bloque
que escribió de cero (el único que no sale de una plantilla): **2 por (C) la regla estaba clara y la
IA la ignoró** —`#9fb3a6` fuera de paleta y espaciado 40/18/20/22 fuera de la escala, con la regla
escrita en tres archivos y el checklist nombrando literalmente el 18— y **1 defecto del chequeo**.
Alrededor, **1 por (B)** —"ninguna afirmación de valor viaja sin cifra, nombre de cliente, plazo o
captura" existe en `BRAND.md` §1 y no existe como chequeo ni como constraint: el gate no la mira— y
**3 por (A)**, que son las que se arreglan acá y están abajo.

**Arreglado y commiteado** (`d9236f1`, `08f7df3` — ninguno inventa un valor de marca):

- **El chequeo de drift iba a dar falla todos los días.** `version` es ahora la fecha del último
  cambio de contenido, no la de la última corrida. Y compara también el HTML de cada deck, no solo
  el catálogo: verificado en las dos direcciones.
- **`validar.py --pieza` reprobaba a los tres decks oficiales por cifras que nunca escribieron.**
  Contaba como "cifra afirmada" todo lo que estaba fuera de las slides: el `<title>`, el header de
  instrucciones y la hoja de estado ("Slide 05 (C1): 4 cifra(s)"). Toda pieza salida de B2 fallaba
  por el nombre del propio módulo ("B2 — 3 boxes"). Ahora cuenta solo dentro de `<div class="slide">`.
- **El gate de arco corría sobre piezas de una sola slide**, donde las cuatro reglas son
  insatisfacibles a la vez: la tabla de precios se llevó tres fallas imposibles de arreglar.
- **"Máximo 3 niveles tipográficos" seguía plano** en `tokens.json`, `llms.txt` y los dos prompts
  canónicos, mientras `BRAND.md` y el checklist ya distinguían pieza a mano de plantilla. **Las tres
  pruebas chocaron con esto.** Y el checklist decía "las plantillas oficiales van de 2 a 9 niveles",
  que se lee como permiso: E4 y G1 están declaradas en falla, no autorizadas.
- **`.ai/brand-prompt.md` estaba desactualizado y es el más peligroso de todos**, porque `llms.txt`
  lo ofrece como "canónico y autocontenido: pegalo y la salida ya sale on-brand sin adjuntar nada
  más". Tenía la voz que `BRAND.md` retractó ("no whimsical" volvió a ilustración), el vocabulario
  propio en inglés contra la regla de mínimo de inglés en castellano, y **cero mención de
  `facts.json`, `[PENDIENTE]` o BORRADOR**. Quien lo pegaba solo publicaba cifras inventadas. Ahora
  lleva la voz canónica y el contrato completo; la versión corta también.
- **Cuatro chequeos que ninguna plantilla oficial podía pasar** (`precedencia.json` orden 6): el 2
  (hue 20-65° sin piso de saturación mete siete colores oficiales adentro — el piso del 40% ya
  estaba en `validar.py`), el 9 (el `box-shadow` del contenedor lo traen las 41 plantillas), el 15
  (un solo eje, y M3 tiene dos columnas) y el 17 (ponía el wordmark a y=3.2% siempre, y así **la
  portada oficial falla el chequeo que el sistema llama el más importante**: M1 va a y=7%).
- **La regla 3b no estaba en los decks armados**, solo en las 41 plantillas sueltas. Y el header de
  los decks hablaba solo de `[XX]`: ahora dice que "dato" incluye un nombre de servicio, un claim o
  una oferta.
- **Tres desambiguaciones que dos pruebas independientes pidieron:** el lima pasa de "exactamente
  uno por slide" a techo con cero válido (`constraints.json` contradecía al checklist y a las
  plantillas); el canal para reportar contradicciones mandaba escribir en `.ai/VALIDACION-IA.md`,
  que una IA llegada por URL no puede escribir, y ahora el bloque PEDIDO A HUMANOS de la propia
  pieza **es** el canal; y `data-pedido-a-humanos` —que el validador honra y usan los tres decks—
  no estaba documentado en ningún lado, así que declarar los huecos te contaba en contra.
- **La unidad del 75/25** (el deck, no la slide) ya estaba resuelta en `constraints.json` y
  `BRAND.md` seguía diciendo "cada pieza".

**Necesita tu decisión** (ninguna se inventa acá; siguen abiertas todas las de la corrida anterior):

1. **`facts.json` no tiene un campo de capacidades.** El pedido de la prueba 2 era "anunciá una
   capacidad concreta del equipo" y **el sistema no puede responder qué capacidades hay**: tiene
   empresa, cifras, clientes y equipo. La pieza terminó escribiendo sobre la única capacidad
   deducible y mandando el resto a preguntar. ¿Qué capacidades se pueden anunciar?
2. **Falta el marcador de lo NO numérico.** `[XX]` y `[PENDIENTE]` son de cifras; un nombre de
   servicio, un claim de posicionamiento o una oferta comercial no tienen instrumento. Es la causa
   raíz de lo más peligroso de esta corrida. ¿Se extiende `[PENDIENTE]` a texto, o va un marcador
   nuevo?
3. **"Staff Augmentation" sigue como pendiente de validación en `BRAND.md`** y está en el
   `texto_ejemplo` de B1, que es la slide de propuesta del deck de credenciales. Las dos IAs que
   tocaron esa plantilla lo publicaron. ¿Se valida o se saca del ejemplo?
4. **El bloque PEDIDO A HUMANOS es el único elemento que el sistema EXIGE y no especifica.** No hay
   plantilla, geometría, escala ni token. Las dos fallas duras del deck están las dos ahí adentro, y
   `#9fb3a6` —el gris que usan los tres decks oficiales en ese bloque— **no está en `tokens.json`**
   y no hay token de "texto sutil sobre oscuro" para reemplazarlo. (Abierta desde la corrida
   anterior, ahora con la evidencia de por qué cuesta.)
5. **El deck armado no dice qué recortar.** El usuario pidió 5 slides y el deck que matchea tiene 8.
   El sistema autoriza recortar ("revisá el arco") y no dice qué sale. La IA eligió sola, y eligió
   bien por la razón equivocada: sacó las dos slides que no podía llenar con datos aprobados. Es
   exactamente la decisión de diseño que estos decks existen para quitarle al usuario. ¿Se publican
   variantes de 5, o una regla de prioridad de recorte?
6. **La ley de precedencia sigue sin cubrir los documentos que el sistema manda usar:** `ai/claude.md`
   (el punto de entrada, lo único que el usuario entrega), `ai/metodo.md` (declarado OBLIGATORIO y
   donde vive la métrica de títulos), `.ai/brand-prompt.md` y `VOICE-RESEARCH.md` (que trae datos de
   compañía como "~50 personas"). Las tres pruebas chocaron con esto por separado.
7. **El aviso anti-resumen no alcanza, y ahora está medido.** `WebFetch` sobre `ai/claude.md`
   devolvió un resumen sin las URLs literales — la falla exacta que el aviso de la v1.5 intenta
   evitar. **El aviso no sirve porque la herramienta resume el archivo incluyendo el aviso.** La
   prueba solo salió adelante bajándolo crudo con `curl`; un usuario que no elige su herramienta de
   fetch se queda trabado en el paso 0.
8. **El selector sigue sin una sola fila para lo que no es slide**: cero para post, carrusel,
   one-pager, landing, banner o tabla de precios de tres opciones (el pricing existe solo para dos
   escenarios, E3/E4). Es la abierta n°6 de la corrida anterior y no se movió.

**Del mundo afuera** (solo lo que cambia una decisión):

- **Agent Skills dejó de ser una cosa de Claude: es un formato abierto y multi-herramienta.** Una
  carpeta con `SKILL.md` que carga por etapas —nombre y descripción al arrancar, el cuerpo cuando la
  tarea coincide, los archivos referenciados solo si hacen falta—, hoy leída por Claude, ChatGPT y
  Codex, Gemini CLI, Copilot, VS Code, Cursor y varias decenas más
  ([especificación](https://agentskills.io/specification)). Es exactamente la arquitectura que
  Atlassian midió como 92% más barata que el markdown "todo junto", que es lo que hace
  `llms-full.txt`. Verificado por herramienta: en **ChatGPT** corren en Chat y Work (web, desktop y
  mobile) empaquetadas como plugin, y sueltas en desktop, Codex CLI e IDE, con las skills ocupando
  como máximo el 2% de la ventana de contexto
  ([docs](https://learn.chatgpt.com/docs/build-skills)); en **Claude** la distribución soportada es
  un plugin marketplace, que es un repo de git —y este brand system ya es uno—; en **Gemini** solo
  la CLI, **la app y los Gems no**, así que ahí la URL sigue siendo el único canal; en **Copilot**
  desde `.github/skills`, `.claude/skills` o `.agents/skills`. Las cinco entradas por herramienta
  quedaron actualizadas con esto (1.6, copilot 1.2) y con el estado real: **Magoya todavía no
  publica una skill**.
- **Atlassian genera todos los formatos desde un solo modelo de contenido**: el contenido del MCP,
  la skill del design system, los DESIGN.md. O sea: la arquitectura de acá —fuentes, `generate.py`,
  capa publicada— es la correcta, y lo que falta es **un target de salida más**, no un rediseño.
- **DTCG sigue en 2025.10** (hay un draft de julio de 2026) y la adoptaron Figma, Penpot, Sketch,
  Tokens Studio, Style Dictionary y Terrazzo. No cambia la decisión abierta sobre el `$schema` de
  `tokens.json`, la encarece: cada vez más consumidores esperan `$value`/`$type`.
- **Carbon MCP sigue en preview público y Polaris no tiene MCP de primera parte** (hay servidores de
  comunidad y una skill de Polaris para Claude Code). Nadie resolvió mejor que acá el problema de
  "una persona que no sabe diseño con un link".

**Propuesta para la próxima** (3, por impacto):

1. **Un chequeo de contenido, porque el riesgo se mudó al texto.** El checklist mira superficie
   visual y las dos piezas que publicaron algo que no debían pasaron limpias. El chequeo 18 sería
   la regla que ya existe enterrada en `BRAND.md` §1: ninguna afirmación de valor viaja sin cifra,
   nombre de cliente, plazo o captura — y una lista de lo que no está aprobado (capacidades, ofertas,
   nombres de servicio). Junto con el marcador de lo no numérico (decisión 2), es lo único que frena
   la falla más cara de esta corrida.
2. **Publicar el brand system como skill, generada desde las mismas fuentes.** Es un target más de
   `generate.py`, no un rediseño, y sirve a las cuatro herramientas de una. Antes de moverlo, medirlo
   en casa como quedó propuesto la corrida pasada: misma pieza por URL y por skill, contando tokens y
   turnos. Si el gap se parece al 92% de Atlassian, la decisión deja de ser teórica.
3. **Mover la lista plana de URLs al principio de las cinco entradas.** El aviso anti-resumen está
   arriba y no funciona, porque el fetch resume el archivo entero, aviso incluido. Una lista de URLs
   al inicio sobrevive mejor a un resumen que un párrafo pidiendo que no te resuman.

**Cambios al protocolo, con la evidencia de esta corrida:**

- **Un directorio exclusivo por agente a ciegas.** Los tres compartieron el scratchpad y el segundo
  vio el `credenciales.html` del primero. El worktree aísla el repo y no el directorio de trabajo.
- **Prohibirles renderizar la pieza en un navegador.** La primera corrida de la prueba del deck se
  colgó diez minutos verificando el render y hubo que relanzarla; con la instrucción de verificar
  leyendo el HTML, terminó.
- **Pedir la hoja de estado ANTES de pulir la pieza.** Con eso, la corrida que se colgó igual habría
  dejado su registro.
- **La contaminación de contexto se repitió y las tres la declararon:** memoria del usuario con datos
  de marca y clientes, y en un caso **una cifra de contrato real** — justo el dato que a esa prueba
  le faltaba. No la usó, y esa es la mejor evidencia de que el contrato de entrega funciona cuando
  hay un instrumento.

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

## 2026-09-01 · corrida real: deck comercial v3 → v4 (feedback de la mesa de Pato)

Tercer uso real y el mejor input que recibió el sistema. Veredicto de esa mesa: **el sistema
funciona** — una IA llevó una pieza real de "casi on-brand" a 14/16 auditorías usando solo lo
publicado, sin inventar tokens. Las fricciones no eran de diseño.

**Arreglado en esta pasada** (siete, ninguna necesitaba decisión humana):

| # | Qué decía el feedback | Qué verifiqué | Qué quedó |
|---|---|---|---|
| 2.1 | dos escalas tipográficas sin regla de frontera | `typography.scale` (rem) y `slideScale` (pt) conviven sin decir cuál va cuándo. Una pieza real se construyó entera con la equivocada | `typography.cual_escala_uso`: slides → slideScale, todo lo demás → scale |
| 2.2 | margen 7% vs eje 7.5% | los dos existen y nada explica el vínculo | `margen_7_vs_eje_7_5`: 134 es el piso legal, 144 el eje de trabajo. Desde cero usá 144 y cumplís los dos |
| 2.3 | "máximo 3 niveles" contra slides de 7 | `tokens.json` decía "Máximo 3 niveles por pieza" y precede al checklist, así que arreglar el checklist no alcanzaba | la regla ahora distingue pieza a mano (3) de plantilla (el techo de la plantilla) |
| 2.4 | unidades ambiguas: "y: 3.2" | **era peor que lo reportado.** La plantilla pone `top:3.2cqw` = 61px, o sea **3.2% del ANCHO**. Medido contra el alto da 34px | el constraint ahora dice "ambas son % del ancho, NO del alto" con los px resueltos |
| 2.5 | el checklist no audita el logo propio | **0 menciones de "wordmark" en los 17 chequeos**. El elemento que el manual llama "LA firma" era el único sin auditoría | **auditoría 17: variante, tamaño, posición y letterforms contra el asset canónico** |
| 2.6 | logos de clientes: el sistema dice gris, los archivos son a color | **peor que lo reportado**: son raster embebido dentro de un `<pattern>`, así que no se pasan a gris cambiando `fill` ni recolorando paths — hace falta un filtro | la regla del manifiesto ahora lo dice, con el cómo |
| 2.7 | la lista de recursos no se declara cerrada | 0 cláusulas de exclusividad en `BRAND.md`, contra `facts.json` que sí la tiene | cláusula copiada: la lista es EXCLUYENTE, lo que no está no existe, y si falta algo falta un módulo |
| 2.9 | claims que envejecen solos | "Nine years" es correcto hoy y miente en 2027 | `facts.json.derivados_del_tiempo` con la fórmula para recalcular |

**Y el guardián del bug que encontró un humano a ojo.** Chequeo 11 nuevo: todas las variantes del
wordmark tienen que compartir geometría. Fira ya, y encontró **tres dibujos distintos**, no dos:
el set publicado (`black/cream/deep/green`, 8 paths, 139×38), `cream-prod` (1 path, 60×15.96) y
`animado` (8 paths pero otra geometría). Ningún archivo del sistema advertía nada.

**Necesita tu decisión** (las dos que el sistema no puede resolver solo):
1. **Cuál de los tres wordmarks es la marca vigente.** Es el fix más urgente de la lista: es un bug
   activo que afecta a todo consumidor, humano o IA. Con eso republico el set y borro el resto.
2. **Poblar `facts.json`** con las cifras del doc de origen, y definir **dueño y canal** para
   propagar aprobaciones. El método exige propagar y no dice cómo — el feedback tiene razón: la
   obligación existe y el camino no. Sin esto ninguna pieza comercial sale de borrador.

**Queda para G4** (diseño, no spec): módulo **cierre-statement** —ya hay prototipo, es la slide 10
del deck sin la red de nodos— y el mini-capítulo de **componentes interactivos** (chip selected,
hover, focus, rail), que hoy cada pieza inventa.

**Lo que esa mesa admitió no haber visto sola** y vale más que el resto: el wordmark viejo lo detectó
Facu, y a la red de nodos la degradó a "ratificable" en vez de aplicarle el estándar de `facts.json`
—no está en el sistema, no existe—. Las dos lecciones están incorporadas: la cláusula de lista
cerrada (2.7) es exactamente ese estándar, y la auditoría 17 es el chequeo que faltaba.

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
