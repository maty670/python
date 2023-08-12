diccionario = dict(
    nombre = "qweq",
    apellido = "zxczxc",
    edad=30,
)



# Crear un diccionario a partir de 2 listas
keys = ("Nombre","Apellido","Edad",("calle","altura"))            # Tupla
values = ["Juan","Perez",18,"direccion 1234"]
diccionario = dict(zip(keys,values))
# >>>{'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 18, ('calle', 'altura'): 'direccion 1234'}

# Si en lugar de una Tupla tuviera una lista, habria que usar frozenset(lista) para poder implementar el diccionario





# Crear diccionarios a partir de un listado de claves
listado_keys = ["nombre","apellido","edad"]
diccionario_vacio = dict.fromkeys(listado_keys)
# >>>{'nombre': None, 'apellido': None, 'edad': None}
 
## Crear diccionarios a partir de un listado de claves pero con un valor para todas las claves
keys = ("Nombre","Apellido",("calle","altura"),"edad")
diccionario2 = dict.fromkeys(keys, "Vacio")
# >>>{'Nombre': 'Vacio', 'Apellido': 'Vacio', frozenset({'altura', 'calle'}): 'Vacio'}


