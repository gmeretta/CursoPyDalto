class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Impresionante, cometiste el siguiente error: {err}")
        
# raise ZeroDivisionError("lanzo una excepción")

try:
    raise MiExcepcion("Atención !!! Excepción Cool")
except:
    print("como va a cometer ese error?")