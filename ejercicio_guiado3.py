"""
Toda fecha tiene sucesos importantes ¿cómo recordarlos? Las efemérides son conjunto de
acontecimientos importantes ocurridos en una misma fecha, por lo que aquí intentaremos
utilizar lo aprendido para almacenar eventos importantes y consultarlos.
Supongamos los siguientes eventos:
● 1 de Enero: Año Nuevo
● 27 de Febrero: Terremoto en Chile
● 8 de Marzo: Día de la mujer
● 21 de Mayo: Glorias Navales
● 18 de Septiembre: Fiestas Patrias
● 19 de Septiembre: Glorias del Ejército
● 25 de Diciembre: Navidad
"""

efemerides ={
    "1 de Enero": "Año Nuevo",
    "27 de Febrero": "Terremoto en Chile",
    "8 de Marzo": "Día de la mujer",
    "21 de Mayo": "Glorias Navales",
    "18 de Septiembre": "Fiestas Patrias",
    "19 de Septiembre": "Glorias del Ejército",
    "25 de Diciembre": "Navidad"
}



# efemerides ={
#     "1 de enero": "Año Nuevo",
#     "27 de febrero": "Terremoto en Chile",
#     "8 de marzo": "Día de la mujer",
#     "21 de mayo": "Glorias Navales",
#     "18 de septiembre": "Fiestas Patrias",
#     "19 de septiembre": "Glorias del Ejército",
#     "25 de diciembre": "Navidad"
# }

# print(efemerides['18 de Septiembre'])
# print("claves", efemerides.keys())
# print(efemerides.values())
fecha = input("Ingrese una fecha: ").lower()
print("fecha ingresada", fecha)
for clave, valor in efemerides.items():
    if clave.lower() == fecha:
        print(f"La fecha ingresada se celebra: {valor}")
        break
# efemerides.get(fecha)
# print(f"La fecha ingresada se celebra: {efemerides[fecha]}")
# print(f"La fecha ingresada se celebra: {efemerides.get(fecha, 'No se celebra nada')}")

# separar split por espacio
saludo = "hola, mundo, como estas"
print(saludo.split(", ")) # ['hola', 'mundo', 'como estas']
print(saludo.split()) # ['hola', 'mundo', 'como', 'estas']
