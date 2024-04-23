"""
ejercicio grupal

"""

auto = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020,
    "precio": 15000000,
    "color": "blanco",
    "motor": "2.0",
    "patente": "AB123CD"
}

print(auto)
auto["conductor"] = "David"
print(auto)

chile ={
    "idioma": "español",
    "comida_tipica": "empanadas",
    "baile_tipico": "cueca",
    "bebida_tipica": "terremoto",
    "moneda": "peso",
    "capital": "Santiago"
}
print(f"Diccionario de Chile: {chile}")
chile["comuna"] = "Coronel"
print(f"Dic Chile Nuevo: {chile}")
chile["idioma"] = "chileno"
print(f"Dic Chile Nuevo2: {chile}")
del chile["comuna"]
print(f"Dic Chile Nuevo3: {chile}")