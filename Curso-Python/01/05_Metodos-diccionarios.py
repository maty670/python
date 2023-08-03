diccionario = {
    "nombre": "Lucas",
    "apellido": "Gonzalez",
    "Edad": 30
}

# Retornar las keys del diccionario
print(f"Claves del diccionario: {diccionario.keys()}")

# Obtener el valor de una clave. 
# Con el metodo get() si no encuentra la clave, lanza un 'None' y el programa continua en lugar de lanzar una excepcion
print(f"Valor de la clave 'nombre': {diccionario.get('nombre')}")


# Eliminar un elemento del diccionario por una key
elemento_eliminado = diccionario.pop("Edad")
print(f"Se elimino un elemento '{elemento_eliminado}' ---> {diccionario}")

# Para iterar el dict
print(diccionario.items())