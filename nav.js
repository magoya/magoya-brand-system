/* Cierra el menú "Conocer la marca" al hacer click afuera o con Escape. */
(function(){
  var g = document.querySelector('.nav-group');
  if(!g) return;
  document.addEventListener('click', function(e){ if(g.open && !g.contains(e.target)) g.open = false; });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape' && g.open){ g.open = false; g.querySelector('summary').focus(); } });
})();

/* Selector ES / EN: lleva a la misma sección en el otro idioma (las dos ediciones comparten los id). */
(function(){
  var l = document.querySelector('.mg-topbar a.lang');
  if(!l) return;
  l.addEventListener('click', function(){ if(location.hash) l.href = l.href.split('#')[0] + location.hash; });
})();
