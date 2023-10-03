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
n = 50
p = 1

# Generar vector con n terminos independientes
b=[]
for i in range(0,n):
    #numero_aleatorio = random.randint(1, 9)
    b.append(i+1)

A = generar_matriz (n,p)







############################ Metodo gradientes conjugados ############################
from  time  import*


t1=perf_counter(); #Calcula tiempo inicio del algoritmo


def grad_conj(m, b, x0, tol, maxiter):

    n = len(b)
    if not x0:
        x0 = np.zeros(n)
        
    grad0 = np.dot(m, x0) - b        
    d = -grad0                      
    
    for i in range(maxiter):
        alpha = np.dot(grad0, grad0) / np.dot(np.dot(d, m), d)
        x0 = x0 + d * alpha
        grad = grad0 + np.dot(m, alpha * d)
        if np.linalg.norm(grad) < tol:
            return x0
        beta = np.dot(grad, grad) / np.dot(grad0, grad0)
        d = -grad + beta * d
        grad0 = grad
    return x0,i
    
tol = 1e-5
maxit=1000    
    
x,it = grad_conj(A, b, None, tol, maxit)
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