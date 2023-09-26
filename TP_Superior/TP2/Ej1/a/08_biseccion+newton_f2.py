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
        x = x - f(x) / df(x)
        it += 1

    return x,f(x) ,it



def biseccion(a,b,max_it,tol,f,df):
    it=0
    m=(a+b)/2.0
    while max_it>it and abs(f(m))>tol:
        m=(a+b)/2.0
        if np.sign(f(m))==np.sign(f(a)):
            a=m
        else:
            b=m    
        it+=1

    raiz,residuo,iteracionesNewton = newton_raphson(m,1e-10,50,f,df)
    return raiz,residuo,it,iteracionesNewton
    
# biseccion(extremo_A,extremo_b,max_iteraciones,tolerancia,funcion,derivada)
raiz,residuo,iteracionesBiseccion,iteracionesNewton = biseccion(-5,6,50,0.1,f2,df2)
print(f"Raiz: {raiz}")
print(f"Iteraciones: Biseccion({iteracionesBiseccion}) + Newton({iteracionesNewton})")
print(f"Residuo: {residuo}")

