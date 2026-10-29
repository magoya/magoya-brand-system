/* Idioma en la misma página (brand-book, library, icons, logos): ?lang=en la lee en inglés.
   El <head> de la página ya lo marca antes de pintar; esto lo repite por si falta,
   y cambia los atributos que no se pueden duplicar con data-l (alt, title, aria-label). */
(function(){
  var h = document.documentElement;
  if(/[?&]lang=en(&|$)/.test(location.search)){ h.setAttribute('data-lang','en'); h.lang = 'en'; }
  if(h.getAttribute('data-lang') !== 'en') return;
  ['alt','title','aria-label'].forEach(function(at){
    [].forEach.call(document.querySelectorAll('[data-en-'+at+']'), function(el){ el.setAttribute(at, el.getAttribute('data-en-'+at)); });
  });
})();

/* Cierra el menú "Conocer la marca" al hacer click afuera o con Escape. */
(function(){
  var g = document.querySelector('.nav-group');
  if(!g) return;
  document.addEventListener('click', function(e){ if(g.open && !g.contains(e.target)) g.open = false; });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape' && g.open){ g.open = false; g.querySelector('summary').focus(); } });
})();

/* Selector ES / EN: lleva a la misma sección en el otro idioma (las dos ediciones comparten los id).
   En una página con data-lang-toggle (brand-book, library, icons, logos) alterna ?lang=en en la misma página.
   En los dos casos conserva el #hash. */
(function(){
  var l = document.querySelector('.mg-topbar a.lang');
  if(!l) return;
  if(l.hasAttribute('data-lang-toggle')){
    var en = document.documentElement.getAttribute('data-lang') === 'en';
    var base = location.pathname.split('/').pop() || 'brand-book.html';
    var dest = function(){ return base + (en ? '' : '?lang=en') + location.hash; };
    l.href = dest();
    l.setAttribute('hreflang', en ? 'es' : 'en');
    l.addEventListener('click', function(){ l.href = dest(); });
    return;
  }
  l.addEventListener('click', function(){ if(location.hash) l.href = l.href.split('#')[0] + location.hash; });
})();
