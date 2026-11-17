# Magoya — íconos del sistema e íconos agro, en texto

> Generado por `ai/generate.py` desde los archivos de `assets/`. No se edita a mano.

Una AI que lee por link recibe texto, no imágenes: un `.svg` pedido por su URL no le llega. Este archivo trae el código SVG completo de cada vector propio de Magoya, para pegarlo tal cual.

**Reglas de uso**

- El código se copia entero. No se redibuja, no se simplifica y no se le cambian las proporciones.
- Un bloque está completo solo si empieza con `<svg` y termina con `</svg>`. Si te llegó cortado, no lo completes: pedilo de nuevo.
- Lo único que se puede cambiar es el color, y solo por un valor de la paleta de `tokens.json`.
- Cada vector dice si trae ancho y alto. Los que no traen (avatares, favicon, íconos) necesitan `width` y `height` por CSS al pegarlos inline: sin eso quedan en cero o se estiran al ancho del contenedor.
- Las fotos y los logos de terceros no están acá: no son texto. Van por URL, con su ficha en https://brand.magoya.com/ai/assets.json (claves `fotos` y `carpetas`).

## Íconos del sistema

Trazo 2px redondeado, grid 24×24, `stroke="currentColor"`: se pegan inline y el color se da por CSS. Embebidos como `<img>` salen negros.

### ai.svg · Datos & AI

https://brand.magoya.com/assets/icons/ai.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 3l1.7 4.8L17.5 9.5l-4.8 1.7L11 16l-1.7-4.8L4.5 9.5l4.8-1.7zM19 15l.9 2.1L22 18l-2.1.9L19 21l-.9-2.1L16 18l2.1-.9z"/></svg>
```

### arrow.svg · Sistema / UI

https://brand.magoya.com/assets/icons/arrow.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h16M13 5l7 7-7 7"/></svg>
```

### at.svg · Comunicación & redes

https://brand.magoya.com/assets/icons/at.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M16 12v1.5a2.5 2.5 0 005 0V12a9 9 0 10-3.5 7.1"/></svg>
```

### bell.svg · Comunicación & redes

https://brand.magoya.com/assets/icons/bell.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9a6 6 0 0112 0c0 6 2 7 2 7H4s2-1 2-7M10 20a2 2 0 004 0"/></svg>
```

### briefcase.svg · Negocio

https://brand.magoya.com/assets/icons/briefcase.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="8" width="18" height="12" rx="2"/><path d="M9 8V6a3 3 0 016 0v2M3 13h18"/></svg>
```

### calendar.svg · Negocio

https://brand.magoya.com/assets/icons/calendar.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>
```

### chart-bars.svg · Datos & AI

https://brand.magoya.com/assets/icons/chart-bars.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>
```

### chart-line.svg · Datos & AI

https://brand.magoya.com/assets/icons/chart-line.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 16l5-5 4 3 7-8M3 21h18"/></svg>
```

### chat.svg · Comunicación & redes

https://brand.magoya.com/assets/icons/chat.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 01-8 8H4l2-3a8 8 0 1115-5zM9 12h.01M13 12h.01M17 12h.01"/></svg>
```

### check.svg · Sistema / UI

https://brand.magoya.com/assets/icons/check.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12l5 5L20 6"/></svg>
```

### checklist.svg · Producto & UX

https://brand.magoya.com/assets/icons/checklist.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6l1.5 1.5L8 5M4 12l1.5 1.5L8 11M4 18l1.5 1.5L8 17M11 6h9M11 12h9M11 18h9"/></svg>
```

### chip.svg · Datos & AI

https://brand.magoya.com/assets/icons/chip.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="7" width="10" height="10" rx="2"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/></svg>
```

### cloud.svg · Plataforma & código

https://brand.magoya.com/assets/icons/cloud.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 18a4 4 0 010-8 6 6 0 0111.6-1A4.5 4.5 0 0117 18H6z"/></svg>
```

### code.svg · Plataforma & código

https://brand.magoya.com/assets/icons/code.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 8l-4 4 4 4M16 8l4 4-4 4"/></svg>
```

### dashboard.svg · Plataforma & código

https://brand.magoya.com/assets/icons/dashboard.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="8" height="10" rx="1.5"/><rect x="13" y="3" width="8" height="6" rx="1.5"/><rect x="13" y="11" width="8" height="10" rx="1.5"/><rect x="3" y="15" width="8" height="6" rx="1.5"/></svg>
```

### database.svg · Datos & AI

https://brand.magoya.com/assets/icons/database.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="7" ry="2.5"/><path d="M5 5v14c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5V5M5 12c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5"/></svg>
```

### deploy.svg · Plataforma & código

https://brand.magoya.com/assets/icons/deploy.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21V8M6 14l6-6 6 6M4 3h16"/></svg>
```

### doc.svg · Negocio

https://brand.magoya.com/assets/icons/doc.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2h9l5 5v15H6zM15 2v5h5M9 13h6M9 17h6"/></svg>
```

### download.svg · Sistema / UI

https://brand.magoya.com/assets/icons/download.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M6 9l6 6 6-6M4 21h16"/></svg>
```

### field.svg · Agro

https://brand.magoya.com/assets/icons/field.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20L10 4M14 4l7 16M6.5 13h11M5 17h14M8 9h8"/></svg>
```

### flow.svg · Producto & UX

https://brand.magoya.com/assets/icons/flow.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="6" height="6" rx="1.5"/><rect x="15" y="15" width="6" height="6" rx="1.5"/><path d="M9 6h4a3 3 0 013 3v6"/></svg>
```

### gear.svg · Producto & UX

https://brand.magoya.com/assets/icons/gear.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1"/></svg>
```

### globe.svg · Negocio

https://brand.magoya.com/assets/icons/globe.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/></svg>
```

### growth.svg · Negocio

https://brand.magoya.com/assets/icons/growth.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 17l6-6 4 4 8-8M15 7h6v6"/></svg>
```

### hashtag.svg · Comunicación & redes

https://brand.magoya.com/assets/icons/hashtag.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3L7 21M17 3l-2 18M4 8h17M3 16h17"/></svg>
```

### heart.svg · Comunicación & redes

https://brand.magoya.com/assets/icons/heart.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20s-8-4.5-8-10a4.5 4.5 0 018-3 4.5 4.5 0 018 3c0 5.5-8 10-8 10z"/></svg>
```

### info.svg · Sistema / UI

https://brand.magoya.com/assets/icons/info.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 12v5"/></svg>
```

### layers.svg · Plataforma & código

https://brand.magoya.com/assets/icons/layers.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l9 5-9 5-9-5 9-5zM3 14l9 5 9-5"/></svg>
```

### layout.svg · Producto & UX

https://brand.magoya.com/assets/icons/layout.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M10 10v10"/></svg>
```

### leaf.svg · Agro

https://brand.magoya.com/assets/icons/leaf.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 4C10 4 4 10 4 20c10 0 16-6 16-16zM4 20C8 14 12 10 17 7"/></svg>
```

### link.svg · Plataforma & código

https://brand.magoya.com/assets/icons/link.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.5 13.5a5 5 0 007.4.4l2-2a5 5 0 00-7-7.1l-1.2 1.2M13.5 10.5a5 5 0 00-7.4-.4l-2 2a5 5 0 007 7.1l1.2-1.2"/></svg>
```

### lock.svg · Negocio

https://brand.magoya.com/assets/icons/lock.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 018 0v4M12 15v2"/></svg>
```

### mail.svg · Comunicación & redes

https://brand.magoya.com/assets/icons/mail.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>
```

### mobile.svg · Producto & UX

https://brand.magoya.com/assets/icons/mobile.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="3" width="8" height="18" rx="2"/><path d="M11 17.5h2"/></svg>
```

### partnership.svg · Negocio

https://brand.magoya.com/assets/icons/partnership.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="12" r="5"/><circle cx="15" cy="12" r="5"/></svg>
```

### phone.svg · Comunicación & redes

https://brand.magoya.com/assets/icons/phone.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 3h4l2 5-2.5 1.5a12 12 0 006 6L16 13l5 2v4a2 2 0 01-2 2A16 16 0 013 5a2 2 0 012-2z"/></svg>
```

### pie.svg · Datos & AI

https://brand.magoya.com/assets/icons/pie.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 12V3M12 12l6.5 6"/></svg>
```

### pin.svg · Sistema / UI

https://brand.magoya.com/assets/icons/pin.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6-7-11a7 7 0 0114 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>
```

### play.svg · Comunicación & redes

https://brand.magoya.com/assets/icons/play.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M10 8.5l6 3.5-6 3.5z"/></svg>
```

### plug.svg · Plataforma & código

https://brand.magoya.com/assets/icons/plug.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 7V3M15 7V3M7 7h10v4a5 5 0 01-10 0V7zM12 16v5"/></svg>
```

### plus.svg · Sistema / UI

https://brand.magoya.com/assets/icons/plus.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
```

### rain.svg · Agro

https://brand.magoya.com/assets/icons/rain.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 14a4 4 0 010-8 6 6 0 0111.6-1A4.5 4.5 0 0117 14H6zM8 17l-1 3M12 17l-1 3M16 17l-1 3"/></svg>
```

### route.svg · Producto & UX

https://brand.magoya.com/assets/icons/route.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="5" r="2"/><circle cx="18" cy="19" r="2"/><path d="M6 7v4a4 4 0 004 4h4a4 4 0 014 4"/></svg>
```

### satellite.svg · Datos & AI

https://brand.magoya.com/assets/icons/satellite.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 5a7 7 0 017 7M12 1a11 11 0 0111 11"/></svg>
```

### screen.svg · Producto & UX

https://brand.magoya.com/assets/icons/screen.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/></svg>
```

### search.svg · Producto & UX

https://brand.magoya.com/assets/icons/search.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="6"/><path d="M16 16l5 5"/></svg>
```

### seed.svg · Agro

https://brand.magoya.com/assets/icons/seed.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3c4 3 6 6 6 10a6 6 0 01-12 0c0-4 2-7 6-10zM12 9v7"/></svg>
```

### sensor.svg · Datos & AI

https://brand.magoya.com/assets/icons/sensor.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="5" cy="19" r="1.5"/><path d="M4 11a9 9 0 019 9M4 4a16 16 0 0116 16"/></svg>
```

### server.svg · Plataforma & código

https://brand.magoya.com/assets/icons/server.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="7" rx="1.5"/><rect x="3" y="13" width="18" height="7" rx="1.5"/><path d="M7 7.5h.01M7 16.5h.01"/></svg>
```

### share.svg · Comunicación & redes

https://brand.magoya.com/assets/icons/share.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="5" r="2.5"/><circle cx="18" cy="19" r="2.5"/><path d="M8.2 10.8l7.6-4.6M8.2 13.2l7.6 4.6"/></svg>
```

### soil.svg · Agro

https://brand.magoya.com/assets/icons/soil.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18M3 11h12M18 11h3M3 16h6M12 16h9M3 21h18"/></svg>
```

### sprout.svg · Agro

https://brand.magoya.com/assets/icons/sprout.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21v-8M12 13C12 9 9 7 4 7c0 5 3 6 8 6zM12 11c0-4 3-6 8-6 0 5-3 6-8 6z"/></svg>
```

### star.svg · Sistema / UI

https://brand.magoya.com/assets/icons/star.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.7 5.8 6.3.8-4.6 4.3 1.2 6.1L12 17l-5.6 3 1.2-6.1L3 9.6l6.3-.8z"/></svg>
```

### sun.svg · Agro

https://brand.magoya.com/assets/icons/sun.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/></svg>
```

### target.svg · Negocio

https://brand.magoya.com/assets/icons/target.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg>
```

### tractor.svg · Agro

https://brand.magoya.com/assets/icons/tractor.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="7" cy="17" r="3"/><circle cx="17" cy="17" r="2"/><path d="M10 17h5M4 14V8h7l2 5h6v4M9 8V4h4"/></svg>
```

### video.svg · Comunicación & redes

https://brand.magoya.com/assets/icons/video.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3"/></svg>
```

### x.svg · Sistema / UI

https://brand.magoya.com/assets/icons/x.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
```

## Íconos agro

Mismo trazo y mismo uso que los íconos del sistema.

### alerta-lote.svg

https://brand.magoya.com/assets/studio/icons/agro/alerta-lote.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4l9 16H3zM12 10v4M12 17h.01"/></svg>
```

### chat-ia.svg

https://brand.magoya.com/assets/studio/icons/agro/chat-ia.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M8 9h8M8 13h5M18 4a3 3 0 0 1 3 3v8a3 3 0 0 1-3 3h-5l-5 3v-3H6a3 3 0 0 1-3-3V7a3 3 0 0 1 3-3zM12 2l.7 1.8L14.5 4.5l-1.8.7L12 7l-.7-1.8L9.5 4.5l1.8-.7z"/></svg>
```

### dron.svg

https://brand.magoya.com/assets/studio/icons/agro/dron.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M6 6l3 3M18 6l-3 3M6 18l3-3M18 18l-3-3M4 4m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0M20 4m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0M4 20m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0M20 20m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0M9 9h6v6H9z"/></svg>
```

### escaneo.svg

https://brand.magoya.com/assets/studio/icons/agro/escaneo.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8V6a2 2 0 0 1 2-2h2M16 4h2a2 2 0 0 1 2 2v2M20 16v2a2 2 0 0 1-2 2h-2M8 20H6a2 2 0 0 1-2-2v-2M4 12h16"/></svg>
```

### gota.svg

https://brand.magoya.com/assets/studio/icons/agro/gota.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l4.5 6.5a5.5 5.5 0 1 1-9 0z"/></svg>
```

### grafico.svg

https://brand.magoya.com/assets/studio/icons/agro/grafico.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19h16M7 16V9M12 16V5M17 16v-4"/></svg>
```

### hoja.svg

https://brand.magoya.com/assets/studio/icons/agro/hoja.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 21c.5-4.5 2.5-8 7-10M9 18c6.2 0 10-3.5 10-10c0-.7-.1-1.4-.2-2c-2 1.3-4 1.5-7 2c-3.7.6-5.8 2.7-5.8 6c0 1.6.6 3 1.5 4z"/></svg>
```

### lote.svg

https://brand.magoya.com/assets/studio/icons/agro/lote.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 5l6-2l6 2l6-2v14l-6 2l-6-2l-6 2zM9 3v16M15 5v16"/></svg>
```

### mapa-pin.svg

https://brand.magoya.com/assets/studio/icons/agro/mapa-pin.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-6-5.5-6-10a6 6 0 1 1 12 0c0 4.5-6 10-6 10zM12 11m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/></svg>
```

### nube-lluvia.svg

https://brand.magoya.com/assets/studio/icons/agro/nube-lluvia.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M7 16a4 4 0 1 1 .5-7.97A5.5 5.5 0 0 1 18 9.5a3.5 3.5 0 0 1-.5 6.5H7zM8 19l-1 2M12 19l-1 2M16 19l-1 2"/></svg>
```

### reloj-campana.svg

https://brand.magoya.com/assets/studio/icons/agro/reloj-campana.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0M12 7v5l3 2"/></svg>
```

### satelite.svg

https://brand.magoya.com/assets/studio/icons/agro/satelite.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3.707 6.293l2.586-2.586a1 1 0 0 1 1.414 0l5.586 5.586a1 1 0 0 1 0 1.414l-2.586 2.586a1 1 0 0 1-1.414 0l-5.586-5.586a1 1 0 0 1 0-1.414zM6 10l-3 3l3 3l3-3M10 6l3-3l3 3l-3 3M12 12l1.5 1.5M14.5 17a2.5 2.5 0 0 0 2.5-2.5M14.5 21a6.5 6.5 0 0 0 6.5-6.5"/></svg>
```

### semilla.svg

https://brand.magoya.com/assets/studio/icons/agro/semilla.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21v-6M12 15a6 6 0 0 1 6-6h2v1a6 6 0 0 1-6 6zM12 15a5 5 0 0 0-5-5H6v1a5 5 0 0 0 5 5z"/></svg>
```

### sensor.svg

https://brand.magoya.com/assets/studio/icons/agro/sensor.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 12m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0M8.5 8.5a5 5 0 0 0 0 7M15.5 15.5a5 5 0 0 0 0-7M5.7 5.7a9 9 0 0 0 0 12.6M18.3 18.3a9 9 0 0 0 0-12.6"/></svg>
```

### sol.svg

https://brand.magoya.com/assets/studio/icons/agro/sol.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 12m-4 0a4 4 0 1 0 8 0a4 4 0 1 0 -8 0M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4M18.4 5.6L17 7M7 17l-1.4 1.4"/></svg>
```

### tractor.svg

https://brand.magoya.com/assets/studio/icons/agro/tractor.svg

viewBox 0 0 24 24 · SIN ancho ni alto propios: el tamaño se da por CSS (`width` y `height`), o no se ve

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0M19 17m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0M7 14v-6h4l2 5M13 8h4l2 6M4 8h3"/></svg>
```
