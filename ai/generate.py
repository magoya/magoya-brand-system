#!/usr/bin/env python3
"""Genera la capa machine-readable del brand system.
Correr desde la raíz del repo: python3 ai/generate.py
Regenera: assets/icons/*.svg, ai/assets.json (con la ficha de cada foto), ai/vectores.md y ai/vectores/*.md,
.ai/presets/AGENTS.md, .ai/presets/cursor-rule.mdc.txt, llms-full.txt, ai/kit.zip
Es idempotente: correrlo después de cada cambio de assets o de los documentos que entran en llms-full.txt."""
import re, os, json, html, struct

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

# ---------- 2. assets.json ----------
CATDOC = {
 'assets': ('Raíz: wordmarks del logo y marcas a mano (círculo y flecha)', 'El wordmark es LA firma de la marca. Nunca redibujarlo: usar el SVG tal cual. Variantes por fondo: cream sobre oscuro, dark sobre claro. Las marcas a mano resaltan una palabra o un dato con un círculo o una flecha; nunca subrayado.'),
 'assets/avatars': ('4 avatares oficiales derivados del wordmark', 'La cara = redes de comunidad (IG, X). La m = canales corporativos (LinkedIn, favicon). Nunca usar el monograma m dentro de cards. No inventar avatares nuevos.'),
 'assets/icons': ('Los 58 íconos de línea del sistema (export de icons.html)', 'Trazo 2px redondeado, grid 24×24, stroke=currentColor (recoloreables). ATENCION: embebido como <img> currentColor renderiza NEGRO: inlinear el SVG y setear color por CSS, o reemplazar currentColor por el hex. Sobre oscuro: crema #F6F1EB con UNO destacado en lima. Sobre claro: #161616, el destacado va #009145.'),
 'assets/photos': ('Fotografía real: aérea de campo y personas', 'Aérea de campo: color natural con overlay verde profundo para fondos con texto, siempre enfoque cenital. Personas: siempre a color, sin ningún detalle encima, mejor en espacios abiertos. Nunca stock.'),
 'assets/logos': ('Logos de cuentas objetivo, sueltos en la raíz de logos/', 'Mismo trato que los de cliente: siempre reales, en gris.'),
 'assets/logos/clients': ('Logos REALES de clientes', 'Los únicos logos permitidos en un logo wall. OJO: los SVG son a COLOR y traen la imagen embebida como raster dentro de un <pattern>, así que NO se pasan a gris cambiando fill ni recoloreando paths: hay que aplicar un filtro (CSS filter:grayscale(1) o un feColorMatrix). El sistema los exige en escala de grises y con tamaño óptico parejo; el archivo no viene así.'),
 'assets/logos/partners': ('Logos reales del stack tecnológico', 'Se muestran en su color oficial.'),
 'assets/downloads': ('Descargas: membrete de documentos (header y footer) y colecciones .zip', ''),
 'assets/font': ('Manrope variable (única tipografía)', 'Pesos 200–800. Display 800 tracking −3%. También en Google Fonts como "Manrope".'),
 'assets/font/manrope': ('Archivos de la fuente', ''),
 'assets/favicon': ('Favicons oficiales', 'Avatar m al corte, sin padding extra.'),
 'assets/studio/icons/agro': ('Íconos agro del Studio', ''),
 'assets/studio/icons/ai': ('Logos oficiales de plataformas de AI', 'Usar la variante correcta según fondo (-black sobre claro).'),
 'assets/studio/icons/social': ('Logos oficiales de redes', 'Idem variantes por fondo.'),
 'assets/studio/devices': ('Mockups de dispositivos', ''),
 # assets/refs NO va en el manifiesto: está gitignored, así que sus URLs dan 404
 # en brand.magoya.com. Es material fuente y BRAND.md ya dice que no se publica.
}
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
# ---------- 2a. fotos: una ficha por archivo ----------
# Una AI que lee por link no ve la foto: la elige por su ficha. La descripción sale del
# alt de la ficha de library.html (la escribió una persona), nunca se inventa acá.
def _jpg_size(p):
    f = open(p, 'rb'); f.read(2)
    while True:
        b = f.read(1)
        while b and b != b'\xff': b = f.read(1)
        if not b: return (0, 0)
        m = f.read(1)
        while m == b'\xff': m = f.read(1)
        if m in (b'\xc0', b'\xc1', b'\xc2'):
            f.read(3); h, w = struct.unpack('>HH', f.read(4)); return (w, h)
        n = struct.unpack('>H', f.read(2))[0]; f.read(n - 2)

_lib = open('library.html').read()
fotos = []
for f in tree.get('assets/photos', []):
    p = f'assets/photos/{f}'
    m = re.search(r'<img src="%s" alt="([^"]*)"(?: data-en-alt="([^"]*)")?' % re.escape(p), _lib)
    w, h = _jpg_size(p) if f.lower().endswith(('.jpg', '.jpeg')) else (0, 0)
    ficha = {'archivo': f, 'url': f'{BASE}/{p}',
             'familia': 'aérea de campo' if f.startswith('field-') else 'personas',
             'ancho_px': w, 'alto_px': h,
             'orientacion': 'cuadrada' if w == h else ('horizontal' if w > h else 'vertical'),
             'peso_kb': os.path.getsize(p) // 1024,
             'descripcion': html.unescape(m.group(1)) if m else ''}
    if m and m.group(2): ficha['description_en'] = html.unescape(m.group(2))
    fotos.append(ficha)
print(f'fotos con ficha: {sum(1 for x in fotos if x["descripcion"])} de {len(fotos)}')

manifest = {
 'que_es': 'Manifiesto completo de assets del brand system de Magoya. Cada URL es pública y fetcheable sin auth. Antes de usar cualquier asset, leer BRAND.md (reglas) y tokens.json (valores).',
 'doctrina': f'{BASE}/BRAND.md',
 'tokens': f'{BASE}/tokens.json',
 'como_se_consume': {
  'regla': 'Todo elemento de la marca es un archivo del sistema: tiene URL directa y figura en este manifiesto. Nada vive solo adentro de una página, un ZIP o un PDF.',
  'por_que': 'Una AI que lee por link recibe texto (Markdown, JSON, TXT). Un archivo de imagen (.svg, .jpg, .png) no le llega: probado el 17 de noviembre de 2026 con el fetch de Claude contra brand.magoya.com. El texto llega en cualquier herramienta.',
  'vectores_de_la_marca': {'como': 'texto', 'donde': f'{BASE}/ai/vectores.md',
   'detalle': 'Wordmark, avatares, miscelánea gestual, componentes, favicon, los 58 íconos del sistema y los íconos agro, con su código SVG completo. Se pegan tal cual: nunca se redibujan.'},
  'fotos': {'como': 'por URL, o como archivo cargado', 'donde': 'la clave "fotos" de este manifiesto',
   'detalle': 'La AI no ve la foto por link: la elige por su ficha (familia, medidas, orientación, descripción) y la referencia por URL; la imagen la carga el navegador de quien abre la pieza. En una herramienta que trabaja con archivos cargados, la foto se sube como archivo.'},
  'logos_de_terceros': {'como': 'por URL', 'donde': 'las carpetas assets/logos y assets/studio/icons/ai y social',
   'detalle': 'Logos de clientes, partners, plataformas y redes: se referencian por URL, nunca se redibujan ni se inventan.'},
  'descargas': 'ZIP, PDF y fuentes son para personas. Una AI no los abre por link: lo que traen adentro también está publicado como archivo suelto.'},
 'total_archivos': total,
 'iconos_sistema': icon_entries,
 'fotos': fotos,
 'carpetas': carpetas}
json.dump(manifest, open('ai/assets.json','w'), ensure_ascii=False, indent=1)
print(f'assets.json: {total} archivos en {len(carpetas)} carpetas')

# ---------- 2b. vectores.md: los SVG propios de la marca, como texto ----------
# El fetch de una AI rechaza los .svg (llegan como imagen). El mismo código, adentro de un
# .md, llega entero. La fuente sigue siendo el archivo de assets/: esto es su lectura en texto.
VECTORES = [
 ('Logo · wordmark', 'assets', lambda f: 'wordmark' in f,
  'Es LA firma de la marca. Variantes por fondo: cream sobre oscuro; deep, black o green sobre claro. `magoya-wordmark-animado.svg` es solo para web.'),
 ('Avatares', 'assets/avatars', None,
  'La cara va en redes de comunidad; la m, en canales corporativos y favicon. El monograma m no va dentro de cards. No se inventan avatares.'),
 ('Miscelánea gestual', 'assets/marks', None,
  'Flechas, círculos, X y ✓ para resaltar una palabra o un dato. Lima para acentos; Verde digital; o Verde Magoya cuando el fondo contrasta. Nunca subrayado.'),
 ('Componentes', 'assets/components', None,
  'CTA (pill de 44px) y box (radio 12px). Las medidas exactas están en tokens.json.'),
 ('Favicon', 'assets/favicon', None, 'Avatar m al corte, sin padding extra.'),
 ('Íconos del sistema', 'assets/icons', None,
  'Trazo 2px redondeado, grid 24×24, `stroke="currentColor"`: se pegan inline y el color se da por CSS. Embebidos como `<img>` salen negros.'),
 ('Íconos agro', 'assets/studio/icons/agro', None, 'Mismo trazo y mismo uso que los íconos del sistema.'),
]
# Dos salidas con el mismo contenido:
#   ai/vectores.md            todo junto, para cargar como archivo (va en el kit)
#   ai/vectores/<parte>.md    partido en tres, para leer por link: un fetch de AI suele cortar
#                             alrededor de los 100.000 caracteres, y lo que queda al final se pierde
PARTE = {'Logo · wordmark': 'logo', 'Avatares': 'logo', 'Favicon': 'logo',
         'Miscelánea gestual': 'miscelanea', 'Componentes': 'miscelanea',
         'Íconos del sistema': 'iconos', 'Íconos agro': 'iconos'}
def _cabecera(titulo):
    return [f'# {titulo}', '',
       '> Generado por `ai/generate.py` desde los archivos de `assets/`. No se edita a mano.', '',
       'Una AI que lee por link recibe texto, no imágenes: un `.svg` pedido por su URL no le llega. '
       'Este archivo trae el código SVG completo de cada vector propio de Magoya, para pegarlo tal cual.', '',
       '**Reglas de uso**', '',
       '- El código se copia entero. No se redibuja, no se simplifica y no se le cambian las proporciones.',
       '- Un bloque está completo solo si empieza con `<svg` y termina con `</svg>`. Si te llegó cortado, no lo completes: pedilo de nuevo.',
       '- Lo único que se puede cambiar es el color, y solo por un valor de la paleta de `tokens.json`.',
       '- Cada vector dice si trae ancho y alto. Los que no traen (avatares, favicon, íconos) necesitan `width` y `height` por CSS al pegarlos inline: sin eso quedan en cero o se estiran al ancho del contenedor.',
       '- Las fotos y los logos de terceros no están acá: no son texto. Van por URL, con su ficha en '
       f'{BASE}/ai/assets.json (claves `fotos` y `carpetas`).', '']
_cat = {e['nombre']: e['categoria'] for e in icon_entries}
todo = _cabecera('Magoya — los vectores de la marca, en texto')
partes = {}
n_vec = 0
for titulo, carpeta, filtro, regla in VECTORES:
    fs = [f for f in tree.get(carpeta, []) if f.endswith('.svg') and (filtro is None or filtro(f))]
    fs.sort(key=lambda f: ('animado' in f, f))   # el wordmark estático primero: es el que se usa
    if not fs: continue
    sec = [f'## {titulo}', '', regla, '']
    for f in fs:
        nota = f' · {_cat[f[:-4]]}' if carpeta == 'assets/icons' and f[:-4] in _cat else ''
        _src = open(f'{carpeta}/{f}').read().strip()
        _tag = re.search(r'<svg[^>]*>', _src).group(0)
        _vb = re.search(r'viewBox="([^"]+)"', _tag)
        _medida = (f'viewBox {_vb.group(1)}' if _vb else 'sin viewBox') + (
            ' · trae ancho y alto propios' if re.search(r'\swidth="', _tag) and re.search(r'\sheight="', _tag)
            else ' · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve')
        sec += [f'### {f}{nota}', '', f'{BASE}/{carpeta}/{f}', '', _medida, '', '```svg', _src, '```', '']
        n_vec += 1
    todo += sec
    partes.setdefault(PARTE[titulo], []).extend(sec)
open('ai/vectores.md', 'w').write('\n'.join(todo))
os.makedirs('ai/vectores', exist_ok=True)
NOMBRE = {'logo': 'Magoya — logo, avatares y favicon, en texto',
          'miscelanea': 'Magoya — miscelánea gestual y componentes, en texto',
          'iconos': 'Magoya — íconos del sistema e íconos agro, en texto'}
for k, sec in partes.items():
    open(f'ai/vectores/{k}.md', 'w').write('\n'.join(_cabecera(NOMBRE[k]) + sec))
print(f'vectores.md: {n_vec} vectores, {os.path.getsize("ai/vectores.md")//1024}KB · partes: '
      + ', '.join(f'{k} {os.path.getsize(f"ai/vectores/{k}.md")//1024}KB' for k in partes))

# ---------- 2b'. gemelo en texto del preset de Cursor ----------
# brand.magoya.com sirve el .mdc como binario y un fetch de AI no lo puede leer (probado el
# 17 nov 2026). El mismo contenido con extensión .txt sí llega.
open('.ai/presets/cursor-rule.mdc.txt', 'w').write(open('.ai/presets/cursor-rule.mdc').read())

# ---------- 2c. preset AGENTS.md: el mismo cuerpo que el preset de Copilot ----------
# AGENTS.md es el archivo de instrucciones que leen Codex, Cursor, Copilot, Gemini CLI y otros
# agentes de repo. El cuerpo no se escribe dos veces: sale del preset de Copilot.
_cuerpo = open('.ai/presets/copilot-instructions.md').read().split('-->', 1)[1].strip()
_agents = """<!--
CÓMO USAR ESTE ARCHIVO — AGENTS.md (Codex, Cursor, Copilot, Gemini CLI y otros agentes de repo)
Guardalo en la raíz del repo donde trabajás, con este nombre:

    AGENTS.md

Si el repo ya tiene un AGENTS.md, pegá esta sección al final en vez de sobrescribir.
Claude Code lee CLAUDE.md: para ese caso está el preset claude-code-CLAUDE.md.
Gemini CLI lee GEMINI.md por defecto: se le indica AGENTS.md con context.fileName en .gemini/settings.json.
Generado por ai/generate.py desde copilot-instructions.md. No se edita a mano.
-->

""" + _cuerpo + f"""

## Dónde está todo

- Protocolo de consumo para AI (modo de lectura, assets, fallas conocidas, contrato de entrega): {BASE}/ai/protocolo.md
- Vectores propios (wordmark, avatares, miscelánea, íconos) como texto, para pegar tal cual: {BASE}/ai/vectores.md
- Fotos y logos: se referencian por URL desde {BASE}/ai/assets.json. Si hacen falta en el repo, se bajan como archivo. No se redibujan ni se generan.
"""
open('.ai/presets/AGENTS.md', 'w').write(_agents)
print(f'preset AGENTS.md: {len(_agents)//1024}KB')

# ---------- 3. llms-full.txt: todo en un fetch ----------
parts = []
parts.append(open('llms.txt').read())
parts.append('\n\n# ===== BRAND.md (doctrina completa) =====\n\n' + open('BRAND.md').read())
# capa verbal: Guía editorial V2 (voz y tono + instrucciones para AI) y Brand Playbook (oct 2026): A-D en Markdown + vocabulario
for _titulo, _f in [('GUIA EDITORIAL (voz y tono + instrucciones operativas para AI · .ai/verbal/guia-editorial.md)', '.ai/verbal/guia-editorial.md'),
                    ('ESTRATEGIA (capa verbal A · .ai/verbal/estrategia.md)', '.ai/verbal/estrategia.md'),
                    ('APLICACION (capa verbal D · .ai/verbal/aplicacion.md)', '.ai/verbal/aplicacion.md'),
                    ('VOCABULARIO (vocabulary.json)', 'vocabulary.json')]:
    parts.append('\n\n# ===== ' + _titulo + ' =====\n\n' + open(_f).read())
# voz.md y lenguaje.md quedan fuera del fetch único para no pasar ~200KB (algunas AIs truncan):
# su voz ya está en la guía editorial y su vocabulario y glosario en vocabulary.json.
parts.append('\n\n# ===== VOZ Y LENGUAJE (detalle) =====\n\nEl detalle del playbook (objetivos por mercado, diales, '
             'postura, lo que Magoya no dice, glosario completo y ejemplos) está en '
             'https://brand.magoya.com/.ai/verbal/voz.md y https://brand.magoya.com/.ai/verbal/lenguaje.md\n')
parts.append('\n\n# ===== CONSTRAINTS (minimos/maximos/clearspace/safe areas) =====\n\n' + open('ai/constraints.json').read())
parts.append('\n\n# ===== PRECEDENCIA (quien gana cuando dos reglas chocan) =====\n\n' + open('ai/precedencia.json').read())
parts.append('\n\n# ===== METODO DE TRABAJO (obligatorio) =====\n\n' + open('ai/metodo.md').read())
parts.append('\n\n# ===== CHECKLIST VISUAL =====\n\n' + open('.ai/checklist.md').read())
parts.append('\n\n# ===== CHECKLIST VERBAL (texto) =====\n\n' + open('.ai/checklist-verbal.md').read())
open('llms-full.txt', 'w').write('\n'.join(parts))
import os as _os
print(f'llms-full.txt: {_os.path.getsize("llms-full.txt")//1024}KB')

# ---------- 4. kit.zip: los archivos para cargar en una herramienta que no abre links ----------
# La lista es la de la sección 5.2 de ai/protocolo.md. Sin compresión y con fecha fija, para que
# regenerar sin cambios dé el mismo archivo byte a byte.
import zipfile
KIT = ['ai/protocolo.md', 'llms-full.txt', 'tokens.json', 'tokens.css', 'ai/facts.json',
       'ai/vectores.md', 'ai/assets.json', '.ai/verbal/voz.md', '.ai/verbal/lenguaje.md']
with zipfile.ZipFile('ai/kit.zip', 'w', zipfile.ZIP_STORED) as z:
    for f in KIT:
        zi = zipfile.ZipInfo(os.path.basename(f), date_time=(2026, 1, 1, 0, 0, 0))
        zi.external_attr = 0o644 << 16
        z.writestr(zi, open(f, 'rb').read())
print(f'kit.zip: {len(KIT)} archivos, {os.path.getsize("ai/kit.zip")//1024}KB')
