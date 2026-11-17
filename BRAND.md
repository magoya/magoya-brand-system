# Magoya · Brand System v1.4

> Manual de marca en Markdown, pensado para ser consumido por personas y por modelos de AI.
> Tokens exactos en [`tokens.json`](tokens.json) y [`tokens.css`](tokens.css). Manual visual navegable en [`brand-book.html`](brand-book.html).
> **Las reglas visuales de este archivo espejan las del brand book visual.** Si una regla cambia acá, cambia allá, y al revés.

**Regla madre del sistema:** todo asset que se puede usar tiene que estar en el brand, con su ficha: qué es, cuándo se usa, cuándo no, y de dónde se baja ([`library.html`](library.html)).

## 1. Qué es Magoya

> **Capa verbal: Magoya Brand Voice Playbook (octubre de 2026, edición en español y edición en inglés) y Guía editorial V2.** Jerarquía de fuentes del playbook (p. 2): el playbook es la fuente de verdad de estrategia, posicionamiento, oferta y método; la Guía editorial de voz y tono V2 manda sobre voz, estilo y vocabulario; casos y cifras salen solo de fuentes aprobadas del equipo. La edición en inglés define cómo se dice en inglés: se escribe de forma nativa, nunca como traducción línea por línea, y cada cambio futuro se registra en el log de alineación con la frase en español y en inglés, y necesita aprobación (ES p. 2, EN p. 2). La Guía editorial ("Manual voz y tono MAGOYA V2") está en [`.ai/verbal/guia-editorial.md`](.ai/verbal/guia-editorial.md). El detalle vive en `estrategia.html`, `voz.html`, `lenguaje.html`, `aplicacion.html` y `ai.html` (edición en inglés en [`en/`](en/)), y en su versión machine-readable: [`.ai/verbal/estrategia.md`](.ai/verbal/estrategia.md), [`.ai/verbal/voz.md`](.ai/verbal/voz.md), [`.ai/verbal/lenguaje.md`](.ai/verbal/lenguaje.md), [`.ai/verbal/aplicacion.md`](.ai/verbal/aplicacion.md) y [`vocabulary.json`](vocabulary.json). Antes de entregar un texto: [`.ai/checklist-verbal.md`](.ai/checklist-verbal.md). Si algo de acá difiere de la fuente que corresponde, prevalece la fuente. La capa visual (§2 a §9) se actualizó con el feedback del equipo del 22 de octubre de 2026; la §10 es el manual propio de IA en Campo.

**Etiquetas del playbook (p. 2).** *Principio*: cómo pensamos. *Recomendación*: buena práctica; usar criterio. *Obligatorio*: sin excepciones salvo aprobación por escrito.

### 1.1 Identidad y posicionamiento

**Definición (obligatorio, p. 4).** Magoya es una consultora hands-on en software y AI para empresas del agro. *Magoya is a hands-on software and AI consulting firm for agribusiness.* Una línea: "Consultora hands-on en software y AI para empresas del agro." «Estrategia y ejecución» no se usa para definir a Magoya: lo reemplaza hands-on. «Tecnología» no reemplaza a «software y AI». En inglés, *consulting firm*, nunca *consultancy*, *consultant* ni *agency* (EN p. 4).

**Tagline.** **Software and AI for agribusiness.** Va siempre en inglés, en cualquier idioma (EN pp. 4 y 53). Es el segundo mensaje más repetido de la marca. Funcional ahora, inspirador después: lo que se puede soltar es «consultora» y «hands-on» (se dicen inmediatamente después, en la firma o en la presentación); la base no negociable es software + AI + agro / agribusiness (pp. 51–52).

**Propósito, norte interno (p. 5).** Potenciar el uso del software y la AI en el agro para que sean una verdadera fuerza de transformación del sector. **Nuestra búsqueda (p. 6):** que el uso y el impacto del software y la AI sean el criterio que guíe todo el proceso de construcción de soluciones.

**Qué hacemos (p. 8).** Trabajamos con las empresas del agro para resolver sus desafíos de negocio con software y AI, y para que esos productos evolucionen con el negocio y generen resultados.

**Diferenciales, cinco, en este orden (p. 9):** 01 Fluidez en agro · 02 Tres empresas en una · 03 Hands-on · 04 Orientados al resultado · 05 Equipos locales, experiencia global. En inglés (EN p. 9): Domain fluency · Three companies in one · Hands-on · Outcome-driven · Local teams, global experience.

**Propuesta de valor (p. 10).** Especialistas en todo el ciclo del desarrollo de un producto, con un mismo equipo y un mismo método.

**Los tres espacios, nombres obligatorios (p. 11):** **Estrategia** · **Diseño y desarrollo** · **Adopción y uso** (EN p. 11: Strategy · Design and development · Adoption and usage). No se dice: consultoría estratégica; diagnóstico como espacio (es parte del método); implementación como un espacio aparte (vive en Diseño y desarrollo); servicios de escala, *adoption and usage services* ni *rollout*.

**La oferta (p. 12).** *Estrategia:* research e ideación de nuevos features · análisis de product-market fit · análisis de nuevo target o nuevos mercados · estrategia de adopción de AI. *Diseño y desarrollo:* diseño UX/UI · desarrollo e implementación web y mobile · implementación de AI · infraestructura y DevOps · integración de ecosistemas · data cleaning e integraciones de datos · talento. *Adopción y uso:* onboarding, adopción y loyalty programs · customer success y customer support (L1, L2 y L3) · soporte a campo · adopción de AI · medición de uso y de valor. No van al frente: mantenimiento se ofrece si el cliente lo pide; staff augmentation entra tarde, cuando ya se habla de propuesta concreta; el asesoramiento agronómico no es un servicio, es una razón para creer. La edición en inglés lista *Staff augmentation* en lugar de «Talento» (EN p. 12).

**Boilerplate corto (p. 13).** "Magoya es una consultora hands-on en software y AI para empresas del agro. Trabajamos con compañías que ven al software y la AI como parte central de su negocio: entendemos el problema junto a ellas, construimos soluciones y acompañamos hasta que el producto se usa en el campo. Equipos propios de producto, ingeniería y agronomía en Estados Unidos, Brasil y Argentina." El largo y la versión en inglés están en `estrategia.html` y `en/estrategia.html`.

**Territorios de posicionamiento, en orden de prioridad (p. 14).** Construir la asociación de Magoya con el uso es la prioridad.
- **01 · Uso · 50% (prioritario).** «El éxito no es llegar al lanzamiento del producto. El éxito es que ese producto se use.» El software no vale por sí mismo: vale por su uso. La adopción es el momento en que alguien pasa de no usuario a usuario; es una parte del uso, no su sinónimo (p. 15). **Usage Loop (p. 16):** el uso es todo el ciclo y la adopción es una de las ocho etapas (Estrategia, Diseño y desarrollo, Onboarding, Adopción, Uso sostenido, Retención, Valor y retorno, Mejoras), con tres preguntas al centro: ¿Quién lo va a usar? ¿En qué contexto? ¿Qué valor genera? El nombre «Usage Loop» es un activo de marca, no una marca.
- **02 · Integración · 30%.** «Nuestra primera opción es construir sobre lo que ya existe.» Vemos el todo cuando otros ven partes (p. 18).
- **03 · Hands-on colaborativo · 20%** (en la página de territorios: «Hands-on: colaborativo, dentro del trabajo»). «Trabajamos dentro del problema, junto a tu equipo.» Trabajamos junto al equipo del cliente en todo el ciclo, ponemos a prueba nuestro propio diagnóstico y nos quedamos hasta ver el resultado. El valor se ve en semanas (pp. 14 y 19).

En inglés (EN p. 14): *Usage: tools that get adopted and used* · *Integration: build on what exists* · *Hands-on: collaborative, in the work* ("We work inside the problem, alongside your team."). El 50/30/20, y el 70/30 de cada vocero, son guías de planificación de contenidos, no restricciones que deban forzarse en cada texto (Guía editorial V2, §4).

**Audiencias (p. 20).** Magoya le vende a empresas grandes del agro: B2B enterprise, no empresas medianas ni startups. Audiencia primaria: negocio y producto. Emergente: customer success. Decisores: CPO, CEO o negocio (a veces el CFO). Gatekeepers: el CTO y las segundas líneas; con el CTO funciona mejor el territorio hands-on, con un discurso específico y más técnico.

**Razones para creer (pp. 21–25).** Trece, con versión corta y larga en `estrategia.html`. La 09 es «Generamos valor desde el principio: ciclos cortos con avances concretos y medibles». La 10 es la cifra de clientes del playbook (las otras cifras aprobadas están en `ai/facts.json`, como «más de nueve años», p. 9): «El 95% de nuestros clientes es promotor de Magoya y la relación promedio supera los 5 años». La edición en inglés suma a la 12: "For now, it runs only in Argentina." (EN p. 22).

**El Método Magoya (p. 26). No se hace ejecución sin Discovery.** 1 · Discovery · 2 · Ideación · 3 · Planificación · 4 · Ejecución · 5 · Medición y evolución. Cada etapa tiene acuerdos, entregables y métricas. El Método Magoya es un activo, no una marca (p. 54).

**Valores (p. 27):** Coraje · Evidence-driven · Compromiso · Cocreación. En inglés (EN p. 28): Courage · Evidence-driven · Follow-through · Built together. **Pilares (p. 28):** Perspectiva ante todo · Articular para hacer que pase · Pensamiento iterativo · Enseñar a pescar (EN p. 29: Perspective first · Connect the pieces · Move and learn · Capability stays).

**La promesa (p. 29).** Magoya acompaña a las empresas del agro a redefinir sus problemas de uso de software y obtener mayor valor y resultados.

**Arquetipo (p. 30).** Un partner que cuestiona para encontrar la pregunta correcta y explora para descubrir la solución que funciona: El Sabio y El Explorador. En inglés no se usan Sage ni Explorer: son **Perspective** y **Momentum** (EN p. 31).

**Qué se construye primero (p. 32).** Tres capas, en orden: 01 «Hola, soy Magoya» · 02 «Soy experta en uso» · 03 «Soy referente en el mercado». **Objetivos por mercado (p. 33):** Argentina reposiciona, Brasil se presenta desde cero, Estados Unidos valida un posicionamiento más estratégico. Riesgo: «mostrarnos grandes» se cae si se apoya en adjetivos; lo que nos hace grandes se cuenta con pruebas: clientes, años de relación, geografías, casos en producción.

### 1.2 Personalidad, postura y voz

**Personalidad (p. 34).** Cuatro rasgos, en este orden, y cada uno ecualiza al siguiente: **Estratega · Responsable · Curiosa · Franca**. **Obligatorio:** en inglés, Responsable se traduce *Accountable*, nunca *responsible*: accountable es hacerse cargo del resultado. En inglés los rasgos son *Strategic, accountable, curious, candid* (EN p. 35).

**La postura (p. 35).** Magoya está del lado de entender, hacer y acompañar: es parte del ecosistema, tiene respeto por lo logrado, trabaja desde donde está el cliente, propone una práctica fáctica y piensa que el lanzamiento es sólo el principio.

**Contra qué lucha (p. 36).** Nos paramos en frente del arquetipo del mago: el que piensa que «al usuario no le importa cómo se resuelven las cosas». Estamos a favor de evidenciar, mostrar, fundamentar y educar. Doce archienemigos; el 03 es «Entregar un producto y no acompañar su implementación». En inglés el archienemigo central no es el mago: es **the black-box approach** (EN p. 37).

**Lo que Magoya no dice (obligatorio, p. 37).** Seis frases prohibidas: «Lo que tenés no sirve» · «Hay que hacerlo todo de nuevo» · «Sólo nosotros podemos resolverlo» · «Esto se hace así» · «Transformamos» · «Esta tecnología es fácil de aplicar» · «Estos problemas son fáciles de resolver» · «El problema es del cliente o del usuario». Detalle en `forbidden_phrases` de [`vocabulary.json`](vocabulary.json).

**Voz.** Convicción sin soberbia, constructiva, como partner, clara y honesta, centrada en el uso y el valor. Siete principios de expresión verbal (pp. 42–43): hablamos con convicción y apertura («nuestra lectura es» antes que «esto es así»); hacemos preguntas que abren; decimos lo que hay que decir, con cuidado; hablamos claro para que las cosas pasen («uso» antes que «adopción»); hablamos como partner; hablamos desde lo que construimos; hablamos de AI con naturalidad (primero el problema y el resultado, después la herramienta). **Diales (p. 40):** el default es Magoya global; el ajuste por país es la excepción, no la regla. No hay un tono distinto por mercado (p. 41); los diales son orientativos (Guía editorial V2, §4).

### 1.3 Lenguaje

**Vocabulario vetado (obligatorio, pp. 45–46).** Magoya no usa estas palabras; entre paréntesis, qué escribir en su lugar:
agtech (consultora hands-on) · digital, solo (software · producto de software · desarrollo de software) · transformación digital (resultados y lo que se resuelve concretamente) · custom («diseñado para resolver el desafío») · software factory · dev shop · agencia (consultora hands-on) · tecnología, sola (software) · ayudar (trabajar con · colaborar · hacer junto a · acompañar) · adopción como sinónimo de uso (uso, y que la adopción quede como sub-etapa) · DIPI (Método Magoya para el proceso completo · Discovery para la primera fase) · building blocks (sin reemplazo definido) · usar lo que ya tenés (construir sobre lo que ya existe).
No quedaron vetados: «soluciones» (con criterio, nunca con adjetivos genéricos como «integrales» o «innovadoras»), «framework» y «metodología» («método» es la preferida) y «adopción» en su contexto correcto. La edición en inglés suma filas propias: *transform* (junto a *digital transformation*), *help, helping* y *end-to-end, innovative solutions, disruption* (EN pp. 47–48). La lista completa con su porqué está en [`vocabulary.json`](vocabulary.json).

**Vocabulario vetado.** Decisión del 29 oct 2026 (Facu, punto a confirmar 1 del brief): las entradas del vocabulario vetado del playbook (pp. 45–46; edición en inglés, pp. 47–48) son obligatorias tal como las define cada fila, por ejemplo «tecnología» sola, «digital» solo o «adopción» como sinónimo de uso. Lo que no está en la lista se evalúa por su función y contexto, como dice la Guía editorial V2 (§3). Así se lee la jerarquía de la p. 2: la Guía manda sobre el vocabulario en general y el playbook fija esta lista.

**AI (p. 46).** Se escribe **AI**, en inglés, en cualquier idioma del texto: hacemos «software y AI». Única excepción: **IA en Campo**, el nombre del programa, que se escribe siempre así (nunca "AI en Campo").

**Quién es quién (pp. 47–48; EN pp. 49–50).** El glosario ES · EN · PT por mercado está en [`vocabulary.json`](vocabulary.json). Lo que más se rompe: «distribuidor» es *dealer*, nunca *distributor*; *retailer* es otra figura (el que tiene contacto con el productor); la empresa de maquinaria es *OEM* (no *OEM company*); el equipo comercial del cliente es *sales rep* (no *commercial*); fruticultura es *fruit grower, orchard grower* (no *orchard farmer*). «Agribusiness» nombra al cliente, no al sector: en inglés el sector es *agriculture*, *ag* o *the industry*. Tipos de cultivo: extensivos e intensivos; en inglés, *row crops* y *specialty* o *fresh crops*.

**Escribir en inglés (solo para textos en inglés, EN p. 46).** Write natively, never translate. Lo primero es la conclusión, el pedido o el hallazgo. Voz activa y "we". Contracciones en LinkedIn, el website y el email; menos en propuestas y SOWs. Un solo calificador: "Our read is". Serial comma siempre ("Strategy, design and development, and adoption and usage."). US spelling y formatos, obligatorios para contenido de Estados Unidos (organization, analyze; October 21, 2026; 36%; $2M). *Usage* nombra el territorio, la métrica y el loop; *use* es el verbo. *Clients* son nuestras empresas; *customers*, sus compradores; *users*, la gente en sus productos. Sin "the space" para el sector: *agriculture*, *ag* o *the industry* ("space" es para nuestros tres espacios). Sin calcos del español: "not X, but Y", "an agriculture where", cláusulas con "with" encadenadas, em dashes. Palabras simples: *use*, no *leverage*; *clear*, no *seamless*; sin *cutting-edge, world-class, robust, unlock, empower, holistic*. Títulos en sentence case, nunca Title Case.

### 1.4 Arquitectura, voces y canales

**Arquitectura (p. 54).** Una sola marca comercial: Magoya, marca madre. Método Magoya y Usage Loop son activos, no marcas. Los voceros (directores y expertos, desde sus cuentas personales) hablan de su territorio primario en un 70% y de los otros dos en un 30%. IA en Campo es una marca de programa presentada por Magoya, no una marca de Magoya ni una línea de negocio; se escribe «IA en Campo, presentado por Magoya».

**Voceros (p. 55).** Varu (Varina Baldi): Magoya · Hands-on · Integración. Cami: Uso. Facu: Uso (perspectiva producto). Pato: Integración. Leo: territorio adyacente. Kinsie · Cami Reis: Uso (localizado).

**Canales e idioma (p. 57).** El inglés es el idioma principal del website, de LinkedIn y de Instagram. LinkedIn es el canal primario (thought leadership y territorios); Instagram, el secundario (equipo, países, cultura; no posicionamiento técnico); el sitio es el hub de la marca. La personalidad es la misma en Argentina, Brasil y Estados Unidos; lo que cambia por mercado es el vocabulario, el estadio de construcción y el énfasis por audiencia (p. 41).

**Focos de contenido (p. 58).** El Método Magoya etapa por etapa · los puntos de vista de marca de cada territorio · AI desde el lado de quien construye (el lado de quien la usa es IA en Campo) · casos sin logos: aprendizajes agregados · presencia en países. Mezcla: 90% experto, 10% humano.

### 1.5 Reglas de evidencia (obligatorio, p. 59)

Cada afirmación se puede rastrear.
- **Partir de evidencia.** Observaciones, experiencias, datos, razonamiento o fuentes confiables. Análisis, hipótesis y tendencias sirven si se identifican como tales.
- **Relato de casos.** Contexto observado → problema o hipótesis → intervención → resultado o aprendizaje. Sin medición aprobada, solo consecuencias que el equipo pueda confirmar.
- **Generalizaciones.** No presentar intuiciones como hechos del sector. Indicar el alcance. No inventar cantidades de proyectos, períodos ni porcentajes.
- **Métricas.** Validadas por alguien de Magoya, con unidad, alcance, período y base de comparación. La AI no inventa, estima ni completa números. Las cifras aprobadas viven en [`ai/facts.json`](ai/facts.json).
- **Clientes.** No nombrarlos ni hacerlos identificables, tampoco por descarte, sin autorización expresa.
- **Capacidades.** Explicar qué capacidad se gana, qué proceso mejora y qué valor se genera. No reducir el relato a recortes de personas.

### 1.6 Instrucciones para agentes de AI (p. 60; edición en inglés, p. 62)

Antes de redactar y antes de entregar.

**Reglas de generación.**
- Identificar objetivo, audiencia, canal, idioma, fuente y restricciones de confidencialidad. Si falta algo indispensable, preguntar.
- No inventar hechos, cifras, resultados, citas, clientes, fechas ni experiencias.
- Diferenciar hecho validado, interpretación, hipótesis y ejemplo.
- Ante fuentes o reglas en conflicto: señalarlo, no resolverlo en silencio.
- Decisiones, riesgos o cifras relevantes: entregar como borrador pendiente de revisión.
- Confirmar que los números variables estén actualizados.
- Para un texto en inglés, la edición en inglés suma: "Spanish input: rebuild it for an English reader, via the glossary." (EN p. 62).

**Control antes de entregar.**
- Responde al brief y respeta el posicionamiento.
- Constructivo, sin soberbia, con un punto de vista útil.
- Toda cifra real tiene validación humana.
- Usa bien «uso», «adopción», los espacios y el Método Magoya.
- Sin palabras vetadas; «AI» e «IA en Campo» correctos.
- Nivel técnico, tono e idioma adaptados a la audiencia y al canal. En inglés: "Native English: active voice, US spelling, serial comma, no jargon." (EN p. 62).
- Lo pendiente queda señalado.

La Parte II de la Guía editorial V2 desarrolla estas mismas instrucciones (jerarquía de fuentes, validación humana y permisos, control antes de entregar) y el contrato de entrega está en [`ai/precedencia.json`](ai/precedencia.json): un dato que no está en `ai/facts.json` va como `[PENDIENTE]` y el entregable sale BORRADOR, con un bloque PEDIDO A HUMANOS.

**Gobernanza (p. 61).** El dueño del documento aprueba cualquier cambio de contenido en los dos idiomas (hoy figura «a definir»). Un cambio al vocabulario o a una regla se propone, se revisa con los voceros que afecta y se aprueba antes de publicarse. Una excepción puntual se documenta y no cambia la regla general.

## 2. Logo & avatares

- **Wordmark** redondeado (4 versiones: verde digital `#00DE68` sobre blanco · crema sobre verde profundo · negro `#161616` sobre blanco · verde profundo sobre crema). Nunca reconstruir ni alterar espaciado. Versión web animada: `assets/magoya-wordmark-animado.svg`.
- **Avatares** (círculo `#00DE68` + marca blanca): `go`, `o`, `cara`, `m`. La **cara** = redes de comunidad; la **m** = monograma funcional (favicon, app icon, canales corporativos).
- Aire mínimo: la altura de la "m". Tamaño mínimo: 90px pantalla / 24mm impreso. Más chico que eso, usar el avatar "m".
- ✗ No estirar, rotar, sombrear, degradar. ✗ Wordmark en lima. ✗ Recolorear avatares.

## 3. Color

| Color | HEX | Pantone (aprox.) | Rol |
|---|---|---|---|
| Verde Magoya | `#133825` | PMS 553 | **El verde protagonista de Magoya**: fondos, overlays, superficies oscuras, texto sobre claro |
| Verde digital | `#00DE68` | PMS 3282 | Identidad: wordmark, avatares, micro-acentos y data-viz. **Resalta la frase clave de un titular sobre fondo oscuro.** Como texto SOLO sobre oscuro |
| Lima | `#A2FF00` | PMS 382 2X | **Poca superficie: acentos, detalles, CTA o resaltar una palabra con la miscelánea gestual.** Nunca texto sobre blanco |
| Crema Magoya | `#ECE3DB` | PMS Warm Gray 2 | Neutro cálido; texto sobre verde profundo |
| Sage | `#EEF2EC` | PMS Cool Gray 1 | Superficie clara |
| Negro Magoya | `#161616` | PMS Black 5 2X | Texto, titulares, cards dark |

Los Pantone son el **match más cercano por distancia RGB** contra la librería Solid Coated (no existe una conversión exacta hex→Pantone): confirmar contra el libro físico antes de mandar a producción.

**Regla de color.** Ahora que el lima es uno de los colores de la paleta de IA en Campo, Magoya potencia el **Verde Magoya `#133825`** como su verde protagonista y deja el **lima** para acentos, detalles o CTA, con **mucha menos proporción** que el Verde Magoya. Para resaltar la frase clave de un titular sobre fondo oscuro se usa el **Verde digital `#00DE68`**, no el lima (ejemplo: "Software and AI **for agribusiness.**"). Respetá la paleta en todas las piezas, tanto en los posteos con foto como en los más vectoriales.

**Proporciones de uso.** El Verde Magoya ocupa la mayor superficie y el lima mucha menos. Los porcentajes exactos todavía no están definidos: no apliques porcentajes ni inventes una proporción numérica.

**Accesibilidad (no negociable):** lima nunca como texto sobre claro (1.25:1). Verde sobre blanco como texto = `#009145` y solo ≥24px bold. `#00DE68` como texto solo sobre fondos oscuros. Captions sobre claro: mínimo `#6E756D`.

## 4. Tipografía

**Manrope** (variable 200–800, self-hosted). Fallback: **Arial**. Display ExtraBold 800 con tracking −3%; cuerpo Regular 400. Kickers MAYÚSCULAS +12% tracking.

Reglas: **3 niveles tipográficos** por pieza; el peso hace la jerarquía; labels de botón en sentence case. **Emojis: nunca en títulos**; solo se permiten manitos que señalan (👈 👉 👇) para dirigir a un CTA y banderas de países para geografía, ningún otro.

**Resaltar una palabra.** Para resaltar en un titular hay dos formas: color (Verde digital #00DE68 sobre fondo oscuro) o el círculo gestual de la miscelánea nueva (`assets/marks/circle1.svg`, `circle2.svg`). Flechas, círculos, X y ✓ (`assets/marks/`): lima para detalles, acentos o resaltar una palabra; Verde digital; o Verde Magoya cuando el fondo contrasta (por ejemplo sobre Verde digital). Nunca subrayado ni bloque resaltador sólido detrás del texto. El círculo es más propio de IA en Campo: en Magoya se usa con medida y siempre con el trazo gestual nuevo. Los archivos vienen en verde oscuro (#003922): se recolorean según la regla de arriba.

## 5. Fotografía

Dos familias fotográficas, cada una con su regla:
- **Aérea de campo**: color natural, con **overlay verde profundo** (scrim 55–86%) para fondos con texto. **Siempre enfoque cenital.** El scrim es el único gradiente permitido.
- **Personas**: gente real del equipo, **siempre a color** (5 fotos aprobadas: `varu-ceo-color.jpg`, `equipo-campo-planta.jpg`, `equipo-campo-remera.jpg`, `equipo-campo-espalda.jpg`, `equipo-campo-remera-verde.jpg`; el banco suma más con la sesión nueva) y mejor **en espacios abiertos**. Sin ningún detalle encima: ni barra, ni acento verde, ni overlay. Luz natural, gesto genuino.
- ✗ Stock corporativo posado, oficinas genéricas. ✗ Fotos de personas en blanco y negro o con un detalle de color encima. ✗ Fotos de campo que no sean cenitales.

## 6. Iconografía

Línea 2px, terminaciones y esquinas redondeadas, grid 24×24, `currentColor`. **Set agro de 16 íconos + 10 logos de AI + 13 de redes en `assets/studio/icons/`, los mismos archivos que usa Magoya Studio.** Negro sobre claro, crema sobre oscuro, **lima solo el ícono destacado (uno por pieza)**. Librería propia de 58 iconos en 7 categorías (`icons.html`); completar con Lucide (misma gramática) si hace falta volumen. Nunca rellenos sólidos ni 3D.

## 7. Componentes

- **CTA, botón, box y chip.** CTA = pill de radio 44px en Verde digital o lima, con la flecha en un círculo Verde Magoya (`assets/components/cta.svg`), uno por pieza. Botones secundario (verde profundo) y terciario (outline): rectángulo de radio 10px. Box = radio 12px, cualquier color de la marca menos lima, una sola imagen en el rectángulo claro y el texto sobre el pleno (`assets/components/box.svg`). Chip = pill outline, nunca sólido.
- **Espaciado sistematizado.** Todo margin/padding/gap sale de la escala base-4 de `tokens.json` (4/8/12/16/24/32/48/64/96), nunca valores arbitrarios. Aire entre bloques ≥24; dentro de un componente 8–16. Paddings canónicos: botón 13px/26px, chip 6px/15px (spec completa en `components` de `tokens.json`).
- **Alineación.** Una pieza tiene UN eje principal (por defecto, izquierda): todos los bloques de texto arrancan ahí. Los elementos de una fila comparten centro vertical y un gap único (8 o 12). Padding interno simétrico, nunca 4 valores distintos.
- Estados: hover (lima→`#8BDB00`, resto brightness), focus ring `rgba(0,222,104,.45)` sin blur.
- **Cards: siempre en mosaico**: misma grilla, mismos aires, alturas que calzan; nunca sueltas. Tipos: hiring (negro + lima), quote (foto + cita), stat (número 800 −3%). El contacto dentro de una card dark es un **link en lima**, no un botón (los botones viven fuera de las cards).
- ✗ **El monograma "m" circular NO va en cards.** El avatar "m" es identidad de canal (favicon, app icon, perfil corporativo) y pie de papelería; dentro de una card compite con el wordmark y agrega un segundo logo a la pieza. En una card, la marca es el wordmark.
- Logo wall: logos **siempre reales**, en gris, grilla pareja.

## 8. Papelería & corporativo

- **Posteos de redes**: 8 posteos de referencia en PNG 1080×1350 (`assets/social/`, ZIP `assets/downloads/magoya-redes.zip`). Son referencias, no archivos editables. Respetan la paleta tanto con foto como en versión vectorial, y cuando usan los recursos (CTA, box, flechas, círculos, X y ✓) siguen sus reglas.
- **Templates de deck**: dos bases. *Uso interno* (índice, carátulas e internas): PDF de 17 slides en `assets/deck/magoya-interno.pdf`. *Uso con clientes* (más institucional): solo previews en `assets/deck/clientes-*.jpg`; el PDF completo no se publica porque incluye condiciones de cada cliente. Las bases también están armadas en Claude.
- **Membrete A4**: wordmark verde arriba-izq (20% del ancho), pie con filete verde digital + avatar m. Header y footer vectoriales listos: `assets/downloads/doc-header.svg` · `doc-footer.svg`.
- Docs: wordmark esquina sup-izq ≤1/5 del ancho; Manrope o Arial; nunca logo como marca de agua.

## 9. Reglas de oro (resumen ejecutable)

1. El Verde Magoya `#133825` es el verde protagonista y ocupa la mayor superficie. Los porcentajes exactos no están definidos: no apliques porcentajes.
2. Lima en poca superficie: acentos, detalles, CTA o resaltar una palabra con la miscelánea gestual.
3. Verde digital `#00DE68` = identidad (logo/avatares) y resaltado de la frase clave en titulares sobre oscuro; lima ≠ logo.
4. Personas siempre a color, sin ningún detalle encima, mejor en espacios abiertos. Aérea de campo siempre cenital. Magoya no usa ilustración.
5. Logos de clientes SIEMPRE reales, jamás placeholders.
6. Todo redondeado, como el wordmark. CTA pill 44px (Verde digital o lima), botón rect 10px, box radio 12px (nunca lima), chip pill outline.
7. Resaltar: color (Verde digital sobre oscuro) o el círculo gestual nuevo. Flechas, círculos, X y ✓ en lima, Verde digital o Verde Magoya según el fondo. Nunca subrayado.
8. El monograma "m" no va en cards.
9. **Emojis prohibidos**: la única excepción son las manitos que señalan (👈 👉 👇) hacia un CTA y las banderas de países para geografía. Nunca en títulos.
10. ✗ Pieza 100% negra o 100% verde (siempre equilibrio) · ✗ Resaltador sólido tras texto · ✗ gradientes glossy/3D/estética AI · ✗ puzzle (metáfora del brand viejo) · ✗ naranja/amarillo del brand viejo.
11. **AI, en cualquier idioma**: se escribe AI para nombrar la inteligencia artificial, también en textos en español. Única excepción: el nombre propio **IA en Campo**. Regla del Magoya Brand Voice Playbook (p. 46; edición en inglés, p. 48); el resto de la capa verbal en §1.

## 10. IA en Campo (manual propio)

**No es una sección de este brand: es una marca de programa presentada por Magoya, con su propio sistema de marca** (`ai-en-campo/`, octubre 2026). Programa abierto de AI aplicada al agro: carruseles, reels, webinars y capacitaciones abiertas, por ahora solo en Argentina. Magoya habla de AI desde el lado de quien la construye; IA en Campo, desde el lado de quien la usa. **Cuándo NO:** propuestas comerciales, casos de cliente formales, deck de ventas, sitio: eso es core Magoya.

**Logo.** Signo ‹ia + leyenda EN CAMPO, en tres versiones: con placa, simple y con "Una iniciativa de Magoya" (`ai-en-campo/assets/descargas/logos.zip`). La minúscula es solo del logo: en texto se escribe siempre **IA en Campo**.

**Paleta (alto contraste, llamativa a propósito).** Comparte con Magoya la base (verde profundo `#003922`, verde lima `#80FF00`, negro `#161616`); sale el verde pleno y el crema; entran **violeta eléctrico `#B700FF`** y **blanco `#FFFFFF`**. El violeta es el acento y marca todo lo que es AI y el contenido de IA en Campo News. Combinaciones: frase clave texto oscuro sobre lima · título blanco sobre negro · botón blanco sobre violeta.

**Tipografía.** Par propio, distinto del de Magoya: **Plus Jakarta Sans** (variable 200–800, OFL) para títulos y bajadas; **Helvetica** para texto largo y pies (fallback Arial). Título 800 con tracking −3% (~14% del ancho en un posteo de 1080 px), bajada 500 Medium (~6,5%). Máximo 3 niveles por pieza; nunca una tercera familia; cuerpo nunca menos de 11 px.

**Resaltado.** Una sola frase por título, en MAYÚSCULAS, sobre bloque verde lima con texto oscuro (puede ir levemente inclinado). Emojis: nunca en títulos; solo la manito que señala (👈 👉 👇) para dirigir al botón.

**Imágenes.** Lo humano del campo, de cerca: planos cortos, nítidos, color natural, verdes vivos. La foto trae lo humano; lo gráfico trae la AI.

**Íconos.** 16 íconos pixelados (siguen el lenguaje del logo), monocromos: negro sobre claro, blanco sobre oscuro; uno destacado por pieza (lima sobre oscuro).

**Personaje.** Tiene la forma de las fichas de herramientas (ChatGPT, Gemini): es la ficha de IA en Campo que cobró vida. Mueve la mirada y pone la emoción; no explica. Siempre interactúa con algo y va anclado a un borde (10–15% del ancho), una aparición por pieza (en carruseles, portada y cierre como máximo), mira hacia lo importante y nunca tapa datos. No va en piezas con personas reales ni donde el dato tiene que leerse serio.

**Componentes.** Todo toma la forma de la placa del logo: **esquinas cortadas en diagonal**. Botones en tres niveles (primario violeta, secundario lima, terciario outline), label en minúscula salvo la primera letra, un solo primario por pieza, hover con sombra sólida tipo píxel; sobre violeta, el primario pasa a lima. Chips: etiqueta rectangular sólida, MAYÚSCULAS, sin punto ni ícono, sin hover. Cards en mosaico con esquina cortada: lima para preguntas del lote, violeta para IA en Campo News, verde profundo para webinars y citas. Nada de esto vuelve al core.

**Formatos.** Piezas para redes que hacen decir "a ver" (no buscan un feed uniforme) y miniaturas de YouTube 16:9 con la frase clave en bloque lima sobre fondo oscuro verde y violeta.

**Pendientes que marca el propio manual:** componentes como primera propuesta; colores de caption, link y check "a confirmar"; el verde `#009145` del ícono destacado sobre claro no está en la paleta; alinear el lima `#80FF00` con el de Magoya; una miniatura de YouTube usa la sigla en español en lugar de AI; el logo con placa necesita versión en alta o SVG.

**Identidad anterior (retirada).** El lienzo verde digital pleno, la placa negra con texto crema, el lockup "IA en Campo · por Magoya" en Manrope y los doodles/flourishes del Studio eran la identidad previa del programa: se retiraron del repo el 29 oct 2026 y no se usan en piezas nuevas.

## Mapa de archivos del sistema

| Página | Qué documenta |
|---|---|
| `estrategia.html` · `voz.html` · `lenguaje.html` · `aplicacion.html` | Capa verbal del Magoya Brand Voice Playbook (octubre 2026) y bloques de la Guía editorial V2 |
| `en/` | Edición en inglés del sitio (Home, Strategy, Voice, Language, Voices and channels, Working with AI), con el playbook en inglés |
| `brand-book.html` | Identidad visual: logo, color, tipografía, fotografía, iconografía, componentes, reglas de oro |
| `library.html` | Recursos: ficha + descarga de cada asset aprobado |
| `icons.html` | 58 iconos copiables |
| `logos.html` | Logos de clientes y stack tecnológico |
| `ai-en-campo/` | Sistema de marca de IA en Campo (sitio propio, octubre 2026) |
| `ai.html` | Integrar con AI: cómo cargar esta marca en una herramienta de AI y cómo validar el resultado |

Capa machine-readable: `llms.txt` (resumen estable), `.ai/brand-prompt.md` y `.ai/brand-prompt-short.md` (prompts para pegar), `.ai/checklist.md` (validación visual), `.ai/checklist-verbal.md` (validación de texto), `.ai/verbal/` y `vocabulary.json` (capa verbal) y `.ai/presets/` (uno por herramienta). **Todos derivan de este archivo: si una regla cambia acá, hay que propagarla ahí.**

`assets/refs/` es **material fuente no publicable** (exports originales del diseñador): se conserva como referencia de trazado, no se enlaza ni se distribuye.

---

*Pendientes de contenido: porcentajes exactos de uso del color; archivos vectoriales de la miscelánea nueva de redes (círculo y flechas); link al Artifact base del deck; logos vectoriales de ProducePay/HabiTerre/IntelinAir; validación de Staff Augmentation; unificación del email de contacto (hoy conviven `people@` e `info@`).*
