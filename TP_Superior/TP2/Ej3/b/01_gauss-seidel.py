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

# Dimensione de la matriz A y termino p
n = 10
p = 1

# Generar vector con n terminos independientes
b=[]
for i in range(0,n):
    numero_aleatorio = random.randint(1, 9)
    b.append(numero_aleatorio)

A = generar_matriz (n,p)


######################################## Gauss-Seidel ##############################################
from  time  import*


t1=perf_counter(); #Calcula tiempo inicio del algoritmo

def gauss_seidel(A, b, x0, K, tol=1e-15, max_iter=100):
    n = len(A)
    x = x0.copy()
    
    for k in range(max_iter):
        x_prev = x.copy()
        for i in range(n):
            sigma_forward = sum(A[i][j] * x[j] for j in range(i))
            sigma_backward = sum(A[i][j] * x_prev[j] for j in range(i+1, n))
            x[i] = ((K + 1) * x_prev[i] - K * x0[i] + b[i] - sigma_forward - sigma_backward) / A[i][i]
        
        if all(abs(x[i] - x_prev[i]) < tol for i in range(n)):
            break
    
    return x,k+1



tamA= len(A)
x0=np.zeros(tamA)
tol = 1e-5
maxit=1000
K=-1

x,it = gauss_seidel(A,b,x0,K,tol,maxit)
t2=perf_counter(); #Calcula tiempo final del algoritmo














# Errores
Error_list=""
for i in range(len(A)):
    Error=0
    for j in range(len(A)):
        Error += ((A[i][j] * x[j]))
    Error_list = Error_list + (f"Error:(|{b[i]} - |{Error}||)= {abs(b[i]-abs(Error))}\n")
    
print(f"MATRIZ A:{A}")
print(f"VECTOR b:{b}")
print("El vector solucion es: \n"+str(x))
print(Error_list)
print(f"Iteraciones: {it}")
print("\nEl tiempo de ejecución es: "+str(t2-t1))