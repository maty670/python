n = input("INGRESE UN NUMERO ENTRE 1 Y 100\n")
n = int(n)

if n > 0 and n <=100:
    print(f"¡Muy bien! El {n} es una gran opción")
elif n < 1:
    print("Favor de ingresar un número mayor a 0")
elif n > 100:
    print("Favor de ingresar un número menor o igual a 100")
    