a = 5
b = 8
c = a + b
print(c)

nombreCompleto = "Gustavo Omar" # camel Case
nombre_completo = "Gustavo Omar" # snake Case (recomendado)

nombre = "Gustavo" # declaración + definición
nombre = "Omar" # redefinición
print(nombre)

numero = 10
numero += 1
print(numero)

# concatenación
bienvenida = "Hola " + nombre + " ¿Cómo estás?"
print(bienvenida)

# formateo con f Strings - convierte a texto
bienvenida = f"Hola {nombre} {numero} ¿cómo estás?"
print(bienvenida)

del nombre # borrando una variable
print(bienvenida) # sigue funcionando bien

# operadores de pertenencia
print("ola" in bienvenida)
print("Ola" in bienvenida)
print("ola" not in bienvenida)
