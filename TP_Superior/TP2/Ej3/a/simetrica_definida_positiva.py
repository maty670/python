import numpy as np

def generar_matriz(n,p):
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                A[i, j] = 1.
            else:
                A[i, j] = 1. / (p + (i + j))
    return A

p=1
dimension = 10

matriz = generar_matriz(dimension,p)

n = matriz.shape[0]  

determinantes = []





for i in range(n):
    for j in range(n):
        for k in range(i+1, n+1):
            for l in range(j+1, n+1):
                submatriz = matriz[i:k, j:l]
                if submatriz.shape[0] == submatriz.shape[1]:  # Verifica si la submatriz es cuadrada
                    determinante_submatriz = np.linalg.det(submatriz)
                    determinantes.append((i, j, k-1, l-1, determinante_submatriz))


for i, j, k, l, det in determinantes:
    print(f"Submatriz [{i}:{k}, {j}:{l}] - Determinante: {det}")

def analizar_determinantes(determ_list):
    for i in determ_list:   
        for det in i:
            if(det<0):
                return False
    
    return True

if (analizar_determinantes):
    print("Todos los determinantes son mayores a 0, la matriz ES simetrica diagonal positiva")
else:
    print("Existe un determinante menor a 0, la matriz NO ES simetrica diagonal positiva")
