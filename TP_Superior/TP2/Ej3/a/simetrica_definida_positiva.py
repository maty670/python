import numpy as np

# Matriz de A de Dimension [10x10], A = At ,con p=1
matriz = np.array([[1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10],
                   [1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10, 1/11],
                   [1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10, 1/11, 1/12],
                   [1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10, 1/11, 1/12, 1/13],
                   [1/5, 1/6, 1/7, 1/8, 1/9, 1/10, 1/11, 1/12, 1/13, 1/14],
                   [1/6, 1/7, 1/8, 1/9, 1/10, 1/11, 1/12, 1/13, 1/14, 1/15],
                   [1/7, 1/8, 1/9, 1/10, 1/11, 1/12, 1/13, 1/14, 1/15, 1/16],
                   [1/8, 1/9, 1/10, 1/11, 1/12, 1/13, 1/14, 1/15, 1/16, 1/17],
                   [1/9, 1/10, 1/11, 1/12, 1/13, 1/14, 1/15, 1/16, 1/17, 1/18],
                   [1/10, 1/11, 1/12, 1/13, 1/14, 1/15, 1/16, 1/17, 1/18, 1/19]])

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
