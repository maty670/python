import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

datos = pd.read_csv("Introduccion_IA_Python_Domestika\\03_Ejercicio_Regresion_Lineal\\datos_procesados.csv")
print(datos.head())

sb.scatterplot(x=datos["median_house_value"],y=datos["median_income"],data=datos)
plt.show()
