#!/usr/bin/env python3
"""
Validador de la capa de consumo para AI.

Chequea lo que se puede chequear sin criterio: que los links resuelvan, que la
capa generada no se haya despegado de sus fuentes, que el conteo de assets sea
el mismo en todas las entradas y que el copy siga la regla AI / IA en Campo.

No opina de diseño y no inventa valores: si falta una definición, la reporta
como hueco para que la decida una persona.

    python3 ai/validar.py                    # la capa, local
    python3 ai/validar.py --red              # además verifica cada URL publicada
    python3 ai/validar.py --entrega texto.md # un entregable: contrato de entrega
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


# ─── 1. la capa generada no se despegó de sus fuentes ───────────────────────
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


# ─── 2. huecos declarados en el spec ────────────────────────────────────────
def check_pendientes():
    c = cargar('ai/constraints.json')
    p = c.get('pendiente_de_definir') or []
    items = p if isinstance(p, list) else list(p.values()) if isinstance(p, dict) else [p]
    if items:
        huecos.append('constraints.json declara %d definiciones pendientes — mientras estén ahí, la AI tiene '
                      'que asumir: %s' % (len(items), ' · '.join(str(i)[:90] for i in items)))
    else:
        ok.append('constraints.json: sin definiciones pendientes')
    f = cargar('ai/facts.json')
    pa = f.get('pendiente_de_aprobar') or []
    if pa:
        huecos.append('facts.json tiene %d datos sin aprobar (no se pueden publicar hasta que los confirme una '
                      'persona): %s' % (len(pa), ' · '.join(str(i)[:80] for i in (pa if isinstance(pa, list) else [pa]))))


# ─── 3. cobertura de espacios y estilos ─────────────────────────────────────
def check_cobertura():
    c = cargar('ai/constraints.json')
    plano = json.dumps(c, ensure_ascii=False).lower()
    exigidas = {
        'escala de espaciado': ['escala', 'base-4', 'base 4'],
        'tamaño mínimo de logo': ['tamano_minimo', 'tamaño mínimo', '90px'],
        'clearspace del logo': ['clearspace'],
        'regla de color': ['protagonista'],
        'ancho máximo de párrafo': ['ancho_maximo', 'caracteres por línea'],
        'jerarquía tipográfica': ['niveles_maximos', 'kickers', 'tracking'],
        'nomenclatura AI': ['nomenclatura'],
    }
    faltan = [k for k, ks in exigidas.items() if not any(x in plano for x in ks)]
    if faltan:
        huecos.append('constraints.json no cubre: %s — son cosas que el usuario tendría que asumir'
                      % ', '.join(faltan))
    else:
        ok.append('constraints.json cubre las 7 familias de restricción (espacios, logo, color, texto, nomenclatura)')


# ─── 4. AI, no la sigla en español (Brand Playbook oct 2026, slide 50) ──────
# Regla: se escribe AI en cualquier idioma del texto. Única excepción: el nombre propio
# "IA en Campo", que se escribe siempre así (nunca "AI en Campo" ni con minúscula).
# No cuentan: nombres de archivo (VALIDACION-IA.md, agente-validacion-ia.md).
# marcadores de que el texto ENUNCIA la regla, no la incumple
ENUNCIA_REGLA = ('la sigla en español', 'Buscá la palabra suelta `IA`', '"do_not_write"',
                 'IA (como sigla', 'nunca "AI en Campo"', "nunca 'AI en Campo'", 'Nunca "AI en Campo"',
                 'nunca “AI en Campo”', 'o con minúscula', 'con minúscula', '"never": "AI en Campo"',
                 'Nunca <span class="no">“AI en Campo”',
                 # el lockup de IA en Campo parte el nombre en dos renglones: "IA" / "en Campo"
                 'class="l1">IA<span class="mk">', 'altura de "IA"', 'derecha de "IA"',
                 '<td><span class="no">“AI en Campo”</span></td>')


def check_nomenclatura():
    malos = []
    # los SVG de assets/pieces llevan copy VISIBLE y quedaban fuera del barrido: la pieza
    # patrón del 4:5 publicaba "AI EN CAMPO" en el kicker y ninguna corrida lo vio.
    objetivo = sorted(set(glob.glob('*.html') + glob.glob('ai/*.json') + glob.glob('ai/*.md')
                          + ['llms.txt', 'llms-full.txt', 'BRAND.md', 'vocabulary.json',
                             '.ai/checklist.md', '.ai/checklist-verbal.md']
                          + glob.glob('.ai/verbal/*.md')
                          + glob.glob('assets/pieces/*.svg') + glob.glob('assets/studio/*.svg')))
    for f in objetivo:
        if not os.path.exists(f):
            continue
        s = io.open(f, encoding='utf-8', errors='ignore').read()
        for m in re.finditer(r'\b(IA|AI)\b', s):
            antes, despues = s[max(0, m.start() - 1):m.start()], s[m.end():m.end() + 9]
            if antes in '-_' and antes:
                continue                                   # nombre de archivo
            if despues.startswith('.md') or despues.startswith('-'):
                continue
            nombre = s[m.start():m.end() + 9]
            if m.group(1) == 'IA' and nombre in ('IA en Campo', 'IA EN CAMPO'):   # mayúsculas: kicker
                continue                                   # el nombre propio, bien escrito
            if m.group(1) == 'AI' and not re.match(r'AI en [Cc]ampo', s[m.start():m.end() + 9]):
                continue                                   # AI suelto es la forma correcta
            amplio = s[max(0, m.start() - 110):m.end() + 110]
            if any(k in amplio for k in ENUNCIA_REGLA):
                continue
            v = s[max(0, m.start() - 40):m.end() + 26]
            malos.append('%s: …%s…' % (f, re.sub(r'\s+', ' ', v)))
    if malos:
        fallas.append('%d lugares no siguen la regla AI (se escribe AI en cualquier idioma; única excepción, '
                      'el nombre propio "IA en Campo"). Primeros: %s'
                      % (len(malos), ' || '.join(malos[:6])))
    else:
        ok.append('nomenclatura: AI en todo el copy y "IA en Campo" bien escrito')


# ─── 5. links publicados ────────────────────────────────────────────────────
def check_links():
    urls = set()
    for f in ['llms.txt', 'llms-full.txt'] + glob.glob('ai/*.md'):
        if not os.path.exists(f):
            continue
        s = io.open(f, encoding='utf-8', errors='ignore').read()
        urls |= set(re.findall(r'https://brand\.magoya\.com/[^\s)\]"\'<>,]+', s))
    for j in ['ai/assets.json']:
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


# ─── 6. peso de las entradas ────────────────────────────────────────────────
def check_peso():
    for f in ['llms-full.txt', 'llms.txt'] + glob.glob('ai/*.md'):
        if not os.path.exists(f):
            continue
        kb = os.path.getsize(f) / 1024
        if f == 'llms-full.txt' and kb > 200:
            huecos.append('llms-full.txt pesa %.0fKB: arriba de ~200KB varias AI lo truncan al pegarlo' % kb)
    ok.append('peso: llms-full.txt %.0fKB' % (os.path.getsize('llms-full.txt') / 1024))



# ─── 7. el conteo de assets publicado coincide con el manifiesto ─────────────
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


# ─── 8. color: ningún token en el rango naranja/amarillo del brand viejo ──────
def check_color():
    # el hue prohibido necesita un calificador de saturación: sin él, toda la familia
    # crema de tokens.json cae en el rango 20-65°.
    import colorsys
    tok = io.open('tokens.json', encoding='utf-8').read()
    malos = []
    for hexs in set(re.findall(r'#([0-9A-Fa-f]{6})', tok)):
        r, g, b = (int(hexs[i:i+2], 16) / 255 for i in (0, 2, 4))
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        if 20 <= h * 360 <= 65 and s > 0.40:
            malos.append('#%s (hue %.0f°, sat %.0f%%)' % (hexs.upper(), h * 360, s * 100))
    if malos:
        huecos.append('%d colores de tokens.json caen en el rango prohibido 20-65° con saturación '
                      'alta: %s' % (len(malos), ', '.join(sorted(malos))))
    else:
        ok.append('color: ningún token saturado en el rango naranja/amarillo')


# ─── modo entrega: valida un entregable, no el repo ─────────────────────────
def validar_entrega(path):
    """El hallazgo que motivó esto: en una auditoría una AI declaró cinco cifras como no
    verificables en su reporte y las dejó escritas en el entregable. Declarar no es contener."""
    s = io.open(path, encoding='utf-8', errors='ignore').read()
    texto = s
    # lo que va después del título PEDIDO A HUMANOS habla SOBRE el entregable, no es contenido
    m = re.search(r'PEDIDO A HUMANOS', texto, re.I)
    if m:
        texto = texto[:m.start()]
    texto = re.sub(r'<!--.*?-->', ' ', texto, flags=re.S)      # los comentarios traen instrucciones, no copy
    texto = re.sub(r'<(script|style|title|head)[^>]*>.*?</\1>', ' ', texto, flags=re.S | re.I)
    texto = re.sub(r'<[^>]+>', ' ', texto)
    # el texto de un hueco declarado describe qué falta: no es una afirmación del entregable
    texto = re.sub(r'\[(PENDIENTE|XX)[^\]]*\]', ' ', texto)

    pendientes = len(re.findall(r'\[PENDIENTE\]|\[XX\]', s))
    borrador = 'BORRADOR' in s.upper()
    pedido = bool(re.search(r'PEDIDO A HUMANOS', s, re.I))

    # cifras aprobadas: lo que está en facts.json puede viajar
    hechos = io.open('ai/facts.json', encoding='utf-8').read()
    aprobadas = set(re.findall(r'\b(\d[\d.,]*)\b', hechos))

    # dos formas de afirmar una cifra, y las dos tienen que estar respaldadas:
    #   con unidad  -> "68%", "3x", "40k"
    #   cardinal    -> "21 AgTech domains", "10 countries"
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
    print('ENTREGA: %s' % path)
    print('=' * 72)
    if sueltas:
        print('\n[FALLA] %d cifras afirmadas que no están en facts.json: %s'
              % (len(sueltas), ', '.join(sorted(set(sueltas))[:12])))
        print('        Ninguna de estas puede viajar en el entregable. Van como [PENDIENTE].')
    else:
        print('\n[OK] no hay cifras sin respaldo en facts.json')

    if pendientes and not borrador:
        print('\n[FALLA] el entregable tiene %d huecos ([PENDIENTE]/[XX]) y NO está marcado como '
              'BORRADOR. Con un hueco adentro no puede salir como final.' % pendientes)
    elif pendientes:
        print('\n[OK] %d huecos declarados y el entregable está marcado como BORRADOR' % pendientes)
    else:
        print('\n[OK] sin huecos: el entregable puede salir como final')

    if pendientes and not pedido:
        print('\n[FALLA] hay huecos pero falta el bloque "PEDIDO A HUMANOS" con qué dato falta '
              'y a quién se le pide.')
    elif pendientes:
        print('\n[OK] el pedido a humanos está presente')

    ok_total = (not sueltas and not (pendientes and not borrador)
                and not (pendientes and not pedido))
    print('\n' + '-' * 72)
    print('el entregable %s' % ('PUEDE entregarse' if ok_total else 'NO puede entregarse todavía'))
    return 0 if ok_total else 1


if '--entrega' in sys.argv:
    i = sys.argv.index('--entrega')
    if i + 1 >= len(sys.argv):
        print('uso: python3 ai/validar.py --entrega <archivo>')
        sys.exit(2)
    sys.exit(validar_entrega(sys.argv[i + 1]))


# ─── 9. el wordmark: una sola geometría ────────────────────────────────────
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

for fn in (check_pendientes, check_cobertura, check_nomenclatura, check_links,
           check_peso, check_conteo_assets, check_color, check_wordmark, check_drift):
    try:
        fn()
    except Exception as e:
        fallas.append('%s explotó: %s: %s' % (fn.__name__, type(e).__name__, e))

print('=' * 72)
print('VALIDACIÓN DE LA CAPA DE CONSUMO PARA AI%s' % ('  (con red)' if CON_RED else '  (local)'))
print('=' * 72)
for t, xs in (('FALLA', fallas), ('HUECO (necesita decisión humana)', huecos), ('OK', ok)):
    for x in xs:
        print('\n[%s] %s' % (t, x))
print('\n' + '-' * 72)
print('fallas: %d · huecos: %d · ok: %d' % (len(fallas), len(huecos), len(ok)))
sys.exit(1 if fallas else 0)
