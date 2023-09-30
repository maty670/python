import numpy as np

def jacobi(matrix, b, initial_guess, K, tol=1e-15, max_iterations=100):
    n = len(matrix)
    x = initial_guess.copy()
    x_prev = initial_guess.copy()
    
    for iteration in range(max_iterations):
        for i in range(n):
            sum_1 = sum(matrix[i][j] * x[j] for j in range(i))
            sum_2 = sum(matrix[i][j] * x_prev[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum_1 - sum_2) / matrix[i][i]
        
        # Aplicar la relajación
        for i in range(n):
            x[i] = (K + 1) * x[i] - K * x_prev[i]
        
        # Comprobar la convergencia
        if all(abs(x[i] - x_prev[i]) < tol for i in range(n)) or iteration>=max_iterations-1:
            error = np.linalg.norm(np.array(x) - np.array(x_prev))
            return x,iteration,error
        
        x_prev = x.copy()
    
    raise Exception("El método no convergió después de {} iteraciones.".format(max_iterations))

# Ejemplo de uso
A = np.array([[10, 2, 1, 1, 0],
              [1, 5, 1, 0, 1],
              [2, 3, 10, 1, 0],
              [0, 2, 3, 8, 1],
              [1, 0, 2, 3, 9]])
#np.random.rand(n,n)
b = np.array([1, 1, 1, 1, 1])
tamA= len(A)
x0=np.zeros(tamA)
K = 0

solution,iteraciones,error = jacobi(A, b, x0, K)
print("Solución:", solution)
print("Iteraciones:", iteraciones)
print("Error:", error)