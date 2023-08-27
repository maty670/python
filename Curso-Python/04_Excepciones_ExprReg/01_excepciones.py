def sumar_dos():
    
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            return int(a) + int(b)
        except:
            print("Datos invalidos. No se pudo ejecutar la suma")
        
print(sumar_dos())