lista = ["qweqwe",32]
dato1,dato2 = lista
#print(dato2)




"""
Cuando usar tuplas '()' :
Las tuplas son una excelente opción si lo que quieres es que los datos de tu colección sean de solo lectura, que nunca cambien y 
se mantengan constantes. Tienen la capacidad de garantizar que los datos que contienen nunca serán alterados.
Las tuplas pueden utilizarse como claves en un diccionario siempre que contengan tipos inmutables (cadenas, números u otras tuplas).

Cuando usar listas '[]' :
Por otro lado, las listas pueden ser fácilmente modificadas, ya que son mutables.
Se puede añadir elementos, eliminarlos, cambiarlos de posición o intercambiar unos por otros.
Las listas son útiles si lo que quieres es que tus datos sean flexibles, que puedan ser modificados cuando sea necesario.
Las listas soportan una variedad de métodos incorporados de Python que llevan a cabo ciertas operaciones sobre ellas, operaciones no soportadas por la tuplas.

Conjuntos '{}' :
Iguales a las tuplas pero Los conjuntos no permiten elementos duplicados y presentan sus datos desordenados
Ademas no se pueden acceder a sus elementos por sus indices [i]
"""

# Para colocar un conjunto dentro de otro conjunto
# Utilizar la funcion 'frozenset' en el subconjunto
# Congela la lista y la hace inmutable
subconjunto1 = frozenset(["aaa","bbb",111,"qweqweqwe"])             # Lista
subconjunto2 = frozenset(("ccc","ddd",333,"zxczxczxc"))             # Tupla
conjunto = {subconjunto1,subconjunto1,subconjunto2,1010,1010,1010,"zzz","zzz"}
print(conjunto)



# Verificar si un conjunto es un subconjunto
conjunto1 = {1,2,3,4,5,6,7}
conjunto2 = {1,3,6}                     # El conjunto2 es un subconjunto del conjunto1
conjunto3 = {1,3,5,10,15}               # El conjunto2 NO es un subconjunto del conjunto1
print(conjunto2.issubset(conjunto1))


# Comprobar si dos conjuntos tienen elementos completamente distintos
conjunto1 = {1,3,5,7,9}
conjunto2 = {2,4,6,8,10}                # El conjunto2 tiene todos sus elementos distintos al conjunto1
conjunto3 = {"a","b","c",1}             # El conjunto3 tiene uno de sus elementos iguales al conjunto1, isdisjoint() sera falso
print(conjunto1.isdisjoint(conjunto2))