"""
calcular el sueldo de un trabajador
consultar cuantos trabajadores para calcular su sueldo 
preguntar los dias trabajados
guardar en un arreglo si es mas de un trabajador y mostrar la informacion
"""

print("Bienvenido al calculo de sueldo")
cantidad_trabajadores = int(input("Ingrese la cantidad de trabajadores: "))
trabajadores = []
sueldo_diario = 30000
for i in range(cantidad_trabajadores):
    trabajador = {}
    trabajador["nombre"] = input("Ingrese el nombre del trabajador: ")
    opcion = input("Trabajo todo el mes: (Si/No) ")
    if opcion == "Si":
        trabajador["dias_trabajados"] = 30
    else:
        trabajador["dias_trabajados"] = int(input("Ingrese los dias trabajados: "))
    trabajadores.append(trabajador)

for trabajador in trabajadores:
    sueldo = trabajador["dias_trabajados"] * sueldo_diario
    sueldo = "${:,.2f}".format(sueldo)
    print("-------------------------------------------------")
    print(f"El sueldo de {trabajador['nombre']} es: {sueldo}")
    print("-------------------------------------------------")