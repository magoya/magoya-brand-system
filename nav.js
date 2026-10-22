/* Cierra el menú "Conocer la marca" al hacer click afuera o con Escape. */
(function(){
  var g = document.querySelector('.nav-group');
  if(!g) return;
  document.addEventListener('click', function(e){ if(g.open && !g.contains(e.target)) g.open = false; });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape' && g.open){ g.open = false; g.querySelector('summary').focus(); } });
})();
