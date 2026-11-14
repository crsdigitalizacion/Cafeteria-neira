# Cafetería Neira · propuesta de web

Propuesta de web para la **Cafetería Neira** (C. Albia de Castro, 10 · Lobete, Logroño), hecha por **CRS Digital**.

## Qué incluye

- **Inicio**: la fachada pasa de día a noche al deslizar y se enciende el logo en neón (vídeo horizontal en ordenador y vertical en móvil).
- **Carta**: la carta se abre como un libro y dentro está el menú del día; después, la carta completa por secciones.
- **Historia**: más de 50 años en Lobete y la reapertura en 2026.
- **Contacto**: dirección, horario, teléfono e Instagram.
- **Reservas**: formulario en 4 pasos que abre WhatsApp con el mensaje ya escrito.
- Indicador de **abierto / cerrado** según el horario real.
- Transición con el logo de neón al cambiar de página y menú de tres puntos en el móvil.

## Cómo verla

Abre `index.html` en el navegador. Es un único archivo con todas las imágenes dentro, así que se puede publicar tal cual (por ejemplo con GitHub Pages: *Settings → Pages → Deploy from branch → main / root*).

## Cómo editarla

Los archivos de trabajo están en `src/`:

- `plantilla.html`: el diseño y el código (las imágenes van como marcadores `{{nombre}}`).
- `menu-del-dia.json`: el menú del día.
- `img/`, `frames/` (vídeo del ordenador) y `framesm/` (vídeo del móvil).

Después de cambiar algo, ejecuta dentro de `src/`:

```
python3 build.py
```

y se vuelve a generar `index.html`.

> El menú del día de la carta está escrito en `plantilla.html`. Para cambiarlo cada semana, edita `menu-del-dia.json` y pide que se vuelva a montar la pizarra con esos datos.
