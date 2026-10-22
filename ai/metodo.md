# Método de trabajo para escribir y revisar contenido de Magoya

**Versión 4.0 · 2026-10-22** · Parte del flujo de todas las entradas por AI. Cumplir la marca al pie
de la letra es la mitad del trabajo; la otra mitad es que la historia esté bien contada. Un texto
on-brand con la historia mal contada es un texto fallido.

## Fase 0: del material crudo a la idea

El insumo real nunca es un outline: es un transcript, un documento de otra persona, un texto viejo
para reciclar, o los tres a la vez.

1. **Inventariá lo que te dieron**, sin editar nada: cada bloque de contenido con su origen. Marcá
   cuál es texto aprobado (no se toca) y cuál es materia prima (se puede reordenar).
2. **Escribí LA idea vos, y mostrala.** Una frase: lo único que la audiencia se tiene que llevar. Si
   el material no alcanza para escribirla, eso no te frena: **la escribís como hipótesis y la marcás
   como tal** en el pedido a humanos. Lo que no se hace es avanzar sin haberla escrito.
3. **Registrá lo que agregás.** Todo bloque que no venía en el material es una decisión tuya: listala
   con su motivo. Lo que se agrega sin registro es donde aparecen las contradicciones con el brief.
4. **Buscá la contradicción antes de escribir.** Cruzá el material contra `ai/facts.json` y contra las
   decisiones ya tomadas. Un dato del material que contradice a `facts.json` es un bloqueo, no un
   detalle: ese dato no sale hasta que una persona decida. Y un pedido del brief que contradice una
   regla de la marca se reporta antes de intentarlo, no después.

### Gate de Fase 0: los títulos solos

Si el contenido tiene partes (secciones, slides de un carrusel, bloques de un documento), escribí
primero los títulos en orden, solos, y leelos de un tirón. Si no se reconstruye el argumento, no
estás listo para escribir el cuerpo.

**Cada título es una aserción**, no una etiqueta de tema. "Baselining and four initial experiments"
es etiqueta; "Four experiments tell us where the model breaks" es aserción. Medido: 2 de 12 en una
propuesta real (17%). Objetivo ≥80%.

## Fase 1: escribir

- Buscá la oportunidad de contar mejor: ¿ese dato rinde más como cifra destacada que enterrado en
  una lista? ¿eso que parece una lista es un caso? ¿ese párrafo es una frase esperando a ser dicha?
- El texto más corto que cuente la historia completa, gana. Una idea por bloque.
- La voz y el vocabulario salen de `.ai/verbal/guia-editorial.md` y `vocabulary.json`; la identidad,
  la oferta y el método, de `.ai/verbal/estrategia.md`.

## Fase 2: las pasadas (agentes si tu plataforma los tiene)

Nunca entregues la primera versión. Si podés desplegar subagentes, desplegalos; si no, hacé las
pasadas actuando cada rol por separado.

1. **Agente de títulos, el que más mueve la aguja.** Cada título de contenido tiene que ser una
   **aserción**: sujeto + verbo + afirmación. La base no es estética: assertion-evidence mide mejor
   comprensión y mejor recall diferido que topic-subtopic (Garner & Alley, n=110).
   **El test:** leé solo los títulos en orden. Si no se reconstruye el argumento, los títulos están
   mal, no el cuerpo.
2. **Agente de copy: marca, no reescribe.** El texto aprobado no se toca. Su trabajo es señalar:
   qué afirmación viaja sin cifra ni plazo, qué frase es relleno, qué dato no tiene fuente, y qué
   contradice algo ya decidido, incluida la capa verbal: `.ai/checklist-verbal.md` (las 8 preguntas
   de la guía editorial: brief y posicionamiento, tono constructivo, hecho vs. hipótesis vs. ejemplo,
   cifras con validación humana, permisos de clientes, uso/adopción/espacios/método, adaptación a
   audiencia y canal, lo que queda por confirmar; más definición, AI y traducciones del playbook).
   Fuente de la voz: `.ai/verbal/guia-editorial.md`. Devuelve una lista de observaciones, no una
   versión nueva. Si el copy es materia prima y sí hay que escribirlo, lo dice explícito antes.
3. **Agente de diseño (si hay algo visual).** Verifica `.ai/checklist.md`, `tokens.json` y
   `ai/constraints.json`. **Cuando dos reglas oficiales se contradicen, aplicá
   `ai/precedencia.json` y reportá la contradicción; no la resuelvas por criterio propio.**
4. **Agente crítico, el que refuta.** Una sola consigna: *encontrá la parte más débil y proponé cómo
   contarla mejor.* La ronda que refuta encuentra más que la que construye. Si el crítico no encontró
   nada, no estaba criticando.

## Fase 3: criterio de entrega

**Técnico.** Los chequeos de `.ai/checklist-verbal.md` para el texto y los de `.ai/checklist.md` si
hay algo visual. Si tenés el repo:

```
python3 ai/validar.py --entrega <tu-archivo>
```

**Narrativo.**

| Qué | Umbral | Cómo se mide |
|---|---|---|
| Títulos-aserción | ≥80% | contalos: sujeto + verbo + afirmación |
| La historia leída solo de títulos | cierra | leelos en orden, sin el cuerpo |
| Bloque prescindible | ninguno | si borrás un bloque y la historia no pierde nada, borralo |
| El dato más fuerte | en el lugar más visible | si la mejor cifra está enterrada, movela |

**No midas legibilidad con Flesch, INFLESZ ni Fernández Huerta.** Las fórmulas piden prosa corrida de
100+ palabras y los bullets sin verbo inflan el score: medido sobre una propuesta real, el largo de
oración ya daba sano mientras 10 de 12 títulos no decían nada. El test de títulos es el que discrimina.

**Contrato de entrega** (`ai/precedencia.json` lo detalla). Lo esencial:

- Un dato que no está en `facts.json` **no se escribe**. Va como `[PENDIENTE]` visible.
- Si el material trae un dato que **contradice** a `facts.json`, ese dato no sale.
- Toda entrega con huecos lleva al final un bloque **PEDIDO A HUMANOS**: qué falta y a quién se le pide.
- Con aunque sea un `[PENDIENTE]`, el entregable se marca **BORRADOR**. Sin ninguno, puede salir
  como final.

Entregá también una nota corta de decisiones: qué agregaste que no venía en el material, qué
contradicciones encontraste y qué encontró el crítico.

## Changelog

- **4.0** (2026-10-22): el método deja de armar piezas desde un catálogo, que se retiró del sistema por decisión del equipo. Queda para escribir y revisar contenido de marca: la idea antes del texto, los títulos-aserción, las pasadas de copy, diseño y crítica, y el contrato de entrega. El validador pasa a `validar.py --entrega`.
- **3.2** (2026-10-19): el agente de copy corre el checklist verbal rearmado sobre las 8 preguntas de la Guía editorial V2 (`.ai/verbal/guia-editorial.md`), que pasa a ser la fuente de la voz y el tono; las cifras sin validación humana y los conflictos entre fuentes se señalan, no se resuelven.
- **3.1** (2026-10-19): el agente de copy y el criterio de entrega suman el checklist verbal del Magoya Brand Playbook (octubre 2026).
- **1.0 a 3.0** (2026-08-10 a 2026-08-19): versiones atadas al catálogo de piezas que se retiró en la 4.0.
