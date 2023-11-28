# Creando una lista con list

lista = list(["Hola Gustavo", 60, 1.81]) 
print(lista)

# cantidad de elementos de la lista
print(len(lista))

# agregando un elemento a la lista
lista.append("jajaja")
print(lista)

print(len(lista))

lista.append("jojojo")

print(lista)
# print(len(lista.append("titi"))) # ERROR ????

# insert en una posición
lista.insert(2, "uno ochenta uno")
print(lista)

# agregando varios elementos
lista.extend([False, 2023])
print(lista)

# eliminando un elemento por índice
print(lista.pop(0))
print(lista)

print(lista.pop(-1)) # saca el último
print(lista) 

# removiendo por valor
lista.remove("jojojo")
print(lista)

# ordenando la lista
listaN1 = [ 1,2,7,9,5,3]
print(listaN1)

# invierte la lista
listaN1.reverse()
print(listaN1)

listaN2 = [ 1,2,7,9,5,3]
print(listaN2)

# orden inverso
listaN2.sort()
listaN2.reverse()
print(listaN2)

print(dir(list))
print("====")
print(dir(tuple))
print("====")
print(dir(dict))




