# Portfolio de análisis de datos

Sitio web estático hecho con [Quarto](https://quarto.org). Los proyectos se escriben en
archivos `.qmd` con código Python, y Quarto genera las páginas con gráficos, mapas y
tablas interactivas. No hace falta base de datos ni servidor: los datos viven en
archivos CSV/GeoJSON dentro de cada proyecto.

## Estructura

```
portfolio/
├── _quarto.yml              ← configuración general (título, menú, tema)
├── index.qmd                ← portada
├── proyectos.qmd            ← listado automático de proyectos
├── sobre-mi.qmd             ← presentación, formación, contacto
├── styles.scss              ← estilos y colores del modo claro (el mundo «Expediente»)
├── styles-dark.scss         ← solo los colores del modo oscuro
├── _parciales/              ← plantillas: carátula, fojas de la portada, libro de entradas
├── _figuras/                ← figuras isométricas interactivas y miniaturas
├── PRODUCT.md, DESIGN.md    ← para quién es el sitio y cómo está diseñado
├── requirements.txt         ← librerías de Python que usa el sitio
├── .github/workflows/       ← publicación automática en GitHub Pages
└── proyectos/
    ├── _plantilla/                  ← plantilla para copiar (no se publica)
    ├── locales-gastronomicos-mdp/   ← cada proyecto es una carpeta
    │   ├── index.qmd                ← la página del proyecto
    │   ├── miniatura.png            ← imagen de la tarjeta
    │   └── datos/                   ← CSV y GeoJSON que usa la página
    └── comentarios-instagram/
```

## Primera vez: instalar

1. Instalá Quarto: https://quarto.org/docs/get-started/
2. Instalá las librerías de Python (idealmente en un entorno virtual):

   ```bash
   pip install -r requirements.txt
   ```

## Ver el sitio en tu computadora

Desde la carpeta `portfolio`:

```bash
quarto preview
```

Se abre el navegador y la página se actualiza sola cada vez que guardás un archivo.
También podés usar VS Code con la extensión de Quarto (botón "Preview").

## Agregar un proyecto

1. Copiá `proyectos/_plantilla/` y renombrala, por ejemplo `proyectos/eph-ingresos/`
   (sin guion bajo adelante).
2. Poné tus datos en `datos/` y una imagen `miniatura.png`.
3. Editá `index.qmd`. Completá `expediente` (número correlativo) y `medida` (el tamaño
   del dato): con eso se arman la carátula, la foja
   de la portada y la fila del libro de entradas en Proyectos.

Cada `##` del proyecto es una foja: el número en el margen se pone solo.

## Figuras interactivas

Las figuras isométricas de cada proyecto se generan con un script en `_figuras/` y se
insertan en la página con un div:

```markdown
::: {incluir="_figura-mesa.html"}
:::
```

Para reconstruir una figura no hace falta Node, porque Quarto trae Deno
(en Windows está en `AppData\Local\Programs\Quarto\bin\tools\x86_64\deno.exe`):

```bash
deno run -A _figuras/<nombre>/build.mjs
```

Las miniaturas de las tarjetas se regeneran desde los datos:

```bash
python _figuras/miniaturas.py
```

Si un archivo de datos es muy pesado (más de ~20 MB), conviene guardar una versión
ya resumida o en formato Parquet. Para mapas, simplificá las geometrías con
https://mapshaper.org antes de usarlas.

## Publicar en GitHub Pages (gratis)

1. Creá un repositorio en GitHub llamado `portfolio` y subí esta carpeta.
2. En el repositorio: **Settings → Actions → General → Workflow permissions** →
   elegí "Read and write permissions".
3. Hacé un push a `main`. La acción "Publicar sitio" renderiza todo y crea la rama
   `gh-pages`.
4. En **Settings → Pages**, elegí como fuente la rama `gh-pages` (carpeta `/root`).
5. El sitio queda en `https://renzomirabella.github.io/portfolio`.

## Antes de publicar

- Los enlaces de GitHub (RenzoMirabella) y LinkedIn (renzomirabella) ya están en `_quarto.yml`, `sobre-mi.qmd` y las fichas de los proyectos.
- Los mapas usan el fondo gris de Esri, porque las teselas de CARTO ahora piden API key.
- Revisá los textos de `index.qmd` y `sobre-mi.qmd`.
