# Regresion Lineal
# Predecir grados Fahrenheit segun grados Celsius

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

datos = pd.read_csv("Introduccion_IA_Python_Domestika\\01_Regresion_Lineal\\celsius.csv")


# 'hue' -> Parámetro que se utiliza en algunas funciones para separar los datos en subconjuntos y representarlos con diferentes colores
# 'palette' -> Se utiliza para personalizar la gama de colores que se utilizarán al trazar datos categóricos en un gráfico
sb.scatterplot(x="celsius",y="fahrenheit",data=datos,hue="fahrenheit",palette="coolwarm")
plt.show()





# Caracteristicas (X), etiqueta (y)
# X.values = [-40 -10   0   8  15  22  38]
X = datos["celsius"]
y = datos["fahrenheit"]
print(type(X))
print(X.values,'\n\n')




# EL modelo necesita que este en otro formato: arreglos de 1 posicion
# [ [-40] [-10] [0] [8] [15] [22] [38] ]
X_procesada = X.values.reshape(-1,1)
y_procesada = y.values.reshape(-1,1)
print(type(X_procesada))
print(X_procesada)



# Creacion del modelo de Regresion Lineal, 'pip install -U scikit-learn'
from sklearn.linear_model import LinearRegression
modelo = LinearRegression()
# Entrenamiento
modelo.fit(X_procesada,y_procesada)
# Prediccion de un valor de grados Farenheit al ingresar
# un valor de grado Celsius
celcius = 50
print("Prediccion: ",modelo.predict([[celcius]]))

# Evaluacion(0 al 1) con las X e y para ver que tan bien entrenado
# quedo segun los datos
print("Evaluacion: ",modelo.score(X_procesada,y_procesada))