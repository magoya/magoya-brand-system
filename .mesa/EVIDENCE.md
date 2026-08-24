# Evidencia

`[E]` evidencia verificable · `[I]` inferencia · `[S]` supuesto

## G0 — Encuadre

| # | Hallazgo | Fuente | Tipo | Confianza |
|---|---|---|---|---|
| 1 | El que arma el deck no es dueño del copy: el texto entra "ya aprobado, bloqueado" y los huecos se devuelven a Varu/Pato | `magoya-deck/ROADMAP.md:3, :35, :42` | E | alta |
| 2 | El "agente de copy que reescribe cada texto" no tiene mandato real; lo que hace falta es señalar qué falta | `ai/metodo.md:27` vs. hallazgo 1 | I | alta |
| 3 | Nadie llega con la narrativa pensada: el insumo real es transcript de Granola (16 reuniones), doc de la CEO, decks viejos | `brand-system/PLAN.md:13, :17` | E | alta |
| 4 | La causa documentada de que un deck no cerrara fue "narrativa sin dueño" y "multi-audiencia sin hilo único" — no las plantillas | `brand-system/PLAN.md:21-23` | E | alta |
| 5 | La Fase 1 de metodo.md exige como INSUMO ("escribí LA idea") lo que el equipo nunca produce | `ai/metodo.md:11` vs. hallazgo 3 | I | alta |
| 6 | Los decks de cuenta grande son en inglés y no traducidos; salió material con inglés roto ("tested during the righ ag window") | `VOICE-RESEARCH.md:296, :306` | E | alta |
| 7 | El sistema tiene una sola voz para cinco audiencias | `VOICE-RESEARCH.md:320` | E | alta |
| 8 | El costo se paga en vueltas: 48 commits en 9 días en la propuesta JD, 27 de ellos apply/feedback/fix/sync; slide de inversión retocada ~7 veces; 3 variantes de PDF por audiencia | `john-deere-pilot-proposal` (git log 2026-07-09 → 07-17) | E | alta |
| 9 | El costo de copy inventado ya tiene mitigación puesta (`ai/facts.json`), tras el commit "revert invented copy to grounded/flagged versions" | JD, commit 2026-07-10 | E | alta |
| 10 | **Cero decks reales pasaron por la capa**: salió 2026-08-13, el último deck de cuenta grande es 2026-08-11 | fechas de repo | E | alta |
| 11 | Ningún archivo fuera de `brand-system` referencia `selector.json`, `templates/index.json` ni `metodo.md`. El usuario "cualquier IA de un tercero" todavía no apareció | grep en `/Users/facu/Claude` | E | alta |
| 12 | Bus factor = 1: Facu produce, decide y tiene el material fuente | `ROADMAP.md:245` (R6) | E | alta |
| 13 | Hay cola más barata con exposición directa en cuentas que facturan: roster con nombres falsos (A5, "el placeholder más caro"), cita de Camila (A6), pase de inglés | `ROADMAP.md:123` | E | alta |
| 14 | Faltan tres números para evaluar la inversión: valor de deal por deck, decks/mes y vueltas promedio, horas por vuelta | `ai/facts.json:27` los declara sin fuente | E | alta |
