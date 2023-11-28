def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados
    
resultado = suma([5,3,9,10,20,3])
print (resultado)

# utilizando args

def sumaarg(nombre, *numeros):
    return f"{nombre} la suma es {sum(numeros)}"

resultado = sumaarg("Gustavo", 5,3,9,10,20,3)
print (resultado)
    