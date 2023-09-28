import numpy as np
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





###################################################  Grafica del Colibri ###################################################

plt.figure(figsize=(8, 6))
plt.xlim(-20, 20)
plt.ylim(-20, 20)


# Graficar los puntos hallados con Biseccion y Newwon
plt.scatter(x1, y1, color='y', marker='o', label='P1')
#plt.scatter(x2, y2, color='y', marker='o', label='P2')              # Punto 2 es un punto que sobra y no era necesario para calcular el colibri
#plt.scatter(x3, y3, color='y', marker='o', label='P3')              # Punto 3 es un punto que sobra y no era necesario para calcular el colibri
plt.scatter(x4, y4, color='y', marker='o', label='P4')
plt.scatter(x5, y5, color='y', marker='o', label='P5')
#plt.scatter(x6, y6, color='y', marker='o', label='P6')              # Punto 6 es un punto que sobra y no era necesario para calcular el colibri
#plt.scatter(x7, y7, color='y', marker='o', label='P7')              # Punto 7 es un punto que sobra y no era necesario para calcular el colibri
#plt.scatter(x8, y8, color='y', marker='o', label='P8')              # Punto 8 es un punto que sobra y no era necesario para calcular el colibri
#plt.scatter(x9, y9, color='y', marker='o', label='P9')              # Punto 9 es un punto que sobra y no era necesario para calcular el colibri
plt.scatter(x10, y10, color='y', marker='o', label='P10')
plt.scatter(x11, y11, color='y', marker='o', label='P11')
plt.scatter(x12, y12, color='y', marker='o', label='P12')
plt.scatter(x13, y13, color='y', marker='o', label='P13')
plt.scatter(x14, y14, color='y', marker='o', label='P14')
plt.scatter(x15, y15, color='y', marker='o', label='P15')
plt.scatter(x16, y16, color='y', marker='o', label='P16')



# Graficar Polinomio P1 primero entre el punto 1 y el punto 4, y luego entre punto 6 y el punto 7
P1_intervalo1 = np.linspace(x1, x4, 100)
plt.plot(P1_intervalo1, f(P1,P1_intervalo1), color='g')


# Graficar Polinomio P2 primero entre el punto 14 y el punto 13, y luego entre punto 9 y el punto 7
P2_intervalo1 = np.linspace(x14, x13, 100)
plt.plot(P2_intervalo1, f(P2,P2_intervalo1), color='r')


# Graficar Polinomio P3 entre el punto 11 y el punto 10
P3_intervalo1 = np.linspace(x11, x10, 100)
plt.plot(P3_intervalo1, f(P3,P3_intervalo1), color='b')


# Graficar Polinomio P4 entre el punto 4 y el punto 5
P4_intervalo1 = np.linspace(x4, x5, 100)
plt.plot(P4_intervalo1, f(P4,P4_intervalo1), color='c')


# Graficar Polinomio P5 primero entre el punto 1 y el punto 15
P5_intervalo1 = np.linspace(x1, x15, 100)
plt.plot(P5_intervalo1, f(P5,P5_intervalo1), color='m')


# Graficar Polinomio P6 primero entre el punto 5 y el punto 10
P6_intervalo1 = np.linspace(x5, x10, 100)
plt.plot(P6_intervalo1, f(P6,P6_intervalo1), color='k')


# Graficar Polinomio P7 primero entre el punto 11 y el punto 12
P7_intervalo1 = np.linspace(x11, x12, 100)
plt.plot(P7_intervalo1, f(P7,P7_intervalo1), color='g')


# Graficar Polinomio P8 primero entre el punto 13 y el punto 12
P8_intervalo1 = np.linspace(x13, x12, 100)
plt.plot(P8_intervalo1, f(P8,P8_intervalo1), color='y')


# Graficar Polinomio P9 primero entre el punto 14 y el punto 15
P9_intervalo1 = np.linspace(x14, x15, 100)
plt.plot(P9_intervalo1, f(P9,P9_intervalo1), color='c')




plt.title('Gráfico del Colibri')
plt.grid(True)
plt.show()