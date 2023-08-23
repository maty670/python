# Leer un archivo txt de una manera mas optima

import os
import sys

ruta_areaTrabajo = os.getcwd()
sys.path.append(f"{ruta_areaTrabajo}")


# A diferencia open() en donde se tiene que cerrar el archivo con el metodo close(), 
# la declaración with cierra el archivo sin necesidad de que se lo indique

with open("conexion-agencia.txt",encoding="UTF-8") as archivo:
    # Almacenando el contenido del txt en un string
    texto_string = archivo.read()


with open("conexion-agencia.txt",encoding="UTF-8") as archivo:
    # Retornar todas las lineas del archivo como una lista[linea1,linea2,linea3,....]
    lineas = archivo.readlines()
    
