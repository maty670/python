import numpy as np
import math
import matplotlib.pyplot as plt

# Funciones polinomicas en forma de tuplas
P1 = (-0.00648,-0.2674,-2.662,-6.959)
P2 = (-82.08,398.9,-651.7,371.8)
P3 = (-0.342,3.791,-16.47,26.26)
P4 = (0.4102,2.549,6.472,2.406)
P5 = (-0.0166,-0.5157,-3.794,-1.834)
P6 = (-0.007784,0.03998,-0.3053,-9.409)
P7 = (-0.003877,0.1498,-0.3954,-0.7499)
P8 = (0.0002778,-0.01556,0.7777,4.172)
P9 = (0.1023,-0.3259,1.8,12.55)

# Evaluar una funcion polinomica Px en un valor x
def f(Px,x):
    return Px[0]*x**3 + Px[1]*x**2 + Px[2]*x + Px[3]


def interseccion(Pa,Pb,x):
    C1 = Pa[0] - Pb[0]
    C2 = Pa[1] - Pb[1]
    C3 = Pa[2] - Pb[2]
    C4 = Pa[3] - Pb[3]
    return C1*x**3 + C2*x**2 + C3*x +C4

def derivada(Pa,Pb,x):
    C1 = Pa[0] - Pb[0]
    C2 = Pa[1] - Pb[1]
    C3 = Pa[2] - Pb[2]
    C4 = Pa[3] - Pb[3]
    return 3*C1*x**2 + 2*C2*x + C3

def newton_raphson(x0, tol, max_iter,Pa,Pb):
    it = 0
    x = x0

    while abs(interseccion(Pa,Pb,x)) > tol and it < max_iter:
        x = x - interseccion(Pa,Pb,x) / derivada(Pa,Pb,x)
        it += 1

    return x,interseccion(Pa,Pb,x) ,it

def biseccion(a,b,max_it,tol,Pa,Pb):
    it=0
    m=(a+b)/2.0
    while max_it>it and abs(interseccion(Pa,Pb,m))>tol:
        m=(a+b)/2.0
        if np.sign(interseccion(Pa,Pb,m))==np.sign(interseccion(Pa,Pb,a)):
            a=m
        else:
            b=m    
        it+=1
        
    #newton_raphson(x0,tolerancia,max_iterac,Pa,Pb)
    raiz,residuo,iteracionesNewton = newton_raphson(m,1e-10,50,Pa,Pb)  
    
    # Evaluar la raiz en el polinomio para obtener la imagen           
    fx = f(Pa,raiz)
    
    
    return raiz,fx,residuo,iteracionesNewton,it



#biseccion(extremo_A,extremo_b,max_iteraciones,tolerancia,Pa,Pb)
x1,y1,residuo_1,iteracionesNewton_1,iteracionesBiseccion_1 = biseccion(-8,-2,50,0.01,P4,P9)
print(f"Punto: P1({x1},{y1}) ")

