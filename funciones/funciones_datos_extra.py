def frase(nombre, apellido,adjetivo="tonto"): # default
    return f'Hola {nombre} {apellido} sos muy {adjetivo}'

frase_resultante = frase(adjetivo = "inteligente", apellido = "meretta", nombre = "gustavo")
frase_resultante = frase(apellido = "meretta", nombre = "gustavo")
print(frase_resultante)