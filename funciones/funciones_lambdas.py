numeros = [1,2,3,4,5,6,7,8,9,11,13,14]

def es_par(num) :
    if (num % 2 == 0) :
        return True
    return False

numeros_pares = filter(es_par, numeros)
print(type(numeros_pares))
print(list(numeros_pares))

# con lambdas

numeros_pares = filter(lambda numero : numeros%2 == 0, numeros)