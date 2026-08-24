# Agente de validación: ¿puede cualquier IA consumir este brand al máximo?

**Corre semanal** (tarea programada `validar-fusion-ia-brand`). Este archivo es el protocolo —
editalo y la próxima corrida usa la versión nueva. El registro de cada corrida va en
[`VALIDACION-IA.md`](VALIDACION-IA.md).

La pregunta que el agente tiene que poder contestar cada semana, con evidencia:

> Si alguien que no sabe de diseño le pasa un link de `brand.magoya.com` a la IA que tenga a mano
> y le pide una pieza, ¿sale bien la primera vez, sin que esa persona tenga que adaptar ni asumir nada?

Un "sí" no se declara: se prueba a ciegas y se puntúa contra el checklist.

---

## Bloque 1 — Validación determinística

```bash
cd /Users/facu/Claude/brand-system && python3 ai/validar.py --red
```

Chequea sin criterio humano: referencias cruzadas selector ↔ plantillas, slots sin límite de texto,
cifras de ejemplo que se puedan entregar como reales, drift entre la capa publicada y sus fuentes,
URLs que no resuelven, cobertura de las familias de restricción, nomenclatura IA/AI y peso de las
entradas. **Exit code 1 = hay fallas.**

Reglas de actuación:

- **Falla mecánica** (link roto, drift, referencia que no cierra, cifra sin `[XX]`, `AI` en copy
  español): arreglala y commiteala. Son bugs, no decisiones.
- **Hueco** (`pendiente_de_definir`, dato sin aprobar, slot sin nota): **NO lo llenes**. Va a la
  sección "Necesita tu decisión" del ledger, con la pregunta concreta y por qué importa.
- Si el validador se rompe por un cambio de estructura, arreglá el validador y decilo.

## Bloque 2 — Prueba a ciegas (la medición que importa)

Tres subagentes independientes, cada uno con **solo una URL pública** y un pedido — nada más. Sin
contexto de esta conversación, sin acceso al repo: exactamente lo que tiene un usuario afuera.

**Cada uno con `isolation: "worktree"`.** En la primera corrida dos agentes compartieron directorio
y uno sobreescribió el script del otro. No invalidó los resultados —de hecho produjo un hallazgo por
accidente— pero la ceguera tiene que ser por sandbox, no por instrucción. Pediles igual que declaren
toda fuente que usen, para poder descartar la corrida si tocaron el repo.

| # | Entrada | Pedido |
|---|---|---|
| 1 | `https://brand.magoya.com/ai/claude.md` | un deck de 5 slides para presentarle a un cliente AgTech nuevo qué hace Magoya |
| 2 | `https://brand.magoya.com/llms-full.txt` | un post de LinkedIn anunciando una capacidad concreta del equipo |
| 3 | `https://brand.magoya.com/ai/gemini.md` | un carrusel 4:5 de **IA en campo** para productores |

Después, **un cuarto subagente crítico que no vio cómo se generó nada** puntúa cada salida contra
los 16 chequeos de [`checklist.md`](checklist.md) y contra `ai/constraints.json`. Y mide la métrica
primaria: **qué porcentaje de los títulos de contenido son aserciones** (sujeto + verbo +
afirmación) y no etiquetas de tema. Línea de base 17% sobre una propuesta real; objetivo ≥80%. Para cada pieza:
chequeos que pasan, cuáles fallan y **por qué falló** — ¿la regla no estaba escrita, estaba escrita
pero enterrada, o estaba clara y la IA la ignoró?

Esa última columna es el producto real del bloque: distingue un hueco del spec de un problema de
fetch de un límite del modelo. Solo el primero se arregla acá.

Rotá el pedido cada corrida (una landing, un one-pager comercial, una tabla de precios, un banner
de LinkedIn) para no optimizar contra un solo caso.

## Bloque 3 — Investigación externa

Qué cambió desde la corrida anterior (fecha en el ledger). Buscá y verificá, no supongas:

1. **Mecanismos de consumo por herramienta** — Claude (Skills, MCP, Projects, Code), ChatGPT
   (GPTs, Apps, connectors), Gemini (Gems, AI Studio), Copilot. ¿Apareció una forma de entregar
   un design system que le gane a una URL? ¿Cambiaron límites de contexto, de archivo o de fetch?
   Si algo cambió, **hay que actualizar la entrada de esa herramienta** (`ai/<tool>.md`), que se
   versiona por separado justamente para esto.
2. **Convenciones** — estado de `llms.txt`, DTCG design tokens, servidores MCP de design systems.
3. **Comparación** — cómo publican para IA Atlassian, Polaris, Carbon, Material. ¿Alguien resolvió
   algo que acá se resuelve peor?

Descartá lo que sea marketing. Solo entra lo que cambie una decisión concreta del sistema.

## Bloque 4 — Escribir el ledger

Agregá una entrada arriba en [`VALIDACION-IA.md`](VALIDACION-IA.md) con este formato:

```markdown
## AAAA-MM-DD

**Validador:** N fallas · N huecos · N ok
**Prueba a ciegas:** pieza 1 — X/16 · pieza 2 — X/16 · pieza 3 — X/16
**Arreglado y commiteado:** …
**Necesita tu decisión:** …  (la pregunta concreta, nunca un valor inventado)
**Del mundo afuera:** …  (solo lo que cambie algo, con link)
**Propuesta para la próxima:** …  (máximo 3, ordenadas por impacto)
```

Commiteá el ledger y los arreglos mecánicos. **Nunca** commitees un valor de marca que no esté ya
decidido en `tokens.json`, `constraints.json` o `BRAND.md`.

## Cierre

Un párrafo, en criollo, con lo que hay que saber. Si no hay nada accionable, decilo en una línea:
_"Validador limpio, prueba a ciegas 16/16/15, nada nuevo afuera."_ No infles el reporte.

---

## Buscá contradicciones, no solo estructura

El aprendizaje más caro de la primera auditoría: `validar.py` daba **0 fallas** y había **16
contradicciones reales** entre documentos oficiales. El validador cruza estructura (¿resuelven los
links, tienen límite los slots) y no consistencia entre reglas escritas en prosa en archivos
distintos. Cuando el crítico marque un chequeo como fallado, preguntate siempre si el que está mal
es la pieza o **el chequeo**: 37 de 41 plantillas fallaban el límite de 3 niveles tipográficos, y la
que estaba mal era la regla. `ai/precedencia.json` dice quién gana; si una contradicción nueva no
entra en esa ley, va al ledger como decisión pendiente.

## Lo que este agente NO hace

- No inventa valores de marca. Si falta una definición, la pregunta.
- No cambia decisiones de diseño ya tomadas porque otro sistema hace otra cosa.
- No toca nombres de archivo ni URLs publicadas: romperían los links y las entradas por herramienta.
- No publica datos de `facts.json` que estén en `pendiente_de_aprobar`.
