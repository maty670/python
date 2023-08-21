numeros_duplicados = [2,4,6,8,10]
list = []
for n in numeros_duplicados:
    list.append(n*2)
# list >> [4, 8, 12, 16, 20]

# Otra manera mas simple de hacerlo
list = [x*2 for x in numeros_duplicados] 
# list >> [4, 8, 12, 16, 20]













animales = ["Gato","Perro","Loro","Vaca","Gallina","Tiburon","Tigre","Aguila"]
colores = ["Negro","Blanco","Marron","Blanco","Marron","Gris","Blanco","Negro"]

# El continue se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar
# El break cierra el bucle todo el codigo posterior no se ejecuta (ni siquiera los else)
for animal in animales:
    if animal=="Gato":
        continue
    if animal=="Tiburon":
        break
    
"""
>> Perro
>> Loro
>> Vaca
>> Gallina
"""









# Para iterar 2 listas del mismo tamaño al mismo tiempo con zip()
for a,c in zip(animales,colores):
    a,c
""" 
print((f"{a} - {c}"))
 >> Gato - Negro
 >> Perro - Blanco
 >> Loro - Marron
 >> Vaca - Blanco
 >> ...
"""







# Iterar entre un rango numerico con range(inicio,final,incremento)
for num in range(1,10,2):
    num                     #1,3,5,7,9













# Recorrer una lista con su indice
# x es una tupla c: (indice,valor)
for x in enumerate(animales):
    Indice = x[0]     # Indice >>> 0,1,2,3
    Valor = x[1]      # Valor  >>> Gato,Perro,Loro,Vaca
















################## Almacenando diccionarios dentro de una lista personas[]    
personas=[]  

keys = ("Nombre","Apellido","Edad",("calle","altura"))         
values1 = ["Juan","Perez",18,"direccion 1234"]       
values2 = ["Lucas","Gonzalez",29,"direccion 5678"]      
values3 = ["Pedro","Lopez",14,"direccion 0101"]

personas.append(dict(zip(keys,values1)))
personas.append(dict(zip(keys,values2)))
personas.append(dict(zip(keys,values3)))

# Recorriendo listado con diccionarios
for per in personas:
    (f"{per[keys[0]]} - {per[keys[1]]} - {per[keys[2]]} - {per[keys[3]]} ")
    
""""
>> Juan - Perez - 18 - direccion 1234
>> Lucas - Gonzalez - 29 - direccion 5678   
>> Pedro - Lopez - 14 - direccion 0101
"""


"""
Otra manera seria:
for per in personas:
    for key_value in per.items():
        key = key_value[0]
         value = key_value[1]
        print(f'{key} - {value}')
"""


######################################################################
 