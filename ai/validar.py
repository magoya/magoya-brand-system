#!/usr/bin/env python3
"""
Validador de la capa de consumo para IA.

Chequea lo que se puede chequear sin criterio: que los links resuelvan, que las
referencias cruzadas cierren, que la capa generada no se haya despegado de sus
fuentes, que no haya slots sin límite y que el copy en español no diga "AI".

No opina de diseño y no inventa valores: si falta una definición, la reporta
como hueco para que la decida una persona.

    python3 ai/validar.py            # local, sin red
    python3 ai/validar.py --red      # además verifica cada URL publicada
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
    usados = set()
    for fila in sel['decision']:
        for campo in ('usa', 'alternativa'):
            for m in re.findall(r'\b([A-M]\d{1,2})\b', str(fila.get(campo, ''))):
                usados.add(m)
    faltan = sorted(usados - ids)
    if faltan:
        fallas.append('selector.json apunta a módulos que no existen en templates/index.json: %s' % ', '.join(faltan))
    else:
        ok.append('selector.json: %d filas, todos los módulos citados existen' % len(sel['decision']))

    sin_ruta = sorted(ids - usados)
    if sin_ruta:
        huecos.append('%d módulos no son alcanzables desde el selector (una IA no tiene cómo elegirlos): %s'
                      % (len(sin_ruta), ', '.join(sin_ruta)))


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

for fn in (check_selector, check_slots, check_pendientes, check_cobertura,
           check_nomenclatura, check_links, check_peso, check_conteo_assets,
           check_drift):
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
