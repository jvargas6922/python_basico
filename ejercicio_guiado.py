"""
import sys
buscar = sys.argv[1]
print(buscar)
"""
"""
import random
lista =[1,2,3,4,5,6,7,8,9,0]
print("lista principal",lista)
random.shuffle(lista)
print('lista aleaoria',lista)

for i in lista:
    if i == 5:
        print("numero encontrado")
        break
    else:
        print("numero no encontrado")
"""

"""
import sys
import random


buscar = sys.argv[1]
buscar = int(buscar)
lista =[1,2,3,4,5,6,7,8,9,0]
# print("lista principal",lista)
random.shuffle(lista)
print('lista aleaoria',lista)

for i in lista:
    if i == buscar:
        print(f"numero encontrado en la posicion {lista.index(i)}")
        break
    else:
        print("numero no encontrado")

"""



import sys
import random


buscar = sys.argv[1]
# print(buscar)
buscar = int(buscar)
lista = [1,2,3,4,5,6,7,8,9,0]
#posicion =  0,1,2,3,4,5,6,7,8,9 
#valor =     1,2,3,4,5,6,7,8,9,0
random.shuffle(lista)
print(enumerate(lista))

print('lista aleaoria',lista)
for position, elemento in enumerate(lista):
    # Si el elemento es igual a lo que buscamos terminamos el ciclo
    print(elemento)
    if elemento == buscar:
        print("¡Elemento encontrado! Se terminará del ciclo",elemento)
        break
    else:
        # Si es que no es el elemento buscado lo reportamos
        print("Elemento no encontrado", elemento)