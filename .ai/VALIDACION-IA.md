# Validación de la fusión AI ↔ brand system

Registro de las corridas del agente semanal. Protocolo:
[`agente-validacion-ia.md`](agente-validacion-ia.md). Lo más nuevo arriba.

La métrica que se sigue corrida a corrida es **la prueba a ciegas**: cuántos chequeos pasa un
contenido hecho por una AI que solo recibió un link. Todo lo demás es diagnóstico de por qué.

Las corridas anteriores al 22 de octubre de 2026 quedan en el historial de git; acá siguen solo las
decisiones que todavía aplican.

---

## Necesita tu decisión (abiertas al 2026-10-22)

1. **Proporciones de uso del color.** La proporción por porcentajes quedó sin efecto con el feedback
   del equipo del 22 de octubre y todavía no hay una nueva. Está declarada en
   `ai/constraints.json` (`pendiente_de_definir`).
2. **Fotos a color del equipo.** La única foto de persona disponible es la de Varina Baldi, a color.
   Faltan las del resto del equipo.
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
