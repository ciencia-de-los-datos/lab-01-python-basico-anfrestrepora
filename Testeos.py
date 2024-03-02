with open("data.csv", "r") as file:
    truck_events = file.readlines()


len(truck_events)
truck_events = [line.replace("\n", '') for line in truck_events]
truck_events = [line.split("\t") for line in truck_events]
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
 
#print(suma_columna)

#------------------------------------

with open("data.csv", "r") as file:
    lista = file.readlines()


len(lista)
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

# Convertir el diccionario a una lista de tuplas y ordenar alfabéticamente
lista_tuplas = sorted(contador_letras.items())


# Imprimir la lista de tuplas (letra, cantidad)
# print("Cantidad de registros por letra:")
# for tupla in lista_tuplas:
#     print(tupla)

#--------------------------------- 3


    
with open("data.csv", "r") as file:
    lista = file.readlines()


lista = [line.replace("\n", '') for line in lista]
lista = [line.split("\t") for line in lista]


# Inicializar un diccionario para almacenar la suma de la segunda columna por cada letra
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
#print(resultado)

#----------------------------------------------------------------------- 4


from datetime import datetime
from collections import defaultdict

with open("data.csv", "r") as file:
    lista = file.readlines()
lista = [line.replace("\n", '') for line in lista]
lista = [line.split("\t") for line in lista]

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
#print(resultado)


#----------------------------------------------------------------5

with open("data.csv", "r") as file:
    lista = file.readlines()
lista = [line.replace("\n", '') for line in lista]
lista = [line.split("\t") for line in lista]


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

#resultado = valores_max_min_por_letra(lista)



#----------------------------------------------------------------6
with open("data.csv", "r") as file:
    lista = file.readlines()
lista = [line.replace("\n", '') for line in lista]
lista = [line.split("\t") for line in lista]

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
#print(resultado)

#------------------------------------------7
with open("data.csv", "r") as file:
    lista = file.readlines()
lista = [line.replace("\n", '') for line in lista]
lista = [line.split("\t") for line in lista]


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
#print(resultado)


#--------------------------------------8
with open("data.csv", "r") as file:
    lista = file.readlines()
lista = [line.replace("\n", '') for line in lista]
lista = [line.split("\t") for line in lista]

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
#print(resultado)


#-----------------------
#------------------------------------------9
with open("data.csv", "r") as file:
    lista = file.readlines()
lista = [line.replace("\n", '') for line in lista]
lista = [line.split("\t") for line in lista]

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
#print(resultado)


#-------------------------------------------10
with open("data.csv", "r") as file:
    lista = file.readlines()
lista = [line.replace("\n", '') for line in lista]
lista = [line.split("\t") for line in lista]

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
#print(resultado)

#-------------------------------------------11
with open("data.csv", "r") as file:
    lista = file.readlines()
lista = [line.replace("\n", '') for line in lista]
lista = [line.split("\t") for line in lista]


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
#print(resultado)

#-------------------------------------------12
with open("data.csv", "r") as file:
    lista = file.readlines()
lista = [line.replace("\n", '') for line in lista]
lista = [line.split("\t") for line in lista]

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
print(resultado)
