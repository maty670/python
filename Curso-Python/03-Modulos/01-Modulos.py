###### Importar un archivo y usar una funcion
import carpeta.calcular_primos as pr
listado_primos = pr.numeros_primos(50)
print(listado_primos)




###### Importar un archivo desde otra carpeta cambiando la ruta actual

import sys

#print(sys.path) lista de nombres de directorios que constituye la ruta de búsqueda actual
sys.path.append("d:\\Datos\\Desktop\\python\\Curso-Python\\03-Modulos\\carpeta")

# Luego de cambiar la ruta actual, se puede importar el modulo
import calcular_primos as cp
listado = cp.numeros_primos(100)
print (listado)

