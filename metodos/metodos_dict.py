diccionario = {
    "nombre" : 'Gustavo',
    "apellido" : 'Meretta',
    "subs" : 1000000
}

claves = diccionario.keys()
print(claves)

valorNombre = diccionario.get("nombre")
print(valorNombre)
# sin get me lanzaría una excepción
print(diccionario.get("kaka"))

# Se puede hacer pero no es muy útil
diccionarioN = {
    0 : 'Gustavo',
    1 : 'Meretta',
    2 : 1000000
}

print(diccionarioN[1])

# clear elimina todo

# eliminando un elemento del diccionario
diccionario.pop("nombre")
print(diccionario)

# generando un iterable
dictIterable = diccionario.items()
print(dictIterable)