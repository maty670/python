import csv
import sys
import os

ruta_areaTrabajo = os.getcwd()
print(ruta_areaTrabajo)

with open(f"{ruta_areaTrabajo}\\Curso-Python\\03-Modulos\\03-Archivos-csv\\archivo.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print (row)



"""

import pandas as pd

df = pd.read_csv("archivo.csv")

# Listar en cabezados
encabezados = df.head()
for e in encabezados:
  print(e)

# Ordenar el DataFrame
df_ordenado = df.sort_values(by=['Edad'],ascending=False)
print(df_ordenado)

# Mostrar las filas segun un criterio
print(df.loc[df['Edad'] > 30])

# Mostrar las filas segun varios criterios y retornando algunas filas
print(df.loc[(df['Edad'] > 30) & (df["Edad"] < 40),["Nombre","Edad"]])

"""

# 06:33:00
# https://trinket.io/python3/b6682a1642