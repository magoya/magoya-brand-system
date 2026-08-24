#!/usr/bin/env python3
"""Genera las 41 plantillas HTML con slots desde el DSL real del exportador.
Correr desde la raíz: python3 ai/templates.py  (generate.py lo invoca solo).
Ejecuta las funciones SPEC reales en Node (no las interpreta) y convierte
los shapes a HTML absoluto en unidades cqw — fidelidad 1:1 con el .pptx.
Salida: ai/templates/<ID>.html + ai/templates/index.json
"""
import json, os, re, subprocess, tempfile, html as htmllib

BASE = 'https://brand.magoya.com'
dsl = json.load(open('ai/slides.json'))['layouts']['dsl_src']
mods = {m['id']: m for m in json.load(open('ai/slides.json'))['modulos']}

# ---------- 1. ejecutar SPEC real en node ----------
runner = '''
var window = {}; var U = 13.333/100;
function IN(v){return v*U;} function FS(cqw){return cqw*9.6;}
''' + dsl + '''
var out = {};
Object.keys(SPEC).forEach(function(id){
  try { out[id] = SPEC[id]('NN').filter(Boolean); }
  catch(e){ out[id] = {error: String(e)}; }
});
console.log(JSON.stringify(out));
'''
with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as f:
    f.write(runner); runner_path = f.name
res = subprocess.run(['node', runner_path], capture_output=True, text=True)
os.unlink(runner_path)
if res.returncode != 0:
    raise SystemExit('node error: ' + res.stderr[:800])
shapes_by_mod = json.loads(res.stdout)
errs = {k: v for k, v in shapes_by_mod.items() if isinstance(v, dict)}
if errs:
    print('MODULOS CON ERROR:', errs)

# ---------- 2. conversión shapes -> HTML ----------
def cq(v):  # unidades del lienzo (100 = ancho) -> cqw
    return f'{round(v, 3)}cqw'

def fs(s):  # tamaño tipográfico: s*9.6pt -> px a 1920 = s*12.8 -> cqw
    return f'{round(s * 12.8 / 19.2, 3)}cqw'

def esc(t):
    return htmllib.escape(str(t)).replace('\\n', '\n')

LOCKED_PAT = re.compile(r'wordmark|logos/|/icons/|motif|avatar|favicon|studio/')

def render(mid, shapes):
    slots, body = [], []
    tno = 0
    for sh in shapes:
        k = sh.get('k')
        x, y = sh.get('x', 0), sh.get('y', 0)
        w, h = sh.get('w', 0), sh.get('h', 5)
        pos = f'left:{cq(x)};top:{cq(y)};width:{cq(w)};height:{cq(h)}'
        if k == 'r':
            st = pos
            if sh.get('fill'):
                alpha = sh.get('alpha')
                if alpha is not None:
                    a = round((100 - alpha) / 100, 2)
                    fill = sh["fill"]
                    st += f';background:#{fill};opacity:{a}'
                else:
                    st += f';background:#{sh["fill"]}'
            if sh.get('line'):
                st += f';border:{round(sh.get("lw",1)*1.33,1)}px solid #{sh["line"]}'
            if sh.get('radius'):
                st += f';border-radius:{cq(sh["radius"])}'
            # el golpe de lima deja de ser geometría anónima: pasa a ser miembro de un
            # grupo elegible. La instrucción "el destacado va en lima" era inejecutable
            # porque el rect no tenía ningún marcador — ahora se puede mover de miembro.
            acc = ' data-accent="lima"' if str(sh.get('fill', '')).upper() == 'A2FF00' else ''
            body.append(f'<div class="r"{acc} style="{st}"></div>')
        elif k == 't':
            tno += 1
            sid = f't{tno}'
            s = sh.get('s', 1.75)
            st = pos + f';font-size:{fs(s)}'
            st += f';font-weight:{800 if sh.get("b") else 400}'
            st += f';color:#{sh.get("c") or "161616"}'
            acc_t = ' data-accent="lima"' if str(sh.get('c', '')).upper() == 'A2FF00' else ''
            st += f';text-align:{sh.get("al","left")}'
            va = sh.get('va', 'top')
            if va != 'top':
                st += f';display:flex;flex-direction:column;justify-content:{ {"middle":"center","bottom":"flex-end"}.get(va,"flex-start") }'
            st += f';line-height:{sh.get("lh", 1.2)}'
            if sh.get('cs') is not None:
                st += f';letter-spacing:{round(sh["cs"]*1.33/ (s*12.8), 4)}em'
            elif sh.get('tight'):
                st += ';letter-spacing:-0.03em'
            text = sh.get('text', '')
            if isinstance(text, list):
                text = ' '.join(str(t.get('text', t)) if isinstance(t, dict) else str(t) for t in text)
            # cifras de ejemplo -> [XX]: imposible entregarlas en silencio como reales
            _t = str(text).strip()
            _m = re.fullmatch(r'[\d.,]+\s*(%|x|×|k|K|M|\+|hs|min)?', _t)
            _es_cifra = bool(_m) and _t != 'NN'
            _con_unidad = bool(_m and _m.group(1))   # 68%, 3x, 40k: es una afirmación, no una numeración
            if _es_cifra and (s >= 2.4 or _con_unidad):
                text = '[XX]'
            # heurística de rol y capacidad
            fpx = s * 12.8
            role = 'display' if s >= 4 else ('titulo' if s >= 2.4 else ('subtitulo' if s >= 1.7 else 'caption'))
            if str(text).isupper() and s <= 1.7: role = 'kicker'
            if str(text).strip() == 'NN': role = 'numero_de_pagina'
            cpl = max(1, int(w * 19.2 / (0.56 * fpx)))
            lines = max(1, int(h * 19.2 / (fpx * sh.get('lh', 1.2))))
            slots.append({'slot': sid, 'rol': role, 'texto_ejemplo': str(text)[:160],
                          'max_caracteres_aprox': int(cpl * lines * 0.9),
                          'max_lineas': lines})
            body.append(f'<p class="t" data-slot="{sid}" data-rol="{role}"{acc_t} style="{st}">{esc(text)}</p>')
        elif k == 'i':
            src = sh.get('src', '')
            url = src if src.startswith('http') else f'{BASE}/{src}'
            locked = bool(LOCKED_PAT.search(src))
            fit = {'contain': 'contain', 'cover': 'cover', 'crop': 'cover'}.get(sh.get('fit'), 'fill')
            tint = sh.get('tint')
            swap = sh.get('swap')
            if (tint or swap) and src.endswith('.svg'):
                color = tint or (swap[0][1] if swap else '161616')
                if not str(color).startswith('#'): color = f'#{color}'
                body.append(
                    f'<div class="im" data-asset="{src}" {"data-locked=\"brand\"" if locked else ""} '
                    f'style="{pos};background:{color};-webkit-mask-image:url({url});mask-image:url({url});'
                    f'-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;-webkit-mask-size:{fit};mask-size:{fit};'
                    f'-webkit-mask-position:center;mask-position:center"></div>')
            else:
                extra = ';filter:grayscale(1)' if sh.get('gray') else ''
                slot_attr = '' if locked else f' data-slot="img{len(slots)}" data-reemplazable="foto: respetar B&N+acento si es persona"'
                body.append(f'<img class="im" src="{url}" {"data-locked=\"brand\"" if locked else slot_attr} '
                            f'style="{pos};object-fit:{fit}{extra}" alt="">')
        elif k == 'c':
            data = json.dumps(sh.get('data', []), ensure_ascii=False)[:400]
            slots.append({'slot': f'chart{tno}', 'rol': 'grafico',
                          'texto_ejemplo': f'tipo {sh.get("type","bar")}',
                          'nota': 'reemplazar por barras/lineas hechas con divs .r usando la paleta; datos de ejemplo en el comentario'})
            body.append(f'<!-- CHART tipo={sh.get("type","?")} datos={esc(data)} -->'
                        f'<div class="chart" data-slot="chart{tno}" style="{pos};border:1px dashed #C4B5A6;'
                        f'display:flex;align-items:center;justify-content:center;color:#666;font-size:1cqw">'
                        f'GRÁFICO ({sh.get("type","bar")}): reconstruir con divs de la paleta</div>')
        elif k == 'tb':
            rows = sh.get('rows', [])
            trs = []
            for r_ in rows[:12]:
                tds = ''.join(f'<td>{esc(c.get("text", c) if isinstance(c, dict) else c)}</td>' for c in r_)
                trs.append(f'<tr>{tds}</tr>')
            slots.append({'slot': f'tabla{tno}', 'rol': 'tabla', 'texto_ejemplo': 'tabla de datos'})
            body.append(f'<table class="tb" data-slot="tabla{tno}" style="{pos}">{"".join(trs)}</table>')
    meta = mods.get(mid, {})
    doc = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>Magoya · módulo {mid} — {htmllib.escape(meta.get('nombre', ''))}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{background:#EEF2EC;padding:2vw;font-family:'Manrope',Arial,sans-serif}}
  .slide{{position:relative;aspect-ratio:16/9;width:100%;max-width:1920px;margin:0 auto;
         container-type:inline-size;overflow:hidden;font-family:'Manrope',Arial,sans-serif;
         box-shadow:0 10px 40px rgba(0,0,0,.12)}}
  .t{{position:absolute;white-space:pre-line;font-family:inherit}}
  .r,.im,.chart{{position:absolute}}
  .tb{{position:absolute;border-collapse:collapse;font-size:1.4cqw}}
  .tb td{{border-bottom:1px solid #DCD0C4;padding:.6cqw .9cqw}}
</style>
<!--
PLANTILLA OFICIAL MAGOYA — módulo {mid} ({htmllib.escape(meta.get('nombre',''))})
Cuándo usarlo: {htmllib.escape(meta.get('cuando_usarlo',''))}

ATENCION — TODO EL TEXTO Y LAS CIFRAS DE ESTA PLANTILLA SON EJEMPLO.
Nunca entregar los textos/cifras de ejemplo como contenido real. Los datos
aprobados de la compania viven en https://brand.magoya.com/ai/facts.json —
si el dato que necesitas no esta ahi, pedilo al usuario; no lo inventes.

REGLAS PARA LA IA (no negociables):
1. NO tocar posiciones, tamaños, colores ni tipografías. La geometría ES la marca.
2. Solo reemplazar el TEXTO INTERNO de los elementos con data-slot, respetando
   max_caracteres_aprox y max_lineas de ai/templates/index.json. Si tu texto no
   entra, acortá el texto — nunca achiques la fuente ni muevas la caja.
3b. Los elementos data-accent="lima" son el golpe de lima de la slide. Podés MOVER
   el acento a otro elemento del mismo grupo (sacale el atributo a uno y ponéselo a
   otro, junto con el color #A2FF00) cuando el destacado semántico sea otro — por
   ejemplo si estás proponiendo el modelo de la card 1 y no el de la card 2. Regla:
   como máximo UNO por slide, y cero es válido. Lo que no se cambia es la geometría.
4. Los elementos data-locked="brand" (wordmark, logos, íconos, motivos) no se
   tocan, no se reemplazan, no se mueven.
5. Las imágenes data-reemplazable aceptan otra foto REAL respetando su regla.
5. El texto "NN" del número de página se reemplaza por el número real (2 dígitos).
-->
</head><body>
<div class="slide" data-modulo="{mid}">
{chr(10).join(body)}
</div>
</body></html>'''
    return doc, slots

os.makedirs('ai/templates', exist_ok=True)
index = {'como_armar_un_deck_de_varias_slides': {
          'starter': f'{BASE}/ai/templates/deck-starter.html (y .txt) — documento base: pegá los <div class="slide"> uno abajo del otro ahí adentro',
          'reglas': ['un solo <head> (el del starter: trae Manrope y los estilos .slide/.t/.r/.im)',
                     'separacion entre slides: 48px (escala base-4) — ya esta en el starter',
                     'fondo de la pagina: #EEF2EC (sage) — nunca un color fuera de la paleta',
                     'el numero de pagina (rol numero_de_pagina) va correlativo en 2 digitos desde la primera slide de contenido',
                     'no repetir dos veces el mismo modulo seguido; alterná los pares espejo (H1/H2, I1/I2)']},
         'que_es': 'Plantillas HTML oficiales de los 41 módulos, generadas del exportador real. Se usan TAL CUAL: copiá el archivo, llená los data-slot respetando max_caracteres, no toques nada más. La geometría, colores y tipografía ya son la marca. IMPORTANTE: si tu fetch de .html llega convertido/resumido, usá url_texto_crudo (.txt, mismo contenido servido como texto plano). TODO texto y cifra de las plantillas es EJEMPLO: los datos reales aprobados están en ai/facts.json — lo que no esté ahí se pide, no se inventa.',
         'datos_reales': f'{BASE}/ai/facts.json',
         'como_elegir': f'{BASE}/ai/selector.json',
         'constraints': f'{BASE}/ai/constraints.json',
         'modulos': []}
ok = 0
for mid in sorted(shapes_by_mod):
    shp = shapes_by_mod[mid]
    if isinstance(shp, dict):
        continue
    doc, slots = render(mid, shp)
    open(f'ai/templates/{mid}.html', 'w').write(doc)
    open(f'ai/templates/{mid}.txt', 'w').write(doc)  # copia text/plain: WebFetch de .html convierte a markdown y rompe el copy-paste
    m = mods.get(mid, {})
    index['modulos'].append({'id': mid, 'nombre': m.get('nombre',''), 'cuando_usarlo': m.get('cuando_usarlo',''),
                             'url': f'{BASE}/ai/templates/{mid}.html',
                             'url_texto_crudo': f'{BASE}/ai/templates/{mid}.txt', 'slots': slots})
    ok += 1
starter = '''<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>Magoya · deck</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&display=swap" rel="stylesheet">
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:#EEF2EC;padding:2vw;font-family:'Manrope',Arial,sans-serif}
  .slide{position:relative;aspect-ratio:16/9;width:100%;max-width:1920px;margin:0 auto 48px;
         container-type:inline-size;overflow:hidden;font-family:'Manrope',Arial,sans-serif;
         box-shadow:0 10px 40px rgba(0,0,0,.12)}
  .t{position:absolute;white-space:pre-line;font-family:inherit}
  .r,.im,.chart{position:absolute}
  .tb{position:absolute;border-collapse:collapse;font-size:1.4cqw}
  .tb td{border-bottom:1px solid #DCD0C4;padding:.6cqw .9cqw}
</style>
<!--
DECK STARTER OFICIAL MAGOYA
Peg\u00e1 ac\u00e1 abajo los <div class="slide"> de cada plantilla (ai/templates/<ID>.txt),
en el orden de tu narrativa. NO copies el <head> de cada plantilla: este ya tiene todo.
Numeraci\u00f3n: reemplaz\u00e1 cada "NN" por el n\u00famero correlativo en 2 d\u00edgitos.
Las cifras que veas como [XX] son datos que TEN\u00c9S QUE PEDIR: est\u00e1n en ai/facts.json
o no existen todav\u00eda. Nunca las completes con algo verosímil.
-->
</head><body>

<!-- pegá los <div class="slide"> acá, uno abajo del otro -->

</body></html>'''
open('ai/templates/deck-starter.html','w').write(starter)
open('ai/templates/deck-starter.txt','w').write(starter)
json.dump(index, open('ai/templates/index.json','w'), ensure_ascii=False, indent=1)
print(f'plantillas generadas: {ok}/41 · index.json con slots y max_caracteres')
