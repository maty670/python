import numpy as np
import matplotlib.pyplot as plt

from mpmath import mp

# Configura la precisión a 100 dígitos decimales
mp.dps = 100


# Funciones polinomicas en forma de tuplas
P1 = ('-0.00648','-0.2674','-2.662','-6.959')
P2 = ('-82.08','398.9','-651.7','371.8')
P3 = ('-0.342','3.791','-16.47','26.26')
P4 = ('0.4102','2.549','6.472','2.406')
P5 = ('-0.0166','-0.5157','-3.794','-1.834')
P6 = ('-0.007784','0.03998','-0.3053','-9.409')
P7 = ('-0.003877','0.1498','-0.3954','-0.7499')
P8 = ('0.0002778','-0.01556','0.7777','4.172')
P9 = ('0.1023','-0.3259','1.8','12.55')

# Evaluar una funcion polinomica Px en un valor x
def f(Px,x):
    Px0 = mp.mpf(float(Px[0]))
    Px1 = mp.mpf(float(Px[1]))
    Px2 = mp.mpf(float(Px[2]))
    Px3 = mp.mpf(float(Px[3]))
    return Px0*x**3 + Px1*x**2 + Px2*x + Px3


def interseccion(Pa,Pb,x):
    C1 = mp.mpf(Pa[0]) - mp.mpf(Pb[0])
    C2 = mp.mpf(Pa[1]) - mp.mpf(Pb[1])
    C3 = mp.mpf(Pa[2]) - mp.mpf(Pb[2])
    C4 = mp.mpf(Pa[3]) - mp.mpf(Pb[3])
    return C1*x**3 + C2*x**2 + C3*x +C4

def derivada(Pa,Pb,x):
    C1 = mp.mpf(Pa[0]) - mp.mpf(Pb[0])
    C2 = mp.mpf(Pa[1]) - mp.mpf(Pb[1])
    C3 = mp.mpf(Pa[2]) - mp.mpf(Pb[2])
    C4 = mp.mpf(Pa[3]) - mp.mpf(Pb[3])
    return 3*C1*x**2 + 2*C2*x + C3

def newton_raphson(x0, tol, max_iter,Pa,Pb):
    it = 0
    x = x0

    while abs(interseccion(Pa,Pb,x)) > tol and it < max_iter:
        x = x - interseccion(Pa,Pb,x) / derivada(Pa,Pb,x)
        it += 1
    
    return x,abs(interseccion(Pa,Pb,x)) ,it

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
    raiz,residuo,iteracionesNewton = newton_raphson(m,1e-30,50,Pa,Pb)  
    
    # Evaluar la raiz en el polinomio para obtener la imagen           
    fx = f(Pa,raiz)
    
    
    return raiz,fx,residuo,iteracionesNewton,it



#biseccion(extremo_A,extremo_b,max_iteraciones,tolerancia,Polinomio_a,Polinomio_b)

x1,y1,residuo_1,iteracionesNewton_1,iteracionesBiseccion_1 = biseccion(-16,-14,50,0.01,P1,P5)
x2,y2,residuo_2,iteracionesNewton_2,iteracionesBiseccion_2 = biseccion(-5,-4,50,0.01,P1,P8)
x3,y3,residuo_3,iteracionesNewton_3,iteracionesBiseccion_3 = biseccion(-4,-3,50,0.01,P1,P9)
x4,y4,residuo_4,iteracionesNewton_4,iteracionesBiseccion_4 = biseccion(-2,-1,50,0.01,P1,P4)
x5,y5,residuo_5,iteracionesNewton_5,iteracionesBiseccion_5 = biseccion(-4,-3,50,0.01,P4,P6)
x6,y6,residuo_6,iteracionesNewton_6,iteracionesBiseccion_6 = biseccion(0,1,50,0.01,P1,P6)
x7,y7,residuo_7,iteracionesNewton_7,iteracionesBiseccion_7 = biseccion(1,3,50,0.01,P1,P2)
x8,y8,residuo_8,iteracionesNewton_8,iteracionesBiseccion_8 = biseccion(1,3,50,0.01,P2,P5)
x9,y9,residuo_9,iteracionesNewton_9,iteracionesBiseccion_9 = biseccion(2,3,50,0.01,P2,P6)
x10,y10,residuo_10,iteracionesNewton_10,iteracionesBiseccion_10 = biseccion(5,7,50,0.01,P3,P6)
x11,y11,residuo_11,iteracionesNewton_11,iteracionesBiseccion_11 = biseccion(3,4,50,0.01,P3,P7)
x12,y12,residuo_12,iteracionesNewton_12,iteracionesBiseccion_12 = biseccion(14,16,50,0.01,P7,P8)
x13,y13,residuo_13,iteracionesNewton_13,iteracionesBiseccion_13 = biseccion(2,3,50,0.01,P2,P8)
x14,y14,residuo_14,iteracionesNewton_14,iteracionesBiseccion_14 = biseccion(1,3,50,0.01,P2,P9)
x15,y15,residuo_15,iteracionesNewton_15,iteracionesBiseccion_15 = biseccion(-3,-2,50,0.01,P5,P9)
x16,y16,residuo_16,iteracionesNewton_16,iteracionesBiseccion_16 = biseccion(-6,-5,50,0.01,P5,P7)


print(f"""Punto1({x1},{y1} Iteraciones Biseccion({iteracionesBiseccion_1}) Iteraciones Newton({iteracionesNewton_1})
Punto2({x2},{y2}) Iteraciones Biseccion({iteracionesBiseccion_2}) Iteraciones Newton({iteracionesNewton_2})
Punto3({x3},{y3}) Iteraciones Biseccion({iteracionesBiseccion_3}) Iteraciones Newton({iteracionesNewton_3})
Punto4({x4},{y4}) Iteraciones Biseccion({iteracionesBiseccion_4}) Iteraciones Newton({iteracionesNewton_4})
Punto5({x5},{y5}) Iteraciones Biseccion({iteracionesBiseccion_5}) Iteraciones Newton({iteracionesNewton_5})
Punto6({x6},{y6}) Iteraciones Biseccion({iteracionesBiseccion_6}) Iteraciones Newton({iteracionesNewton_6})
Punto7({x7},{y7}) Iteraciones Biseccion({iteracionesBiseccion_7}) Iteraciones Newton({iteracionesNewton_7})
Punto8({x8},{y8}) Iteraciones Biseccion({iteracionesBiseccion_8}) Iteraciones Newton({iteracionesNewton_8})
Punto9({x9},{y9}) Iteraciones Biseccion({iteracionesBiseccion_9}) Iteraciones Newton({iteracionesNewton_9})
Punto10({x10},{y10}) Iteraciones Biseccion({iteracionesBiseccion_10}) Iteraciones Newton({iteracionesNewton_10})
Punto11({x11},{y11}) Iteraciones Biseccion({iteracionesBiseccion_11}) Iteraciones Newton({iteracionesNewton_11})
Punto12({x12},{y12}) Iteraciones Biseccion({iteracionesBiseccion_12}) Iteraciones Newton({iteracionesNewton_12})
Punto13({x13},{y13}) Iteraciones Biseccion({iteracionesBiseccion_13}) Iteraciones Newton({iteracionesNewton_13})
Punto14({x14},{y14}) Iteraciones Biseccion({iteracionesBiseccion_14}) Iteraciones Newton({iteracionesNewton_14})
Punto15({x15},{y15}) Iteraciones Biseccion({iteracionesBiseccion_15}) Iteraciones Newton({iteracionesNewton_15})
Punto16({x16},{y16}) Iteraciones Biseccion({iteracionesBiseccion_16}) Iteraciones Newton({iteracionesNewton_16})
""")

################################## Cual es la distancia mas extensa entre los puntos encontrados ##################################
def menorResiduo(residuos):
    min = residuos[0]
    punto_min=1
    max = residuos[0]
    punto_max=1
    
    for i in range(0,len(residuos)):
        res = residuos[i]
        punto = i+1
        if abs(res) < abs(min):
            min = res
            punto_min = punto
        elif abs(res) > abs(max):
            max = res    
            punto_max = punto
    return min,max,punto_min,punto_max
    
lista_residuos = (residuo_1,residuo_2,residuo_3,residuo_4,residuo_5,residuo_6,residuo_7,residuo_8,residuo_9,residuo_10,
                 residuo_11,residuo_12,residuo_13,residuo_14,residuo_15,residuo_16)

min,max,punto_min,punto_max = menorResiduo(lista_residuos)

print(f"""Distancia max corta: {min}, en el punto P{punto_min}
Distancia mas extensa: {max}, en el punto P{punto_max}
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



# Graficar Polinomio P1 primero entre el punto 1 y el punto 4
P1_intervalo1 = np.linspace(float(x1), float(x4), 1000)
plt.plot(P1_intervalo1, f(P1,P1_intervalo1), color='g')


# Graficar Polinomio P2 primero entre el punto 14 y el punto 13
P2_intervalo1 = np.linspace(float(x14), float(x13), 1000)
plt.plot(P2_intervalo1, f(P2,P2_intervalo1), color='r')


# Graficar Polinomio P3 entre el punto 11 y el punto 10
P3_intervalo1 = np.linspace(float(x11), float(x10), 1000)
plt.plot(P3_intervalo1, f(P3,P3_intervalo1), color='b')


# Graficar Polinomio P4 entre el punto 4 y el punto 5
P4_intervalo1 = np.linspace(float(x4), float(x5), 1000)
plt.plot(P4_intervalo1, f(P4,P4_intervalo1), color='c')


# Graficar Polinomio P5 primero entre el punto 1 y el punto 15
P5_intervalo1 = np.linspace(float(x1), float(x15), 1000)
plt.plot(P5_intervalo1, f(P5,P5_intervalo1), color='m')


# Graficar Polinomio P6 primero entre el punto 5 y el punto 10
P6_intervalo1 = np.linspace(float(x5), float(x10), 1000)
plt.plot(P6_intervalo1, f(P6,P6_intervalo1), color='k')


# Graficar Polinomio P7 primero entre el punto 11 y el punto 12
P7_intervalo1 = np.linspace(float(x11), float(x12), 1000)
plt.plot(P7_intervalo1, f(P7,P7_intervalo1), color='g')


# Graficar Polinomio P8 primero entre el punto 13 y el punto 12
P8_intervalo1 = np.linspace(float(x13), float(x12), 1000)
plt.plot(P8_intervalo1, f(P8,P8_intervalo1), color='y')


# Graficar Polinomio P9 primero entre el punto 14 y el punto 15
P9_intervalo1 = np.linspace(float(x14), float(x15), 1000)
plt.plot(P9_intervalo1, f(P9,P9_intervalo1), color='c')




plt.title('Gráfico del Colibri')
plt.grid(True)
plt.show()