###### Importar un archivo y usar una funcion
import calcular_primos as pr
listado_primos = pr.numeros_primos(50)
print(listado_primos)









###################### Importar un archivo desde otra carpeta cambiando la ruta actual ###############

import sys

#print(sys.path) lista de nombres de directorios que constituye la ruta de búsqueda actual
#sys.path.append("d:\\Datos\\Desktop\\python\\Curso-Python\\03-Modulos\\carpeta")









import os
# obtener la ruta absoluta del directorio de trabajo actual
ruta_areaTrabajo = os.getcwd()

# obtener la ruta especificada del archivo
dir_archivo = __file__
sys.path.append(f"{ruta_areaTrabajo}\\Curso-Python\\03-Modulos\\01_Modulos")

# Luego de cambiar la ruta actual, se puede importar el modulo
import calcular_primos as cp
listado = cp.numeros_primos(500)
print (listado)


