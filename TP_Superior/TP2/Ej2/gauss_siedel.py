import numpy as np

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
    
    return x,abs(x[i] - x_prev[i]),k


A= np.array([[5, -1, 1, 1, 1],
             [-1, 6, -1, 1, 1],
             [1, -1, 7, -1, 1],
             [1, 1, -2, 8, -2],
             [1, 1, 1, -3, 9]])

b= [1,1,1,1,1]

tamA= len(A)
x0=np.zeros(tamA)
tol = 1e-15
maxit=200
K=0

x,res,it = gauss_seidel(A,b,x0,K,tol,maxit)

print("X",x)
print("Res",res)
print("Iteraciones",it)