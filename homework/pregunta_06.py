"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    conteo_max_min = {}
    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split('\t')
            tuplas = partes[4].strip().split(',')
            for tupla in tuplas:
                clave, valor_str = tupla.split(':')
                valor = int(valor_str)
                if clave not in conteo_max_min:
                    conteo_max_min[clave] = [valor, valor]
                else:
                    conteo_max_min[clave][0] = min(conteo_max_min[clave][0], valor)
                    conteo_max_min[clave][1] = max(conteo_max_min[clave][1], valor)
    
    return sorted((letra, minimo, maximo) for letra, (minimo, maximo) in conteo_max_min.items())
