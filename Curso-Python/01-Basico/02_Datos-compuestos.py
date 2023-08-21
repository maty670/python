listaVacia = list()
tuplaVacia = tuple()
conjuntoVacio = set()

lista = ["Cadena",75,"23","Abc","Cadena"]
tupla = ("Cadena",75,"23","Abc","Cadena")
conjunto = {"Cadena",75,"23","Abc","Cadena"}

"""
Cuando usar tuplas:
Las tuplas son una excelente opción si lo que quieres es que los datos de tu colección sean de solo lectura, que nunca cambien y 
se mantengan constantes. Tienen la capacidad de garantizar que los datos que contienen nunnca serán alterados.
Las tuplas pueden utilizarse como claves en un diccionario siempre que contengan tipos inmutables (cadenas, números u otras tuplas).

Cuando usar listas:
Por otro lado, las listas pueden ser fácilmente modificadas, ya que son mutables.
Se puede añadir elementos, eliminarlos, cambiarlos de posición o intercambiar unos por otros.
Las listas son útiles si lo que quieres es que tus datos sean flexibles, que puedan ser modificados cuando sea necesario.
Las listas soportan una variedad de métodos incorporados de Python que llevan a cabo ciertas operaciones sobre ellas, operaciones no soportadas por la tuplas.

Conjuntos:
Iguales a las tuplas pero Los conjuntos no permiten elementos duplicados y presentan sus datos desordenados
"""


print(f"""
      lista: {lista}
      tupla : {tupla}
      conjunto: {conjunto}
      """)


for x in lista:
    if isinstance(x, int): 
        print(f"Int: {x}")
    if isinstance(x, str): 
        if x.isnumeric():
            print(f"String numerico: {x}")
        else:
            print(f"String: {x}")
            
            
#----------------------------------------------------------------------------------
diccionario = {
    "Nombre": "qweqwe",
    "Edad": 56,
    "Telefono": 4534646,
    "Altura": 1.75
}

print("#######################")
print(diccionario["Nombre"])
print(diccionario["Edad"])
print(diccionario["Telefono"])
print(diccionario["Altura"])

print("qweqeqwe")


    
