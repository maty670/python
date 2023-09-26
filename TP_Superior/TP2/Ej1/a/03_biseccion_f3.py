import numpy as np
import math
import matplotlib.pyplot as plt


# Funcion f1(x)
def f1(x):
    return x*np.exp(-x/2)

# Funcion f2(x)
def f2(x):
    return math.atan(x)

# Funcion f3(x)
def f3(x):
    return (-1)*math.cos(abs(x) + math.pi/4) + 0.8

def biseccion(a,b,max_it,tol,f):
    it=0
    m=(a+b)/2.0
    while max_it>it and abs(f(m))>tol:
        m=(a+b)/2.0
        if np.sign(f(m))==np.sign(f(a)):
            a=m
        else:
            b=m    
        it+=1

    return m,f(m),it
    
# biseccion(extremo_A,extremo_b,max_iteraciones,tolerancia,funcion)
raiz,residuo,iteraciones=biseccion(-5,6,50,1e-10,f3)
print(f"Raiz: {raiz}")
print(f"Iteraciones: {iteraciones}")
print(f"Residuo: {residuo}")
