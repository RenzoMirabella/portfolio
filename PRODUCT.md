# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

- **Reclutadores y RR.HH.** que cubren búsquedas de analista de datos (jr/ssr) en empresas de Buenos Aires o remotas. Llegan desde un CV o LinkedIn, miran poco tiempo y deciden si contactar.
- **Equipos de sector público, ONGs y consultoras** que trabajan con datos sociales, urbanos o de políticas públicas. Abren un proyecto y quieren ver criterio: fuentes, validación, limitaciones.

## Product Purpose

Portfolio personal de Renzo Mirabella, estudiante avanzado de Sociología (UNMdP, tesis en 2027) con Diplomatura en Ciencia de Datos (UTN). Muestra proyectos de análisis de datos propios, con datos relevados por él, para conseguir entrevistas laborales. Éxito: que el visitante entienda en segundos qué hace Renzo, abra un proyecto y lo contacte.

## Positioning

Combina trabajo de campo sociológico con análisis cuantitativo: relevamientos propios (scraping), cruce con el territorio (barrios, mapas) y validación honesta de los métodos (anotación a mano, intervalos de confianza, cobertura declarada, limitaciones explícitas). No es un portfolio de dashboards genéricos con datasets de Kaggle.

## Operating Context

- Sitio estático hecho con Quarto (`_quarto.yml`), páginas `.qmd` con Python (pandas, plotly, folium, itables) congeladas en `_freeze/`.
- Publicación en GitHub Pages vía GitHub Actions (`.github/workflows/publish.yml`).
- Cada proyecto es una carpeta en `proyectos/` con `index.qmd`, `miniatura.png` y `datos/`. `proyectos/_plantilla/` es la plantilla para proyectos nuevos y el sistema tiene que seguir funcionando cuando se agreguen más.
- Modo claro y oscuro según preferencia del visitante.

## Capabilities and Constraints

- Idioma: español rioplatense (voseo), `lang: es`, coma decimal y punto de miles.
- Los gráficos plotly y mapas folium se generan en Python; su estilo vive en la función `estilo()` de cada proyecto.
- Enlaces: GitHub `RenzoMirabella`, LinkedIn `renzomirabella`, sitio `renzomirabella.github.io/portfolio`.
- CV descargable: todavía no existe (hay un comentario preparado en `sobre-mi.qmd`).

## Evidence on Hand

- Proyecto «Locales gastronómicos de Mar del Plata»: 1.261 locales relevados de Google Maps, 124 polígonos de barrios, mapas, rankings y tabla (`proyectos/locales-gastronomicos-mdp/`).
- Proyecto «Qué se comenta en la cuenta de Instagram del presidente»: 32.482 comentarios de 69 posts, validación del clasificador con 378–450 casos anotados a mano (`proyectos/comentarios-instagram/`).
- Formación, experiencia e idiomas en `sobre-mi.qmd`.
- No hay testimonios, clientes, empleadores de datos ni métricas de impacto: no inventarlos.

## Product Principles

1. Los proyectos son la prueba: todo lo demás está para llevar a ellos.
2. Mostrar el método, no solo el resultado: fuentes, cobertura y limitaciones a la vista.
3. Legible en 30 segundos para RR.HH., profundo para quien lee la metodología.
4. Fácil de mantener por una sola persona: agregar un proyecto = copiar la plantilla.
5. Privacidad y honestidad con los datos (agregados, sin transcribir comentarios, sin exagerar).

## Accessibility & Inclusion

Contraste AA en claro y oscuro, navegación por teclado, gráficos con texto que explique la conclusión (no solo color).
