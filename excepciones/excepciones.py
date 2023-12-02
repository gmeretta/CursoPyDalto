def sumar_dos():
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            resultado = int(a) + int(b)
        except Exception as e:
           print("pedí un numero")
           print(f"Error {e} \n")       
        else:
            break
        finally:
            print("Siempre")
    return resultado

print(sumar_dos())