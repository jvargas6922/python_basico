import random
"""
edad = int(input('Ingrese su edad: '))
if edad >= 18: # true
    print("eres mayor de edad")
else: # false
    print("eres menor de edad")
"""

"""
if(condicion){
    //codigo
}else{

}
"""
"""
numero = input("Ingrese un numero: ")
if numero != "":
    numero = int(numero)
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("Es un numero impar")
    #----------------->    
else:
    print("No ingreso ningun numero")
"""
"""
peso = int(input("Ingrese su peso: "))
altura = int(input("Ingrese su altura: "))

imc = peso / (altura**2)

if imc > 24.9:
    print("Tienes sobrepeso")
elif imc < 18.5:
    print("tienes bajo peso")
else:
    print("Tienes un peso normal")
"""
"""
= asignacion
== comparar valores
=== compara valores y tipos de datos
"""
"""
valor = int(input("Ingrese un numero: "))

if valor == 0: # 5 = 0
    print("El numero es 0")
elif valor % 2 == 0: # 5 % 2 = 1
    print("El numero es par")
else:
    print("el numero es impar")
"""

# password = input("ingrese su contraseña:")
#len me permite contar caracteres
# print("cantidad de caracteres", len(password))
# if len(password) < 5:
#     print("La contraseña es muy corta")
# elif password == "123456"
#     print("Contraseña correcta")
# else:
#     print("Contraseña robusta")

"""
match password:
    case "123456":
        print("Contraseña correcta")
    case _ if len(password) < 5:
        print("La contraseña es muy corta")
    case _:
        print("Contraseña robusta")
"""

"""
1 Piedra
2 Papel
3 Tijera

jugadas
piedra vs tijera
    gana piedra
papel vs piedra
    gana papel
tijera vs papel
    gana tijera
"""
"""
opcion_usuario = input("Ingrese una opcion: ")
numero_aleatorio = random.choice([1,2,3])



print(numero_aleatorio)

match 


    
