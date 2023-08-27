import os
import sys

ruta_areaTrabajo = os.getcwd()
sys.path.append(f"{ruta_areaTrabajo}")





# Abriendo el archivo txt
file = open("conexion-agencia.txt",encoding="UTF-8")

# Almacenando el contenido del txt en un string
texto_string = file.read()


# Cerrando el archivo, de lo contrario no se podria leer nuevamente por motivos de seguridad
file.close()







# Abriendo el archivo txt
file = open("conexion-agencia.txt",encoding="UTF-8")

# Retornar todas las lineas del archivo como una lista[linea1,linea2,linea3,....]
lineas = file.readlines()

# Cerrando el archivo
file.close()


# Si quisiera ir leyendo linea por linea, deberia usar file.readline(). Asi no se lee todo el archivo
# completo en una sola instruccion