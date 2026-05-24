"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


"""
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

"""
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os

import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt
import pandas as pd


def pregunta_01():
    # Configuración de colores, orden de pintado y grosores de línea
    color_por_medio = {
        "Television": "dimgrey",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey",
    }

    zorder_por_medio = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    grosor_por_medio = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 3,
        "Radio": 2,
    }

    # Cargar datos
    ruta_entrada = "files/input/news.csv"
    df = pd.read_csv(ruta_entrada, index_col=0)

    # Preparar carpeta de salida
    carpeta_salida = "files/plots"
    os.makedirs(carpeta_salida, exist_ok=True)

    plt.figure()

    # Líneas principales
    for medio in df.columns:
        plt.plot(
            df[medio],
            label=medio,
            color=color_por_medio[medio],
            zorder=zorder_por_medio[medio],
            linewidth=grosor_por_medio[medio],
        )

    plt.title("How people get their news", fontsize=16)

    eje = plt.gca()
    eje.spines["top"].set_visible(False)
    eje.spines["left"].set_visible(False)
    eje.spines["right"].set_visible(False)
    eje.get_yaxis().set_visible(False)

    primer_anio = df.index[0]
    ultimo_anio = df.index[-1]

    # Puntos y etiquetas en el año inicial
    for medio in df.columns:
        valor_inicial = df.loc[primer_anio, medio]

        plt.scatter(
            x=primer_anio,
            y=valor_inicial,
            color=color_por_medio[medio],
            zorder=zorder_por_medio[medio],
        )

        plt.text(
            primer_anio - 0.2,
            valor_inicial,
            f"{medio} {valor_inicial}%",
            ha="right",
            va="center",
            color=color_por_medio[medio],
        )

    # Puntos en el año final
    for medio in df.columns:
        valor_final = df.loc[ultimo_anio, medio]
        plt.scatter(
            x=ultimo_anio,
            y=valor_final,
            color=color_por_medio[medio],
        )

    # Guardar imagen
    ruta_salida = os.path.join(carpeta_salida, "news.png")
    plt.savefig(ruta_salida, bbox_inches="tight")
    plt.close()

    return ruta_salida


if __name__ == "__main__":
    pregunta_01()
