diccionario = {
    "nombre": "Gustavo",
    "apellido": "Meretta",
    "subs": 1000000
}

for key in diccionario.items():
    print(key)
    
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave {key} y el valor es {value}")
    
frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

for fruta in frutas:
    if fruta == "granada":
        continue
    if fruta == "pera":
        break    
    print ( f"me voy a comer una {fruta}")
    
# iterando un texto
cadena = "Hola Gustavo"
for letra in cadena:
    print(letra)
    
numeros = [1,2,3,4,5]
numeros_duplicados = [ x*2 for x in numeros]
print(numeros_duplicados)
    

          