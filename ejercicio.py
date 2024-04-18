"""
usuarios 
equipos 
contraseñas
Entrada:
El usuario selecciona el equipo a acceder
Proceso:
    cuando ingresa al equipo valido, debe ingresar credenciales
    si las credenciales son correctas, se le da acceso al equipo
    sino se hace un caso de uso
salida:
    Se le muestra al usuario un mensaje que corresponda a sus acciones
"""

equipo = int(input("Ingrese el equipo al que quiere acceder:"))
ingreso_equipo = "Acceso a equipo"
mensaje_equipo = "Ingrese credenciales"
match equipo:
    case 1:
        print(f"{ingreso_equipo} 1")
        print(mensaje_equipo)
        #usuario = admin
        #clave = 1234
        usuario = input("Ingrese su usuario:")
        clave = input("Ingrese su clave:")
        if str(usuario) and str(clave) != "":
            if usuario == "admin" and clave == "1234":
                print("Acceso concedido")
            else:
                print("Credenciales incorrectas")
        else:
            print("No ingreso los campos requeridos")

    case 2:
        print(f"{ingreso_equipo} 2")
        print(mensaje_equipo)
        #usuario = soyadmin
        #clave 
    case 3:
        print(f"{ingreso_equipo} 3")
        print(mensaje_equipo)
        #usuario = soloyo 
        #clave 
    case 4:
        print(f"{ingreso_equipo} 4")
        print(mensaje_equipo)
        #usuario = hola
        #clave 
    case 5:
        print(f"{ingreso_equipo} 5")
        print(mensaje_equipo)
        #usuario = soyUsuario
        #clave qw123_?/·#)
    case _:
        print("Equipo no encontrado")