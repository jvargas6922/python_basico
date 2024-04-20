"""
diccionaio ={
    clave: valor,
    clave: valor,
    clave: valor
}
para poder saber p recorrer los datos debemos revisar la clave y el valor que se necesita mapear
"""
#constante
#NUMERO = 9
# una variable
#numero = 8
#Numero = 7

#snake_case
#nombre_estudiante = 'Juan'

"""
estudiantes = {
    'nombre': 'Juan',
    'edad': 22,
    'cursos': 'Matematicas',
    'calificaciones': 10
}

lista_nombre =['Juan', 'Pedro', 'Maria', 'Ana']

print(estudiantes)
print(estudiantes['nombre'])
print(estudiantes['cursos'])
print(estudiantes['cursos'])
#print(estudiantes['profesion'])
#AGREGAR UNA NUEVA CLAVE A MI DICCIONARIO
estudiantes['profesion'] = 'Ingeniero'
print(estudiantes)
print(f"profesion antigua {estudiantes['profesion']}")

#CAMBIAR EL VALOR DE UNA CLAVE DENTRO DE MI DICCIONARIO
estudiantes['profesion'] = 'Contador'
print(estudiantes)
print(f"profesion nueva {estudiantes['profesion']}")

print(lista_nombre[0])
#lista_nombre.insert(0,"Joffred")
print(lista_nombre[0])
print(estudiantes['nombre'])

print(lista_nombre[2])
print(lista_nombre[-2])

#CLAVES DUPLICADAS
duplicados = {
    "clave": 1,
    "clave": 2
    }
print(duplicados)

"""


"""
#ELIMINAR ELEMENTOS DE UN DICCIONARIO

compras = {
    "celular": 140000,
    "notebook": 489990,
    "tablet": 120000,
    "cargador": 12400
    }
print(compras)
#ELIMINANDO CON del
del compras["celular"]
print(compras)
#ELIMINANDO CON pop
compras.pop("tablet")
print(compras)

"""

#UNIR DICCIONARIOS
#UNIR DICCIONARIOS CON EL METODO update()
diccionario_a = {
    "nombre": "Alejandra",
    "apellido": "López",
    "edad": 33,
    "altura": 1.55
}

diccionario_b = { 
    "mascota":"miti",
    "ejercicio":"bicicleta",
    "altura": 2.00
}
print(diccionario_a)
print(diccionario_b)

#diccionario_a.update(diccionario_b)
#dic1         funcion    dic2
#dic1.update(dic2)
print(diccionario_a)
diccionario_b.update(diccionario_a)
print(diccionario_b)



