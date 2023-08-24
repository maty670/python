# Escribir en un txt los datos de dos listas
nombres = ["Juan,Camila,Pedro,Lucas,Roberto"]
edad = [22,36,19,33,50]

import os
import sys

ruta_areaTrabajo = os.getcwd()
sys.path.append(f"{ruta_areaTrabajo}")

with open("Curso-Python\\03-Modulos\\04-Problemas-archivos\\nombres_edades.txt","w",encoding="UTF-8") as arch:
    arch.writelines("• Los datos son:\n")
    for n,e in zip(nombres,edad):
        arch.writelines(f"{e}\n")