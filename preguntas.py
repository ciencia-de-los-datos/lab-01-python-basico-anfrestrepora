"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

from datetime import datetime
from collections import defaultdict

def pregunta_01():
    with open("data.csv", "r") as file:
        lista = file.readlines()
    lista = [line.replace("\n", '') for line in lista]
    lista = [line.split("\t") for line in lista]

    truck_events=lista
    colsum = [
    [row[1]] 
    for row in truck_events
    ]
    timesheet = [
    [int(field) if i_row >= 0 else field for field in row]
    for i_row, row in enumerate(colsum)
    ]
  
    suma_columna = 0
    for fila in timesheet:
        suma_columna += fila[0]
 
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return suma_columna


def pregunta_02():
    with open("data.csv", "r") as file:
        lista = file.readlines()
    lista = [line.replace("\n", '') for line in lista]
    lista = [line.split("\t") for line in lista]

    contador_letras = {}

# Contar la cantidad de registros por letra
    for fila in lista:
        letra = fila[0]  # Obtener la primera letra de cada fila
        if letra in contador_letras:
            contador_letras[letra] += 1
        else:
            contador_letras[letra] = 1
    
    lista_tuplas = sorted(contador_letras.items())

# Convertir el diccionario a una lista de tuplas y ordenar alfabéticamente
            
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """    
    return lista_tuplas


def pregunta_03():
    with open("data.csv", "r") as file:
        lista = file.readlines()
    lista = [line.replace("\n", '') for line in lista]
    lista = [line.split("\t") for line in lista]
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
 
    suma_por_letra = {}

        # Calcular la suma de la segunda columna por cada letra
    for fila in lista:
            letra = fila[0]  # Obtener la primera letra de cada fila
            valor = int(fila[1])  # Obtener el valor de la segunda columna

            if letra in suma_por_letra:
                suma_por_letra[letra] += valor
        
            else:
                suma_por_letra[letra] = valor
        
        

    resultado=sorted(suma_por_letra.items(), key=lambda x: x[0])    
  
    return resultado


def pregunta_04():
    with open("data.csv", "r") as file:
        lista = file.readlines()
    lista = [line.replace("\n", '') for line in lista]
    lista = [line.split("\t") for line in lista]
    
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    lista_original=lista
    lista_reformateada = []
    # Iteramos sobre la lista original y reformateamos las fechas
    for tupla in lista_original:
        nueva_tupla = list(tupla)  # Convertimos la tupla a lista para modificarla
        fecha_str = nueva_tupla[2]  # Obtenemos la fecha de la tercera columna

        # Reformateamos la fecha para obtener solo el año y el mes en formato YY-MM
        nueva_fecha_str = fecha_str[:7]  # Tomamos los primeros 7 caracteres (YY-MM)

        # Actualizamos la tercera columna con la nueva fecha formateada
        nueva_tupla[2] = nueva_fecha_str

        # Convertimos la lista nuevamente a tupla y la agregamos a la lista reformateada
        lista_reformateada.append(tuple(nueva_tupla))

    def contar_registros_por_mes(lista):
        registros_por_mes = defaultdict(int)

        for tupla in lista:
            fecha_str = tupla[2]  # Suponiendo que la fecha está en la tercera columna
            if fecha_str:  # Comprueba si la cadena no está vacía
                try:
                    fecha = datetime.strptime(fecha_str, '%Y-%m')
                    mes = fecha.strftime('%m')  # Obtenemos solo el mes en formato 'MM'
                    registros_por_mes[mes] += 1
                except ValueError as e:
                    print(f"Error al procesar la fecha {fecha_str}: {e}")

        # Convertir el diccionario en una lista de tuplas y ordenarla por mes
        resultado_tuplas = sorted(registros_por_mes.items())

        return resultado_tuplas

    resultado = contar_registros_por_mes(lista_reformateada)
           
    return resultado


def pregunta_05():
    with open("data.csv", "r") as file:
        lista = file.readlines()
    lista = [line.replace("\n", '') for line in lista]
    lista = [line.split("\t") for line in lista]
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    
    def valores_max_min_por_letra(datos):
        max_min_por_letra = {}

        for fila in datos:
            letra = fila[0]
            valor = int(fila[1])

            if letra not in max_min_por_letra:
                max_min_por_letra[letra] = {'max': valor, 'min': valor}
            else:
                max_min_por_letra[letra]['max'] = max(max_min_por_letra[letra]['max'], valor)
                max_min_por_letra[letra]['min'] = min(max_min_por_letra[letra]['min'], valor)

        # Ordenar el resultado en orden alfabético descendente por la letra
        resultado_ordenado = sorted([(letra, max_min_por_letra[letra]['max'], max_min_por_letra[letra]['min']) for letra in max_min_por_letra], reverse=False)

        return resultado_ordenado
    resultado = valores_max_min_por_letra(lista)   
    
    return resultado


def pregunta_06():
    with open("data.csv", "r") as file:
        lista = file.readlines()
    lista = [line.replace("\n", '') for line in lista]
    lista = [line.split("\t") for line in lista]
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    def obtener_valores_extremos(datos):
        # Creamos un diccionario para almacenar los valores extremos por clave
        valores_extremos = {}

        # Iteramos sobre los datos para procesar la columna 5
        for fila in datos:
            columna_5 = fila[4]  # Suponiendo que la columna 5 está indexada en 4
            diccionario_codificado = columna_5.split(',')  # Separamos el diccionario en elementos

            # Procesamos cada elemento del diccionario
            for elemento in diccionario_codificado:
                clave, valor_str = elemento.split(':')
                valor = int(valor_str)

                # Actualizamos los valores mínimos y máximos asociados a cada clave
                if clave not in valores_extremos:
                    valores_extremos[clave] = {'min': valor, 'max': valor}
                else:
                    valores_extremos[clave]['min'] = min(valores_extremos[clave]['min'], valor)
                    valores_extremos[clave]['max'] = max(valores_extremos[clave]['max'], valor)

        # Convertimos el diccionario a la lista de tuplas de la forma requerida
        resultado = [(clave, valores_extremos[clave]['min'], valores_extremos[clave]['max']) for clave in valores_extremos]
        # Ordenamos la lista por clave en orden ascendente
        resultado.sort()
        return resultado
    resultado = obtener_valores_extremos(lista)
    

    return resultado


def pregunta_07():
    with open("data.csv", "r") as file:
        lista = file.readlines()
    lista = [line.replace("\n", '') for line in lista]
    lista = [line.split("\t") for line in lista]
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    def asociar_letras_con_valor(datos):
        asociaciones = {}

        # Iteramos sobre los datos para construir el diccionario de asociaciones
        for fila in datos:
            valor_col2 = fila[1]  # Valor de la columna 2
            letra_col1 = fila[0]   # Letra de la columna 1

            if valor_col2 not in asociaciones:
                asociaciones[valor_col2] = [letra_col1]  # Creamos una nueva lista con la letra
            else:
                asociaciones[valor_col2].append(letra_col1)  # Agregamos la letra a la lista existente

        # Convertimos el diccionario a una lista de tuplas
        lista_tuplas = sorted([(valor, letras) for valor, letras in asociaciones.items()], key=lambda x: x[0])

        return lista_tuplas

    resultado = asociar_letras_con_valor(lista)

    return resultado


def pregunta_08():
    with open("data.csv", "r") as file:
        lista = file.readlines()
    lista = [line.replace("\n", '') for line in lista]
    lista = [line.split("\t") for line in lista]
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    def generar_lista_tuplas(datos):
        # Creamos un diccionario para almacenar las letras asociadas a cada valor de la segunda columna
        asociaciones = {}

        # Iteramos sobre los datos para construir el diccionario de asociaciones
        for fila in datos:
            letra = fila[0]   # Letra de la primera columna
            valor = fila[1]   # Valor de la segunda columna

            # Si el valor no está en el diccionario, lo inicializamos con un conjunto vacío
            if valor not in asociaciones:
                asociaciones[valor] = set()

            # Agregamos la letra al conjunto asociado al valor
            asociaciones[valor].add(letra)

        # Ordenamos las letras asociadas a cada valor y las convertimos en una lista
        for valor in asociaciones:
            asociaciones[valor] = sorted(list(asociaciones[valor]))

        # Convertimos el diccionario a una lista de tuplas y ordenamos por el valor de la segunda columna
        lista_tuplas = sorted([(valor, asociaciones[valor]) for valor in sorted(asociaciones.keys())])

        return lista_tuplas

    resultado = generar_lista_tuplas(lista)    
    return resultado


def pregunta_09():
    with open("data.csv", "r") as file:
        lista = file.readlines()
    lista = [line.replace("\n", '') for line in lista]
    lista = [line.split("\t") for line in lista]
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    def contar_registros_por_clave(datos):
        
        conteo_claves = {}

        # Iteramos sobre los datos para contar la cantidad de registros por clave de la columna 5
        for fila in datos:
            columna_5 = fila[4]  # Suponiendo que la columna 5 está indexada en 4
            pares_clave_valor = columna_5.split(',')  # Separamos los pares clave-valor

            # Iteramos sobre los pares clave-valor y contamos la cantidad de veces que aparece cada clave
            for par in pares_clave_valor:
                clave, valor = par.split(':')  # Dividimos el par clave-valor
                if clave in conteo_claves:
                    conteo_claves[clave] += 1
                else:
                    conteo_claves[clave] = 1
        
        conteo_claves_ordenado = {k: v for k, v in sorted(conteo_claves.items())}

        return conteo_claves_ordenado
    resultado = contar_registros_por_clave(lista)
    return resultado


def pregunta_10():
    with open("data.csv", "r") as file:
        lista = file.readlines()
    lista = [line.replace("\n", '') for line in lista]
    lista = [line.split("\t") for line in lista]
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    def obtener_cantidad_elementos(datos):
        resultado = []

        # Iteramos sobre los datos para obtener la cantidad de elementos de las columnas 4 y 5
        for fila in datos:
            letra = fila[0]  # Letra de la columna 1

            # Cantidad de elementos de la columna 4
            cantidad_col4 = len(fila[3].split(','))

            # Cantidad de elementos de la columna 5 (pares clave-valor)
            pares_clave_valor = fila[4].split(',')
            cantidad_col5 = len(pares_clave_valor)

            resultado.append((letra, cantidad_col4, cantidad_col5))

        return resultado

    resultado = obtener_cantidad_elementos(lista)
    return resultado


def pregunta_11():
    with open("data.csv", "r") as file:
        lista = file.readlines()
    lista = [line.replace("\n", '') for line in lista]
    lista = [line.split("\t") for line in lista]
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

    def suma_por_letra_columna4(datos):
        suma_por_letra = {}

        # Iteramos sobre los datos para calcular la suma de la columna 2 para cada letra de la columna 4
        for fila in datos:
            letras_columna4 = fila[3].split(',')  # Separamos las letras de la columna 4
            valor_columna2 = int(fila[1])  # Convertimos el valor de la columna 2 a entero

            # Iteramos sobre las letras de la columna 4 y actualizamos la suma correspondiente
            for letra in letras_columna4:
                if letra in suma_por_letra:
                    suma_por_letra[letra] += valor_columna2
                else:
                    suma_por_letra[letra] = valor_columna2

        # Ordenamos el diccionario alfabéticamente por las claves (letras)
        suma_por_letra_ordenada = {k: v for k, v in sorted(suma_por_letra.items())}

        return suma_por_letra_ordenada


    resultado = suma_por_letra_columna4(lista)    
    return resultado


def pregunta_12():
    with open("data.csv", "r") as file:
        lista = file.readlines()
    lista = [line.replace("\n", '') for line in lista]
    lista = [line.split("\t") for line in lista]
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    def suma_columna5_por_letra_columna1(datos):
        suma_por_letra = {}

        # Iteramos sobre los datos para calcular la suma de la columna 5 para cada letra de la columna 1
        for fila in datos:
            letra_columna1 = fila[0]  # Letra de la columna 1
            valores_columna5 = fila[4].split(',')  # Separamos los pares clave-valor de la columna 5

            # Iteramos sobre los pares clave-valor y sumamos los valores para la letra de la columna 1
            for par in valores_columna5:
                valor = int(par.split(':')[1])  # Obtenemos el valor de la clave-valor
                if letra_columna1 in suma_por_letra:
                    suma_por_letra[letra_columna1] += valor
                else:
                    suma_por_letra[letra_columna1] = valor
        suma_por_letra_ordenada = {k: v for k, v in sorted(suma_por_letra.items())}

        return suma_por_letra_ordenada
        


    resultado = suma_columna5_por_letra_columna1(lista)    
    return resultado
