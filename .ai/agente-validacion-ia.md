# Agente de validación: ¿puede cualquier AI consumir este brand al máximo?

**Corre semanal** (tarea programada `validar-fusion-ia-brand`). Este archivo es el protocolo —
editalo y la próxima corrida usa la versión nueva. El registro de cada corrida va en
[`VALIDACION-IA.md`](VALIDACION-IA.md).

La pregunta que el agente tiene que poder contestar cada semana, con evidencia:

> Si alguien que no sabe de diseño le pasa un link de `brand.magoya.com` a la AI que tenga a mano
> y le pide un contenido, ¿sale bien la primera vez, sin que esa persona tenga que adaptar ni asumir nada?

Un "sí" no se declara: se prueba a ciegas y se puntúa contra el checklist.

---

## Bloque 1 — Validación determinística

```bash
# desde la raíz del repo
python3 ai/validar.py --red
```

Chequea sin criterio humano: drift entre la capa publicada y sus fuentes, URLs que no resuelven,
conteo de assets consistente entre entradas, cobertura de las familias de restricción, nomenclatura
AI (regla del Brand Playbook, slide 50), colores fuera de rango, geometría única del wordmark y peso
de las entradas. **Exit code 1 = hay fallas.**

Reglas de actuación:

- **Falla mecánica** (link roto, drift, conteo desparejo, la sigla en español en vez de AI en el
  copy, o "IA en Campo" mal escrito): arreglala y commiteala. Son bugs, no decisiones.
- **Hueco** (`pendiente_de_definir`, dato sin aprobar): **NO lo llenes**. Va a la
  sección "Necesita tu decisión" del ledger, con la pregunta concreta y por qué importa.
- Si el validador se rompe por un cambio de estructura, arreglá el validador y decilo.

## Bloque 2 — Prueba a ciegas (la medición que importa)

Tres subagentes independientes, cada uno con **solo una URL pública** y un pedido — nada más. Sin
contexto de esta conversación, sin acceso al repo: exactamente lo que tiene un usuario afuera.

**Cada uno con `isolation: "worktree"` Y con un directorio de salida exclusivo.** En la primera corrida dos agentes compartieron directorio
y uno sobreescribió el script del otro. No invalidó los resultados —de hecho produjo un hallazgo por
accidente— pero la ceguera tiene que ser por sandbox, no por instrucción. Pediles igual que declaren
toda fuente que usen, para poder descartar la corrida si tocaron el repo.

| # | Entrada | Pedido |
|---|---|---|
| 1 | `https://brand.magoya.com/ai/claude.md` | un mail para presentarle a un cliente nuevo del agro qué hace Magoya |
| 2 | `https://brand.magoya.com/llms-full.txt` | un post de LinkedIn anunciando una capacidad concreta del equipo |
| 3 | `https://brand.magoya.com/ai/gemini.md` | un carrusel 4:5 de **IA en Campo** para productores |

Después, **un cuarto subagente crítico que no vio cómo se generó nada** puntúa cada salida contra
[`checklist-verbal.md`](checklist-verbal.md), contra los chequeos de [`checklist.md`](checklist.md) que apliquen y contra `ai/constraints.json`. Y mide la métrica
primaria: **qué porcentaje de los títulos de contenido son aserciones** (sujeto + verbo +
afirmación) y no etiquetas de tema. Línea de base 17% sobre una propuesta real; objetivo ≥80%. Para cada pieza:
chequeos que pasan, cuáles fallan y **por qué falló** — ¿la regla no estaba escrita, estaba escrita
pero enterrada, o estaba clara y la AI la ignoró?

Esa última columna es el producto real del bloque: distingue un hueco del spec de un problema de
fetch de un límite del modelo. Solo el primero se arregla acá.

Rotá el pedido cada corrida (un texto de landing, un post, una propuesta, un carrusel de IA en
Campo) para no optimizar contra un solo caso. Se puede repetir un pedido a propósito cuando la parte
del sistema que ejercita es nueva, pero decilo en el ledger.

**Tres instrucciones que la corrida del 2026-09-07 mostró que hacen falta, textuales:**

- **Cada agente escribe SOLO en su propio directorio** (`.../ciegas/pN/`). Los tres compartieron el
  scratchpad y el segundo vio la pieza del primero. El worktree aísla el repo, no el directorio de
  trabajo.
- **Prohibido renderizar la pieza en un navegador**: verificar leyendo el HTML. Una corrida se colgó
  diez minutos ahí y hubo que relanzarla entera.
- **La hoja de estado se escribe ANTES de pulir la pieza.** Con eso, una corrida que se cuelga igual
  deja su registro.

**Congelá el push mientras las pruebas están en el aire, y pedí la hora de cada fetch.** El
2026-08-31 otra sesión pusheó a mitad de corrida y Pages rebuildeó con dos de las tres pruebas
todavía leyendo: los puntajes de esa corrida no se pueden comparar con los de la siguiente porque
midieron dos versiones distintas del sistema. Antes de lanzar los agentes, mirá si hay otra sesión
trabajando en el repo (`git log --since='2 hours ago'`, worktrees abiertos) y no pushees nada hasta
que las tres terminen.

**Y no confíes en el worktree para la ceguera: aísla el filesystem, no el contexto.** En la misma
corrida el harness le inyectó a un agente el `MEMORY.md` del usuario, y otro vio la pieza de un
tercero a través del panel de browser compartido. Los tres lo declararon porque se los pediste
explícitamente — seguí pidiéndolo, es lo único que lo detecta.

## Bloque 3 — Investigación externa

Qué cambió desde la corrida anterior (fecha en el ledger). Buscá y verificá, no supongas:

1. **Mecanismos de consumo por herramienta** — Claude (Skills, MCP, Projects, Code), ChatGPT
   (GPTs, Apps, connectors), Gemini (Gems, AI Studio), Copilot. ¿Apareció una forma de entregar
   un design system que le gane a una URL? ¿Cambiaron límites de contexto, de archivo o de fetch?
   Si algo cambió, **hay que actualizar la entrada de esa herramienta** (`ai/<tool>.md`), que se
   versiona por separado justamente para esto.
2. **Convenciones** — estado de `llms.txt`, DTCG design tokens, servidores MCP de design systems.
3. **Comparación** — cómo publican para AI Atlassian, Polaris, Carbon, Material. ¿Alguien resolvió
   algo que acá se resuelve peor?

Descartá lo que sea marketing. Solo entra lo que cambie una decisión concreta del sistema.

## Bloque 4 — Escribir el ledger

Agregá una entrada arriba en [`VALIDACION-IA.md`](VALIDACION-IA.md) con este formato:

```markdown
## AAAA-MM-DD

**Validador:** N fallas · N huecos · N ok
**Prueba a ciegas:** pedido 1: X/N · pedido 2: X/N · pedido 3: X/N
**Arreglado y commiteado:** …
**Necesita tu decisión:** …  (la pregunta concreta, nunca un valor inventado)
**Del mundo afuera:** …  (solo lo que cambie algo, con link)
**Propuesta para la próxima:** …  (máximo 3, ordenadas por impacto)
```

Commiteá el ledger y los arreglos mecánicos. **Nunca** commitees un valor de marca que no esté ya
decidido en `tokens.json`, `constraints.json` o `BRAND.md`.

## Cierre

Un párrafo, en criollo, con lo que hay que saber. Si no hay nada accionable, decilo en una línea:
_"Validador limpio, prueba a ciegas sin fallas, nada nuevo afuera."_ No infles el reporte.

---

## Buscá contradicciones, no solo estructura

El aprendizaje más caro de la primera auditoría: `validar.py` daba **0 fallas** y había **16
contradicciones reales** entre documentos oficiales. El validador cruza estructura (¿resuelven los
links, cierra el conteo) y no consistencia entre reglas escritas en prosa en archivos distintos.
Cuando el crítico marque un chequeo como fallado, preguntate siempre si el que está mal es la pieza
o **el chequeo**. `ai/precedencia.json` dice quién gana; si una contradicción nueva no
entra en esa ley, va al ledger como decisión pendiente.

## Lo que este agente NO hace

- No inventa valores de marca. Si falta una definición, la pregunta.
- No cambia decisiones de diseño ya tomadas porque otro sistema hace otra cosa.
- No toca nombres de archivo ni URLs publicadas: romperían los links y las entradas por herramienta.
- No publica datos de `facts.json` que estén en `pendiente_de_aprobar`.
