import numpy as np
K = 0
#Aplico JACOBI
def jacobi (A,b,x0,tol,maxit):
  D=np.diag(np.diag(A))
  LU= A-D
  x=x0
  for i in range(maxit):
    D_inv = np.linalg.inv(D)
    xtemp=x
    x=np.dot(D_inv,np.dot(-LU,x))+np.dot(D_inv,b)
    x=abs(np.dot(K+1,x)-np.dot(K,xtemp))
    error=np.linalg.norm(abs(x-xtemp))

    print(f"Iteracion: {i}, x={x}, Error: {error}")
    if error <tol:
      return x
  return x

A = np.array([[10, 2, 1, 1, 0],
              [1, 5, 1, 0, 1],
              [2, 3, 10, 1, 0],
              [0, 2, 3, 8, 1],
              [1, 0, 2, 3, 9]])
#np.random.rand(n,n)
b = np.array([1, 1, 1, 1, 1])
#np.random.rand(n,)
tamA= len(A)
x0=np.zeros(tamA)
tol = 1e-15
maxit=200
#Compruebo que A es diagonal dominante
n= len(b)
it=0
for i in range(n):
  Aii=A[i][i]
  sum=0
  for j in range(n):
    if i!=j:
      sum = sum + abs(A[i][j])
  if Aii>sum:
    print("Fila: ", i , "es diagonal dominante")
    it+=1
  else:
    print ("Fila: ", i , " NO es diagonal dominante")
    break

if it ==n:
  print ("Matriz diagonal dominante, Jacobi convergirá")
else: 
  print ("Matriz no es diagonal dominante, Jacobi no convergirá")

x=jacobi(A,b,x0,tol,maxit)