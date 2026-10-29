/* Menú lateral + pop-up de descargas. Sin dependencias. */
(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('#dock a'));
  var map = {};
  links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
  var sections = Object.keys(map).map(function (id) { return document.getElementById(id); }).filter(Boolean);

  // Recursos por sección: salen de las tarjetas de la sección "Recursos".
  var recMap = { logo: 'rec-logo', tipografia: 'rec-tipografia', imagenes: 'rec-imagenes',
                 iconografia: 'rec-iconografia', piezas: 'rec-piezas', youtube: 'rec-youtube',
                 personaje: 'rec-personaje' };
  var pop = document.getElementById('dlpop');
  var dismissed = false;

  function showPop(id) {
    if (!pop) return;
    var rec = recMap[id] && document.getElementById(recMap[id]);
    if (!rec || dismissed) { pop.classList.add('off'); return; }
    document.getElementById('dlk').textContent = rec.getAttribute('data-sec') + ' · descarga';
    document.getElementById('dlt').textContent = rec.getAttribute('data-title');
    document.getElementById('dlm').textContent = rec.getAttribute('data-meta');
    document.getElementById('dlb').textContent = rec.getAttribute('data-btn');
    document.getElementById('dlgo').setAttribute('href', rec.getAttribute('data-href'));
    pop.hidden = false;
    // forzar reflow para que la transición se vea
    void pop.offsetWidth;
    pop.classList.remove('off');
  }

  var close = document.getElementById('dlclose');
  if (close) close.addEventListener('click', function () { dismissed = true; pop.classList.add('off'); });

  function setActive(id) {
    links.forEach(function (a) { a.classList.remove('act'); a.removeAttribute('aria-current'); });
    if (map[id]) { map[id].classList.add('act'); map[id].setAttribute('aria-current', 'true'); }
    showPop(id);
  }

  if (!('IntersectionObserver' in window) || !sections.length) return;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) setActive(e.target.id); });
  }, { rootMargin: '-35% 0px -55% 0px', threshold: 0 });
  sections.forEach(function (s) { io.observe(s); });

  // En celular el menú es una fila con scroll: mantener visible el ítem activo.
  var dock = document.getElementById('dock');
  var mo = new MutationObserver(function () {
    var act = dock.querySelector('a.act');
    if (act && dock.scrollWidth > dock.clientWidth) {
      dock.scrollTo({ left: act.offsetLeft - 16, behavior: 'smooth' });
    }
  });
  mo.observe(dock, { attributes: true, subtree: true, attributeFilter: ['class'] });
})();
