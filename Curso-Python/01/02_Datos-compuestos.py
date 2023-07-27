lista = ["Cadena",75,"23","Abc","Cadena"]
tupla = ("Cadena",75,"23","Abc","Cadena")
conjunto = {"Cadena",75,"23","Abc","Cadena"}
# La tupla y el conjunto son iguales a la lista pero no 
# se pueden modificar sus elementos. Los conjuntos a su vez
# presentan sus datos desordenados, no se pueden acceder a
# sus elementos por sus indices [i], y no puede haber
# repetidos


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


    
