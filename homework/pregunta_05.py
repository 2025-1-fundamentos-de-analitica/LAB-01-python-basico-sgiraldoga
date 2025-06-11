"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    conteo_max_min = {}
    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split('\t')
            letra = partes[0].strip()
            valor = int(partes[1])
            if letra not in conteo_max_min:
                conteo_max_min[letra] = [valor, valor]
            else:
                conteo_max_min[letra][0] = max(conteo_max_min[letra][0], valor)
                conteo_max_min[letra][1] = min(conteo_max_min[letra][1], valor)
    
    return sorted((letra, maximo, minimo) for letra, (maximo, minimo) in conteo_max_min.items())
