import re

texto = """Hola maestro. esta es la cadena 173837). como estas mi capitan
Esta es la segunda linea 22) de texto
y esta ess la final (linea 356) definitivamente mi ababab capitan"""

resultado = re.search("Hola", texto)
resultado = re.findall("esta", texto, flags = re.IGNORECASE)

resultado = re.findall(r"\d", texto)
resultado = re.findall(r"\D", texto) # todo menos dígitos

resultado = re.findall(r"\w", texto)
resultado = re.findall(r"\W", texto)
resultado = re.findall(r"\s", texto)
resultado = re.findall(r"\S", texto)
resultado = re.findall(r".", texto)
resultado = re.findall(r"\n", texto)
resultado = re.findall(r"\.", texto)
resultado = re.findall(r"\d\.\s", texto)
resultado = re.findall(r"^Hola", texto)
resultado = re.findall(r"an$", texto)
resultado = re.findall(r"$", texto, flags =re.M)
resultado = re.findall(r"\d{3,4}\)", texto, flags =re.M)
resultado = re.findall(r"(ab){2,4}", texto)
resultado = re.findall(r"[ab]{2,4}", texto)
resultado = re.findall(r"\d{2,4}|Hola", texto)

print (resultado)