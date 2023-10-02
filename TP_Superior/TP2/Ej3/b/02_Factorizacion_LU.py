import numpy as np
from mpmath import mp
import random

def generar_matriz(n,p):
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                A[i, j] = 1.
            else:
                A[i, j] = 1. / (p + (i + j))
    return A

# Dimensione de la matriz A
n = 20
p = 5

# Generar venctor con n terminos independientes
b=[]
for i in range(0,n):
    numero_aleatorio = random.randint(1, 9)
    b.append(numero_aleatorio)

A = generar_matriz (n,p)
print(A)

'''
determinante = np.linalg.det(A)
print(f"Det[A]: {determinante}")

if (determinante==0.0):
    print("El determinante es igual: 0 -> No tiene inversa")
'''




 


############################################ Factorizacion LU ############################################

from  time  import*
import scipy
import scipy.linalg


t1=perf_counter(); #Calcula tiempo inicio del algoritmo
# Función LU, aquí se inserta la matriz y su tamaño
P, L, U = scipy.linalg.lu(A)
t2=perf_counter(); #Calcula tiempo final del algoritmo

A = np.array(A,float)
P = np.array(P,float)
L = np.array(L,float)
U = np.array(U,float)



print("\nEl tiempo de ejecución es: "+str(t2-t1))

L = np.dot(P,L)
y = np.linalg.solve(L,b)


x = np.linalg.solve(U,y)
print("La solución de X es: \n"+str(x))
R = np.linalg.norm(np.dot(A, x) - b)
print("El residuo es: " + str(R))












