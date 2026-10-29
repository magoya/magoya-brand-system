#!/usr/bin/env python3
"""Genera la capa machine-readable del brand system.
Correr desde la raíz del repo: python3 ai/generate.py
Regenera: assets/icons/*.svg, ai/assets.json, llms-full.txt
Es idempotente: correrlo después de cada cambio de assets o de los documentos que entran en llms-full.txt."""
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
 'assets/pieces': ('Piezas de la identidad ANTERIOR de IA en Campo (retirada)', 'No usar en piezas nuevas: el sistema vigente de IA en Campo está en ai-en-campo/ (violeta #B700FF, Plus Jakarta Sans, esquinas cortadas).'),
 'assets/studio': ('Logos de terceros + kit de la identidad ANTERIOR de IA en Campo', 'Los doodles, flourishes, badge y mark del lockup anterior están retirados: no usar en piezas nuevas. El sistema vigente de IA en Campo está en ai-en-campo/.'),
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
manifest = {
 'que_es': 'Manifiesto completo de assets del brand system de Magoya. Cada URL es pública y fetcheable sin auth. Antes de usar cualquier asset, leer BRAND.md (reglas) y tokens.json (valores).',
 'doctrina': f'{BASE}/BRAND.md',
 'tokens': f'{BASE}/tokens.json',
 'total_archivos': total,
 'iconos_sistema': icon_entries,
 'carpetas': carpetas}
json.dump(manifest, open('ai/assets.json','w'), ensure_ascii=False, indent=1)
print(f'assets.json: {total} archivos en {len(carpetas)} carpetas')

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
