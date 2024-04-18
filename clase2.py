"""
ciclo 
while  es un ciclo que se cumple mientras no se cumpla la condicion

while condicion:
    #codigo a evaluar

"""
import getpass


"""
password = getpass.getpass("Ingresa tu contraseña: ")

while password != "123456789":
    print("Contraseña incorrecta")
    password = getpass.getpass("Ingresa tu contraseña: ")
    print(password)

print("contraseña correcta!!!!!!")
"""
"""
i = 0
while i < 10:
    print(f"Esto se mostrará 10 veces esta es la iteracion {i}")
    # i+=1
    # i = i + 1
    i += 2
"""
"""
saludo = "Hola"
saludo += " Mundo"
#print(saludo)
saludo += " chao"
 print(saludo)
 """
"""
i = 1
while i < 10:
    print(i)
"""

i = 1
suma = 0
while i <= 100:
    suma += i
    print("valor de suma: ",suma)
    i += 1
    print("valor de i: ", i)
    print("\n")

print(f"El valor de la suma es: {suma}")