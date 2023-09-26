import numpy as np
import math
import matplotlib.pyplot as plt

# Funcion f1(x)
def f1(x):
    return x*np.exp(-x/2)
# Derivada f1'(x)
def df1(x):
    return np.exp(-x/2) - (x/2)*np.exp(-x/2)

# Funcion f2(x)
def f2(x):
    return math.atan(x)

# Derivada f2'(x)
def df2(x):
    return 1 / (1 + x**2)

# Funcion f3(x)
def f3(x):
    return (-1)*math.cos(abs(x) + math.pi/4) + 0.8

# Derivada f3'(x)
def df3(x):
    return x*(math.sin(abs(x)) + math.cos(abs(x))) / (math.sqrt(2) * abs(x))
    #return (f3(x-1)-f3(x)) / ((x-1) - x)



def newton_raphson(x0, tol, max_iter,f,df):
    it = 0
    x = x0

    while abs(f(x)) > tol and it < max_iter:
        x = x - (f(x) / df(x))
        it += 1

    return x,f(x) ,it



# newton_raphson(x0, tolerancia,max_it,funcion,derivada)
raiz,residuo,iteraciones = newton_raphson(0.5, 1e-10,50,f3,df3)

# Resultado
print(f"Raíz: {raiz}")
print(f"Iteraciones: {iteraciones}")
print(f"Residuo: {residuo}")
