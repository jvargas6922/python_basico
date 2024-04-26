# #uso de las funciones 
# # funciones nativas de python
# # len()
# # print()
# # input()
# #sum()

# #funciones definidas por el usuario
# """
# def mi_funcion():
#     print("Hola mundo")
#     return "hola mundo"

# mi_funcion()
# """

# #Ejemplo 1)
# """
# # Menú
# print('Opciones: ')
# print('1) De acuerdo')
# print('2) En desacuerdo')
# print('3) No me interesa')
# # Más código que hace muchas cosas interesantes
# # Nuevamente el Menú
# print('Opciones: ')
# print('1) De acuerdo')
# print('2) En desacuerdo')
# print('3) No me interesa')
# # Otro código que hace muchas cosas interesantes
# # Menú por última vez
# print('Opciones: ')
# print('1) De acuerdo')
# print('2) En desacuerdo')
# print('3) No me interesa')
# # Código final y fin del Programa
# """

# #codigo con funcion
# """
# def imprimir_menu():
#     print('Opciones: ')
#     print('1) De acuerdo')
#     print('2) En desacuerdo')
#     print('3) No me interesa')

# imprimir_menu()
# imprimir_menu()
# imprimir_menu()
# """
# #Ejemplo 2)

# preguntas = ['Enunciado Pregunta 1','Enunciado Pregunta 2','Enunciado Pregunta 3']
# respuestas = []

# #Hacer preguntas
# # Código para la primera pregunta
# print(preguntas[0])
# print('Opciones: ')
# print('1). De acuerdo')
# print('2). En desacuerdo')
# print('3). No me interesa')
# respuestas.append(input('> '))

# # Código para la primera pregunta
# print(preguntas[1])
# print('Opciones: ')
# print('1). De acuerdo')
# print('2). En desacuerdo')
# print('3). No me interesa')
# respuestas.append(input('> '))

# # Código para la primera pregunta
# print(preguntas[2])
# print('Opciones: ')
# print('1). De acuerdo')
# print('2). En desacuerdo')
# print('3). No me interesa')
# respuestas.append(input('> '))

# print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
# print(f'La respuesta a la pregunta 2 fue {respuestas[1]}')
# print(f'La respuesta a la pregunta 3 fue {respuestas[2]}')
# print('Muchas gracias por responder la encuesta')

# #codigo con funcion
# """
# def imprimir_menu():
#     print('Opciones: ')
#     print('1). De acuerdo')
#     print('2). En desacuerdo')
#     print('3). No me interesa')

# preguntas = ['Enunciado Pregunta 1', 'Enunciado Pregunta 2','Enunciado Pregunta 3']
# respuestas = []
# # Hacer preguntas
# for p in preguntas:
#     print(p)
#     imprimir_menu()
#     respuestas.append(input('> '))

# print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
# print(f'La respuesta a la pregunta 2 fue {respuestas[1]}')
# print(f'La respuesta a la pregunta 3 fue {respuestas[2]}')
# print('Muchas gracias por responder la encuesta')
# """

# #Anatomia de una funcion 
# """
# def elevado_2(x):
#     print(x**2)

# #elevar al cuadrado el parametro de entrada
# elevado_2(2)
# elevado_2(3)
# elevado_2(4)
# elevado_2(5)
"""

"""
# def elevar(x,y):
#     print(x**y)
#     #
# #elevar al cuadrado el parametro de entrada y se le pasa un segundo parametro para elevarlo a la potencia que se desee
# elevar(2,2)#4
# elevar(3,3)#27
# elevar(4,2)#16
"""

# """
# def elevar(base,exponente):
#     print(base**exponente)

# elevar(2,2)
# elevar(3,3)
# elevar(4,2)
"""

# #Retorno de una funcion
# """
# def prueba_return():
#     a = "Esta línea se va a imprimir"
#     b = "Esta línea no se va a imprimir"
#     return a # Punto de salida
#     print(b)

# print(prueba_return())
# """


# #Multiples retornos
# """
# def cuadrado_cubo(base):
#     cuadrado = base**2
#     cubo = base**3
#     return cuadrado, cubo

# print(cuadrado_cubo(2))
# """

# #Ejercicio guiado estandarizacion
# """
# import math

# def media(lista):
#     return sum(lista)/len(lista)

# def sdd(lista, media):
#     diff = [(elemento - media)**2 for elemento in lista]
#     return math.sqrt(sum(diff)/(len(lista)-1))

# def resultado(lista):
#     m = media(lista)
#     sd = sdd(lista, m)
#     lista_estandarizada = [(valor-m)/sd for valor in lista]
#     return m, sd, lista_estandarizada

# lista = [1,2,3,4,5,6]
# m , desv_std, lista_estandarizada = resultado(lista)
# print(f"La media es {m}")
# print(f"La desviacion estandar es {desv_std}")
# print(f"La lista estandarizada es {lista_estandarizada}")
"""

# #Tipo de argumentos
"""
# precios = {
#     'Notebook': 700000,
#     'Teclado': 25000,
#     'Mouse': 12000,
#     'Monitor': 250000,
#     'Escritorio': 135000,
#     'Tarjeta de Video': 1500000
#     }

# def filtrar(diccionario, umbral):
#     filtro = {k:v for k,v in diccionario.items() if v > umbral}
#     print(filtro)
#     return filtro
    
# # filtrar(precios, 12000)
# filtrar(precios, 25000)
"""

#Funciones con argumentos
"""
# lista_numeros = [1,2,3,4,5]
# lista_string = ['a','b','c','d','e']

# def sumar_contar_tipos(lista,funcion):
#     tipos = [type(elemento) for elemento in lista]
#     opcion = funcion(lista)
#     return tipos, opcion

# # tipo, conteo = sumar_contar_tipos(lista_string, len)
# # print(tipo)
# # print(conteo)

# tipo, suma = sumar_contar_tipos(lista_numeros, sum)
# print(tipo)
# print(suma)
"""

# """
#Funciones con parametros obligatorios
# def extremo_multiplicado(lista,factor):
#     minimo = min(lista)
#     maximo = max(lista)
#     return factor*minimo, factor*maximo

# #print(extremo_multiplicado(4,[1,2,3,4]))# hay que tener cuidado con el dato que espera nuestra funcion
# print(extremo_multiplicado([1,2,3,4], 4))
# # # se entregan en orden
# # print(extremo_multiplicado(factor = 4, lista = [1,2,3,4]))
# # """


# #Funciones con parametros opcionales
# """
# def elevar(base, exponente, redondear = False):
#     if redondear:
#         valor = round(base**exponente,2)
#     else:
#         valor = base**exponente
#     return valor

# print(elevar(2, 3))
# print(elevar(2, 3, redondear = True))
# """

# #Args y Kwargs
# """
# def f(*args):
#     return args

# output = f(1,[2,3],'hola',{'clave':[4]})
# print(type(output))

# def f(**kwargs):
#     return kwargs

# output = f(valor = 1, texto = 'hola', lista_nombres = [4,5,6,7])
# print(type(output))
# # """

# #ejercicio Guidado expandiendo diccionario
# """
# def get_multiple(diccionario, *claves):
#     return {clave: diccionario[clave] for clave in claves}

# diccionario_prueba = {
#     'manzana': 'verde',
#     'platano': 'amarillo',
#     'frutilla': 'roja'
#     }

# resultado = get_multiple(diccionario_prueba, 'manzana', 'platano')
# print(resultado)
# """

# #variables
# # globales son las que se declaran fuera de una funcion (OjO)
# # locales son las que se declaran dentro de una funcion (OjO)

# #Ejemplo de variable global
# """
# total = 0#variable global
# def agregar_a_total(valor):
#     global total
#     total += valor
#     return total

# print(agregar_a_total(5))

# #Ejemplo de variable local
# def agregar_a_total(valor):
#     total = 2#variable local
#     total += valor
#     return total

# print(agregar_a_total(5))


# #Alcance de una variable
# continent = 'South America'
# def get_continent():
#     saludo = "hola"
#     print(continent)

# get_continent()
# print(saludo)

# #Modificaciondo variables globales desde un entorno local

# continent = 'South America'
# def get_continent():
#     global continent
#     continent = 'America'

# get_continent()
# print(continent)


#ejercicio Guiado loto
import random
pool = [n for n in range(1,42)]

# elegido = random.choice(pool)
# print("El primer número es", elegido)

# pool.remove(elegido)
# elegido = random.choice(pool)
# print("El segundo número es", elegido)

# pool.remove(elegido)
# print(pool)
# elegido = random.choice(pool)
# print("El Comodín número es", elegido)


#con funcion
def sacar_numero(posicion):
    global pool
    elegido = random.choice(pool)
    pool.remove(elegido)
    print(f'El {posicion} es {elegido}')

sacar_numero(4)
sacar_numero(5)
sacar_numero(6)
    




