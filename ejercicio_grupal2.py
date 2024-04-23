"""
PROGRAMA QUE ME INDIQUE SI LA PERSONA ESTA EN DICOM


Entrada
    Persona
        Nombre
        Apellido
        Rut
        Edad
        Direccion
        Email
        Telefono

Proceso
    - Saber si trabaja(Dependiente o Independiente)
    - Saber si tene una deuda vigente, vencida, morosa, castigada
    - 

Salida

"""
# persona ={}
# persona["nombre"] = input("Ingrese su nombre: ")
# persona["apellido"] = input("Ingrese su apellido: ")
# persona["Rut"] = input("Ingrese su Rut: ")
# persona["Edad"] = int(input("Ingrese su Edad: "))
# persona["Direccion"] = input("Ingrese su Direccion: ")
# persona["Email"] = input("Ingrese su Email: ")
# persona["Telefono"] = input("Ingrese su Telefono: ")

# print(persona)

datos_economicos ={}

situacion_laboral ={
    1:'dependiente',
    2:'independiente',
    3:'estudiante',
    4:'cesante',
    5:'desempleado'
}

print("Seleccione su situacion laboral")
situacion = int(input("1.- Dependiente\n2.- Independiente\n3.- Estudiante\n4.- Cesante\n5.- Desempleado\n"))


# for key, value in situacion_laboral.items():
    

# deuda ={
#     'deuda_total': "morosa, vencida o castigada suma de las 3",
#     'deuda_morosa':"deuda que a sido pagada en mas de 30 a 60 dias",
#     'deuda_vencida':"deuda que a sido pagada en mas de 61 a 90 dias",
#     'deuda_castigada':"deuda que a sido pagada en mas de 91 dias",
# }


