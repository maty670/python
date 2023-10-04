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
p = (5**(1/2) - 1)/2

# Generar vector con n terminos independientes
b=[]
x0=[]
for i in range(0,n):
    numero_aleatorio = random.randint(1, 9)
    b.append(numero_aleatorio)
    x0.append(0)

A = generar_matriz (n,p)







############################ Metodo gradientes conjugados ############################
from  time  import*
import scipy
import scipy.linalg


t1=perf_counter(); #Calcula tiempo inicio del algoritmo


def grad_conj(A, b, x0, max_iter,tol):
    x = x0
    r = b - np.dot(A, x)
    p = r
    for k in range(max_iter):
        Ap = np.dot(A, p)
        alpha = np.dot(r, r) / np.dot(p, Ap)
        x = x + alpha * p
        r_new = r - alpha * Ap
        if np.linalg.norm(r_new) < tol:
            break
        beta = np.dot(r_new, r_new) / np.dot(r, r)
        p = r_new + beta * p
        r = r_new
    return x,k+1
    

tol = 1e-5
maxit=1000    
  
    
x,it = grad_conj(A, b, x0, maxit, tol)
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