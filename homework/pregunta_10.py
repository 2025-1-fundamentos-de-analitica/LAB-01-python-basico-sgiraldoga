"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    resultado = []
    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split('\t')
            letra = partes[0].strip()

            elementos_col4 = [x.strip() for x in partes[3].split(",") if x.strip()]
            count_col4 = len(elementos_col4)

            elementos_col5 = [x.strip() for x in partes[4].split(",") if x.strip()]
            count_col5 = len(elementos_col5)

            resultado.append((letra, count_col4, count_col5))
    
    return resultado
