# Riesgos

| # | Riesgo | Prob. | Impacto | Mitigación | Dueño |
|---|---|---|---|---|---|
| R1 | Rediseñar a ciegas: se cambia una capa cuyo modo de falla nunca se midió (E10) | alta | alto | correr la prueba a ciegas como primer acto de G1, antes de proponer nada | pm |
| R2 | Construir para un usuario que no existe (E11): "cualquier IA" contra Facu-en-Claude-Code | media | alto | G2 usa esto como eje de las tres direcciones, no como detalle | pm |
| R3 | Desplazar trabajo más barato y más expuesto (E13: roster falso, cita sin aprobar, inglés roto) | alta | alto | dejarlo explícito en el checkpoint; es decisión de Facu, no del panel | negocio |
| R4 | Que la capa nueva pida más disciplina de la que el flujo real tolera y quede sin usar | media | medio | G3 con usuario-no-adopta; el criterio de éxito exige cero vueltas de reconciliación | pm |
| R5 | Sesgo de autoevaluación: el mismo sistema define el checklist y se puntúa contra él | media | medio | la prueba a ciegas separa generador de crítico; el crítico no ve la generación | pm |
