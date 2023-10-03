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
p = (5**(1/2) - 1)/2

# Generar vector con n terminos independientes
b=[]
for i in range(0,n):
    #numero_aleatorio = random.randint(1, 9)
    b.append(i+1)

A = generar_matriz (n,p)







 


############################################ Factorizacion LU ############################################

from  time  import*
import scipy
import scipy.linalg


t1=perf_counter(); #Calcula tiempo inicio del algoritmo
# Función LU, aquí se inserta la matriz y su tamaño
P, L, U = scipy.linalg.lu(A)


A = np.array(A,float)
P = np.array(P,float)
L = np.array(L,float)
U = np.array(U,float)





L = np.dot(P,L)
y = np.linalg.solve(L,b)


x = np.linalg.solve(U,y)

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
print("\nEl tiempo de ejecución es: "+str(t2-t1))





