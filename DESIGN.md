---
name: Renzo Mirabella · Expediente
description: Portfolio de análisis de datos armado como un expediente de la administración pública argentina.
colors:
  caratula: "#8fc1de"
  caratula-tinta: "#10283a"
  caratula-borde: "#5f97b8"
  papel: "#f4f5f2"
  foja: "#fbfbf9"
  rayado: "#cddde6"
  tinta: "#17171a"
  tinta-suave: "#45484d"
  sello: "#4a2f91"
  sello-fondo: "#e9e4f5"
  chart-violeta: "#7457d0"
  chart-celeste: "#4f9cc9"
  chart-gris: "#8a8d92"
  chart-texto: "#7a7972"
typography:
  display:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.6rem, 5.8vw, 5.4rem)"
    fontWeight: 850
    lineHeight: 0.92
    letterSpacing: "-0.005em"
    fontVariation: "'wdth' 68"
  headline:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.1rem, 4.6vw, 3.9rem)"
    fontWeight: 850
    lineHeight: 0.95
    letterSpacing: "-0.01em"
    fontVariation: "'wdth' 72"
  title:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.85rem"
    fontWeight: 850
    lineHeight: 1.05
    letterSpacing: "-0.01em"
    fontVariation: "'wdth' 80"
  title-foja:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.45rem"
    fontWeight: 800
    lineHeight: 1.08
    fontVariation: "'wdth' 78"
  subtitle:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 800
    letterSpacing: "0.02em"
  body:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
    fontFeature: "'tnum'"
  lead:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 700
    letterSpacing: "0.12em"
  nav:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 650
    letterSpacing: "0.06em"
  tipeado:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: "1.05rem"
    fontWeight: 400
  tipeado-sm:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: "0.9rem"
    fontWeight: 700
rounded:
  none: "0"
  broche: "50%"
spacing:
  pauta-half: "0.875rem"
  pauta: "1.75rem"
  pauta-1-5: "2.625rem"
  pauta-2: "3.5rem"
  pauta-2-5: "4.375rem"
  pauta-3: "5.25rem"
  lateral: "clamp(1rem, 5vw, 4.5rem)"
components:
  button-primary:
    backgroundColor: "{colors.tinta}"
    textColor: "{colors.caratula}"
    rounded: "{rounded.none}"
    padding: "0.85rem 1.4rem"
  button-primary-hover:
    backgroundColor: "{colors.sello}"
    textColor: "{colors.papel}"
  enlace-campo:
    textColor: "{colors.tinta}"
  campo:
    typography: "{typography.label}"
    padding: "0.45rem 0"
  foja:
    backgroundColor: "{colors.foja}"
    textColor: "{colors.tinta}"
    rounded: "{rounded.none}"
    padding: "1rem 1.5rem 1.2rem 0"
  ficha:
    backgroundColor: "{colors.foja}"
    typography: "{typography.tipeado}"
    rounded: "{rounded.none}"
    padding: "0.5rem 1rem 0.75rem"
  libro-fila:
    textColor: "{colors.tinta}"
    padding: "1.75rem 1rem 1.75rem 0"
  nav-link:
    textColor: "{colors.tinta}"
    typography: "{typography.nav}"
  nav-link-active:
    textColor: "{colors.sello}"
  navbar:
    backgroundColor: "{colors.caratula}"
    textColor: "{colors.tinta}"
    padding: "0.6rem 0"
---

# Design System: Renzo Mirabella · Expediente

## Overview

**Creative North Star: "El Expediente"**

Cada página es una carpeta de la administración pública argentina: una carátula de cartulina celeste con campos de formulario, fojas de papel oficio rayado para la lectura, tinta casi negra y un único acento violeta de Mesa de Entradas. El sistema no decora con el expediente: lo usa como estructura. Las secciones se numeran como fojas («Fs. 1», «Fs. 2»), los metadatos son campos tipeados a máquina, los proyectos se registran en un libro de entradas y cada carátula declara su medida (el n del dato).

La densidad es la de un formulario: filetes de tinta de 1,5 px arman las filas, la pauta del papel oficio (1,75 rem) marca el ritmo vertical y las superficies son planas, con esquinas rectas. La voz tipográfica se reparte en dos oficios: la grotesca condensada Archivo en mayúsculas para lo impreso (Asuntos, títulos, rótulos) y Courier Prime para lo que alguien tipeó (números de expediente, fechas, n, fuentes, herramientas). El modo oscuro es la misma carpeta de noche: cartulina azul petróleo, papel grafito, sello lila; solo cambian los colores, nunca las reglas.

No hay animaciones de entrada ni figuras que se muevan solas. Las fojas apiladas se corren al hover y al foco. Todo lo demás está quieto.

**Key Characteristics:**
- Carátula celeste a ancho completo en cada página, con campos de formulario y Asunto en grotesca condensada enorme.
- Papel oficio con rayado sólido (`rayado`) como trama de fondo en fojas, fichas y notas al margen.
- Un solo acento cromático en la interfaz: el violeta del sello.
- Dos voces tipográficas con roles fijos: impreso (Archivo) y tipeado (Courier Prime).
- Esquinas rectas y filetes de tinta en lugar de tarjetas, sombras y radios.
- Claro y oscuro desde las mismas variables `$exp-*`.

## Colors

Una disciplina de escritorio de oficina: cartulina, papel, tinta y un violeta de oficina. Los grises salen de tokens sólidos, no de transparencias.

### Primary
- **Violeta de Mesa de Entradas** (`sello`): el único acento de la interfaz. Enlaces, el número de foja en el margen, el número de expediente en el libro de entradas, la medida de cada foja, los títulos de «Cómo trabajo», el ítem activo del menú y del índice, el contorno de foco y la selección de texto. En oscuro pasa a lila (#b9a5f3).
- **Violeta lavado** (`sello-fondo`): fondo tenue del violeta; hoy lo usan las caras iluminadas de las figuras isométricas. En oscuro, #2a2340.

### Secondary
- **Cartulina Celeste** (`caratula`): el suelo de toda carátula, la barra de navegación, el cierre de la portada y la tapa del fichero en las figuras. También es el color del texto del botón tinta. No es un acento: es superficie. En oscuro, azul petróleo (#173447).
- **Tinta de Cartulina** (`caratula-tinta`): texto secundario sobre la cartulina (bajada de la portada y descripción de la carátula). En oscuro, #c9deeb.
- **Borde de Cartulina** (`caratula-borde`): el aro de los dos agujeros del broche sobre el borde izquierdo de la portada. En oscuro, #0e2230.

### Neutral
- **Papel de Lectura** (`papel`): fondo de página, pie y el centro de los agujeros del broche. En oscuro, papel grafito (#1e2023).
- **Hoja Suelta** (`foja`): fondo de fojas apiladas, ficha técnica, notas al margen, bloques de código y placas de figura; apenas más clara que el papel para que la hoja se despegue. En oscuro, #26292d.
- **Pauta de Oficio** (`rayado`): el renglón del papel oficio, los divisores secundarios (columnas de «Cómo trabajo», celdas de tabla, borde de código). En oscuro, #343a41.
- **Tinta** (`tinta`): texto, filetes de 1,5 px, fondo del botón principal. En oscuro, #ecebe6.
- **Tinta Gastada** (`tinta-suave`): texto secundario (bajadas de foja, descripciones, índice, pie, código desplegable). En oscuro, #b3b5b8.

### Paleta de gráficos
Vive en el Python de cada proyecto (`COLORES`, `AZUL`, `NARANJA`, `GRIS`) y en `_figuras/miniaturas.py`; no lee las variables del sitio.
- **Violeta de Gráfico** (`chart-violeta`): serie principal (`AZUL`), categoría «restaurante», autores distintos. Es el sello aclarado para leerse sobre claro y oscuro.
- **Celeste de Gráfico** (`chart-celeste`): categoría «bar» en mapas y barras.
- **Gris de Gráfico** (`chart-gris`): serie de comparación (`NARANJA` en Instagram, categoría «café»).
- **Gris de Ejes** (`chart-texto`): color de texto de plotly (`GRIS`).
- El mapa de calor recorre el violeta del sello: #d9d1f1 → #9f8ce0 → `chart-violeta` → `sello` → `tinta`.

### Named Rules
**The One Stamp Rule.** En la interfaz, el violeta del sello es el único color con intención: marca lo certificado, lo numerado y lo navegable. La cartulina celeste es suelo, nunca acento.

**The Solid Grays Rule.** Todo texto atenuado usa `tinta-suave` o `caratula-tinta`, y todo divisor tenue usa `rayado`. Ningún texto de la interfaz se atenúa con `opacity` ni con alfa.

**The Same Folder Rule.** El modo oscuro solo redefine las variables `$exp-*` en `styles-dark.scss`. Una regla nueva se escribe una vez en `styles.scss` con `var(--…)` y funciona en los dos temas.

## Typography

**Display Font:** Archivo (variable, wdth 62–125, wght 400–900; con Helvetica Neue, Arial)
**Body Font:** Archivo
**Label/Mono Font:** Courier Prime (con Courier New)

**Character:** Una grotesca de formulario oficial, condensada y muy negra para lo impreso, contra una máquina de escribir para lo que se completó a mano. La pareja es la de cualquier carátula de expediente.

### Hierarchy
- **Display** (850, clamp(2.6rem, 5.8vw, 5.4rem), 0.92; ancho 68 %, mayúsculas, máx. 17ch): el Asunto de la portada, uno solo por página.
- **Headline** (850, clamp(2.1rem, 4.6vw, 3.9rem), 0.95; ancho 72 %, mayúsculas, máx. 22ch): el título de la carátula de cada página.
- **Title** (850, 1.85rem, 1.05; ancho 80 %, mayúsculas): cada h2 numerado como foja, «Cómo trabajo». El cierre de la portada usa la misma voz a clamp(1.6rem, 3.4vw, 2.6rem).
- **Título de foja** (800, 1.45rem, 1.08; ancho 78 %, mayúsculas): títulos de proyecto en las fojas apiladas; 1.6rem y 850 en el libro de entradas; 1.5rem y ancho 75 % en violeta para los criterios.
- **Subtitle** (800, 1.2rem, +0.02em, mayúsculas): h3 dentro de la lectura.
- **Body** (400, 1.0625rem, 1.65; cifras tabulares; máx. 70ch): lectura. `text-wrap: pretty` en párrafos, `balance` en títulos.
- **Lead** (400, 1.2rem, 1.55; máx. 36rem): bajada de portada; 1.15rem en la descripción de carátula.
- **Label** (700, 0.75rem, +0.12em, mayúsculas): rótulo de campo («Expte. N.º», «Iniciador»), encabezados de tabla (750, +0.1em), título del índice (750, +0.14em), rótulos de la ficha (750, 0.72rem).
- **Nav** (650, 0.875rem, +0.06em, mayúsculas): menú. El botón usa 800 a 1.05rem; el enlace de campo, 700 a 0.95rem.
- **Tipeado** (Courier Prime 400, 1.05rem): valor de campo, ficha (0.98rem / 1.5rem), rubros (0.9rem), pie (0.85rem). En 700 y violeta para números de foja, expediente y medida.

### Named Rules
**The Printed and Typed Rule.** Archivo es lo impreso del formulario (rótulos, Asuntos, títulos, botones); Courier Prime es lo que se completó (expedientes, fechas, n, fuentes, herramientas, «Fs. N»). Un dato nunca va en Archivo si en un expediente real lo hubieran tipeado.

**The Condensed Asunto Rule.** Todo título de nivel h2 o mayor va en mayúsculas, peso 800–850 y ancho condensado entre 68 % y 80 %; cuanto más grande, más condensado.

## Layout

Bandas a ancho completo (carátula, «Cómo trabajo», cierre) con un interior de 1400 px como máximo y margen lateral `lateral`. La lectura usa la columna de cuerpo de Quarto con el índice de fojas a la derecha; el número «Fs. N» de cada h2 cuelga en el margen izquierdo, a 1rem del título.

El ritmo vertical entre bloques es múltiplo de la `pauta` (1,75rem): media pauta sobre las fojas, una pauta bajo los campos, 1,5 bajo la ficha y sobre h3, 2,5 sobre cada h2 de foja, 3 sobre «Cómo trabajo». Los rellenos internos de componentes (1rem, 1.5rem) no siguen la pauta.

- **Portada:** grilla de dos columnas 1.55fr / 1fr con 2 pautas de separación; texto a la izquierda, fojas apiladas a la derecha, centradas en vertical.
- **Campos de formulario:** filas de rótulo de 8.5rem y valor, alineadas a la línea de base.
- **Cómo trabajo:** cuatro columnas separadas por divisores `rayado`.
- **Ficha técnica:** dos columnas de celdas con filete.
- **Hasta 991.98px:** la portada pasa a una columna, «Cómo trabajo» pasa a dos columnas y el «Fs. N» se ubica antes del título en lugar del margen.
- **Hasta 575.98px:** desaparecen los agujeros del broche, los campos apilan rótulo sobre valor, las fojas se enderezan y se separan 0.5rem, «Cómo trabajo» y la ficha pasan a una columna y cada asiento del libro de entradas se vuelve una ficha de dos columnas con el Asunto debajo.

## Elevation & Depth

Plano por defecto: la profundidad la dan los filetes de tinta, el cambio de papel (`papel` → `foja`) y la trama del rayado. La única pieza que se levanta es la foja suelta de la pila de la portada, que tiene la sombra de una hoja real y se despega más al hover. Los agujeros del broche tienen una sombra interna para leerse como perforación. Las notas al margen y las placas de figura anulan explícitamente las sombras del framework y del kit.

### Shadow Vocabulary
- **Hoja en pila** (`box-shadow: 0 2px 0 -1px var(--caratula), 0 8px 18px -10px rgba(0,0,0,0.4)`): foja apilada en reposo; el primer término es el canto de la hoja de abajo.
- **Hoja levantada** (`box-shadow: 0 2px 0 -1px var(--caratula), 0 18px 30px -14px rgba(0,0,0,0.5)`): foja en hover o foco, junto con `translate(-0.5rem, -0.35rem)`.
- **Perforación** (`box-shadow: inset 0 1px 2px rgba(0,0,0,0.25)`): agujeros del broche.

### Named Rules
**The Loose Sheet Rule.** Solo una hoja suelta proyecta sombra. Recuadros, notas, tablas, código y figuras se apoyan sobre el papel con un filete, sin sombra.

## Shapes

Esquinas rectas en todo (`$border-radius: 0`): botones, fojas, fichas, notas, tablas, placas. La única excepción sale de un objeto físico: los agujeros redondos del broche. Las formas se trazan con el **filete** (`--filete: 1.5px solid var(--tinta)`): bordes de campo, de navegación, de carátula, de foja, de ficha y de tabla. Los divisores secundarios son de 1px en `rayado` o, en el libro de entradas, 1px en `tinta`.

Las fojas apiladas llevan un margen de foliado: una línea vertical violeta de 1px a 3.75rem del borde izquierdo, sobre el rayado de pauta. Cada hoja de la pila se corre 1.25rem hacia la izquierda y gira entre −0.8° y 0.6°.

## Components

### Buttons
Tinta pesada, como un sello de goma negro.
- **Shape:** esquinas rectas (0), filete de tinta.
- **Primary:** fondo `tinta`, texto `caratula`, 800 mayúsculas a 1.05rem con +0.06em, relleno 0.85rem 1.4rem, flecha SVG enmascarada en `currentColor` después del texto.
- **Hover / Focus:** fondo y borde pasan a `sello`, texto a `papel`; la flecha avanza 4px. Transición 0.2s con `--salida`. Foco: contorno de 2px en `sello` a 3px.
- **Enlace de campo:** acción secundaria junto al botón; texto `tinta` subrayado, 700 mayúsculas a 0.95rem.

### Chips (rubros)
- **Style:** sin fondo ni borde: lista en línea en Courier Prime 0.9rem, cada ítem precedido por un casillero cuadrado de 0.7em con una cruz trazada en `currentColor`, como un formulario tildado a mano.
- **State:** estáticos; no filtran.

### Cards / Containers (fojas apiladas)
- **Corner Style:** rectas.
- **Background:** `foja` con rayado de pauta y margen de foliado violeta.
- **Shadow Strategy:** Hoja en pila / Hoja levantada (ver Elevation & Depth).
- **Border:** filete.
- **Internal Padding:** 1rem 1.5rem 1.2rem, sin relleno izquierdo (lo ocupa la columna de 4.25rem del «Fs. N»).
- **Contenido:** «Fs. N» tipeado en violeta, expediente tipeado en `tinta-suave`, título de foja, bajada de dos líneas como máximo y medida tipeada en violeta. Al hover el título se subraya con 2px.

### Inputs / Fields (campos de formulario)
No hay campos editables; el «campo» es la fila de datos de la carátula.
- **Style:** filete superior en la lista y filete inferior en cada fila; rótulo en Label, valor en Tipeado; relleno 0.45rem 0.
- **Ficha técnica:** la misma idea en grilla de celdas con filete y renglones de 1.5rem en `rayado`.

### Navigation
- **Style:** barra en `caratula` con filete inferior; marca en 800 mayúsculas, ancho 80 %, 1.15rem; enlaces en Nav.
- **Default / Hover / Active:** `tinta` en reposo; `sello` subrayado a 0.4em en hover y en la página actual.
- **Índice de fojas:** título «Fojas» en Label con filete; ítems numerados en Courier Prime violeta; activo en `sello` 700; sin barra lateral.
- **Mobile:** menú hamburguesa de Bootstrap sobre la misma barra.

### Carátula
La cabecera de cada página (`_parciales/title-block.html`): banda `caratula` con filete inferior; campos opcionales «Expte. N.º», «Fecha», «Medida» (máx. 30rem), título en Headline, descripción en `caratula-tinta` y rubros. En la portada la reemplaza la banda `.portada` con los agujeros del broche.

### Libro de entradas
Registro de proyectos en tabla: filetes arriba y abajo, encabezados en Label, filas separadas por 1px de `tinta` con una pauta de relleno vertical. Columnas: expediente (tipeado, violeta, 700), Asunto (título de foja en 850, bajada en `tinta-suave` a 60ch, rubros), medida y fecha tipeadas.

### Notas al margen, tablas y código
- **Notas (callouts):** recuadro con filete, fondo `foja` con rayado de pauta, sin barra de color, sin ícono, sin sombra.
- **Tablas:** fondo transparente, filetes arriba y abajo, encabezado en Label con filete, celdas divididas en `rayado`, cifras tabulares.
- **Código:** fondo `foja`, borde de 1px en `rayado`; el resumen desplegable en 700 mayúsculas a 0.8rem en `tinta-suave`.

### Figuras isométricas
Generadas con el kit anatomy (`_figuras/kit/`) y mapeadas a los tokens del sitio por el bloque `.iso`: caras en blanco (grafito en oscuro), sombras laterales mezclando `tinta` (negro en oscuro) con `foja`, iluminado en `sello` / `sello-fondo`, mar en `caratula` mezclado con `foja`, tapa del fichero en cartulina. La placa lleva filete y no tiene sombra; los rótulos van en Courier Prime con espaciado amplio.

### Gráficos
Plotly con fondo transparente, Archivo 13px en `chart-texto`, sin grilla vertical, coma decimal y punto de miles, leyenda horizontal arriba a la izquierda. Folium con marcadores rellenos por categoría y borde blanco.

## Do's and Don'ts

### Do:
- **Do** abrir cada página con una carátula celeste y un solo Asunto.
- **Do** tipear en Courier Prime todo número de expediente, fecha, n, fuente y herramienta; rotular en Archivo 700 mayúsculas a 0.75rem con +0.12em.
- **Do** separar bloques con múltiplos de la pauta (1,75rem) y trazar filas con el filete de 1.5px en tinta.
- **Do** declarar la medida (el n) de cada proyecto en la carátula, en la foja y en el libro de entradas.
- **Do** reservar el violeta del sello para lo certificado, lo numerado, lo enlazado y lo activo.
- **Do** escribir toda regla nueva en `styles.scss` con `var(--…)` y redefinir solo las variables `$exp-*` en `styles-dark.scss`.
- **Do** mantener todo quieto: sin animaciones de entrada ni figuras que se muevan solas.

### Don't:
- **Don't** redondear esquinas fuera de los agujeros del broche.
- **Don't** agregar sombras a recuadros, notas, tablas, figuras o botones; solo la hoja suelta se levanta.
- **Don't** atenuar texto con `opacity` o alfa; usar `tinta-suave` o `caratula-tinta`.
- **Don't** sumar un segundo acento de interfaz ni usar la cartulina celeste como color de texto o de enlace.
- **Don't** volver a poner barra de color ni ícono en las notas al margen.
- **Don't** mostrar títulos de nivel h2 o mayor en minúscula, sin condensar o por debajo de peso 800.
