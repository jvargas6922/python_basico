"""
#funciones split
saludo = "Hola, como estas?"
# fecha = "12/12/2020"
fecha = "2020/12/12"
correo = "contacto@prueba.com"
print(correo.split("@"))
"""
"""
FORMA TRADICIONAL
#menu 1
print('Opciones: ')
print('1) De acuerdo')
print('2) En desacuerdo')
print('3) No me interesa')

#menu 2
print('Opciones: ')
print('1) De acuerdo')
print('2) En desacuerdo')
print('3) No me interesa')

#menu 3
print('Opciones: ')
print('1) De acuerdo')
print('2) En desacuerdo')
print('3) No me interesa')
"""
#FORMA CON FUNCIONES
def imprimir_menu():
    print('Opciones: ')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')
"""
# imprimir_menu()
# imprimir_menu()
# imprimir_menu()
# imprimir_menu()
#print(4 + 5)
num1 = 4
num2 = 5
suma = num1 + num2
print(suma)
# print(sum(num1,num2))

def sumar(a,b):
    suma = a + b
    print(suma)

sumar(4,5)
sumar(9,10)
sumar(50,80)

"""

preguntas = ['Enunciado Pregunta 1','Enunciado Pregunta 2','Enunciado Pregunta 3']
# print(preguntas[0])
# print(preguntas[1])
# print(preguntas[2])
# for pregunta in preguntas:
#     print(pregunta)
# FORMA TRADICIONAL
# respuestas =[]
# print('Encuesta de Satisfacción')
# print('Enunciado Pregunta 1')
# print('Enunciado Pregunta 2')
# print('Enunciado Pregunta 3')
# opcion = input("elija una opcion a la pregunta")
# respuestas.append(opcion)
# print(respuestas)

"""
#FORMA CON FUNCIONES
respuestas =[]
def encuesta(opciones): 
    while len(respuestas) < len(preguntas): 
        eleccion = input("A continuación podrá elegir tres opciones  \n Ingrese su opción(opciones válidas: ['0', '1', '2', '3']): ") 
    if eleccion in opciones: 
        respuestas.append(eleccion)
        print(respuestas)
        return eleccion 
    else: 
        print("Opción no válida, ingrese una de las opciones válidas: ", opciones)

print("Tus respuestas fueron: ", respuestas) 

encuesta(['0', '1', '2', '3'])
"""
"""
# forma tardicional
respuestas =[]
print(preguntas[0])
print('Opciones: ')
print('1). De acuerdo')
print('2). En desacuerdo')
print('3). No me interesa')
respuestas.append(input('> '))
print(preguntas[1])

#FUNCIONES
def imprimir_menu():
    print('Opciones: ')
    print('1). De acuerdo')
    print('2). En desacuerdo')
    print('3). No me interesa')

preguntas = ['Enunciado Pregunta 1', 'Enunciado Pregunta 2','Enunciado Pregunta 3']
respuestas =[]

for p in preguntas:
    print(p)
    imprimir_menu()
    respuestas.append(input('> '))

print(respuestas)
for r in respuestas:
    print(f"la respuesta fueron las siguiente {r}")
"""


# def resta(a,b):
#     print(a - b)

# val1 = int(input("valor 1"))
# val2 = int(input("valor 2"))
# resta(val1,val2)

def operaciones(a , b = None):
    if a and b:
        suma = a + b
        resta = a - b
        mult = a * b
        div = a / b
        print(f"la suma es {suma}")
        print(f"la resta es {resta}")
        print(f"la multiplicacion es {mult}")
        print(f"la division es {div}")
    elif a:
        potencia = a ** 2
        print(f"la potencia es {potencia}")
    else:
        potencia = b ** 2
        print(f"la potencia es {potencia}")


#operaciones(5,5)
#operaciones(5)
#operaciones(5,0)

# RETORNO DE UNA FUNCION
def  multiplicar():
    a = 5
    b = 10
    return a * b

 valor = multiplicar()
 print(valor)

 def operaciones_matematicas():
    suma = 5 + 5
    resta = 10 - 5
    mult = 5 * 5
    return suma, resta, mult

valores = operaciones_matematicas()
