animales = ["Gato","Perro","Loro","Vaca"]
colores = ["Negro","Blanco","Marron","Blanco"]








# Para iterar 2 listas del mismo tamaño al mismo tiempo con zip()
for a,c in zip(animales,colores):
    (f"{a} - {c}")
""" 
 > Gato - Negro
 > Perro - Blanco
 > Loro - Marron
 > Vaca - Blanco
"""







# Iterar entre un rango numerico con range(inicio,final,incremento)
for num in range(1,10,2):
    num             #1,3,5,7,9













# Recorrer una lista con su indice
# x es una tupla c: (indice,valor)
for x in enumerate(animales):
    Indice = x[0]     # Indice >>> 0,1,2,3
    Valor = x[1]      # Valor  >>> Gato,Perro,Loro,Vaca
















############### Almacenando diccionarios dentro de una lista personas[]    
personas=[]  

keys = ("Nombre","Apellido","Edad",("calle","altura"))         
values1 = ["Juan","Perez",18,"direccion 1234"]       
values2 = ["Lucas","Gonzalez",29,"direccion 5678"]      
values3 = ["Pedro","Lopez",14,"direccion 0101"]

personas.append(dict(zip(keys,values1)))
personas.append(dict(zip(keys,values2)))
personas.append(dict(zip(keys,values3)))

for per in personas:
    (f"{per[keys[0]]} - {per[keys[1]]} - {per[keys[2]]} - {per[keys[3]]} ")
""""
Juan - Perez - 18 - direccion 1234
Lucas - Gonzalez - 29 - direccion 5678   
Pedro - Lopez - 14 - direccion 0101
"""
######################################################################
#03:48:51   