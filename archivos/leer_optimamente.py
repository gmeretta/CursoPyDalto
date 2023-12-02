with open("archivos\\texto_de_dalto.txt", encoding="UTF-8") as archivo: # se abre y se cierra
    contenido = archivo.read()
    print (contenido)