# creando una función

def saludar():
    print("Hola Lucas")
    
saludar()
saludar()
saludar()

def saludar(nombre):
    print(f"{nombre} cómo andás ?")
    
saludar("Gustavo")

# crear una función que devuelve valores

def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num 
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num_entero*2}"
    # print(contraseña)
    return (contraseña, num) # una tupla
    
# desempaquetando la función
passwd, numero = crear_contraseña_random(98)
print(f"tu contraseña es {passwd}")