"""
for iterador in (arreglo u objeto):
    #codigo a iterar

"""

"""
valores = [1,2,3,4,5,6,7,8,9,10]
for iterador in valores:
    print('iteracion', iterador)
"""

"""
# cuando el rango tiene 1 valor indica las iteraciones que se cupliran 
for i in range(10):
    print('iteracion', i)
"""

"""
# cuando el rango tiene 2 valores se indica lo siguiente (incio, fin)
for i in range(4,10):
    print(i)
"""

"""
# cuando el rango tiene 3 valores se indica lo siguiente (incio, fin, incremento)
for i in range(4,10,2):
    print(i)
"""

# print(type(range(4,10,2)))

#lista
estudiantes = ['Diego', 'Ignacio', 'Maria V', 'David', 'Francisco', 'Luis', 'Dennise']

# print(estudiantes)
# print(estudiantes[0])
# print(estudiantes[2])
# print(f"Hola como estan mi nombre es {estudiantes[2]}")
"""
for nombre in estudiantes:
    print(f"Hola como estan mi nombre es {nombre}")
"""
"""
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    if numero == 5:
        print("numero ganador", numero)
    else:
        print("siga intentando", numero)
"""
"""
saludo = "Hola Mundo"
print(saludo)
cantidad = 0
# print(len(saludo))
for i in saludo:
    #print(i)
    if i == "o":
        cantidad+=1
        print(f"existe caracter {i} y la cantidad ={cantidad}")
    else:
        print("no existe caracter")
"""
"""
notas =[1,4,5,3,8,1,1,2,4,5,1,8,8,8,8,9]
# quiero saber la cantidad de estudiantes aprobados y reprobados
aprobados = 0
reprobados = 0
for nota in notas:
    if nota > 5:
        aprobados+=1
    else:
        reprobados+=1

print(f"los estudiantes aprobados son {aprobados}")
print(f"los estudiantes reprobados son {reprobados}")
"""
"""
profesional ={
    'nombre':'Diego',
    'edad': 30,
    'profesion':'Ingeniero',
    'experiencia': 5
}

for clave, valor in profesional.items():
    # print(clave)
    # print(valor)
    print(f"Mi {clave} es {valor}")
"""
"""
texto = "Esternocleidomastoideo"
for pos, letra in enumerate(texto):
    print(f"La letra en la posición {pos} es la {letra}")
    # print(pos)
    # print(letra)
"""
"""
prefijo = ['La','El','La','El']
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']
for prefijo, fruta, color in zip(prefijo, frutas, colores):
    print(f'{prefijo} {fruta} es de color {color}')
    # print(prefijo)
    # print(fruta)
    # print(color
"""
"""
password = "camioneta" #***********
#buscar si existe la "o" en mi password
for letra in password:
    print(letra)
    if letra == "a":
        print("caracter conseguido")
        break
"""
