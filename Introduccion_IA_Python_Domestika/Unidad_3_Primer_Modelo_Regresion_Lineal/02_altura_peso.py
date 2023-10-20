import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Lectura de un arhivo csv que contiene datos del Peso y Altura de 50 personas
datos = pd.read_csv("Introduccion_IA_Python_Domestika\\Unidad_3_Primer_Modelo_Regresion_Lineal\\altura_peso.csv")
# Graficar los datos
sb.scatterplot(x="Peso",y="Altura",data=datos,hue="Altura",palette="BuPu")
plt.title('Gráfico de Pesos(x) y Alturas(y)')
plt.show()
# Caracteristicas (X), etiqueta (y)
X = datos["Peso"]
y = datos["Altura"]
# Procesar X e y
X_procesada = X.values.reshape(-1,1)
y_procesada = y.values.reshape(-1,1)
# Creacion del modelo de Regresion Lineal
from sklearn.linear_model import LinearRegression
modelo = LinearRegression()
modelo.fit(X_procesada,y_procesada)
# Prueba del modelo de prediccion
peso = 33
prediccion = modelo.predict([[peso]])
print(f"Si el peso es {peso}, la prediccion de la altura es {prediccion}")


# Mostrando la recta de prediccion generada
datos=[]
for i in range (30,100):
    peso = int(i)
    prediccion = modelo.predict([[peso]])
    datos.append(prediccion[0][0])
plt.plot(datos,marker="o",linestyle="-")
plt.show()