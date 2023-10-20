# longitude latitude  housing_median_age        total_rooms         total_bedrooms      population      households  median_income   median_house_value  ocean_proximity
# longitud  latitud   antiguedad_media_vivienda total_habitaciones  total_dormitorios   población       hogares     ingreso_medio   valor_casa_mediana  proximidad_oceánica


import pandas as pd
datos = pd.read_csv("Introduccion_IA_Python_Domestika\\Unidad_4_Algoritmos_de_machine_learning\\01_Set_y_Analisis_de_Datos\\housing.csv")


# Ver cabeceras
print(datos.head())

# Analizar la informacion: cantidad,media,std,minimo,25%,50%,75%,maximo
print("\n\n\n")
print("DESCRIPCION DE DATOS:\n",datos.describe())

# total_bedrooms tiene casi 200 valores vacios
print("\n\n\n")
print("INFO DE DATOS: ")
print(datos.info())




######################################## Acondicionar el Set de datos ########################################
# Borrando los datos vacios
datos_na = datos.dropna()
print("\n\n\n")
print("INFO DE DATOS NUEVOS: ")
print(datos_na.info())

# value_counts() -> Devuelve un objeto que contiene recuentos de valores únicos. El objeto resultante estará en orden descendente para que el primer 
# elemento sea el elemento que aparece con más frecuencia. Excluye los valores NA de forma predeterminada
# Convertir la caracteristica categorica a numerica de 'ocean_proximity'
datos_na["ocean_proximity"].value_counts()
'''
<1H OCEAN     9034
INLAND        6496
NEAR OCEAN    2628
NEAR BAY      2270
ISLAND           5
'''
# Existen 5 categorias posibles de "ocean_proximity", por lo que puede hacerse una conversion numerica
# <1H OCEAN, INLAND, NEAR OCEAN, NEAR BAY, ISLAND = 1, 2, 3, 4, 5
# El problema de esta conversion es que los modelos cuando estan entrenando al ver 1 2 3 4 y 5
# pueden darle mayor peso a los que tienen 5 porque numericamente son mas grandes. Para solucionar esto se usan Dummies / One-Hot Enconding

'''
<1H OCEAN   INLAND  NEAR OCEAN  NEAR BAY    ISLAND
    1          0        0           0         0
    0          0        0           1         0
    0          1        0           0         0
    0          0        0           0         1
    0          0        0           0         1
    1          0        0           0         0
'''

#Obtener Dummies
dummies = pd.get_dummies(datos_na["ocean_proximity"],dtype=int)
print("\n\n\n")
print("DUMMIES: ")
print(dummies)

# Agregando los Dummies al los datos_na
datos_na = datos_na.join(dummies)

# Borrando la columna ocean_proximity que ya no la necesitamos (axis=1 se refiere a que quiero borrar una columna llamada 'ocean_proximity')
datos_na = datos_na.drop(["ocean_proximity"],axis=1)
print("\n\n\n")
print("DATOS SIN 'ocean_proximity' con DUMMIES:\n",datos_na.head())

# Guardando el df_concatenado en un archivo nuevo
datos_na.to_csv("Introduccion_IA_Python_Domestika\\Unidad_4_Algoritmos_de_machine_learning\\02_Ejercicio_Regresion_Lineal\\datos_procesados.csv",index = False)


####################################### Correlaciones #######################################
import seaborn as sb
import matplotlib.pyplot as plt
correlaciones = datos_na.corr()

# Los 1 representan una relacion perfecta y -1 una relacion perfecta a la inversa(uno sube y el otro baja) y el 0 no hay relacion
# La diagonal es siempre 1 porque es el contraste de un dato consigo mismo
# • Fuerte relacion entre el valor_casa_mediana(median_house_value) y el ingreso_medio(median_income). A mayor valor de la casa, mayor sera el ingreso medio de la gente
sb.heatmap(correlaciones,annot=True,cmap="YlGnBu")
plt.show()



# Correlaciones unicamente del valor medio de una casa con el resto de caracteristicas
correlaciones_valorMedioCasa = datos_na.corr()["median_house_value"].sort_values(ascending=False)
df = pd.DataFrame(correlaciones_valorMedioCasa)
ax = df.plot(kind='bar')

for i, v in enumerate(correlaciones_valorMedioCasa):
    ax.text(i, v , str(round(v,4)), ha='center')
plt.show()