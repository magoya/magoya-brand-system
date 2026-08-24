# Método de trabajo — obligatorio para cualquier pieza con contenido

**Versión 2.0 · 2026-08-19** · Parte del flujo de todas las entradas por IA. Cumplir la marca al pie
de la letra es la mitad del trabajo; la otra mitad es que la historia esté bien contada. Una pieza
on-brand con la historia mal contada es una pieza fallida.

> **Lo que cambió en la v2.0 y por qué.** Una auditoría a ciegas (dos IA que solo recibieron una URL
> pública) mostró tres cosas. Una: la v1.3 pedía como **insumo** que escribieras "LA idea", y nadie
> llega con eso — el material real es un transcript, un doc de la CEO o un deck viejo. Dos: el agente
> de copy "reescribía cada texto", y el copy entra aprobado y bloqueado: reescribirlo es trabajo que
> después hay que revertir. Tres: declarar un hueco no es lo mismo que no entregarlo — una IA marcó
> cinco cifras como no verificables en su reporte y las dejó escritas en la slide igual.

## Fase 0 — Del material crudo a la narrativa

**Esta fase antes no existía y es donde se pierde el deck.** El insumo real nunca es un outline: es
un transcript, un documento de otra persona, un deck viejo para reciclar, o los tres a la vez.

1. **Inventariá lo que te dieron**, sin editar nada: cada bloque de contenido con su origen. Marcá
   cuál es texto aprobado (no se toca) y cuál es materia prima (se puede reordenar).
2. **Escribí LA idea vos, y mostrala.** Una frase: lo único que la audiencia se tiene que llevar. Si
   el material no alcanza para escribirla, eso no te frena — **la escribís como hipótesis y la marcás
   como tal** en el pedido a humanos. Lo que no se hace es avanzar sin haberla escrito.
3. **Contá los beats y comparalos con lo que te dieron.** Si el material trae 8 bloques y tu narrativa
   necesita 13, esos 5 de más son decisiones tuyas: **listalas una por una con su motivo.** En la
   auditoría, un deck creció de 8 a 13 slides y nadie registró quién agregó las 5 ni por qué — y ahí
   vivían las contradicciones con el brief.
4. **Buscá la contradicción antes de diseñar.** Cruzá el material contra `ai/facts.json` y contra las
   decisiones ya tomadas. Un dato del material que contradice a `facts.json` es un bloqueo, no un
   detalle: la slide no sale hasta que una persona decida. Y un pedido del brief que contradice a
   otro ("dark mode" contra `fondos_permitidos`) se reporta antes de intentarlo, no después.

## Fase 1 — Elegir cada módulo por criterio

- Para cada beat, usá el **selector** (`ai/selector.json`): qué querés contar → qué módulo, sin
  criterio de diseño. Ante dos candidatos, leé el `cuando_usarlo` de los dos y justificá.
- **Si ninguna fila aplica, no fuerces.** Diez de los 41 módulos solo se alcanzan por una cláusula
  condicionada a criterio, y hay tipos de contenido que todavía no tienen fila (journey de dos
  niveles, cinco cifras, cartera de varios casos en un slide). Si tu contenido es uno de esos:
  elegí el módulo más cercano, **declará que elegiste contra el selector y por qué**, y reportá la
  fila que falta. Repurposar un módulo tiene costos invisibles — el acento de lima de B1 está en la
  card del medio, así que usarlo para tres pilares destaca el segundo sin ningún motivo semántico.
- Buscá la oportunidad de contar mejor: ¿ese dato rinde más como cifra gigante que como bullet? ¿eso
  que parece una lista es un caso de éxito? ¿ese párrafo es un statement esperando a ser una frase?
- El deck más corto que cuente la historia completa, gana. Una idea por slide.

## Fase 2 — Las tres pasadas (agentes si tu plataforma los tiene)

Nunca entregues la primera versión. Si podés desplegar subagentes, desplegalos; si no, hacé las
pasadas actuando cada rol por separado.

1. **Agente de títulos — el que más mueve la aguja.** Cada título de contenido tiene que ser una
   **aserción**: sujeto + verbo + afirmación. No una etiqueta de tema. "Baselining and four initial
   experiments" es una etiqueta; "Four experiments tell us where the model breaks" es una aserción.
   *Línea de base medida: 2 de 12 títulos de una propuesta real eran aserciones (17%). El objetivo es
   ≥80%.* La base no es estética: assertion-evidence mide mejor comprensión y mejor recall diferido
   que topic-subtopic (Garner & Alley, n=110).
   **El test:** leé solo los títulos en orden. Si no se reconstruye el argumento, los títulos están
   mal, no el cuerpo.
2. **Agente de copy — marca, no reescribe.** El texto aprobado no se toca. Su trabajo es señalar:
   qué afirmación viaja sin cifra ni plazo, qué frase es relleno, qué dato no tiene fuente, y qué
   contradice algo ya decidido. Devuelve una lista de observaciones, no una versión nueva. Si el copy
   es materia prima y sí hay que escribirlo, lo dice explícito antes de hacerlo.
3. **Agente de diseño.** Verifica plantilla oficial sin cambios de geometría, slots dentro de
   `max_caracteres`, y `ai/constraints.json`. **Cuando dos reglas oficiales se contradicen, aplicá
   `ai/precedencia.json` y reportá la contradicción — no la resuelvas por criterio propio.**
4. **Agente crítico — el que refuta.** Una sola consigna: *encontrá el slide más débil y proponé cómo
   contarlo mejor.* La ronda que refuta encuentra más que la que construye. Si el crítico no encontró
   nada, no estaba criticando.

## Fase 3 — Criterio de entrega

**Técnico.** Los 16 chequeos de `.ai/checklist.md`, más:

```
python3 ai/validar.py --pieza <tu-archivo.html>
```

**Narrativo.**

| Qué | Umbral | Cómo se mide |
|---|---|---|
| Títulos-aserción en slides de contenido | ≥80% | contalos: sujeto + verbo + afirmación |
| La historia leída solo de títulos | cierra | leelos en orden, sin el cuerpo |
| Densidad | mediana ≤110 palabras por slide | contá palabras visibles |
| Slide prescindible | ninguno | si borrás un slide y la historia no pierde nada, borralo |
| El dato más fuerte | en el slide más fuerte | si la mejor cifra está en un bullet, movela |

**No midas legibilidad con Flesch, INFLESZ ni Fernández Huerta.** Las fórmulas piden prosa corrida de
100+ palabras y los bullets sin verbo inflan el score: medido sobre una propuesta real, el largo de
oración ya daba sano mientras 10 de 12 títulos no decían nada. El test de títulos es el que discrimina.

**Contrato de entrega** (`ai/precedencia.json` lo detalla). Lo esencial:

- Un dato que no está en `facts.json` **no se escribe**. Va como `[PENDIENTE]` visible.
- Si el material trae un dato que **contradice** a `facts.json`, la slide no sale.
- Toda entrega lleva un bloque **PEDIDO A HUMANOS**: qué falta, a quién se le pide, qué se desbloquea.
- Con aunque sea un `[PENDIENTE]`, la pieza se entrega marcada **BORRADOR**. Sin ninguno, puede salir
  como final.

Entregá también una nota corta de decisiones: qué módulos elegiste y por qué, qué elegiste contra el
selector, qué agregaste que no venía en el material, y qué encontró el crítico.

## Changelog

- **2.0** (2026-08-19): Fase 0 nueva (del material crudo a la narrativa, con registro de lo que
  agregás y búsqueda de contradicciones antes de diseñar) · el agente de copy marca en vez de
  reescribir · agente de títulos con umbral medido (17% → 80%) · contrato de entrega y
  `validar --pieza` · legibilidad por fórmula descartada con evidencia · `ai/precedencia.json` para
  cuando dos reglas oficiales chocan.
- **1.3** (2026-08-11): fase 1 exige `ai/facts.json` como única fuente de datos de la empresa.
- **1.2** (2026-08-11): fase 2 usa el selector; el agente de diseño valida plantilla-sin-cambios.
- **1.1** (2026-08-10): el checklist técnico pasa a 15 chequeos.
- **1.0** (2026-08-10): primera versión.
