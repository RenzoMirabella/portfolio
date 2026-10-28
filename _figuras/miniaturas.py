"""Regenera las miniaturas de las tarjetas (miniatura.png) con la paleta del sitio.

Se dibujan directo de los datos de cada proyecto:
    python _figuras/miniaturas.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
PAPEL = "#f4f5f2"
CELESTE = "#8fc1de"
TINTA = "#17171a"
SELLO = "#4a2f91"
COLORES = {"restaurante": "#7457d0", "bar": "#4f9cc9", "café": "#8a8d92"}


def origen(texto):
    """Metadato de procedencia que lee Impeccable (impeccable embed-prompt --scan)."""
    return {"impeccable:prompt": "Origen: dibujada con matplotlib por _figuras/miniaturas.py a partir de " + texto + ". No es imagen generada."}


def lienzo():
    fig = plt.figure(figsize=(12, 7), dpi=100, facecolor=PAPEL)
    ax = fig.add_axes([0, 0, 1, 1], facecolor=PAPEL)
    ax.set_axis_off()
    return fig, ax


def locales():
    carpeta = RAIZ / "proyectos" / "locales-gastronomicos-mdp"
    df = pd.read_csv(carpeta / "datos" / "locales_con_barrio.csv")
    df["categoria"] = df["categorias"].str.split("; ").str[0]
    fig, ax = lienzo()
    for cat, color in COLORES.items():
        sub = df[df["categoria"] == cat]
        ax.scatter(sub["lng"], sub["lat"], s=14, c=color, edgecolors="white", linewidths=0.4, zorder=3)
    ax.set_aspect(1 / 0.79)  # corrige la longitud a la latitud de Mar del Plata
    x0, x1 = df["lng"].quantile([0.01, 0.99])
    y0, y1 = df["lat"].quantile([0.01, 0.99])
    ax.set_xlim(x0 - 0.02, x1 + 0.02)
    ax.set_ylim(y0 - 0.01, y1 + 0.01)
    fig.savefig(carpeta / "miniatura.png", facecolor=PAPEL, metadata=origen("datos/locales_con_barrio.csv (1.261 locales, color por primera categoría)"))
    plt.close(fig)


def comentarios():
    carpeta = RAIZ / "proyectos" / "comentarios-instagram"
    temas = pd.read_csv(carpeta / "datos" / "temas_por_autores.csv")
    t = temas[temas["nivel"] != "tema_amplio"].sort_values("comentarios").tail(10)
    fig, ax = lienzo()
    y = range(len(t))
    ax.barh([v + 0.2 for v in y], t["comentarios"], height=0.38, color="#8a8d92")
    ax.barh([v - 0.2 for v in y], t["autores"], height=0.38, color="#7457d0")
    ax.set_xlim(0, t["comentarios"].max() * 1.08)
    ax.set_ylim(-0.8, len(t) - 0.2)
    ax.margins(x=0)
    ax.set_position([0.03, 0.06, 0.94, 0.88])
    fig.savefig(carpeta / "miniatura.png", facecolor=PAPEL, metadata=origen("datos/temas_por_autores.csv (10 temas: comentarios y autores distintos)"))
    plt.close(fig)


def informalidad():
    carpeta = RAIZ / "proyectos" / "informalidad-eph"
    s = pd.read_csv(carpeta / "datos" / "sectores_bajo_la_lupa.csv")
    colores = {"Hasta 5": "#7457d0", "6 a 40": "#4f9cc9", "Más de 40": "#8a8d92", "Sin dato": "#b9bab5"}
    fig, ax = lienzo()
    ax.axhline(41.2, color="#8a8d92", linewidth=1.2, linestyle=(0, (2, 3)), zorder=1)
    ax.scatter(s["informales (miles)"], s["tasa de informalidad (%)"], s=s["ocupados (miles)"] * 2.2,
               c=s["tamano_regla"].map(colores), edgecolors="white", linewidths=1, alpha=0.9, zorder=3)
    ax.set_xlim(-25, 450)
    ax.set_ylim(-5, 102)
    ax.set_position([0.04, 0.06, 0.92, 0.88])
    fig.savefig(carpeta / "miniatura.png", facecolor=PAPEL, metadata=origen("datos/sectores_bajo_la_lupa.csv (50 segmentos rama × tamaño: informales y tasa)"))
    plt.close(fig)


if __name__ == "__main__":
    locales()
    comentarios()
    informalidad()
    print("miniaturas regeneradas")
