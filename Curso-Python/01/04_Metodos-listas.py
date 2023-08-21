lista = ["Fruta","Carne","Verdura","Lacteo"]
print(f"Lista original: {lista}\n")


# Tamaño de la lista
print(f"Tamaño de la lista: {len(lista)}\n")                          


 # Agregar elemento al final de la lista
lista.append("elemento-final")                                     
print(f"Agregando un elemento al final de la lista: {lista}\n")

# Ver el ultimo elemento de una lista
print(f"Ultimo elemento de la lista: {lista[-1]}\n")


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

# Remover un elemento por su valor
valor = 50
elemento_removido = lista.remove(valor)
print(f"Removiendo valor {elemento_removido}: {lista}\n")



# Ordenar una lista
car = ['Ford', 'BMW', 'Volvo']
car.sort()
print(f"Lista ordenada alfabeticamente: {car}\n")



# Ordenar una lista por una key
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

def getCar(e):
  return e['car']

def getAño(e):
  return e['year']

cars.sort(key=getAño)

print(f"Listado ordenado a partir de una key: {cars}\n")
