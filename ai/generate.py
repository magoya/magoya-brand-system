#!/usr/bin/env python3
"""Genera la capa machine-readable del brand system.
Correr desde la raíz del repo: python3 ai/generate.py
Regenera: assets/icons/*.svg, ai/assets.json, ai/slides.json
Es idempotente — correrlo después de cada cambio de assets o slides."""
import re, os, json

BASE = 'https://brand.magoya.com'

# ---------- 1. iconos: de <symbol> inline a archivos ----------
s = open('icons.html').read()
symbols = re.findall(r'<symbol id="i-([a-z-]+)" viewBox="0 0 24 24">(.*?)</symbol>', s, re.S)
cats_raw = re.search(r'const CATS = \[(.*?)\n\];', s, re.S).group(1)
cat_of = {}
cat_desc = {}
for name, sub, icons in re.findall(r'\["([^"]+)", "([^"]+)", \[([^\]]+)\]\]', cats_raw):
    cat_desc[name] = sub
    for ic in re.findall(r'"([a-z-]+)"', icons):
        cat_of[ic] = name
WRAP = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{}</svg>\n')
icon_entries = []
for name, inner in symbols:
    open(f'assets/icons/{name}.svg', 'w').write(WRAP.format(inner.strip()))
    icon_entries.append({'nombre': name, 'categoria': cat_of.get(name, '?'),
                         'url': f'{BASE}/assets/icons/{name}.svg'})
print(f'iconos exportados: {len(icon_entries)}')

# ---------- 2. slides.json ----------
s = open('slides.html').read()
fams = []
for fid in 'ABCDEFGHIJKLM':
    m = re.search(rf'id="fam-{fid.lower()}"[^>]*><h2>([^<]+)</h2><span class="sub">([^<]+)</span>', s)
    if m: fams.append({'id': fid, 'nombre': m.group(1).replace('&amp;','&'), 'que_cubre': m.group(2)})
mods = []
def _texto(html):
    """Saca los tags inline y deja el texto. El regex anterior cortaba en el primer
    <b>, y 9 de 41 modulos perdian el cuando_usarlo a mitad de oracion — L1 se quedaba
    con 61 de 146 caracteres y perdia justo 'logos siempre reales y en gris'."""
    t = re.sub(r'<[^>]+>', '', html)
    t = (t.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
          .replace('&nbsp;', ' ').replace('&times;', '×').replace('&middot;', '·'))
    return ' '.join(t.split())

# el cuando_usarlo termina donde cierra su <p>: hasta ahi se lee todo, tags incluidos
for m in re.finditer(r'data-mod="([A-M]\d+)".*?<span class="nm">([^<]+)</span>.*?<b>Cuándo usarlo:</b>(.*?)</p>', s, re.S):
    mods.append({'id': m.group(1), 'nombre': m.group(2).replace('&amp;','&'),
                 'cuando_usarlo': _texto(m.group(3))})

# ---------- 2b. layouts exactos: extraer el DSL del exportador ----------
i0 = s.find('var C=')
i1 = s.find('window.magoyaBuildDeck')
dsl_src = s[i0:i1] if (i0 > -1 and i1 > i0) else ''
import re as _re
mod_srcs = {}
for _m in _re.finditer(r'SPEC\.([A-M]\d+)\s*=\s*function', dsl_src):
    start = _m.start()
    nxt = _re.search(r'SPEC\.[A-M]\d+\s*=\s*function', dsl_src[_m.end():])
    end = _m.end() + (nxt.start() if nxt else len(dsl_src) - _m.end())
    mod_srcs[_m.group(1)] = dsl_src[start:end].rstrip().rstrip(';') + ';'
for mod in mods:
    if mod['id'] in mod_srcs:
        mod['layout_src'] = mod_srcs[mod['id']]

slides = {
  'que_es': 'Spec machine-readable de los 41 módulos de presentación de Magoya. El deck kit navegable (con export .pptx) vive en slides.html — esta es la receta para que una IA reconstruya cualquier módulo.',
  'si_tu_fetch_trunca': f'Este archivo es grande (~86KB). Si tu fetch llega cortado o resumido, usa los archivos por familia (2-10KB, mismo formato): {BASE}/ai/slides/A.json hasta {BASE}/ai/slides/M.json — una familia por archivo, con layout_src completo por modulo.',
  'lienzo': {'ancho_px': 1920, 'alto_px': 1080, 'margen_interior': '7%',
             'fondos': ['blanco #FFFFFF', 'sage #EFF3EE', 'oscuro #133825 (solo apertura/cierre/citas)'],
             'escala_tipografica_pt': [126, 84, 56, 42],
             'conversion': '1pt = 1.333px sobre el lienzo de 1920x1080 (126pt = 168px). La unidad s del DSL se convierte a pt en la funcion paint() incluida en dsl_src.',
             'reglas': ['un golpe de lima #A2FF00 por slide como máximo',
                        'máximo dos recursos gráficos además de la tipografía',
                        'wordmark chico arriba-izquierda en slides interiores']},
  'layouts': {
    'como_leer': 'Cada modulo trae layout_src: la funcion JS literal del exportador .pptx con la geometria exacta. Coordenadas en % de un lienzo de 100 de ancho x 56.25 de alto (16:9). Helpers: T(texto,{x,y,w,h,s,b,c,al,lh,...})=texto, IMG({src,x,y,w,h,fit,...})=imagen (src relativo a la raiz del sitio), R(...)=rectangulo, bg(fill)=fondo full-bleed, chrome(pg,dark)=wordmark chico arriba-izquierda + numero de pagina. Constantes de color y conversion de unidades: ver dsl_src (la funcion paint() muestra como s se convierte a puntos).',
    'dsl_src': dsl_src},
  'familias': fams, 'modulos': mods,
  'fuente_de_verdad': f'{BASE}/slides.html'}
json.dump(slides, open('ai/slides.json','w'), ensure_ascii=False, indent=1)
os.makedirs('ai/slides', exist_ok=True)
for fam in fams:
    fmods = [m for m in mods if m['id'].startswith(fam['id'])]
    json.dump({'familia': fam, 'lienzo': slides['lienzo'], 'layouts_como_leer': slides['layouts']['como_leer'],
               'modulos': fmods, 'dsl_completo_en': f'{BASE}/ai/slides.json'},
              open(f"ai/slides/{fam['id']}.json",'w'), ensure_ascii=False, indent=1)
print(f'slides.json: {len(fams)} familias, {len(mods)} módulos + {len(fams)} archivos por familia')

# ---------- 3. assets.json ----------
CATDOC = {
 'assets': ('Raíz: wordmarks del logo y motivo de semicírculos', 'El wordmark es LA firma de la marca. Nunca redibujarlo: usar el SVG tal cual. Variantes por fondo: cream sobre oscuro, dark sobre claro.'),
 'assets/avatars': ('4 avatares oficiales derivados del wordmark', 'La cara = redes de comunidad (IG, X). La m = canales corporativos (LinkedIn, favicon). Nunca usar el monograma m dentro de cards. No inventar avatares nuevos.'),
 'assets/icons': ('Los 58 íconos de línea del sistema (export de icons.html)', 'Trazo 2px redondeado, grid 24×24, stroke=currentColor (recoloreables). ATENCION: embebido como <img> currentColor renderiza NEGRO — inlinear el SVG y setear color por CSS, o reemplazar currentColor por el hex. Sobre oscuro: crema #F6F1EB con UNO destacado en lima. Sobre claro: #161616, el destacado va #009145.'),
 'assets/illus': ('Personajes ilustrados y caminos', 'Personajes planos sin rostro, paleta cerrada, zapatillas verdes. Siempre recortados por un borde, lado opuesto al texto. Nunca sobre foto ni junto a un ícono.'),
 'assets/photos': ('Fotografía real del equipo y de campo', 'Personas SIEMPRE en B&N + un acento de color. Foto aérea con scrim verde profundo. Nunca stock.'),
 'assets/photos/merch': ('Fotos reales de merch', 'Verde profundo + crema, bordado discreto.'),
 'assets/logos': ('Wordmarks propios en variantes', 'Ver reglas del logo en BRAND.md sección 2.'),
 'assets/logos/clients': ('Logos REALES de clientes', 'Los únicos logos permitidos en un logo wall. En grilla: escala de grises, tamaño óptico parejo.'),
 'assets/logos/partners': ('Logos reales del stack tecnológico', 'Se muestran en su color oficial.'),
 'assets/motif': ('', ''),
 'assets/downloads': ('Entregables listos: firma de email animada/estática, membrete', 'La firma de email lleva SIEMPRE el wordmark, nunca los avatares.'),
 'assets/font': ('Manrope variable (única tipografía)', 'Pesos 200–800. Display 800 tracking −3%. También en Google Fonts como "Manrope".'),
 'assets/font/manrope': ('Archivos de la fuente', ''),
 'assets/favicon': ('Favicons oficiales', 'Avatar m al corte, sin padding extra.'),
 'assets/pieces': ('Piezas reales exportadas (referencia de calidad)', 'fecha-marcada-ig-portrait es LA pieza canónica de IA en campo (formato madre 4:5).'),
 'assets/studio': ('Kit de la sub-marca IA en campo + logos de terceros', 'Los doodles/flourishes del Studio son SOLO para piezas de IA en campo, no para Magoya core.'),
 'assets/studio/icons/agro': ('Íconos agro del Studio', ''),
 'assets/studio/icons/ai': ('Logos oficiales de plataformas de IA', 'Usar la variante correcta según fondo (-black sobre claro).'),
 'assets/studio/icons/social': ('Logos oficiales de redes', 'Idem variantes por fondo.'),
 'assets/studio/devices': ('Mockups de dispositivos', ''),
 # assets/refs NO va en el manifiesto: está gitignored, así que sus URLs dan 404
 # en brand.magoya.com. Es material fuente y BRAND.md ya dice que no se publica.
}
# ─── perfil de composición por módulo ───────────────────────────────────────
# Derivado de las plantillas ya generadas, nunca a mano: es el eje que le faltaba
# a la IA para componer un deck con ritmo. Sin esto, el selector mapea contenido →
# módulo fila por fila y nadie gobierna la SECUENCIA: el resultado es un deck que
# cumple todas las reglas y sale soso (feedback real, 2026-08-19).
def perfil_de_modulos(idx_modulos):
    import glob as _glob
    CANVAS = {'FFFFFF': 'blanco', 'EEF2EC': 'sage', 'F6F1EB': 'crema',
              '133825': 'verde-profundo', '0C2117': 'verde-profundo',
              '0A1F14': 'verde-profundo', '161616': 'negro'}
    presupuesto = {m['id']: sum(int(s.get('max_caracteres_aprox') or 0) for s in m['slots'])
                   for m in idx_modulos}
    perfiles = {}
    for f in sorted(_glob.glob('ai/templates/[A-M]*.html')):
        mid = f.split('/')[-1][:-5]
        s = open(f, encoding='utf-8').read()
        cuerpo = s[s.find('<div class="slide"'):]
        m = re.search(r'width:100cqw;height:56\.25cqw;background:#([0-9A-Fa-f]{6})', cuerpo)
        lienzo = CANVAS.get(m.group(1).upper(), 'otro') if m else 'sin-fondo'
        rec = {'foto':        len(re.findall(r'class="im"[^>]*(?:photos/|pieces/)', cuerpo)),
               'ilustracion': len(re.findall(r'illus/', cuerpo)),
               'motivo':      len(re.findall(r'motif', cuerpo)),
               'logos':       len(re.findall(r'logos/', cuerpo)),
               'iconos':      len(re.findall(r'/icons/', cuerpo)),
               'grafico':     len(re.findall(r'GRAFICO|dashed|chart', cuerpo, re.I))}
        if rec['foto'] and re.search(r'class="im"[^>]*width:(?:9\d|100)cqw', cuerpo):
            lienzo = 'foto'
        visual = sum(rec.values())
        perfiles[mid] = {'lienzo': lienzo, 'recursos_visuales': visual,
                         'presupuesto_texto': presupuesto.get(mid, 0),
                         'recursos': {k: v for k, v in rec.items() if v}}
    chars = sorted(p['presupuesto_texto'] for p in perfiles.values())
    med = chars[len(chars) // 2] if chars else 0
    for p in perfiles.values():
        if p['recursos_visuales'] >= 2 or p['lienzo'] in ('foto', 'verde-profundo', 'negro'):
            p['peso'] = 'visual'
        elif p['presupuesto_texto'] >= med:
            p['peso'] = 'texto'
        else:
            p['peso'] = 'mixto'
    return perfiles, med


# ─── rol narrativo (beat) por módulo ────────────────────────────────────────
# El eje que gobierna el mercado (Sequoia, Storydoc, el ghost deck de McKinsey) es el
# ROL en el argumento, no la textura. Se deriva de lo que cada módulo ya declara que
# carga estructuralmente — la regla de derivación va publicada, para que sea auditable
# y corregible, no una opinión escondida en el código.
BEAT_POR_MODULO = {
 'M1': 'apertura', 'M2': 'apertura', 'M3': 'pedido',
 'A3': 'estructura', 'A4': 'estructura', 'A5': 'estructura',
 'A1': 'tension', 'H3': 'tension', 'I1': 'tension', 'I2': 'tension',
 'A2': 'contexto', 'H1': 'contexto', 'H2': 'contexto', 'H4': 'contexto',
 'B1': 'propuesta', 'B2': 'propuesta', 'B3': 'propuesta',
 'E1': 'propuesta', 'E2': 'propuesta',
 'F1': 'propuesta', 'F2': 'propuesta', 'F3': 'propuesta', 'F4': 'propuesta',
 'J3': 'propuesta', 'K2': 'propuesta',
 'C1': 'evidencia', 'C2': 'evidencia', 'C3': 'evidencia', 'C4': 'evidencia',
 'D1': 'evidencia', 'D2': 'evidencia', 'D3': 'evidencia', 'D4': 'evidencia',
 'G1': 'evidencia', 'G2': 'evidencia',
 'J1': 'evidencia', 'J2': 'evidencia', 'K1': 'evidencia', 'L1': 'evidencia',
 'E3': 'pedido', 'E4': 'pedido',
}
COMO_SE_DERIVO = {
 'apertura':   'su cuando_usarlo dice que es portada',
 'pedido':     'cierra el deck o pone el ask comercial (escenarios de inversión)',
 'estructura': 'da aire u orientación, no argumenta (agenda, divisor, título de capítulo)',
 'tension':    'statement que reencuadra: una sola idea que carga el sentido',
 'contexto':   'sitúa el mercado o aclara el statement antes de proponer',
 'propuesta':  'qué hacemos, cómo lo hacemos y con quién (servicios, método, journey, pod)',
 'evidencia':  'respalda con cifra, gráfico, caso o tercero',
}
A_REVISAR = {'A1': ('A1 es el único ambiguo: su cuando_usarlo dice "abrir un bloque con una sola '
  'idea", que puede ser tensión o propuesta según el bloque. Se derivó como tensión porque la frase '
  'que carga el sentido suele reencuadrar. Si en la práctica se usa para proponer, corregilo acá.')}


tree = {}
NO_PUBLICABLE = ('assets/refs',)   # gitignored: sus URLs darían 404 en el sitio
for root, dirs, files in os.walk('assets'):
    if root.startswith(NO_PUBLICABLE):
        dirs[:] = []
        continue
    fs = sorted(f for f in files if not f.startswith('.'))
    if fs: tree[root] = fs
carpetas = []
total = 0
for root in sorted(tree):
    desc, reglas = CATDOC.get(root, ('', ''))
    entry = {'carpeta': root, 'descripcion': desc}
    if reglas: entry['reglas'] = reglas
    entry['archivos'] = [f'{BASE}/{root}/{f}' for f in tree[root]]
    total += len(tree[root])
    carpetas.append(entry)
manifest = {
 'que_es': 'Manifiesto completo de assets del brand system de Magoya. Cada URL es pública y fetcheable sin auth. Antes de usar cualquier asset, leer BRAND.md (reglas) y tokens.json (valores).',
 'doctrina': f'{BASE}/BRAND.md',
 'tokens': f'{BASE}/tokens.json',
 'total_archivos': total,
 'iconos_sistema': icon_entries,
 'carpetas': carpetas}
json.dump(manifest, open('ai/assets.json','w'), ensure_ascii=False, indent=1)
print(f'assets.json: {total} archivos en {len(carpetas)} carpetas')

# ---------- 4. plantillas HTML con slots ----------
import subprocess as _sp
r = _sp.run(['python3', 'ai/templates.py'], capture_output=True, text=True)
print(r.stdout.strip() or r.stderr.strip()[:300])

# ---------- 4b. perfil de composicion: el eje que le faltaba a la IA ----------
_idx = json.load(open('ai/templates/index.json'))
_perf, _med = perfil_de_modulos(_idx['modulos'])
for _m in _idx['modulos']:
    _m['perfil'] = _perf.get(_m['id'], {})
for _m in _idx['modulos']:
    _m['perfil']['beat'] = BEAT_POR_MODULO.get(_m['id'], 'revisar')
import collections as _c2
_idx['roles_narrativos'] = {
 'que_es': ('El rol de cada módulo en el argumento. Es el eje que gobierna la secuencia; la textura '
            '(lienzo, peso visual) es consecuencia, no causa. Viene de cómo lo gobierna el mercado: '
            'Sequoia ordena sus 10 slides por rol, y el ghost deck de McKinsey se aprueba leyendo '
            'solo los títulos, en orden, sin las slides.'),
 'como_se_derivo': COMO_SE_DERIVO,
 'a_revisar': A_REVISAR,
 'inventario': dict(_c2.Counter(m['perfil']['beat'] for m in _idx['modulos'])),
}
_idx['como_componer_el_deck'] = {
 'por_que': ('El selector mapea contenido → módulo fila por fila, y nadie gobierna la SECUENCIA. '
             'Un deck puede cumplir todas las reglas de marca y salir soso. Pasó en una prueba real. '
             'Lo que gobierna la secuencia es el ROL de cada slide en el argumento (campo perfil.beat), '
             'no su textura: la textura es consecuencia.'),
 'las_cuatro_reglas': [
   'La última slide es beat "pedido". No se cierra sin pedir algo.',
   'Antes del primer beat "propuesta" tiene que haber al menos un beat "tension". No se propone sin haber puesto el problema.',
   'Después del primer beat "propuesta" tiene que haber al menos un beat "evidencia". No se afirma sin respaldar.',
   'No más de 3 beats iguales seguidos. Cuatro slides de propuesta seguidas es un catálogo, no un argumento.',
 ],
 'si_una_regla_no_se_puede_cumplir': ('decilo explícito en la entrega, con el motivo. Una excepción '
             'declarada es aceptable; una regla incumplida en silencio no. Ejemplo real: el resumen '
             'ejecutivo no tiene CTA, así que no puede cerrar en "pedido" — eso se declara.'),
 'textura_es_diagnostico_no_regla': ('El campo perfil trae lienzo y peso (visual/mixto/texto) para que '
             'puedas ver si el deck se aplana. NO es un gate: fue uno y se retiró, porque el catálogo '
             'no tiene todavía un módulo visual que cargue un método, un journey ni un caso, así que '
             'un deck de producto no podía cumplirlo (0 de 362.880 órdenes posibles). Miralo, no lo '
             'persigas. Si te queda denso, lo correcto es DECIRLO, no forzar la secuencia.'),
 'si_te_queda_soso': ('NO agregues adorno y NO inventes una carátula: hay meta-análisis de que los '
             'detalles decorativos bajan comprensión y recall (seductive details, 177 effect sizes). '
             'Primero revisá el argumento con las cuatro reglas de arriba — soso casi siempre es '
             '"propone sin tensión" o "cuatro propuestas seguidas", no falta de color. Si el argumento '
             'está bien y sigue denso, es que falta un módulo en el catálogo: reportalo.'),
 'inventario': {
   'por_beat': dict(_c2.Counter(m['perfil']['beat'] for m in _idx['modulos'])),
   'por_lienzo': dict(_c2.Counter(m['perfil']['lienzo'] for m in _idx['modulos'])),
   'por_peso': dict(_c2.Counter(m['perfil']['peso'] for m in _idx['modulos'])),
   'mediana_de_presupuesto_de_texto': _med,
   'sin_portador_visual': ('los beats "propuesta" que cargan método, journey o caso (F2, F3, E1, G1) '
             'son todos peso texto y no tienen recambio visual en el catálogo. Es un hueco conocido.'),
 },
}
json.dump(_idx, open('ai/templates/index.json', 'w'), ensure_ascii=False, indent=1)
print('perfil de composicion: %d modulos · lienzos %s' % (len(_perf),
      _idx['como_componer_el_deck']['inventario']['por_lienzo']))

# ---------- 5. llms-full.txt: todo en un fetch ----------
parts = []
parts.append(open('llms.txt').read())
parts.append('\n\n# ===== BRAND.md (doctrina completa) =====\n\n' + open('BRAND.md').read())
parts.append('\n\n# ===== CONSTRAINTS (minimos/maximos/clearspace/safe areas) =====\n\n' + open('ai/constraints.json').read())
parts.append('\n\n# ===== SELECTOR DE MODULOS (que queres contar -> que plantilla) =====\n\n' + open('ai/selector.json').read())
tpl = json.load(open('ai/templates/index.json'))
lines = ['\n\n# ===== PLANTILLAS LISTAS (llenar slots, NO tocar geometria) =====\n',
         tpl['que_es'], '']
for m in tpl['modulos']:
    _p = m.get('perfil', {})
    lines.append(f"- {m['id']} · {m['nombre']} · beat: {_p.get('beat','?')} · lienzo: "
                 f"{_p.get('lienzo','?')} · peso: {_p.get('peso','?')} -> {m['url']} · slots: " +
                 ', '.join(f"{s['slot']}({s['rol']},max {s.get('max_caracteres_aprox','?')}ch)" for s in m['slots'][:6]))
parts.append('\n'.join(lines))
parts.append('\n\n# ===== COMO COMPONER EL DECK (el arco manda, la textura es consecuencia) =====\n\n'
             + json.dumps(tpl['como_componer_el_deck'], ensure_ascii=False, indent=1)
             + '\n\n' + json.dumps(tpl['roles_narrativos'], ensure_ascii=False, indent=1))
parts.append('\n\n# ===== PRECEDENCIA (quien gana cuando dos reglas chocan) =====\n\n' + open('ai/precedencia.json').read())
parts.append('\n\n# ===== METODO DE TRABAJO (obligatorio) =====\n\n' + open('ai/metodo.md').read())
parts.append('\n\n# ===== CHECKLIST DE ENTREGA =====\n\n' + open('.ai/checklist.md').read())
open('llms-full.txt', 'w').write('\n'.join(parts))
import os as _os
print(f'llms-full.txt: {_os.path.getsize("llms-full.txt")//1024}KB')
