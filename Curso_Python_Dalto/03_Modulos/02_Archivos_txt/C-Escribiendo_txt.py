import os
import sys

ruta_areaTrabajo = os.getcwd()
sys.path.append(f"{ruta_areaTrabajo}")

nombres = ["Juan","Camila","Pedro","Lucas","Roberto"]
edades = [22,36,19,33,50]

# Con el parametro 'w' se crea el archivo y se sobreescibe su contenido
with open('Curso-Python\\03-Modulos\\02-Archivos-txt\\carpeta\\archivo_creado.txt','w',encoding="UTF-8") as archivo:
    archivo.writelines("• Los datos son:\n\n")
    for n,e in zip(nombres,edades):
        archivo.writelines(f"Nombre: {n}\nEdad: {e}\n\n")
    
# Con el parametro 'w' se crea el archivo y se sobreescibe su contenido
with open('Curso-Python\\03-Modulos\\02-Archivos-txt\\carpeta\\archivo_creado2.txt','w',encoding="UTF-8") as archivo:
    archivo.writelines(["Ejemplo de texto\n","prueba\n","escrito en el txt\n"])
    archivo.writelines(["Mas texto agregado\n","asdasdasd\n","en el txt\n"])
    
    
# Para anexar texto sin borrar lo que estaba antes, el parametro 'w' se debe
# reemplazar por 'a'
with open('Curso-Python\\03-Modulos\\02-Archivos-txt\\carpeta\\archivo_creado3.txt','a',encoding="UTF-8") as archivo:
    for i in range(0,5):
        archivo.writelines([f"Linea {i}\n","Ejemplo de texto\n","anexado\n\n"])
