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



#biseccion(extremo_A,extremo_b,max_iteraciones,tolerancia,Polinomio_a,Polinomio_b)

x1,y1,residuo_1,iteracionesNewton_1,iteracionesBiseccion_1 = biseccion(-18,-14,50,0.01,P1,P5)
x2,y2,residuo_2,iteracionesNewton_2,iteracionesBiseccion_2 = biseccion(-5,-4,50,0.01,P1,P8)
x3,y3,residuo_3,iteracionesNewton_3,iteracionesBiseccion_3 = biseccion(-4,-3,50,0.01,P1,P9)
x4,y4,residuo_4,iteracionesNewton_4,iteracionesBiseccion_4 = biseccion(-2,-1,50,0.01,P1,P4)
x5,y5,residuo_5,iteracionesNewton_5,iteracionesBiseccion_5 = biseccion(-4,-3,50,0.01,P4,P6)
x6,y6,residuo_6,iteracionesNewton_6,iteracionesBiseccion_6 = biseccion(0,1,50,0.01,P1,P6)
x7,y7,residuo_7,iteracionesNewton_7,iteracionesBiseccion_7 = biseccion(1,3,50,0.01,P1,P2)
x8,y8,residuo_8,iteracionesNewton_8,iteracionesBiseccion_8 = biseccion(1,3,50,0.01,P2,P5)
x9,y9,residuo_9,iteracionesNewton_9,iteracionesBiseccion_9 = biseccion(2,3,50,0.01,P2,P6)
x10,y10,residuo10_1,iteracionesNewton_10,iteracionesBiseccion_10 = biseccion(5,7,50,0.01,P3,P6)
x11,y11,residuo_11,iteracionesNewton_11,iteracionesBiseccion_11 = biseccion(3,4,50,0.01,P3,P7)
x12,y12,residuo_12,iteracionesNewton_12,iteracionesBiseccion_12 = biseccion(14,16,50,0.01,P7,P8)
x13,y13,residuo_13,iteracionesNewton_13,iteracionesBiseccion_13 = biseccion(2,3,50,0.01,P2,P8)
x14,y14,residuo_14,iteracionesNewton_14,iteracionesBiseccion_14 = biseccion(1,3,50,0.01,P2,P9)
x15,y15,residuo_15,iteracionesNewton_15,iteracionesBiseccion_15 = biseccion(-3,-2,50,0.01,P5,P9)
x16,y16,residuo_16,iteracionesNewton_16,iteracionesBiseccion_16 = biseccion(-6,-5,50,0.01,P5,P7)


print(f"""Punto1({x1},{y1})
Punto2({x2},{y2})
Punto3({x3},{y3})
Punto4({x4},{y4})
Punto5({x5},{y5})
Punto6({x6},{y6})
Punto7({x7},{y7})
Punto8({x8},{y8})
Punto9({x9},{y9})
Punto10({x10},{y10})
Punto11({x11},{y11})
Punto12({x12},{y12})
Punto13({x13},{y13})
Punto14({x14},{y14})
Punto15({x15},{y15})
Punto16({x16},{y16})
""")



