lista = ["Fruta","Carne","Verdura","Lacteo"]
print(f"Lista original: {lista}\n")


# Tamaño de la lista
print(f"Tamaño de la lista: {len(lista)}\n")                          


 # Agregar elemento al final de la lista
lista.append("elemento-final")                                     
print(f"Agregando un elemento al final de la lista: {lista}\n")


 # Agregar elemento en una posicion especifica
lista.insert(2,"elemento-posicionado")                             
print(f"Agregando un elemento en una posicion especifica: {lista}\n")


 # Agrega una lista al final
lista.extend([50,12,55,99,50,36,55,33])                                              
print(f"Agrega una lista al final de la primer lista: {lista}\n")


# Eliminar un elemento de una posicion dada
posicion = 4
elemento_eliminado = lista.pop(posicion)
print(f"Eliminando el elemento '{elemento_eliminado}' de la posicion {posicion}: {lista}\n")
