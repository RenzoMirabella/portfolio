---
version: 1
slug: "index-qmd"
primary_target: "index.qmd"
related_targets: ["proyectos.qmd","sobre-mi.qmd","styles.scss"]
---

# Portfolio — portada, listado, Sobre mí y páginas de proyecto

Modo: Experience (portada y listado) · Read (páginas de proyecto y Sobre mí).
Audiencia: RR.HH. de búsquedas de analista de datos; equipos de sector público, ONGs y consultoras.
Acción: abrir un proyecto y contactar. Prueba: los dos proyectos con datos propios y validación.
Restricciones: Quarto + Bootstrap (SCSS), plotly/folium generados en Python, modo claro y oscuro, plantilla de proyecto reutilizable.

## Direction contract

THESIS: Cada proyecto es un expediente: carátula con un solo Asunto (la pregunta), fojas numeradas como secciones y sellos que certifican cómo se validó. Rechaza el hero + chips + grilla de tarjetas del portfolio de datos estándar.

OWN-WORLD: Cartulina celeste como suelo de carátulas, papel oficio blanco con rayado tenue para la lectura, tinta casi negra, sello violeta como único acento. Grotesca condensada en mayúsculas para Asuntos, máquina de escribir para lo «tipeado» en campos (n, fechas, fuentes), filetes de 1,5 px que forman los campos del formulario. Grises por rayado/trama, nunca opacidad. Modo oscuro: carpeta de noche, cartulina azul petróleo, papel grafito, sello lila.

STORY: El visitante entiende en una pantalla que Renzo releva sus propios datos y los valida; ve dos expedientes con su n; abre uno, lee la carátula (pregunta, fuentes, herramientas), recorre fojas y sellos, y llega al contacto.

FIRST VIEWPORT: Carátula celeste a ancho completo. Arriba, filas de campo «Expte. N.º» e «Iniciador». Asunto en grotesca condensada enorme (≈90 px desktop) ocupando 2/3 izquierdos; botón tinta «Abrir expedientes». A la derecha, las fojas de los proyectos apiladas en abanico, cada una con «Fs. N» en el margen, título y n. Sello violeta girado «Relevamiento propio» montado sobre el borde carátula/fojas.

FORM: Expediente de la administración pública argentina, candidato 5 de 7 en mi lista ordenada. seed:d48fb6b3de0570fc. Raises: módulo único de pauta (manual de armado), disciplina tonal tinta/papel/sello (escritorio 1 bit), un imperativo por hoja (afiche WPA), cada pestaña declara su medida (cantera de nubes). Interacción firma: el sello se estampa (escala + giro, una vez) al entrar en vista; las fojas del abanico se separan al hover/focus.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Decisiones abiertas

- Figuras isométricas (skill anatomy): una por proyecto, explicando el mecanismo (scraper → barrio; truncación de comentarios).
- Usuarios de GitHub/LinkedIn pendientes (TU-USUARIO).
