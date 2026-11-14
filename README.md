# Cafetería Neira · propuesta de web

Propuesta de web para la **Cafetería Neira** (C. Albia de Castro, 10 · Lobete, Logroño), hecha por **CRS Digital**.

## Qué incluye

- **Inicio**: la fachada pasa de día a noche al deslizar y se enciende el logo en neón (vídeo horizontal en ordenador y vertical en móvil).
- **Carta**: la carta se abre como un libro y dentro está el menú del día; después, la carta completa por secciones.
- **Historia**: más de 50 años en Lobete y la reapertura en 2026.
- **Contacto**: dirección, horario, teléfono e Instagram.
- **Reservas**: formulario en 4 pasos que abre WhatsApp con el mensaje ya escrito.
- **Aviso legal y privacidad**: los datos marcados en amarillo (titular, NIF, correo) están pendientes de rellenar.
- Indicador de **abierto / cerrado** según el horario real.
- Transición con el logo de neón al cambiar de página y menú de tres puntos en el móvil.

## Cómo verla

Publicada con GitHub Pages en https://crsdigitalizacion.github.io/cafeteria-neira/

La web es `index.html` más la carpeta `a/` (fotos y fotogramas de los vídeos). El móvil solo descarga los fotogramas del vídeo vertical y el ordenador los del horizontal, así que carga mucho más rápido que con todo metido en un solo archivo.

Al compartir el enlace (WhatsApp, redes) se muestra `og.jpg` como vista previa, y `favicon.png` / `apple-touch-icon.png` son los iconos de la pestaña y del móvil. La página incluye los datos del bar para Google (horario, dirección, teléfono).

## Cómo editarla

Los archivos de trabajo están en `src/`:

- `plantilla.html`: el diseño y el código (las imágenes van como marcadores `{{nombre}}`).
- `head.html`: la cabecera de la página (título, descripción, vista previa al compartir e iconos).
- `menu-del-dia.json`: el menú del día.
- `img/`, `frames/` (vídeo del ordenador) y `framesm/` (vídeo del móvil).

Después de cambiar algo, ejecuta dentro de `src/`:

```
python3 build.py
```

y se vuelven a generar `index.html` y la carpeta `a/`.

> El menú del día de la carta está escrito en `plantilla.html`. Para cambiarlo cada semana, edita `menu-del-dia.json` y pide que se vuelva a montar la pizarra con esos datos.
