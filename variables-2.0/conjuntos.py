# creando un conjunto con set

conjunto = set(["Dato 1"])

# un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = { conjunto1, "dato 3"}
print(conjunto2)

# Teoría de conjuntos
conjunto1 = { 1,3,5,7}
conjunto2 = { 1,3,7 }
resultado = conjunto2.issubset((conjunto1))
resultado = conjunto2 <= conjunto1 # idem
print(resultado)
resultado = conjunto1.issubset((conjunto2))
print(resultado)

resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1 # idem
print(resultado)

resultado = conjunto2 > conjunto2
print(resultado)
resultado = conjunto2 >= conjunto2
print(resultado)

# Verificar numero común
resultado = conjunto1.isdisjoint(conjunto2)
print(conjunto1.isdisjoint(conjunto2))
print (resultado)
