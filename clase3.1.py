import sys

"""
lista_impar = {} Diccionario
lista_par = [] Lista
"""

"""
n = 10
print("Metodo de comprension")
lista_par = []
lista_par = [2*i + 2 for i in range(n)]
print(lista_par)
print("Metodo tradicional")
for i in range(n):
    print(i)
    lista_par.append(i*2 + 2)

print(lista_par)
"""
valores = [0,4,5,6,7,8,9]
pares = []
impar = []
print("Metodo de comprension")
divisibles = ["pares" if valor % 2 == 0 else "impar" for valor in valores]
print("arreglo divisibles",divisibles)
pares = [valor for valor in valores if valor % 2 == 0]
impar = [valor for valor in valores if valor % 2 != 0]

print(f" pares {pares}")
print(f"impar {impar}")

# print("Metodo tradicional")
# for valor in valores:
#     if valor % 2 == 0:
#         pares.append(valor)
#     else:
#         impar.append(valor)
# print(f" pares {pares}")
# print(f"impar {impar}")