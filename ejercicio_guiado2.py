import sys
"""
lista_argv = [valor1, valor2, valor3, valor4, valor5, valorN]

"""
nombre_programa = sys.argv[0]
nombre = sys.argv[1]
apellido = sys.argv[2]
edad = sys.argv[3]

print("Mi nombre es :", nombre)
print("Mi apellido es :", apellido)
print("Mi edad es :", edad)
print("El nombre del archivo es :", (nombre_programa))

#interpolacion de strings
print(f"Mi nombre es {nombre} y mi apellido es {apellido} y mi edad es {edad} y el nombre del archivo es {nombre_programa}")







