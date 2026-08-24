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

## G1 — Evidencia · investigador (material crudo → deck)

| # | Hallazgo | Fuente | Tipo | Confianza |
|---|---|---|---|---|
| 15 | Ninguna categoría de corrección domina por conteo (~46 commits JD: ~12 visual, ~11 narrativa, ~7 dato, ~5 variante por audiencia) pero **solo la narrativa regresiona**: el commit `0b53c45` tuvo que *restaurar* la tesis mid-market que una ronda anterior había borrado sin que nadie lo notara | `john-deere-pilot-proposal` git log | E | alta |
| 16 | El corpus de feedback más grande es abrumadoramente visual (F01–F60): "el título no dice nada" aparece 2 veces, "el dato no es real" 1 vez. Las rondas 2 y 3 del Knowledge Experience son 14 carpetas de A/B puramente visual, cero variante narrativa | `AUDITORIA-FEEDBACK.md` F14, F35:112, F43:125 · `magoya-deck-round3/` | E | alta |
| 17 | **La capa no se puede calibrar contra lo que la gente pide.** Pide visual porque el copy entra bloqueado y es el único grado de libertad que queda. Hay que calibrar contra lo que se rompe callado: detectar regresión de tesis entre vueltas vale más que detectar títulos flojos | derivado de 15 y 16 | I | alta |
| 18 | El material crudo **crece ~60% y crece justo donde contradice el brief**: 8 slides en el Master Script → 13 en `app/deck.json` → "14 scenes". Los 5 agregados (Agenda, pillars IT-only, mapa, quote de Apeel, foto de founder) no están en el script | `PLAN.md:13` · `app/deck.json:16,73,120,132,136-142` · `magoya-deck/DESIGN-BRIEFS.md:3` | E | alta |
| 19 | Ahí viven las contradicciones: la CEO pidió "sin personas, sin fotos" y el slide agregado s7c es exactamente una foto de persona. Con los datos igual: "16+ years", "20+ years" y "9+ years" conviven en el mismo archivo, y `facts.json` solo respalda 2017 (=9) | `PLAN.md:16, :80` · `app/deck.json:28, :37, :141` · `ai/facts.json:7, :27` | E | alta |
| 20 | **Quién decidió las 5 slides agregadas y con qué criterio no está escrito en ningún archivo.** `PLAN.md:56` describe el paso como "mapear las 8 slides a arquetipos" — mapeo, no expansión | ausencia de registro | E | alta |
| 21 | Paso invisible, mitad 1: **reconciliar copy nuevo contra decisiones estructurales ya tomadas.** El commit `1898eba` se llama literalmente "reconciled with prior structural decisions" y al día siguiente `dca5848` tuvo que elegir autoridad entre fuentes en conflicto. Ese ledger vive solo en la cabeza de Facu | JD git log | E | alta |
| 22 | Paso invisible, mitad 2: **declarar el hueco en la pieza.** Ya existe como conducta humana y como convención inventada — `70e4e1a` "blank Investment values to USD xx (avoid confusion until confirmed)" — y hay 3-4 commits de propagarla a mano a las otras copias del mismo contenido | JD git log `70e4e1a`, `6524f52` | E | alta |
| 23 | **El gate que se le pide a la IA no mide nada de esto**: los 16 chequeos de `.ai/checklist.md` son 16/16 visuales o léxicos (hex, lima, 75/25, chips, emojis, IA-vs-AI). Cero sobre huecos, procedencia del dato, contradicción con decisión previa o adecuación a audiencia | `.ai/checklist.md` | E | alta |

**Huecos declarados por el investigador (no se tapan):**
- n=1 en decks de cliente real: toda la clasificación de vueltas sale de la propuesta JD. Con un segundo deck de cuenta grande clasificado, el hallazgo 17 pasa de inferencia a evidencia.
- **No hay transcript ni doc crudo en disco.** Se leyó el *resumen* del Master Script y de las 16 reuniones en `PLAN.md:12-26`, no las fuentes. No se puede verificar si la CEO manda narrativa o bullets, y eso cambia por completo qué tiene que hacer la capa en el primer paso.
- Quién agregó las 5 slides: sin registro. Si fue Facu de cabeza, es el paso invisible más caro y hay que escribirlo; si lo pidieron Varu/Pato, el hueco es de sincronización con el Master Script, no de criterio.
