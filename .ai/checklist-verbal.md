> Fuente: Magoya Brand Playbook (octubre de 2026). Cada chequeo cita la slide de la que sale. Si algo de este archivo difiere del playbook, prevalece el playbook.

# Checklist verbal — cualquier texto de Magoya antes de publicar

Lo corre un modelo o una persona sobre cualquier texto de Magoya: post, deck, web, propuesta, mail, copy de una pieza. Complementa a `.ai/checklist.md` (chequeos visuales): una pieza con texto pasa los dos. Todos tienen que dar **sí**. Si alguno falla, corregí nombrando la regla y volvé a correr la lista completa.

Datos de apoyo: `vocabulary.json` (vetos, frases prohibidas, glosario), `.ai/verbal/estrategia.md`, `.ai/verbal/voz.md`, `.ai/verbal/lenguaje.md`, `.ai/verbal/aplicacion.md`.

| # | Chequeo | Cómo se verifica | Falla si… |
|---|---|---|---|
| 1 | **Definición: consultora hands-on en software y AI para empresas del agro** (4, 57) | Buscá cómo se presenta Magoya. Compará contra `definition` y `one_liner` de `vocabulary.json`. El tagline es **Software and AI for agribusiness** | Magoya se define con otra fórmula: "estrategia y ejecución" en vez de hands-on, "tecnología" en vez de "software y AI", o un descriptor vetado (chequeo 3). O el tagline aparece con otra redacción |
| 2 | **AI, nunca la sigla en español** (50) | Buscá la palabra suelta `IA` en todo el texto, en cualquier idioma | Aparece `IA` para nombrar la inteligencia artificial. La única excepción es el nombre propio **IA en Campo**, que se escribe siempre así, en cualquier idioma. Falla también si aparece "AI en Campo" o el nombre con minúscula |
| 3 | **Cero palabras vetadas** (48, 49) | Buscá cada `term` de `vetoed` en `vocabulary.json`: agtech, digital (solo), transformación digital, custom, software factory, dev shop, agencia, tecnología (sola), ayudar, adopción como sinónimo de uso, DIPI, building blocks | Aparece alguno. Se reemplaza por su `use_instead`. No fallan: "soluciones" sin adjetivo genérico, "framework" en contexto técnico y "adopción" como paso dentro del arco de uso (`not_vetoed`) |
| 4 | **Ninguna frase prohibida** (41) | Buscá los enunciados de `forbidden_phrases` y sus paráfrasis: "lo que tenés no sirve", "hay que hacerlo todo de nuevo", "sólo nosotros podemos resolverlo", "esto se hace así", "transformamos", "esta tecnología es fácil de aplicar", "estos problemas son fáciles de resolver", "el problema es del cliente o del usuario" | El texto dice alguna, o dice lo mismo con otras palabras. La slide las llama "siete frases"; enumera ocho enunciados y se chequean todos |
| 5 | **"Uso" antes que "adopción"** (13, 31, 49) | Mirá cada aparición de adopción/adoption | "Adopción" está usada como sinónimo de uso, o como meta final. La adopción es el momento en que alguien pasa de no usuario a usuario: una parte del uso, no su sinónimo |
| 6 | **Peso de los territorios 50/30/20** (37, 60) | En un conjunto de mensajes (un deck, una campaña, el calendario de un mes), contá qué territorio carga cada mensaje: Uso, Integración, Hands-on | La mezcla no se acerca a Uso 50% · Integración 30% · Hands-on 20%, o Uso no es el territorio prioritario. Para un vocero: ~70% su territorio primario y ~30% los otros dos |
| 7 | **Pruebas, no adjetivos** (31, 36, 53) | Marcá cada afirmación de tamaño, calidad o alcance ("global", "líder", "innovadora", "integral") y buscá su respaldo | Una afirmación viaja sin prueba: clientes, años de relación, geografías, casos en producción, un dato. "Mostrarnos grandes se cae si se apoya en adjetivos". Las cifras salen de `ai/facts.json`; lo que no esté ahí va como `[PENDIENTE]` |
| 8 | **Diales según el país** (44, 45) | Identificá el mercado del texto y compará contra los cinco diales: Provocación, Densidad técnica, Cercanía, Venta explícita, Marca de origen | El registro no corresponde: default global 4·2·2·4·1; AR 4·2·4·4·2; BR 3·2·2·3·1; US 3·2·2·4·1. El default es Magoya global y el ajuste por país es la excepción. La personalidad no cambia por mercado: si el texto suena a otra marca en otro país, falla |
| 9 | **Énfasis según la audiencia** (19, 46) | Identificá quién lee: negocio y C-suite, o técnico | Para negocio y C-suite no pesan estratega y curiosa ni va adelante la visión estratégica (si sólo se muestra el build, se desconecta). Para un público técnico no pesan responsable y franca ni hay registro colaborativo (si se entra muy estratégico, suena a consultor genérico). Con el CTO funciona mejor hands-on |
| 10 | **Inglés como idioma principal en web, LinkedIn e Instagram** (62) | Mirá el canal de destino y el idioma | Una pieza para el website, LinkedIn o Instagram de Magoya sale en otro idioma como principal |
| 11 | **Responsable → Accountable** (30) | En textos en inglés, buscá cómo se traduce el rasgo "responsable" | Aparece "responsible" para el rasgo. Va **accountable**: hacerse cargo del resultado |
| 12 | **Distribuidor → dealer** (51) | En textos en inglés, buscá "distributor" | "Distribuidor" (Argentina) se tradujo "distributor". Va **dealer**. "Retailer" es otra figura: el que tiene contacto con el productor |
| 13 | **Agribusiness es el cliente, no el sector** (52) | En inglés, mirá cómo se nombra al sector | "Agribusiness" nombra al sector. En inglés el sector es **agriculture** o **ag**; agribusiness son las empresas del agro, el cliente |
| 14 | **Los cuatro rasgos, en orden** (30, 38) | Leé el texto contra Estratega › Responsable › Curiosa › Franca | La franqueza llega sin la ecualización del rasgo responsable ("este está totalmente equivocado" en vez de "en mi opinión"), o el texto busca impresionar en vez de tomar mejores decisiones juntos |
| 15 | **El usuario nunca es el culpable** (14, 30, 40) | Buscá dónde el texto atribuye un problema de uso | El problema de uso se atribuye al usuario. Cuando el uso falla, la causa se busca en el onboarding, el diseño o la propuesta de valor |
| 16 | **Lo de IA en Campo queda en IA en Campo** (59, 63) | Mirá si una pieza de Magoya trae contenido básico para el productor | Una pieza de la cuenta de Magoya publica contenido educativo básico, tutoriales o tips para el productor: eso es IA en Campo. Y al revés: IA en Campo no habla desde la cuenta de Magoya como contenido propio |

## Glosario rápido de chequeo

- Vetos, reemplazos y frases prohibidas: `vocabulary.json` → `vetoed`, `not_vetoed`, `forbidden_phrases`.
- Términos por mercado (ES · EN · PT): `vocabulary.json` → `glossary`.
- Diales y énfasis por audiencia: `.ai/verbal/voz.md`, secciones 9 y 11.
- Territorios y statements: `.ai/verbal/estrategia.md`, sección 8.
