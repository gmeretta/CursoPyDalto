# creando diccionarios con dict()

diccionario = dict(nombre = "Gustavo", apellido = "Meretta") # este formato permite diccionarios vacíos
otroDict = {
    'nombre' :"gustavo",
    'apellido' : "meretta"
}


# creando diccionario con fromkeys

diccionario = dict.fromkeys("nombre", "apellido")
print (diccionario)

diccionario = dict.fromkeys(["nombre", "apellido", "suscriptores"])
print (diccionario)

diccionario = dict.fromkeys("ABCD") # primer dato es un iterable
print (diccionario)