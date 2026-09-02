#!/usr/bin/env python3
"""
Validador de la capa de consumo para IA.

Chequea lo que se puede chequear sin criterio: que los links resuelvan, que las
referencias cruzadas cierren, que la capa generada no se haya despegado de sus
fuentes, que no haya slots sin límite y que el copy en español no diga "AI".

No opina de diseño y no inventa valores: si falta una definición, la reporta
como hueco para que la decida una persona.

    python3 ai/validar.py                    # la capa, local
    python3 ai/validar.py --red              # además verifica cada URL publicada
    python3 ai/validar.py --pieza deck.html  # una pieza entregada: contrato de entrega
"""
import io, json, os, re, subprocess, sys, glob
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)
BASE = 'https://brand.magoya.com/'
CON_RED = '--red' in sys.argv

fallas, huecos, ok = [], [], []


def cargar(p):
    return json.load(io.open(p, encoding='utf-8'))


# ─── 1. referencias cruzadas: selector ↔ plantillas ──────────────────────────
def check_selector():
    sel = cargar('ai/selector.json')
    idx = cargar('ai/templates/index.json')
    ids = {m['id'] for m in idx['modulos']}
    # OJO: 'usa' es el camino primario y 'alternativa' viene condicionada a criterio de
    # diseño ("si hay foto potente"). Contarlas juntas ocultaba que 10 modulos solo se
    # alcanzan por criterio, que es justo lo que el selector promete evitar.
    primarios, alternos = set(), set()
    for fila in sel['decision']:
        for m in re.findall(r'\b([A-M]\d{1,2})\b', str(fila.get('usa', ''))):
            primarios.add(m)
        for m in re.findall(r'\b([A-M]\d{1,2})\b', str(fila.get('alternativa', ''))):
            alternos.add(m)
    usados = primarios | alternos
    faltan = sorted(usados - ids)
    if faltan:
        fallas.append('selector.json apunta a módulos que no existen en templates/index.json: %s' % ', '.join(faltan))
    else:
        ok.append('selector.json: %d filas, todos los módulos citados existen' % len(sel['decision']))

    sin_ruta = sorted(ids - usados)
    if sin_ruta:
        fallas.append('%d módulos no son alcanzables desde el selector: %s'
                      % (len(sin_ruta), ', '.join(sin_ruta)))
    solo_criterio = sorted(alternos - primarios)
    if solo_criterio:
        huecos.append('%d módulos solo se alcanzan por una cláusula "alternativa" condicionada a '
                      'criterio de diseño, que es lo que el selector promete evitar: %s'
                      % (len(solo_criterio), ', '.join(solo_criterio)))
    else:
        ok.append('selector: los %d módulos tienen camino primario' % len(primarios))


# ─── 2. slots: todos con límite, ninguno con cifra inventada ─────────────────
def check_slots():
    idx = cargar('ai/templates/index.json')
    NO_TEXTO = ('grafico', 'gráfico', 'tabla', 'imagen', 'foto', 'logo', 'icono', 'ícono')
    sin_limite, sin_guia, cifras = [], [], []
    total = 0
    for m in idx['modulos']:
        for s in m.get('slots', []):
            total += 1
            rol = str(s.get('rol', ''))
            sin_medida = not s.get('max_caracteres_aprox') and not s.get('max_lineas')
            if rol in NO_TEXTO:
                # no lleva límite de caracteres, pero tiene que decir qué va adentro
                if not s.get('nota'):
                    sin_guia.append('%s/%s (%s)' % (m['id'], s.get('slot'), rol))
            elif sin_medida:
                sin_limite.append('%s/%s' % (m['id'], s.get('slot')))
            t = str(s.get('texto_ejemplo', ''))
            es_ordinal = re.fullmatch(r'0?\d', t)   # 1, 01, 02… numeración de pasos, no un dato
            if (re.fullmatch(r'[\d.,]+\s*(%|x|×|k|K|M|\+|hs|min)?', t)
                    and t not in ('[XX]', 'NN') and not es_ordinal):
                cifras.append('%s/%s = %s' % (m['id'], s.get('slot'), t))
    if sin_guia:
        huecos.append('%d slots de gráfico/tabla sin nota de qué va adentro (la IA asume): %s'
                      % (len(sin_guia), ', '.join(sin_guia)))
    if sin_limite:
        fallas.append('%d slots sin max_caracteres ni max_lineas (la IA no sabe cuánto texto entra): %s'
                      % (len(sin_limite), ', '.join(sin_limite[:12])))
    else:
        ok.append('slots: %d, todos con límite de texto' % total)
    if cifras:
        fallas.append('%d slots muestran una cifra que se puede copiar como dato real (deberían ir como [XX]): %s'
                      % (len(cifras), ', '.join(cifras[:8])))


# ─── 3. la capa generada no se despegó de sus fuentes ───────────────────────
def check_drift():
    r = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    if r.stdout.strip():
        huecos.append('el repo tenía cambios sin commitear antes de regenerar; el chequeo de drift se saltó')
        return
    g = subprocess.run(['python3', 'ai/generate.py'], capture_output=True, text=True)
    if g.returncode != 0:
        fallas.append('ai/generate.py falló: %s' % g.stderr.strip()[-400:])
        return
    d = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    sucios = [l[3:] for l in d.stdout.strip().split('\n') if l.strip()]
    if sucios:
        fallas.append('la capa publicada estaba desactualizada respecto de sus fuentes; regenerar cambió: %s'
                      % ', '.join(sucios[:10]))
    else:
        ok.append('capa generada al día: regenerar no cambia nada')


# ─── 4. huecos declarados en el spec ────────────────────────────────────────
def check_pendientes():
    c = cargar('ai/constraints.json')
    p = c.get('pendiente_de_definir') or []
    items = p if isinstance(p, list) else list(p.values()) if isinstance(p, dict) else [p]
    if items:
        huecos.append('constraints.json declara %d definiciones pendientes — mientras estén ahí, la IA tiene '
                      'que asumir: %s' % (len(items), ' · '.join(str(i)[:90] for i in items)))
    else:
        ok.append('constraints.json: sin definiciones pendientes')
    f = cargar('ai/facts.json')
    pa = f.get('pendiente_de_aprobar') or []
    if pa:
        huecos.append('facts.json tiene %d datos sin aprobar (no se pueden publicar hasta que los confirme una '
                      'persona): %s' % (len(pa), ' · '.join(str(i)[:80] for i in (pa if isinstance(pa, list) else [pa]))))


# ─── 5. cobertura de espacios y estilos ─────────────────────────────────────
def check_cobertura():
    c = cargar('ai/constraints.json')
    plano = json.dumps(c, ensure_ascii=False).lower()
    exigidas = {
        'escala de espaciado': ['escala', 'base-4', 'base 4'],
        'margen interior de slide': ['margen', '7%'],
        'tamaño mínimo de logo': ['tamano_minimo', 'tamaño mínimo', '90px'],
        'clearspace del logo': ['clearspace'],
        'zona segura en redes': ['zona segura', 'zona_segura', '96'],
        'ancho máximo de párrafo': ['ancho_maximo', 'caracteres por línea'],
        'jerarquía tipográfica': ['niveles_maximos', 'kickers', 'tracking'],
        'nomenclatura IA': ['nomenclatura'],
    }
    faltan = [k for k, ks in exigidas.items() if not any(x in plano for x in ks)]
    if faltan:
        huecos.append('constraints.json no cubre: %s — son cosas que el usuario tendría que asumir'
                      % ', '.join(faltan))
    else:
        ok.append('constraints.json cubre las 8 familias de restricción (espacios, logo, texto, redes, nomenclatura)')


# ─── 6. IA, no AI ───────────────────────────────────────────────────────────
# copy en inglés, nombres propios, identificadores de código y nombres de archivo
PERMITIDO = ('Data &amp; AI', 'Data & AI', 'data &amp; AI', 'data & AI', 'AI Studio',
             'AI-powered', 'with AI', 'moved AI into', 'Agro AI', 'AI=A+', 'src: AI+',
             'src:AI+', 'AI-INTEGRATION', 'AI Patterns', 'AI patterns', 'AI by McKinsey',
             '"AI no es el claim', 'AI o plataformas')
# marcadores de que el texto ENUNCIA la regla, no la incumple
ENUNCIA_REGLA = ('nunca AI', "nunca 'AI'", 'Nunca "AI', 'IA, no AI', 'escribe "AI"',
                 'se admite "AI"', 'en vez de **IA**', 'queda solo para copy',
                 "'AI' solo se escribe", 'Buscá `AI`', 'no AI**', 'no se copia al texto')


def check_nomenclatura():
    malos = []
    # los SVG de assets/pieces llevan copy VISIBLE y quedaban fuera del barrido: la pieza
    # patrón del 4:5 publicaba "AI EN CAMPO" en el kicker y ninguna corrida lo vio.
    objetivo = sorted(set(glob.glob('*.html') + glob.glob('ai/*.json') + glob.glob('ai/*.md')
                          + ['llms.txt', 'llms-full.txt', 'BRAND.md', '.ai/checklist.md']
                          + glob.glob('ai/templates/*.txt')
                          + glob.glob('assets/pieces/*.svg') + glob.glob('assets/studio/*.svg')))
    for f in objetivo:
        if not os.path.exists(f):
            continue
        s = io.open(f, encoding='utf-8', errors='ignore').read()
        for m in re.finditer(r'\bAI\b', s):
            amplio = s[max(0, m.start() - 110):m.end() + 110]
            if any(k in amplio for k in PERMITIDO) or any(k in amplio for k in ENUNCIA_REGLA):
                continue
            v = s[max(0, m.start() - 40):m.end() + 26]
            if True:
                malos.append('%s: …%s…' % (f, re.sub(r'\s+', ' ', v)))
    if malos:
        fallas.append('%d lugares escriben "AI" en copy español (regla: IA). Primeros: %s'
                      % (len(malos), ' || '.join(malos[:6])))
    else:
        ok.append('nomenclatura: ningún "AI" fuera de inglés y nombres propios')


# ─── 7. links publicados ────────────────────────────────────────────────────
def check_links():
    urls = set()
    for f in ['llms.txt', 'llms-full.txt'] + glob.glob('ai/*.md'):
        if not os.path.exists(f):
            continue
        s = io.open(f, encoding='utf-8', errors='ignore').read()
        urls |= set(re.findall(r'https://brand\.magoya\.com/[^\s)\]"\'<>,]+', s))
    for j in ['ai/assets.json', 'ai/templates/index.json', 'ai/slides.json']:
        if os.path.exists(j):
            urls |= set(re.findall(r'https://brand\.magoya\.com/[^\s)\]"\'<>,]+',
                                   io.open(j, encoding='utf-8').read()))
    urls = {u.rstrip('.,;`\'"*') for u in urls}
    faltan_local = sorted(u for u in urls if not os.path.exists(u[len(BASE):]))
    if faltan_local:
        fallas.append('%d URLs publicadas no tienen archivo en el repo: %s'
                      % (len(faltan_local), ', '.join(faltan_local[:8])))
    else:
        ok.append('links: %d URLs publicadas, todas con archivo en el repo' % len(urls))

    if CON_RED:
        import urllib.request
        import urllib.error
        import ssl
        from concurrent.futures import ThreadPoolExecutor

        # Un python sin bundle de CA (macOS sin `Install Certificates.command`, sin certifi)
        # hace fallar TODAS las URLs con SSL_CERTIFICATE_VERIFY_FAILED. Eso no es un link roto:
        # es el entorno. Buscamos un bundle antes de salir a la red.
        candidatos = [os.environ.get('SSL_CERT_FILE')]
        try:
            import certifi
            candidatos.append(certifi.where())
        except ImportError:
            pass
        candidatos.append('/etc/ssl/cert.pem')

        ctx = None
        for cafile in candidatos:
            if cafile and os.path.exists(cafile):
                try:
                    ctx = ssl.create_default_context(cafile=cafile)
                    break
                except Exception:
                    continue

        def probe(u):
            try:
                req = urllib.request.Request(u, method='HEAD',
                                             headers={'User-Agent': 'magoya-brand-validar/1.0'})
                with urllib.request.urlopen(req, timeout=12, context=ctx) as r:
                    return None if r.status < 400 else ('http', '%s → %d' % (u, r.status))
            except urllib.error.HTTPError as e:
                return ('http', '%s → %d' % (u, e.code))
            except Exception as e:
                return ('entorno', '%s → %s: %s' % (u, type(e).__name__, e))

        with ThreadPoolExecutor(max_workers=12) as pool:
            res = [r for r in pool.map(probe, sorted(urls)) if r]
        rotos = sorted(m for tipo, m in res if tipo == 'http')
        sin_red = sorted(m for tipo, m in res if tipo == 'entorno')

        if rotos:
            fallas.append('%d URLs no responden en brand.magoya.com: %s'
                          % (len(rotos), ', '.join(rotos[:8])))
        # Si TODO falla por entorno (sin CA, sin salida a internet), no hay medición: decilo así,
        # no como 353 links rotos.
        if sin_red and len(sin_red) == len(urls):
            huecos.append('no se pudo verificar ninguna URL: el entorno no llega a brand.magoya.com '
                          '(%s). Instalá los certificados de tu Python o corré sin --red' % sin_red[0])
        elif sin_red:
            fallas.append('%d URLs fallan por error de red/TLS: %s'
                          % (len(sin_red), ', '.join(sin_red[:5])))
        elif not rotos:
            ok.append('red: las %d URLs responden 200' % len(urls))


# ─── 8. peso de las entradas ────────────────────────────────────────────────
def check_peso():
    for f in ['llms-full.txt', 'llms.txt'] + glob.glob('ai/*.md'):
        if not os.path.exists(f):
            continue
        kb = os.path.getsize(f) / 1024
        if f == 'llms-full.txt' and kb > 200:
            huecos.append('llms-full.txt pesa %.0fKB: arriba de ~200KB varias IA lo truncan al pegarlo' % kb)
    ok.append('peso: llms-full.txt %.0fKB' % (os.path.getsize('llms-full.txt') / 1024))



# ─── 9. el conteo de assets publicado coincide con el manifiesto ─────────────
def check_conteo_assets():
    real = sum(len(c['archivos']) for c in cargar('ai/assets.json')['carpetas'])
    mal = []
    for f in ['ai/facts.json', 'ai/claude.md', 'ai/chatgpt.md', 'ai/gemini.md',
              'ai/generic.md', 'llms.txt', 'llms-full.txt']:
        if not os.path.exists(f):
            continue
        s = io.open(f, encoding='utf-8', errors='ignore').read()
        for n in set(re.findall(r'(\d{2,4})\s*(?:archivos|assets)\b', s)):
            if int(n) != real:
                mal.append('%s dice %s' % (f, n))
    if mal:
        fallas.append('el manifiesto tiene %d archivos pero se publica otro número en: %s'
                      % (real, ', '.join(sorted(set(mal)))))
    else:
        ok.append('conteo de assets: %d, consistente en todas las entradas' % real)


# ─── 10. reglas del checklist que son aritmética, no criterio ────────────────
def check_reglas_auditables():
    plantillas = sorted(glob.glob('ai/templates/[A-M]*.html'))
    if not plantillas:
        return

    # #5 · golpe de lima. La plantilla es dueña de la regla (decisión de la Mesa, G2):
    # el techo es "como máximo uno", así que lo que falla es tener DOS o más.
    # se cuenta el atributo data-accent, no el hex: el header de instrucciones que va
    # dentro de cada plantilla menciona #A2FF00 y contaminaría el conteo.
    dos_o_mas, con_acento = [], 0
    for f in plantillas:
        n = len(re.findall(r'data-accent="lima"\s+(?:style|data-)', io.open(f, encoding='utf-8').read()))
        if n:
            con_acento += 1
        if n > 1:
            dos_o_mas.append('%s=%d' % (os.path.basename(f)[:-5], n))
    if dos_o_mas:
        fallas.append('%d plantillas tienen más de un golpe de lima (el techo es uno): %s'
                      % (len(dos_o_mas), ', '.join(dos_o_mas)))
    else:
        ok.append('lima: %d de %d plantillas llevan acento, ninguna más de uno'
                  % (con_acento, len(plantillas)))

    # #7 · niveles tipográficos. Techo declarado por la plantilla, no por el checklist.
    TECHO = 7
    pasados = []
    for f in plantillas:
        n = len(set(re.findall(r'font-size:([0-9.]+)cqw', io.open(f, encoding='utf-8').read())))
        if n > TECHO:
            pasados.append('%s=%d' % (os.path.basename(f)[:-5], n))
    if pasados:
        fallas.append('%d plantillas pasan el techo de %d niveles tipográficos: %s'
                      % (len(pasados), TECHO, ', '.join(pasados)))
    else:
        ok.append('tipografía: ninguna plantilla pasa los %d niveles' % TECHO)

    # #2 · el hue prohibido necesitaba un calificador de saturación: sin él, 11 de los
    # hexes de tokens.json (toda la familia crema) caían en el rango 20-65°.
    import colorsys
    tok = io.open('tokens.json', encoding='utf-8').read()
    sospechosos = []
    for hexs in set(re.findall(r'#([0-9A-Fa-f]{6})', tok)):
        r, g, b = (int(hexs[i:i+2], 16) / 255 for i in (0, 2, 4))
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        if 20 <= h * 360 <= 65 and s > 0.40:
            sospechosos.append('#%s (hue %.0f°, sat %.0f%%)' % (hexs.upper(), h * 360, s * 100))
    permitidos = {'#FFC67B'}
    malos = [x for x in sospechosos if x.split()[0] not in permitidos]
    if malos:
        huecos.append('%d colores de tokens.json caen en el rango prohibido 20-65° con saturación '
                      'alta y no están en la excepción: %s' % (len(malos), ', '.join(sorted(malos))))
    else:
        ok.append('color: ningún token saturado en el rango naranja/amarillo fuera de la excepción')


# ─── modo pieza: valida un HTML entregado, no el repo ───────────────────────

def _ritmo(path):
    """DIAGNOSTICO, NO GATE. Imprime la composición para que una persona la mire.

    Fue un gate y se retiró en G3 de la Mesa, por tres razones verificadas:
      1. Es insatisfacible para una clase real de deck: 0 de 362.880 órdenes del deck
         de producto canónico pasaban las cinco reglas, porque el catálogo no tiene un
         módulo visual que cargue un método, un journey ni un caso.
      2. Daba verde sobre secuencias peores que la que hizo abandonar al primer usuario
         real: M2-F3-E4-K2-F2-B2-B3-G2-M2 son 13.482 caracteres y salía [OK].
      3. El eje era cosmético. El mercado gobierna la secuencia por ROL NARRATIVO
         (Sequoia, Storydoc, ghost deck de McKinsey), no por lienzo y peso.
    Una métrica que da verde sobre el deck que hizo abandonar es peor que no tenerla.
    """
    s = io.open(path, encoding='utf-8', errors='ignore').read()
    usados = re.findall(r'data-modulo="([A-M]\d{1,2})"', s)
    if len(usados) < 3:
        return []
    perf = {m['id']: m.get('perfil', {}) for m in cargar('ai/templates/index.json')['modulos']}
    pesos = [perf.get(m, {}).get('peso', '?') for m in usados]
    lienzos = [perf.get(m, {}).get('lienzo', '?') for m in usados]
    problemas = []

    def corridas(xs, valor):
        mejor = act = 0
        for x in xs:
            act = act + 1 if x == valor else 0
            mejor = max(mejor, act)
        return mejor

    if corridas(pesos, 'texto') >= 3:
        problemas.append('%d slides seguidas de peso "texto". Alguna de esas ideas rinde mejor en un '
                         'módulo visual: mirá el campo perfil de templates/index.json' % corridas(pesos, 'texto'))
    for l in set(lienzos):
        if l != '?' and corridas(lienzos, l) > 3:
            problemas.append('%d slides seguidas con lienzo "%s". El lienzo cambia al menos cada 3'
                             % (corridas(lienzos, l), l))
    visuales = pesos.count('visual')
    if visuales < len(usados) / 3:
        problemas.append('solo %d de %d slides son de peso "visual" (mínimo 1 de cada 3). El catálogo '
                         'tiene 19 módulos visuales' % (visuales, len(usados)))
    if len(set(lienzos)) < 2:
        problemas.append('el deck entero usa un solo lienzo (%s)' % lienzos[0])
    repes = [usados[i] for i in range(1, len(usados)) if usados[i] == usados[i-1]]
    if repes:
        problemas.append('módulos repetidos en slides consecutivas: %s' % ', '.join(sorted(set(repes))))

    print('\n--- composición ---')
    print('secuencia: %s' % ' → '.join('%s(%s/%s)' % (m, (perf.get(m,{}).get('peso','?'))[:3],
          (perf.get(m,{}).get('lienzo','?'))[:5]) for m in usados))
    if problemas:
        for p in problemas:
            print('[MIRÁ] %s' % p)
    else:
        print('sin señales de monotonía: %d slides, %d visuales, %d lienzos distintos'
              % (len(usados), visuales, len(set(lienzos))))
    print('OJO: TEXTURA, no veredicto. El argumento y el adorno se miden arriba; lo que')
    print('     nadie mide todavía es si los títulos solos sostienen la historia y la')
    print('     densidad realmente entregada. Que no haya señales acá no dice que esté bien.')
    return problemas


def _arco(path):
    """GATE de argumento. Reemplaza al gate de textura que se retiró en G3: aquel era
    insatisfacible (0 de 362.880 órdenes del deck de producto pasaban) y daba verde
    sobre el deck que hizo abandonar al primer usuario. Estas cuatro reglas gobiernan
    el ROL de cada slide en el argumento, que es el eje que gobierna el mercado.
    Verificado: aceptan el deck de producto y rechazan la secuencia sosa."""
    s = io.open(path, encoding='utf-8', errors='ignore').read()
    usados = re.findall(r'data-modulo="([A-M]\d{1,2})"', s, re.I)
    if not usados:
        print('\n--- argumento ---')
        print('[FALLA] ninguna slide declara data-modulo: no se puede verificar nada.')
        print('        Las plantillas oficiales lo traen; si no está, la pieza no salió del catálogo.')
        return ['sin data-modulo']
    perf = {m['id']: m.get('perfil', {}) for m in cargar('ai/templates/index.json')['modulos']}
    b = [perf.get(m.upper(), {}).get('beat', '?') for m in usados]
    problemas = []
    if b[-1] != 'pedido':
        problemas.append('la última slide es beat "%s" y tiene que ser "pedido": no se cierra sin '
                         'pedir algo' % b[-1])
    if 'propuesta' in b:
        i = b.index('propuesta')
        if 'tension' not in b[:i]:
            problemas.append('propone en la slide %d sin haber puesto tensión antes. Es la causa más '
                             'común de que un deck se lea genérico' % (i + 1))
        if 'evidencia' not in b[i:]:
            problemas.append('propone y no respalda con evidencia después')
    mejor = act = 0
    cual = None
    for k in range(len(b)):
        act = act + 1 if k and b[k] == b[k - 1] else 1
        if act > mejor:
            mejor, cual = act, b[k]
    if mejor > 3:
        problemas.append('%d beats "%s" seguidos: eso es un catálogo, no un argumento' % (mejor, cual))

    print('\n--- argumento ---')
    print('arco: %s' % ' → '.join('%s(%s)' % (m.upper(), x[:4]) for m, x in zip(usados, b)))
    for p in problemas:
        print('[FALLA] %s' % p)
    if not problemas:
        print('[OK] el arco cierra: %d slides' % len(usados))
    else:
        print('       Si alguna de estas no se puede cumplir, declaralo con el motivo en la entrega.')
    return problemas


def _adorno(path):
    """La falla que hizo abandonar al usuario y que nada medía: cuando le dijeron que el
    deck estaba soso, la IA agregó carátulas decorativas. El chequeo de textura no las
    veía y encima las sacaba del denominador."""
    s = io.open(path, encoding='utf-8', errors='ignore').read()
    # un contenedor .slide sin data-modulo solo cuenta como inventado si RENDERIZA como
    # slide (tiene elementos posicionados). El deck-starter trae un .slide con las
    # instrucciones de copiar y pegar, y ese no es una carátula inventada.
    inventadas = 0
    for c in re.finditer(r'<div[^>]*class="[^"]*\bslide\b[^"]*"([^>]*)>(.*?)(?=<div[^>]*class="[^"]*\bslide\b|\Z)', s, re.S):
        if 'data-modulo' in c.group(1):
            continue
        if re.search(r'class="(t|r|im)"', c.group(2)):
            inventadas += 1
    contenedores = inventadas + len(re.findall(r'data-modulo="[A-Ma-m]\d{1,2}"', s))
    declaradas = len(re.findall(r'data-modulo="[A-Ma-m]\d{1,2}"', s))
    problemas = []
    print('\n--- adorno ---')
    if contenedores > declaradas:
        problemas.append('%d slides sin data-modulo sobre %d contenedores: son slides que no salieron '
                         'del catálogo. Si es una carátula inventada, sacala y usá M1 o M2'
                         % (contenedores - declaradas, contenedores))
    idx = {m['id']: m for m in cargar('ai/templates/index.json')['modulos']}
    extra = []
    for mm in re.finditer(r'data-modulo="([A-Ma-m]\d{1,2})"(.*?)(?=data-modulo="|$)', s, re.S):
        mid = mm.group(1).upper()
        if mid not in idx:
            continue
        declarados = {sl['slot'] for sl in idx[mid].get('slots', [])}
        # los slots de imagen los emite la plantilla y index.json no los declara todavía:
        # se comparan por NOMBRE y se ignoran los img*, para no cantar un falso positivo.
        puestos = {x for x in re.findall(r'data-slot="([^"]+)"', mm.group(2))
                   if not re.fullmatch(r'img\d+', x)}
        desconocidos = sorted(puestos - declarados)
        if desconocidos:
            extra.append('%s usa slots que la plantilla no declara: %s' % (mid, ', '.join(desconocidos)))
    if extra:
        problemas.append('slots de más respecto de la plantilla oficial: %s' % ', '.join(extra[:6]))
    for p in problemas:
        print('[FALLA] %s' % p)
    if not problemas:
        print('[OK] todas las slides salen del catálogo, sin elementos de más')
    return problemas

def validar_pieza(path):
    """El hallazgo que motivó esto: en la auditoría una IA declaró cinco cifras como no
    verificables en su reporte y las dejó escritas en la slide. Declarar no es contener."""
    s = io.open(path, encoding='utf-8', errors='ignore').read()
    # el bloque PEDIDO A HUMANOS habla SOBRE la pieza, no es contenido de la pieza
    texto = re.sub(r'<div[^>]*data-pedido-a-humanos.*?</body>', '</body>', s, flags=re.S)
    texto = re.sub(r'<!--.*?-->', ' ', texto, flags=re.S)      # los comentarios traen instrucciones, no copy
    texto = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', texto, flags=re.S)
    texto = re.sub(r'<[^>]+>', ' ', texto)
    # el texto de un hueco declarado describe qué falta: no es una afirmación de la pieza
    texto = re.sub(r'\[(PENDIENTE|XX)[^\]]*\]', ' ', texto)

    pendientes = len(re.findall(r'\[PENDIENTE\]|\[XX\]', s))
    borrador = 'BORRADOR' in s.upper()
    pedido = bool(re.search(r'PEDIDO A HUMANOS', s, re.I))

    # cifras aprobadas: lo que está en facts.json puede viajar
    hechos = io.open('ai/facts.json', encoding='utf-8').read()
    aprobadas = set(re.findall(r'\b(\d[\d.,]*)\b', hechos))

    # dos formas de afirmar una cifra, y las dos tienen que estar respaldadas:
    #   con unidad  -> "68%", "3x", "40k"
    #   cardinal    -> "21 AgTech domains", "10 countries". Esta era la que se escapaba:
    #                  el deck de la auditoría publicó cuatro cifras así, sin unidad.
    sueltas = []
    for m in re.finditer(r'\b(\d[\d.,]*)\s*(%|x|×|k|K|M|\+)(?![\w.])', texto):
        if m.group(1) not in aprobadas:
            sueltas.append(m.group(0).strip())
    for m in re.finditer(r'(?<![\d.,])(\d{1,4})\s+([A-Za-zÁÉÍÓÚÑáéíóúñ][\w-]{2,})', texto):
        num, palabra = m.group(1), m.group(2)
        if re.fullmatch(r'0\d', num):
            continue                      # 01, 02…: numeración de página o de paso
        if num in aprobadas:
            continue
        sueltas.append('%s %s' % (num, palabra))

    print('=' * 72)
    print('PIEZA: %s' % path)
    print('=' * 72)
    if sueltas:
        print('\n[FALLA] %d cifras afirmadas que no están en facts.json: %s'
              % (len(sueltas), ', '.join(sorted(set(sueltas))[:12])))
        print('        Ninguna de estas puede viajar en la pieza. Van como [PENDIENTE].')
    else:
        print('\n[OK] no hay cifras sin respaldo en facts.json')

    if pendientes and not borrador:
        print('\n[FALLA] la pieza tiene %d huecos ([PENDIENTE]/[XX]) y NO está marcada como '
              'BORRADOR. Con un hueco adentro no puede salir como final.' % pendientes)
    elif pendientes:
        print('\n[OK] %d huecos declarados y la pieza está marcada como BORRADOR' % pendientes)
    else:
        print('\n[OK] sin huecos: la pieza puede salir como final')

    if pendientes and not pedido:
        print('\n[FALLA] hay huecos pero falta el bloque "PEDIDO A HUMANOS" con qué dato falta '
              'y a quién se le pide.')
    elif pendientes:
        print('\n[OK] el pedido a humanos está presente')

    prob_arco = _arco(path)          # GATE: el argumento
    prob_adorno = _adorno(path)      # GATE: que la pieza salga del catálogo
    _ritmo(path)                     # diagnóstico de textura, no gate
    ok_total = (not sueltas and not (pendientes and not borrador)
                and not (pendientes and not pedido) and not prob_arco and not prob_adorno)
    print('\n' + '-' * 72)
    print('la pieza %s' % ('PUEDE entregarse' if ok_total else 'NO puede entregarse todavía'))
    return 0 if ok_total else 1


if '--pieza' in sys.argv:
    i = sys.argv.index('--pieza')
    if i + 1 >= len(sys.argv):
        print('uso: python3 ai/validar.py --pieza <archivo.html>')
        sys.exit(2)
    sys.exit(validar_pieza(sys.argv[i + 1]))



# ─── 11. el wordmark: una sola geometría ────────────────────────────────────
def check_wordmark():
    """El bug que motivó esto: assets/ tenía dos dibujos distintos del wordmark
    (cream/black/deep/green compartían uno, y cream-prod era otro con 1 path en vez
    de 8 y otra proporción). El sitio servía uno de los dos y no había forma de saber
    cuál era el vigente. Una pieza real hotlinkeó el equivocado durante dos versiones
    y lo detectó un humano a ojo — ningún archivo del sistema lo advertía."""
    import hashlib
    firmas = {}
    for f in sorted(glob.glob('assets/*wordmark*.svg')):
        s = io.open(f, encoding='utf-8', errors='ignore').read()
        paths = ''.join(re.findall(r'\sd="([^"]+)"', s))
        if not paths:
            continue
        h = hashlib.md5(paths.encode()).hexdigest()[:10]
        vb = re.search(r'viewBox="([^"]+)"', s)
        firmas.setdefault(h, []).append('%s (%s, %d paths)'
            % (os.path.basename(f), vb.group(1) if vb else 's/viewBox', s.count('<path')))
    if len(firmas) > 1:
        grupos = ' || '.join('geometría %s: %s' % (h, ', '.join(fs)) for h, fs in firmas.items())
        fallas.append('hay %d dibujos DISTINTOS del wordmark en assets/ y el sitio sirve uno sin '
                      'decir cuál es el vigente. Toda pieza que hotlinkee hereda el que esté '
                      'publicado. Una persona tiene que decidir cuál es la marca vigente y hay que '
                      'borrar o renombrar el resto. %s' % (len(firmas), grupos))
    elif firmas:
        ok.append('wordmark: %d variantes, todas la misma geometría'
                  % sum(len(x) for x in firmas.values()))

for fn in (check_selector, check_slots, check_pendientes, check_cobertura,
           check_nomenclatura, check_links, check_peso, check_conteo_assets,
           check_reglas_auditables, check_wordmark, check_drift):
    try:
        fn()
    except Exception as e:
        fallas.append('%s explotó: %s: %s' % (fn.__name__, type(e).__name__, e))

print('=' * 72)
print('VALIDACIÓN DE LA CAPA DE CONSUMO PARA IA%s' % ('  (con red)' if CON_RED else '  (local)'))
print('=' * 72)
for t, xs in (('FALLA', fallas), ('HUECO (necesita decisión humana)', huecos), ('OK', ok)):
    for x in xs:
        print('\n[%s] %s' % (t, x))
print('\n' + '-' * 72)
print('fallas: %d · huecos: %d · ok: %d' % (len(fallas), len(huecos), len(ok)))
sys.exit(1 if fallas else 0)
