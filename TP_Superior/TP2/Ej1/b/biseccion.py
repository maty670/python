import numpy as np
import math
import matplotlib.pyplot as plt


P1 = (-0.00648,-0.2674,-2.662,-6.959)
P9 = (0.1023,-0.3259,1.8,12.55)

def interseccion(Pa,Pb,x):
    C1 = Pa[0] - Pb[0]
    C2 = Pa[1] - Pb[1]
    C3 = Pa[2] - Pb[2]
    C4 = Pa[3] - Pb[3]
    print(f"{C1} % {C2} % {C3} % {C4}")
    return C1*x**3 + C2*x**2 + C3*x +C4

def biseccion(a,b,max_it,tol,I,Pa,Pb):
    it=0
    m=(a+b)/2.0
    while max_it>it and abs(I(Pa,Pb,m))>tol:
        m=(a+b)/2.0
        if np.sign(I(Pa,Pb,m))==np.sign(I(Pa,Pb,a)):
            a=m
        else:
            b=m    
        it+=1

    return m,I(Pa,Pb,m),it

#biseccion(extremo_A,extremo_b,max_iteraciones,tolerancia,funcion)
raiz,residuo,iteraciones=biseccion(-5,6,100,1e-30,interseccion,P1,P9)
print(f"Raiz: {raiz}")
print(f"Iteraciones: {iteraciones}")
print(f"Residuo: {residuo}")

'''    
# biseccion(extremo_A,extremo_b,max_iteraciones,tolerancia,funcion)
raiz,residuo,iteraciones=biseccion(-5,6,50,1e-10,f3)
print(f"Raiz: {raiz}")
print(f"Iteraciones: {iteraciones}")
print(f"Residuo: {residuo}")
'''