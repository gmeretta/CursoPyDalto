nombres = ["Lucas", "Matías", "Camila", "Pedro", "Roberto"]
apellidos = ["Dalto", "Zing", "Dalto", "Robertix", "Tarado"]

# registrar información en un TXT

with open ("archivos_problemas_resueltos\\nombres_y_apellidos.txt", "w", encoding = "UTF-8") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------------\n") for n,a in zip(nombres, apellidos)]
    
# esto es lo mismo
# for n,a in zip(nombres, apellidos) :
#     arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------------\n")