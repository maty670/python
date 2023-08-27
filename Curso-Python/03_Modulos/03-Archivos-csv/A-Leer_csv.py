import os
import sys

ruta_areaTrabajo = os.getcwd()
sys.path.append(f"{ruta_areaTrabajo}")


import pandas as pd

df = pd.read_csv("Curso-Python\\03-Modulos\\03-Archivos-csv\\archivo.csv")

# Listar 1er fila desde la cabecera
fila1 = df.head(1)
print(f"• Primera fila:\n{fila1}\n\n\n")

# Listar 1er y segunda fila desde la cabecera
fila1y2 = df.head(2)
print(f"• Primera y segunda filas:\n{fila1y2}\n\n\n")

# Listar ultima fila
fila_ultima = df.tail(1)
print(f"• Ultima fila:\n{fila_ultima}\n\n\n")

# Ordenar el DataFrame
df_ordenado = df.sort_values(by=['Edad'],ascending=True)
print(f"• DataFrame ordenado ascendente por edad:\n{df_ordenado}\n\n\n")

# Listar todos los elementos de una columna
columna_edad = df.loc[:,"Edad"]
print(f"• Listar todos los elementos de la columna Edad:\n{columna_edad}\n\n\n")

# Listar todos los elementos de una columna pero a partir de una fila especifica
columna_edad_ = df.loc[2:,"Edad"]
print(f"• Listar todos los elementos de una columna pero a partir de la fila 2:\n{columna_edad_}\n\n\n")

# Accediento a un elemento especifico del DataFrame
elemento_especifico = df.loc[2,'Edad']
print(f"• Accediendo a un elemento especifico(fila 1 columna Edad):\n{elemento_especifico}\n\n\n")

# Accediento a varios elementos especificos del DataFrame
elementos_especificos = df.loc[[0,2,4],['Apellido','Edad']]
print(f"• Accediendo a varios elementos especificos(fila 0,2,4 columnas Apellido y Edad):\n{elementos_especificos}\n\n\n")


# Accediendo a elementos especificos por posiciones
f1 = df.iloc[0] # Primera fila
f2 = df.iloc[1] # Segunda fila
fUlt = df.iloc[-1] # Última fila

c1 = df.iloc[:, 0] # Primera columna
c2 = df.iloc[:, 1] # Segunda columna
c3 = df.iloc[:, -1] # Última columna

df.iloc[0:5] # Primeras cinco filas
df.iloc[:, 0:5] # Primeras cinco columnas
df.iloc[[0,2,1]]  # Primera, tercera y segunda filas
df.iloc[:, [0,2,1]]  # Primera, tercera y segunda columnas

print(f"""



• Accediendo a filas especificas por posicion:

# Segunda Fila
{f2}

# Primera Columna
{c1}

# Primeras cinco filas
{df.iloc[0:5]}

# Primera y tercer columnas
{df.iloc[:, [0,2]]}

# Segunda y tercer filas con Primera y tercer columnas
{df.iloc[[1,2], [0,2]]}




""")


# Mostrar las filas segun un criterio
edad_mayor_30 = df.loc[df['Edad'] > 30]
print(f"• Filas con edad mayor a 30:\n{edad_mayor_30}\n\n\n")

# Mostrar las filas segun varios criterios y retornando algunas filas
edad_mayor_30_menor_40 = df.loc[(df['Edad'] > 30) & (df['Edad'] < 40),['Nombre','Edad']]
print(f"• Filas con edad mayor a 30 y menor a 40 pero retornando columnas nombre y edad:\n{edad_mayor_30_menor_40}\n\n\n")

# Concatenando 2 DataFrame
df2 = pd.read_csv("Curso-Python\\03-Modulos\\03-Archivos-csv\\archivo2.csv")
df_concatenado = pd.concat([df,df2])
print(f"• Concatenando 2 DataFrame:\n{df_concatenado}\n\n\n")

# Cantidad de filas y de columnas de un DataFrame (retorna una tupla)
print(f"• Cantidad de filas y de columnas del DataFrame concatenado:\n{df_concatenado.shape}\n\n\n")



# Cambiando el tipo de dato de una columna
df_concatenado["Edad"] = df_concatenado["Edad"].astype(str) 

# Eliminar filas duplicadas
df_concatenado = df_concatenado.drop_duplicates()
print(f"• Eliminando filas con valores repetidos:\n{df_concatenado}\n\n\n")


# Guardando el df_concatenado en un archivo nuevo
df_concatenado.to_csv("Curso-Python\\03-Modulos\\03-Archivos-csv\\archivo_concatenado.csv",index = False)





###### https://trinket.io/python3/b6682a1642