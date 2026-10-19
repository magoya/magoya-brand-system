/* Scripts del manual (scroll-spy del rail, --topbar-h y dock), extraídos de brand-book.html */
(function(){
  var links=[].slice.call(document.querySelectorAll('.side a[href^="#"]'));
  if(!links.length) return;
  var targets=links.map(function(a){ return document.getElementById(a.getAttribute('href').slice(1)); });
  var last=-1, raf=null;
  function mark(i){
    if(i===last) return;            // sin cambio real: no se toca el DOM (evita jank)
    last=i;
    links.forEach(function(a,k){
      a.classList.toggle('act', k===i);
      a.classList.toggle('near', Math.abs(k-i)===1);
    });
  }
  function compute(){
    raf=null;
    var y=window.scrollY+window.innerHeight*0.3, best=0;
    for(var k=0;k<targets.length;k++){
      var t=targets[k]; if(!t) continue;
      if(t.getBoundingClientRect().top+window.scrollY<=y) best=k;
    }
    mark(best);
  }
  function onScroll(){ if(raf===null) raf=requestAnimationFrame(compute); }   // 1 cálculo por frame
  window.addEventListener('scroll',onScroll,{passive:true});
  window.addEventListener('resize',onScroll);
  compute();
})();
/* --topbar-h: el topbar es fixed y hace flex-wrap, asi que su alto real cambia
   con el ancho de la ventana. Se mide y se publica como variable CSS. */
(function(){
  var tb = document.querySelector('.mg-topbar');
  if(!tb) return;
  function set(){
    var fijo = getComputedStyle(tb).position === 'fixed';
    document.documentElement.style.setProperty(
      '--topbar-h', fijo ? Math.round(tb.getBoundingClientRect().height) + 'px' : '0px');
  }
  set();
  window.addEventListener('resize', set);
  window.addEventListener('load', set);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(set);
})();
/* rail: ancho de cada pill + magnificacion tipo dock */
(function(){
  var side = document.querySelector('.side');
  if(!side) return;
  var links = [].slice.call(side.querySelectorAll('a'));
  if(!links.length) return;

  /* --w: cuanto tiene que ensancharse el punto para que entre su texto */
  function medir(){
    var max = 0;
    links.forEach(function(a){
      var sp = a.querySelector('span');
      if(!sp) return;
      var w = Math.ceil(sp.getBoundingClientRect().width) + 38;   /* 24 izq + 14 der */
      a.style.setProperty('--w', w + 'px');
      if(w > max) max = w;
    });
    side.style.setProperty('--wmax', (max + 10) + 'px');
  }
  medir();
  window.addEventListener('resize', medir);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(medir);

  /* --s: la pill mas cercana al cursor crece y arrastra a las vecinas.
     Los centros se leen de offsetTop (layout), no de getBoundingClientRect,
     porque ese ya viene con la escala aplicada y se realimentaria. */
  var raf = null, cy = 0;
  function pintar(){
    raf = null;
    links.forEach(function(a){
      var d = Math.abs(cy - (a.offsetTop + a.offsetHeight / 2));
      a.style.setProperty('--s', (1 + 0.26 * Math.exp(-(d * d) / 2704)).toFixed(3));
    });
  }
  side.addEventListener('mousemove', function(e){
    cy = e.clientY - side.getBoundingClientRect().top;
    if (raf === null) raf = requestAnimationFrame(pintar);
  });
  side.addEventListener('mouseleave', function(){
    links.forEach(function(a){ a.style.setProperty('--s', '1'); });
  });
})();
