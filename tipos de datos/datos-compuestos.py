
# Listas - expresadas con corchetes
lista = ["Gustavo Omar", "Soy Meretta", True, 1.81]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
lista[2] = False
print(lista[2])


# Tuplas - expresadas con paréntesis - NO SE PUEDE MODIFICAR 
tupla = ("Gustavo Omar", "Soy Meretta", True, 1.81)
print(tupla)
print(tupla[0])
print(tupla[1])
print(tupla[2])
# tupla[2] = False # ERROR !!!
print(tupla[2])

# Conjuntos - expresados con llaves 
conjunto = {"Gustavo Omar", "Soy Meretta", True, 1.81}

# Se puede reconstruir el conjunto completo pero no cada componente
# No se accede a los elementos por índice
conjunto = {"Hola", " mundo"}
print(conjunto)
# print(conjunto[0]) # ERROR !!!

# No almacena datos duplicados
conjunto = {"Hola", "Hola"}
print(conjunto)

# Diccionarios - como un Json - clave / valor
diccionario = {
    'nombre' : "Gustavo Omar",
    'apellido' : "Meretta",
    'altura' : 1.81,
    'unaLista' : lista
}

# referencia por nombre
print(diccionario['nombre'])
print(diccionario['altura'])

