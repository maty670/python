# longitude latitude  housing_median_age        total_rooms         total_bedrooms      population      households  median_income   median_house_value  ocean_proximity
# longitud  latitud   antiguedad_media_vivienda total_habitaciones  total_dormitorios   población       hogares     ingreso_medio   valor_casa_mediana  proximidad_oceánica


import matplotlib.pyplot as plt
import pandas as pd
datos = pd.read_csv("Introduccion_IA_Python_Domestika\\02_Set_y_Analisis_de_Datos\\housing.csv")



# Histogramas: bins-> Cantidad de barras por histograma
# edgecolor -> Color del borde de las barras

datos.hist(figsize=(15,8),bins=30,edgecolor="black")
plt.show()


# Grafico de dispersion
# hue -> hacer que el color dependa del precio de la casa
# s -> tamaño de los circulos hacer que dependa de la poblacion
import seaborn as sb
sb.scatterplot(x="latitude",y="longitude",data=datos,
               hue="median_house_value",palette="coolwarm",
               s=datos["population"]/100)
plt.show()


# Grafico de dispersion
# datos.median_income > 10  -> filtrar por ingreso medio > 10
import seaborn as sb
sb.scatterplot(x="latitude",y="longitude",data=datos[datos.median_income > 10],
               hue="median_house_value",palette="coolwarm")
plt.show()