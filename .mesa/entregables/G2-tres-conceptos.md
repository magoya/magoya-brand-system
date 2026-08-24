# G2 · Tres direcciones para arreglar la capa

Insumo: 68 hallazgos de G1 y la lente de arquitectura. Todo lo numérico de acá está verificado
sobre el repo, no reportado.

## Lo que cambió respecto del planteo inicial

Las 16 contradicciones **no son 16 problemas**. Después de la lente técnica se ordenan así:

| Origen | Cuántas | Naturaleza |
|---|---|---|
| **Un regex** (`generate.py:36` captura `([^<]+)<` y corta en el primer tag inline) | **9 de 41 módulos** con el `cuando_usarlo` cortado a mitad de oración — L1 conserva 61 de 146 caracteres y pierde "Logos siempre reales y en gris, grilla pareja de 6×2. Jamás placeholders" | **bug de una línea**, no decisión de diseño |
| **Una regla que está mal, no 37 plantillas que están mal** | **4 de 41** plantillas pasan el límite de 3 niveles tipográficos (E4=9, G1=8, M3/G2/D4/D3=7). **19 de 41** tienen cero lima; E4 tiene dos | **decisión de dueño**, no arreglo |
| **Instrucción sin marcador en el HTML** | 16 módulos tienen un `cuando_usarlo` que promete control del golpe de lima; solo 2 (A4, C3) lo tienen sobre un elemento con `data-slot` | **falta un tercer estado** |
| **Detección sin contención** | la prueba B declaró los 5 datos no verificables y los publicó igual: `validar.py` valida el repo (`os.chdir(RAIZ)`), nunca una pieza entregada | **falta un punto de entrada** |

Y `data-locked` **no es la causa**: `LOCKED_PAT` (`templates.py:47`) matchea solo assets de marca, ningún
color. El rect de lima de E1 no tiene ningún atributo. No hay lock que desbloquear: hay una
prohibición en prosa.

---

## Concepto 1 · El spec se compila desde una fuente única

Las reglas viven duplicadas en prosa en 6 archivos. La idea: una fuente legible por máquina, la
prosa se genera (como ya pasa con `llms-full.txt`), y `validar.py` gana un gate: **toda regla tiene
que ser verificable contra las 41 plantillas; una regla que ninguna plantilla puede cumplir rompe el
build.**

**A favor.** La fuente única ya existe y nadie la nombró: `slides.html` es de facto el origen de
geometría *y* de prosa. `generate.py:36` la extrae y `templates.py:211` la copia a `index.json`; el
DSL corre en Node real, no se interpreta. No hay que escribir un compilador. Mata las familias F1 y
F3 por construcción, para siempre.

**En contra.** Prender el gate hoy deja **el build rojo permanente**: el chequeo #7 tiene 37
plantillas en falta y el #5 tiene 19. Un build rojo permanente se apaga. Y solo ~6 de los 16 chequeos
son de slides: el resto (redes, merch, personajes, motivo, botón/chip) no tiene fuente estructurada —
no existe un DSL de piezas de redes. Compilar eso es inventar el modelo de datos primero. Ese es el
proyecto, no la pantalla.

**Deuda.** `tokens.css` está fuera del pipeline (`grep tokens.css ai/*.py` = 0 hits) con 4 hexes que
no están en `tokens.json`: `#5C6B61 #8A9389 #CFC8BC #D2D2CC`. Dos dueños, y el que se mantiene a mano
es justo el que consume quien escribe código.

## Concepto 2 · Ley de precedencia + contrato de entrega

No eliminar las contradicciones: declarar una jerarquía para que la IA **nunca tenga que elegir**, y
separar detectar un hueco de entregarlo.

**A favor.** La precedencia ya gana de facto: `templates.py:172-181` inyecta "REGLAS PARA LA IA (no
negociables)" en las 41 plantillas y la regla 1 ("la geometría ES la marca") ganó en las dos pruebas
a ciegas. Formalizarla es un `ai/precedencia.json` de ~15 líneas. Y la contención tiene la mitad
puesta: `templates.py:91-97` ya manda las cifras de ejemplo a `[XX]` y `validar.py:70-84` ya falla si
un slot muestra una cifra copiable — falta un `validar_pieza(path)` que corra el mismo regex sobre el
HTML entregado. **Eso cierra el hallazgo 68: la prueba B publicó el dato prohibido porque nada corría
sobre su deck.** Es la dirección más barata de las tres, por lejos.

**En contra.** Deja **prosa muerta sin dueño**. Si el `cuando_usarlo` siempre pierde, las 16
instrucciones quedan letra muerta y se siguen sirviendo en `llms-full.txt` y en `index.json`: la IA
lee texto que el sistema le dice ignorar, el validador no tiene cómo detectarlo, y el próximo que
agregue un módulo copia el patrón. Es contención, no arreglo.

## Concepto 3 · Clasificador por forma del dato

Reindexar el selector por forma del dato (cuántas cifras, cuántas columnas, hay foto o no) como hace
Presenton, más las filas que faltan y el camino "no tengo el dato".

**A favor.** La forma del dato es **derivable, no hay que anotarla a mano**: `index.json` ya trae
`rol` y `max_caracteres_aprox` por slot, así que contar slots por rol da la firma del módulo. El
selector deja de ser un archivo a mano con dueño humano. Y ataca de frente lo que se pidió
originalmente: elegir bien el slide.

**En contra.** **No resuelve el desajuste, lo acelera.** Mediana de presupuesto 694 caracteres por
módulo contra 1.062 real: clasificar mejor manda contenido de 1.062 a módulos de 694 con más
precisión. Y los módulos que faltan (3 pilares, 5 métricas, 4 casos) exigen escribir SPEC nuevo en
`slides.html`: 153KB, bus factor 1, sin tests. Es el único camino que obliga a tocar el archivo más
caro del repo.

---

## Recomendación

**Concepto 2, más las dos piezas del Concepto 1 que son de una línea. Concepto 3 se posterga
explícitamente.**

El orden importa y es este:

1. **El regex de `generate.py:36`.** Una línea, recupera 9 `cuando_usarlo` completos y con eso se
   cae buena parte de F3 y algo de F2 **sin decidir nada de diseño**. Efecto en 24% del catálogo.
   Es la mejor relación palanca/costo de toda la mesa.
2. **El bug de `validar.py:38`**, que barre `usa` y `alternativa` en el mismo set y por eso **oculta
   el hallazgo 31**: los 10 módulos que solo se alcanzan por criterio de diseño cuentan como
   alcanzables. Tres líneas, y el hueco aparece solo.
3. **`validar_pieza(path)`** — el contrato de entrega. Es lo único que hoy evita que salga una pieza
   con un dato prohibido, y reusa regex que ya existen.
4. **`ai/precedencia.json`** — la jerarquía explícita, para que ninguna IA tenga que elegir entre dos
   reglas oficiales.
5. **Los tres chequeos que ya son auditables y no estaban**: #5 lima (contar `A2FF00` por slide), #7
   niveles (contar `font-size` únicos) y #2 hue **con el calificador que faltaba** — el chequeo
   prohíbe hue 20-65° y **11 de los 39 hexes de `tokens.json` caen ahí** (toda la familia crema:
   `#F6F1EB` 32.7°, `#DCD0C4` 30°, `#C4B5A6` 30°). Agregando saturación >40% el filtro aísla
   exactamente `#E0A33A` y `#FFC67B`, que es lo que la regla quería decir.
6. **`data-accent="grupo"`** — el tercer estado para F2: los N candidatos elegibles se marcan como
   grupo y la regla pasa a ser "exactamente uno del grupo lleva `#A2FF00`, elegí cuál". Misma
   mecánica que `data-reemplazable`, que ya funciona con 13 usos y 0 fallas. No toca geometría: el
   rect ya existe, solo cambia de qué grupo es miembro. Y por primera vez hace el chequeo #5
   auditable.

**Elegiría el Concepto 1 completo** si aparece un segundo consumidor real de la capa (hoy no hay
ninguno fuera del repo, hallazgo 11) o si el modelo de datos de redes/merch se necesita por otra
razón. **Elegiría el Concepto 3** cuando el desajuste de presupuesto esté resuelto — antes, mejora la
precisión de mandar contenido a un módulo que no le da.

## La decisión que no puede tomar el panel

**¿Quién es dueño de la regla tipográfica y del golpe de lima: la plantilla o el checklist?**

- Si manda la **plantilla**: el checklist se reescribe para admitir 5-7 niveles con jerarquía
  declarada, y "un golpe de lima por slide" pasa a "como máximo uno". Barato, y admite que el
  catálogo es la verdad.
- Si manda el **checklist**: hay que rehacer 37 SPEC en un archivo de 153KB con bus factor 1 y sin
  tests. Caro y riesgoso.

Ninguna de las tres direcciones contiene esta decisión, y sin ella el gate del Concepto 1 nace rojo.
