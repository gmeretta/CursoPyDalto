# iterando una lista
animales = {"pez", "gato", "perro", "loro", "cocodrilo"}
for animal in animales :
    print(animal)
    
print(type(animales))
cantAnimales = len(animales)
print(f"cantidad de animales {cantAnimales}")

# recorriendo números    
numeros = {1, 34, 67, 7, 9}
for numero in numeros :
    print(numero * 2) 
   
# iterando al mismo tiempo 
for numero, animal in zip(animales, numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
    
for num in range(5,10):
    print(num)

for num in range(20):
    print(num)
    
    
for num in enumerate(numeros):
    print(num)
    print(num[0])
    print(num[1])
    
for numero in numeros:
    print(f"ultimo bucle: {numero}")
else:
    print("el bucle termino")
    
# todo lo anterior funciona para tuplas
