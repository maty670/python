import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# longitude latitude  housing_median_age        total_rooms         total_bedrooms      population      households  median_income   median_house_value  ocean_proximity
# longitud  latitud   antiguedad_media_vivienda total_habitaciones  total_dormitorios   población       hogares     ingreso_medio   valor_casa_mediana  proximidad_oceánica

datos = pd.read_csv("Introduccion_IA_Python_Domestika\\Unidad_4_Algoritmos_de_machine_learning\\02_Ejercicio_Regresion_Lineal\\datos_procesados.csv")
print("Cabeceras:")
print(datos.head())

sb.scatterplot(x=datos["median_house_value"],y=datos["median_income"],data=datos)
plt.title("Entre mas ingresos hay, mas cuestan las casas")
plt.show()

# Separar las caracteristicas de las etiquetas
X = datos.drop(["median_house_value"],axis=1)
y = datos["median_house_value"]

# Separar los datos en 2 partes:  
# Un conjunto de entrenamiento para ajustar y mejorar
# Y uno de pruebas con datos que no en el entrenamiento para probarlo y ver si efectivamente aprendio

from sklearn.model_selection import train_test_split

# Funcion que nos va a separar los datos
# test_size -> Cuanto queremos separar para pruebas (.2 es un 20%)
#
X_entrenamiento,X_pruebas,y_entrenamiento,y_pruebas = train_test_split(X,y,test_size=.2)

'''
X_entrenamiento.shape -> (16346 registros, 13 columnas)
y_entrenamiento.shape -> (16346 registros, 1 columnas)
X_pruebas -> (4087 registros, 13 columnas)
y_pruebas -> (4087 registros, 1 columnas)
'''

from sklearn.linear_model import LinearRegression
# Crear modelo
modelo = LinearRegression()
# Entrenar modelo
modelo.fit(X_entrenamiento,y_entrenamiento)

# Generar predicciones con los datos de pruebas y comparar estas predicciones con los valores reales de estos datos de pruebas
predicciones = modelo.predict(X_pruebas)
comparativa = {"Prediccion": predicciones,"Valor Real": y_pruebas}
dataFrame = pd.DataFrame(comparativa)
print(dataFrame)
# Arroja resultados inconsistentes. Algunas predicciones se aproximan muy bien al valor real, pero otras predicciones estan muy lejos del valor real
# Esto ocurre porque existen muchos datos y la linea de regresion lineal batalla por adaptarse
# Algunas veces el modelo funciona muy bien con los datos de entrenamiento pero muy mal con los de pruebas (overfitting o sobreajuste), y significa
# que se aprende mucho los datos de entrenamiento pero luego no puede generalizar