"""
Estructura de datos clase 1

"""

"""
lista es un conjunto de elementos que pueden ser de cualquier tipo
lista =[dato,dato2,dato3]
donde dato1, dato2, dato3 deben ser variables que contengan un valor

"""

lista_numerica = [1,2,3,4,5,6,7,8,9,10,3]
                # 0,1,2,3,4,5,6,7,8,9,10
# print(lista_numerica)
#print(lista_numerica[4])
#print(lista_numerica[8])
#print(lista_numerica[10])
# print(lista_numerica[9])
# print(lista_numerica[5])
#accediendo a la lista con indice negativo
# print(lista_numerica[-1])
# print(lista_numerica[-5])
lista_string = ["hola","mundo","como","estas"]
#metodo que se pueden ocupar en una lista
#print(lista_string.__dir__())
#print(lista_string)
#lista_mixta = [1,2,3,"hola","mundo",True,False]
#print(lista_mixta)
#print(lista_mixta[4])
#print(lista_mixta[-3])

#Metodo append
#lista_string.append(True)
#lista_string.append(20)
#print(lista_string)

pares =[]
for i in lista_numerica:
    if i%2 == 0:
        pares.append(i)
        #lista_string.append(i)

#print("valor",i)

print(f"Los numeros pares son{pares}")
print(f"Los numeros pares son{lista_string}")

#Metodo insert

lista_numerica.insert(5,30)
print(lista_numerica)
pares.insert(4,9)
print(pares)

#Metodo pop
#pares.pop(4)
#print(pares)

#Metodo remove
pares.remove(9)
print(pares)

#Metodo Reverse
pares.reverse()
print(pares)

#Metodo sort
pares.sort()
print(pares)
print(lista_string)
lista_string.sort()
print(lista_string)
