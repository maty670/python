import numpy as np

def gaussseidelb(A,b,x0,maxit,tol):
    A=np.asarray(A,dtype=float)
    b=np.asarray(b,dtype=float)
    x0=np.asarray(x0,dtype=float)
    dim=x0.shape[0]
    aux=A.diagonal()
    M=aux*np.eye((dim))-np.tril(A)
    N=aux*np.eye((dim))-np.triu(A)
    res=[np.linalg.norm(np.dot(A,x0)-b)]
    x=x0.copy()
    it=0
    while res[it]>tol and it<maxit:
        for i in range(dim):
            x[i]=(b[i]+np.dot(M[i, :] , x)+np.dot(N[i , :] , x))/aux[i]
        res.append(np.linalg.norm(np.dot(A,x)-b))
        it+=1
    return x,res[-1],it

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

x,res,it = gaussseidelb(A,b,x0,maxit,tol)

print("X",x)
print("Res",res)
print("Iteraciones",it)