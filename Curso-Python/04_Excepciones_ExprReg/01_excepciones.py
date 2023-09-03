def dividir_dos():
    
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        
        #Intentando convertir los datos en numeros enteros
        try:
            resultado = int(a) / int(b)
        #Si lanzo una excepcion, mostrar mensaje de error
        except ValueError as e:
            print(f"ERROR: Los datos no son enteros \n{type(e).__name__}")
        except ZeroDivisionError as e:
            print(f"ERROR: Entero dividido por 0 \n{type(e).__name__}")
        #Si no lanzo una excepcion, salir del bucle
        else:
            break
        
    return resultado



print(dividir_dos())
