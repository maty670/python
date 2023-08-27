import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
import sys
ruta_areaTrabajo = os.getcwd()
sys.path.append(f"{ruta_areaTrabajo}")

df = pd.read_csv("Curso-Python\\03-Modulos\\04-Graficos\\Ventas_Diarias.csv")

################################################### Grafico con lineas ###################################################
sns.lineplot(x="Fechas",y="Ventas",data=df)
plt.plot("9/01",76576,"o")

plt.show()









################################################### Crear el gráfico de barras ###################################################
ax = sns.barplot(x="Fechas", y="Ventas", data=df)

# Mostrar el valor de cada venta en la parte superior de cada barra
for index, row in df.iterrows():
    plt.text(index, row['Ventas'], str(row['Ventas']), ha='center', va='bottom')



# Establecer los valores en el eje vertical
ax.set_yticks([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000])

# Rotar las etiquetas del eje x para mejorar la legibilidad
ax.set_xticklabels(df["Fechas"], rotation=90, ha="right")

plt.show()




################################################### Grafico de dispersion ###################################################
df = pd.read_csv("Curso-Python\\03-Modulos\\04-Graficos\\dispersion.csv")
sns.scatterplot(x="tiempo",y="dinero",data=df)
plt.show()