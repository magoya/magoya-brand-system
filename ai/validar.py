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
    objetivo = sorted(set(glob.glob('*.html') + glob.glob('ai/*.json') + glob.glob('ai/*.md')
                          + ['llms.txt', 'llms-full.txt', 'BRAND.md', '.ai/checklist.md']
                          + glob.glob('ai/templates/*.txt')))
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
        rotos = []
        for u in sorted(urls):
            try:
                req = urllib.request.Request(u, method='HEAD')
                with urllib.request.urlopen(req, timeout=12) as r:
                    if r.status >= 400:
                        rotos.append('%s → %d' % (u, r.status))
            except Exception as e:
                rotos.append('%s → %s' % (u, type(e).__name__))
        if rotos:
            fallas.append('%d URLs no responden en brand.magoya.com: %s' % (len(rotos), ', '.join(rotos[:8])))
        else:
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
def validar_pieza(path):
    """El hallazgo que motivó esto: en la auditoría una IA declaró cinco cifras como no
    verificables en su reporte y las dejó escritas en la slide. Declarar no es contener."""
    s = io.open(path, encoding='utf-8', errors='ignore').read()
    texto = re.sub(r'<!--.*?-->', ' ', s, flags=re.S)          # los comentarios traen instrucciones, no copy
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

    ok_total = not sueltas and not (pendientes and not borrador) and not (pendientes and not pedido)
    print('\n' + '-' * 72)
    print('la pieza %s' % ('PUEDE entregarse' if ok_total else 'NO puede entregarse todavía'))
    return 0 if ok_total else 1


if '--pieza' in sys.argv:
    i = sys.argv.index('--pieza')
    if i + 1 >= len(sys.argv):
        print('uso: python3 ai/validar.py --pieza <archivo.html>')
        sys.exit(2)
    sys.exit(validar_pieza(sys.argv[i + 1]))


for fn in (check_selector, check_slots, check_pendientes, check_cobertura,
           check_nomenclatura, check_links, check_peso, check_conteo_assets,
           check_reglas_auditables, check_drift):
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
