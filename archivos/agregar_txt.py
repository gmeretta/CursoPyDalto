with open('archivos\\texto_de_daltoW.txt', 'a', encoding="UTF-8") as archivo:
    # sobreescribiendo
    # archivo.write("jajajaja escirbiendo")
    archivo.writelines(["jajajaja escirbiendo linea\n", "otra línea\n"])
    archivo.writelines(["jajajaja escirbiendo linea\n", "otra línea\n"])
    archivo.writelines(["jajajaja escirbiendo linea\n", "otra línea\n"])
    archivo.writelines(["línea final"])