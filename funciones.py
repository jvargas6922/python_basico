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


