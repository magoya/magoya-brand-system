# Plan — Capa de narrativa: de material crudo a deck bien contado

**Estado general**: 🟡 en curso · **Gate abierto**: G4 (G0-G3 cerrados; el eje narrativo ejecutado) · **Última actualización**: 2026-08-19

## Problema (G0)

**Lo que llegó pedido:** "la IA no analiza bien el copy ni elige bien los slides".

**El problema real, según la evidencia:** el sistema asume que el contenido llega pensado y
aprobado, y se planta justo *después* del trabajo difícil. En la realidad el insumo es crudo
—transcript de Granola, un doc de la CEO, un deck viejo para reciclar— y sin dueño de narrativa.
El costo no se paga escribiendo ni maquetando: se paga en las vueltas de reconciliación (detectar
qué falta, a quién pedírselo, mantener variantes por audiencia).

Y hay un agujero de medición encima: **ningún deck real pasó todavía por la capa**. La capa
copiá-pegá salió el 2026-08-13; el último deck de cuenta grande es del 2026-08-11.

## Criterio de éxito

Una IA que recibe **material crudo real** (un transcript o un doc, más `ai/facts.json`) produce un
deck donde: (1) la historia se entiende leyendo solo los títulos en orden, (2) pasa los 16 chequeos,
(3) **declara explícitamente qué le falta y a quién pedírselo** en vez de rellenar, y (4) no obliga
a una vuelta de reconciliación.

Línea de base = puntaje de la prueba a ciegas. Sin ese número no hay con qué comparar.

## Gates

| Gate | Estado | Entregable | Owner | Fecha | Nota |
|---|---|---|---|---|---|
| G0 Encuadre | **cerrado** | problema + criterio | pm | 2026-08-19 | reencuadrado: el problema está aguas arriba |
| G1 Evidencia | **cerrado** | 68 hallazgos + línea de base | investigador, analista-datos | 2026-08-19 | 2 pruebas a ciegas: 16 contradicciones con el validador en 0 fallas |
| G2 Conceptos | **cerrado** | 3 direcciones + recomendación | pm, arquitectura | 2026-08-19 | ejecutado el concepto 2 completo (D3) |
| G3 Challenge | **cerrado** | tensiones + cambios obligatorios | red-team, usuario-no-adopta, dominio, challenger-mercado | 2026-08-19 | retiró el gate de textura; el eje pasó a rol narrativo (D5, D6) |
| G4 Baja | pendiente | flujo de decisión en baja | flujos | | ver nota de adaptación |
| G5 Alta | pendiente | los archivos reales de la capa | interfaz | | ver nota de adaptación |
| G6 Handoff | pendiente | spec de la capa | spec, arquitectura | | |

**Nota de adaptación:** esta iniciativa no tiene UI. El artefacto es un spec que lee una IA. G4 se
reinterpreta como el árbol de decisión en baja fidelidad y G5 como los archivos publicados. Si no,
G4/G5 se saltan y se va de G3 a G6.

## Fuera de alcance (explícito)

- Reescribir el copy. La lente de dominio mostró que el texto entra bloqueado y aprobado: el agente
  de copy que hoy "reescribe cada texto" no tiene mandato. Se cambia el mandato, no se amplía.
- El pase nativo de inglés y la voz por audiencia. Es un problema real y caro (JD/Bayer/IntelinAir)
  pero es una decisión de personas, no de sistema. Va a la cola, no acá.
- Nombres de archivo y URLs publicadas.

## Bloqueos

- **La prueba a ciegas no corrió.** Es la línea de base de todo. Hasta que exista, cualquier rediseño
  es a ciegas. Se corre en G1.
- Negocio no firma el ROI sin tres números que no están en `ai/facts.json`: valor de deal por deck de
  cuenta grande, decks por mes y vueltas promedio, horas por vuelta. Registrado como disidencia.
