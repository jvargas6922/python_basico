"""
    opciones de comida con sus precios
    opciones de bebidas con sus precios
    propina
    iva
    subtotal
    Total

    Entrada
        Mensaje de bienvenida
        Input comida
        Input bebida
    Proceso
        Calculo de costo almuerzo
        Calculo de iva
        Calculo de propina
    Salida
    Total recibo
"""

print("Bienvenido a nuestro restaurante")
print("Opciones de comida")
print("1.- Pollo con papas $ 5.000")
print("2.- Carne mechada con pure $ 6.000")
print("3.- Pescado con arroz $ 7.000")
print("opciones de bebida")
print("1.- Agua $ 500")
print("2.- Bebida $ 1.000")
print("3.- Jugo $ 1.500")

opcion_comida = input("Ingrese la opcion de comida: ")
#comida
if opcion_comida != "":  
    opcion_comida = int(opcion_comida) 
    if(opcion_comida == 1):
        costo_comida = 5000
    elif(opcion_comida == 2):
        costo_comida = 6000
    elif(opcion_comida == 3):
        costo_comida = 7000
else:
    costo_comida = 0

opcion_bebida = input("Ingrese la opcion de bebida: ")

#bebida
if opcion_bebida != "":
    opcion_bebida = int(opcion_bebida)
    if(opcion_bebida == 1):
        costo_bebida = 500
    elif(opcion_bebida == 2):
        costo_bebida = 1000
    elif(opcion_bebida == 3):
        costo_bebida = 1500
else:
    costo_bebida = 0

subtotal = costo_comida + costo_bebida
iva = subtotal * 0.19

print("Desea agregar propina")
desicion = input("Si/No: ")
if desicion == "Si":
    propina = subtotal * 0.10
else:
    propina = 0

total_recibo = subtotal + iva + propina
print(total_recibo)