texto = input("Ingrese un texto cualquiera:\n")

while True:
    
    repeticiones = input("¿ Cuantas veces quiere que el texto se repita ?\n")
    repeticiones = int(repeticiones)
    
    if (repeticiones <=0):
        print("El numero debe ser mayor a 0, vuelva a intentarlo")
    else:
        for x in range(0,repeticiones):
            print(f"{texto}") 
        break
