"""
computador = {
    'notebook': 489990,
    'tablet': 120000,
    'cargador': 12400
    }

for clave,valor in computador.items():
    # print("clave dentro del for", clave)
    print("valores", valor)

# METODO KEYS
# print(computador.keys())
# claves = computador.keys()

#METODO VALUES
#computador.values()
valores = computador.values()

# print("claves diccionario", claves)
print("valores diccionario", valores)

carro_compra = computador.items()
print(carro_compra)

total_pagar = 0
for clave, valor in carro_compra:
    total_pagar += valor

print(f"Total a pagar ${total_pagar}")

#PREGUNTAMOS SI EXISTE EL ELEMENTO EN EL DICCIONARIO
print(computador.get('iphone'))
# print(computador.get('cargador'))
if computador.get('iphone') == None:
    print("No existe el producto")

tupla_ej = ("Abril", 2021)
print(type(tupla_ej))

api_pokemon = "https://pokeapi.co/api/v2/pokemon"
print(type(api_pokemon))
{[
    "nombre": "pikachu",
    "tipo": "electrico",
    "habilidades": ["estatico", "paralizador"],
    "imagen": "https://pokeapi.co/api/v2/pokemon/25
]}
"""

muchos_animales = {
    'Gato',
    'Perro',
    'Tortuga',
    'Gato',
    'Perro',
    'Tortuga',
    'Gato',
    'Perro',
    'Tortuga',
    'Gato',
    'Perro',
    'Tortuga',
    'Hurón',
    'Hamster',
    'Erizo de Tierra'
    }

print(muchos_animales)

#CONVERTIR DICCIONARIO EN UNA LISTA
computador ={
    "Mac": "Mac OS",
    "Lenovo": "Windows",
    "HP": "Linux",
    "Dell": "Windows XP",
    "Acer": "Fedora"
}

# dato_computador  = computador.items()
# #CONVERTIR MI TUPLA EN UNA LISTA
# lista_computador = list(dato_computador)
# #CONVERTIR MI TUPLA EN SET
# set_computador = set(dato_computador)
# print(type(lista_computador))
# print(type(set_computador))

#FUNCION DIR 
# saludo = "Hola Mundo"
# print(dir(saludo))

# print(dir(computador))

#FUNCION SUMAR

var = [1,2,3,4,5,6,7,10,33,50,100,98,76,54,32,21,12,11,9,8,7,6,5,4,3,2,1]
var.sort(reverse=True)
print(var)
mayor = var[0]
print(mayor)

#VALOR MAYOR DE LA LISTA
print(max(var))
mayor_precio = max(var)

print(min(var))
menor_precio = min(var)

print(f"El valor mayor es {mayor_precio} y el menor es {menor_precio}")

# print(orden)
# suma = 0
# for i in var:
#     suma += i

# print(suma)
# print(sum(var))


