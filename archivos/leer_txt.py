archivo = open("archivos\\texto_de_dalto.txt", encoding="UTF-8")

# print(archivo)

# print(archivo.read())

# lineas = archivo.readlines()

# print(lineas)
# print(lineas[0])

linea = archivo.readline() # línea completa
print(linea)


linea = archivo.readline(2) # línea completa
print(linea)

archivo.close()
