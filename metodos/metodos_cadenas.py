cadena1 = "Hola soy Gustavo"
cadena2 = "Bienvenido maquinola"

print(dir(cadena1)) # devuelve atributos válidos del objeto.

resultado = dir(cadena1) # función

print(resultado)

mayus = cadena1.upper() # método

print(mayus)

minus = cadena1.upper().lower() # método

print(minus)

# capitalize

# buscamos una cadena en otra cadena

busqueda_find = cadena1.find("la")
print (busqueda_find)
busqueda_find = cadena1.find("caca")
print (busqueda_find) # -1 si no encuentra
# con index nos lanza un error - ver excepciones

print(cadena1.isnumeric()) # False
print("5".isnumeric()) # True
print("5 ".isalpha()) # False
print(" u".isalpha()) # False
print("hhf".isalpha())
print(cadena1.count("a"))
print(cadena1.count("k")) # devuelve 0

print(len(cadena1)) # es una función no un método

# endswith
# startwith

print("hola".endswith("la"))

print("hola".replace("la","LA"))

# separar cadenas

cadena_separada = cadena1.split(" ")

print(cadena_separada[1])

