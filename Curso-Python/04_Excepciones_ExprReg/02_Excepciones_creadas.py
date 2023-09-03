# Creando excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Cometiste el siguiente error: {err}")

# Lanzando y manejando la excepcion
try:
    raise MiExcepcion("ERROR-002")
except:
    print("Excepcion capturada")