#!/usr/bin/env python3
"""
Decks armados: los tres decks que más se piden, ya compuestos.

POR QUÉ EXISTE ESTO. La medición de la primera semana de uso real fue: cero piezas
salieron bien con "usuario X + link". Todas las que salieron bien necesitaron un
proceso encima — una mesa de cuatro pasadas, un humano cazando un bug, y una terminal
para verificar. El sistema publicaba REGLAS y el usuario tenía que tomar DECISIONES:
qué archivo leer, en qué orden, qué módulo, en qué secuencia, con qué lienzo. Cada
decisión es una chance de que salga mal, y quien pide la pieza no sabe diseño — que
es la razón por la que existe el sistema.

Estos tres decks quitan esas decisiones. La secuencia, los lienzos y el arco ya están
resueltos y validados contra las cuatro reglas de composición. El usuario solo cambia
texto.

NO SE EDITAN A MANO: se generan desde las plantillas oficiales, así que si mañana
cambia un módulo los tres decks se regeneran y no se despegan del catálogo.

    python3 ai/decks.py
"""
import io, json, os, re, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)
SALIDA = 'ai/decks'
BASE = 'https://brand.magoya.com'

IDX = json.load(io.open('ai/templates/index.json', encoding='utf-8'))
MOD = {m['id']: m for m in IDX['modulos']}
HECHOS = json.load(io.open('ai/facts.json', encoding='utf-8'))

# ─── los tres decks ─────────────────────────────────────────────────────────
# Cada slide declara POR QUÉ está: qué beat del argumento sirve. Eso hace la
# secuencia auditable en vez de una lista de módulos sin fundamento.
DECKS = {
 'credenciales': {
   'titulo': 'Credenciales · qué hace Magoya',
   'cuando': 'primer contacto con un cliente nuevo que todavía no sabe qué hacemos',
   'secuencia': [
     ('M1', 'abre con el negocio del cliente en pantalla antes de la primera palabra'),
     ('A1', 'la tensión: el problema que la audiencia reconoce y que nadie le resolvió'),
     ('B1', 'la propuesta: los tres modelos de trabajo'),
     ('F2', 'cómo trabajamos, una frase por fase'),
     ('C1', 'las credenciales en números'),
     ('L1', 'prueba social: los clientes reales'),
     ('G1', 'un caso completo, para que el argumento aterrice'),
     ('M3', 'el pedido'),
   ],
 },
 'propuesta-piloto': {
   'titulo': 'Propuesta de piloto · con escenarios e inversión',
   'cuando': 'ya hubo conversación y hay que proponer un piloto concreto con precio',
   'secuencia': [
     ('M1', 'portada con el contexto de la cuenta'),
     ('A1', 'la tensión: el problema puntual que este piloto ataca'),
     ('H1', 'el contexto de mercado que hace que sea ahora y no en seis meses'),
     ('F2', 'el método con el que lo vamos a atacar'),
     ('F1', 'el timeline del piloto, de dónde arranca a dónde termina'),
     ('G1', 'un caso comparable: ya lo hicimos con otro'),
     ('E3', 'el scope: quién está en el equipo en cada escenario'),
     ('E4', 'la inversión: cuánto dura y cuánto cuesta cada escenario'),
     ('M3', 'el pedido con los próximos pasos'),
   ],
 },
 'cierre-de-proyecto': {
   'titulo': 'Cierre de proyecto · resultados para el sponsor',
   'cuando': 'terminó una etapa y hay que mostrarle al sponsor qué se logró',
   'secuencia': [
     ('M1', 'portada'),
     ('A2', 'de dónde partimos: el contexto acordado al arrancar'),
     ('C1', 'los resultados en números'),
     ('D1', 'la evolución en el tiempo de la métrica principal'),
     ('A4', 'respiro entre bloques, para que los datos no se lean como un muro'),
     ('D4', 'el detalle: una proporción principal y los avances secundarios'),
     ('J1', 'la voz del cliente sobre el trabajo'),
     ('G2', 'antes y después, cerrado'),
     ('M3', 'el pedido: la etapa que sigue'),
   ],
 },
}

# ─── qué instrucción va en cada slot según su rol ───────────────────────────
INSTRUCCION = {
 'kicker':           'KICKER',
 'display':          'TÍTULO — una aserción, no una etiqueta',
 'titulo':           'TÍTULO — una aserción',
 'subtitulo':        'BAJADA — la promesa concreta',
 'bajada':           'BAJADA',
 'caption':          'CAPTION — una línea',
 'label':            'LABEL',
 'nombre':           'NOMBRE',
 'rol':              'ROL',
 'cita':             'CITA — textual, con nombre y rol reales',
 'dato':             '[XX]',
 'cifra':            '[XX]',
 'descriptor':       'QUÉ MIDE',
 'paso':             'PASO',
 'item':             'ÍTEM',
 'pie':              'PIE',
 'cta':              'CTA — sentence case',
 'chip':             'CHIP',
}


def texto_de_slot(slot, mod_id):
    """Qué va en el slot: una instrucción corta con su presupuesto, o [XX] si es cifra.
    La instrucción tiene que ENTRAR en el slot: si el presupuesto es chico, se acorta."""
    rol = str(slot.get('rol', ''))
    ejemplo = str(slot.get('texto_ejemplo', ''))
    if rol == 'numero_de_pagina':
        return None                                    # lo pone el ensamblador
    if ejemplo == '[XX]' or rol in ('dato', 'cifra'):
        return '[XX]'
    base = INSTRUCCION.get(rol, rol.upper() or 'TEXTO')
    tope = slot.get('max_caracteres_aprox')
    if tope:
        etiqueta = '[%s · máx %s]' % (base, tope)
        if len(etiqueta) > int(tope):                  # no entra: se acorta
            corto = base.split(' — ')[0]
            etiqueta = '[%s · %s]' % (corto, tope)
            if len(etiqueta) > int(tope):
                etiqueta = '[%s]' % corto[:max(3, int(tope) - 2)]
        return etiqueta
    return '[%s]' % base


def hechos_aprobados():
    """Lo único que se rellena de verdad: los datos que facts.json ya aprobó."""
    d = {}
    for k in ('datos_aprobados', 'cifras', 'aprobado'):
        v = HECHOS.get(k)
        if isinstance(v, list):
            for item in v:
                if isinstance(item, dict) and item.get('cifra'):
                    d[str(item['cifra'])] = item
    anio = datetime.date.today().year
    d['_anios'] = anio - int(HECHOS.get('derivados_del_tiempo', {}).get('activa_desde', 2017))
    return d


def bloque_de_slide(mod_id):
    s = io.open('ai/templates/%s.html' % mod_id, encoding='utf-8').read()
    i = s.index('<div class="slide"')
    j = s.rindex('</div>') + len('</div>')
    return s[i:j]


def armar(nombre, spec, hechos):
    starter = io.open('ai/templates/deck-starter.html', encoding='utf-8').read()
    piezas, pagina, mapa = [], 0, []
    for orden, (mod_id, por_que) in enumerate(spec['secuencia'], 1):
        m = MOD[mod_id]
        bloque = bloque_de_slide(mod_id)
        # el texto de cada slot pasa a ser la instrucción de qué va ahí
        for sl in m.get('slots', []):
            nuevo = texto_de_slot(sl, mod_id)
            if nuevo is None:
                continue
            pat = r'(data-slot="%s"[^>]*>)(.*?)(</p>)' % re.escape(sl['slot'])
            bloque = re.sub(pat, lambda mm: mm.group(1) + nuevo + mm.group(3),
                            bloque, count=1, flags=re.S)
        # numeración: solo las interiores llevan número, como M1/M2/M3 del catálogo
        beat = m['perfil']['beat']
        if beat not in ('apertura',) and mod_id != 'M3':
            pagina += 1
            bloque = bloque.replace('>NN<', '>%02d<' % pagina)
        bloque = bloque.replace('>NN<', '><')
        piezas.append('<!-- %02d · %s · beat %s — %s -->\n%s'
                      % (orden, mod_id, beat, por_que, bloque))
        mapa.append({'orden': orden, 'modulo': mod_id, 'beat': beat,
                     'lienzo': m['perfil']['lienzo'], 'por_que': por_que,
                     'plantilla': m['url']})
    cuerpo = '\n\n'.join(piezas)
    aviso = ('<!--\n  DECK ARMADO · %s\n  %s\n\n'
             '  Cambiá SOLO el texto que está entre corchetes. El [XX] es un dato que\n'
             '  tenés que pedir: está en %s/ai/facts.json o no existe todavía —\n'
             '  no lo completes con algo verosímil.\n\n'
             '  NO muevas ni cambies posiciones, tamaños, colores ni tipografía: la\n'
             '  geometría ES la marca. Los elementos data-locked no se tocan.\n\n'
             '  La secuencia ya está decidida y validada. Si sacás o agregás una slide,\n'
             '  verificá el arco: la última tiene que pedir algo, y antes de proponer\n'
             '  tiene que haber una tensión.\n-->\n' % (spec['titulo'], spec['cuando'], BASE))
    # Hoja de pedido: qué hay que juntar antes de que esto salga a un cliente.
    # Un deck sin llenar ES un borrador, así que lo dice y cumple su propio contrato
    # de entrega (ai/precedencia.json). Va fuera de los .slide: no cuenta como slide.
    faltantes = []
    for x in mapa:
        m = MOD[x['modulo']]
        cifras = [s['slot'] for s in m.get('slots', [])
                  if str(s.get('texto_ejemplo', '')) == '[XX]' or s.get('rol') in ('dato', 'cifra')]
        if cifras:
            faltantes.append('Slide %02d (%s): %d cifra(s) — %s'
                             % (x['orden'], x['modulo'], len(cifras), ', '.join(cifras)))
    hoja = ('<div data-pedido-a-humanos style="max-width:1920px;margin:0 auto 48px;padding:40px 48px;'
            'background:#161616;color:#ECE3DB;font:400 15px/1.6 Manrope,Arial,sans-serif">'
            '<div style="font:800 13px/1 Manrope;letter-spacing:.12em;color:#A2FF00;'
            'margin-bottom:18px">BORRADOR · NO SALE A CLIENTE ASÍ</div>'
            '<div style="font:800 26px/1.2 Manrope;margin-bottom:20px">PEDIDO A HUMANOS</div>'
            '<p style="max-width:70ch;margin-bottom:18px">Este deck está compuesto y validado: la '
            'secuencia, los lienzos y el arco ya están resueltos. Lo que falta es el contenido. '
            'Cambiá cada texto entre corchetes por el real. Los <b>[XX]</b> son datos que hay que '
            '<b>pedir</b>, no completar: si no están aprobados en '
            '<code>ai/facts.json</code>, no viajan en la pieza.</p>'
            '<ul style="margin:0 0 18px 22px">'
            + ''.join('<li style="margin-bottom:6px">%s</li>' % f for f in faltantes)
            + '</ul>'
            '<p style="max-width:70ch;color:#9fb3a6">Cuando no quede ningún corchete, borrá este '
            'bloque y el deck sale como final. Verificalo con '
            '<code>python3 ai/validar.py --pieza tu-archivo.html</code>.</p></div>')
    html = starter.replace('<!-- pegá los <div class="slide"> acá, uno abajo del otro -->',
                           aviso + cuerpo + '\n\n' + hoja)
    html = html.replace('<title>Magoya · deck</title>',
                        '<title>Magoya · %s</title>' % spec['titulo'])
    return html, mapa


def main():
    os.makedirs(SALIDA, exist_ok=True)
    hechos = hechos_aprobados()
    catalogo = {
     'que_es': ('Los tres decks que más se piden, YA COMPUESTOS. La secuencia, los lienzos y el '
                'arco están resueltos y validados: no hay que elegir módulos ni componer. '
                'Cambiás el texto entre corchetes y listo.'),
     'por_que': ('Medición de la primera semana de uso real: cero piezas salieron bien con '
                 '"usuario X + link". El sistema publicaba reglas y el usuario tenía que tomar '
                 'decisiones de diseño que no sabe tomar. Esto le quita las decisiones.'),
     'como_se_usa': [
       'Elegí el deck que corresponde al momento (ver "cuando" de cada uno).',
       'Bajá el .html y abrilo. Cada texto entre corchetes dice qué va ahí y cuántos caracteres entran.',
       'Cambiá SOLO el texto. Un [XX] es un dato que hay que pedir, nunca completar.',
       'Si sacás o agregás una slide, revisá el arco (ver reglas_del_arco).',
     ],
     'reglas_del_arco': IDX['como_componer_el_deck']['las_cuatro_reglas'],
     'version': datetime.date.today().isoformat(),
     'decks': {},
    }
    for nombre, spec in DECKS.items():
        html, mapa = armar(nombre, spec, hechos)
        ruta = '%s/%s.html' % (SALIDA, nombre)
        io.open(ruta, 'w', encoding='utf-8').write(html)
        catalogo['decks'][nombre] = {
          'titulo': spec['titulo'],
          'cuando_usarlo': spec['cuando'],
          'url': '%s/%s' % (BASE, ruta),
          'slides': len(mapa),
          'arco': ' → '.join('%s(%s)' % (x['modulo'], x['beat']) for x in mapa),
          'composicion': mapa,
        }
        print('%-22s %d slides · %s' % (nombre, len(mapa),
              ' → '.join(x['modulo'] for x in mapa)))
    io.open('%s/index.json' % SALIDA, 'w', encoding='utf-8').write(
        json.dumps(catalogo, ensure_ascii=False, indent=1) + '\n')
    print('%s/index.json · %d decks' % (SALIDA, len(DECKS)))


if __name__ == '__main__':
    main()
