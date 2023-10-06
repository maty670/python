def es_primo(n):
    if(n<=1):
        return False
    
    # Corroborar que el numero solo se divide entre 1 y si mismo
    for i in range(2,n-1):    
        if (n%i==0):
            return False
    
    return True


            

def numeros_primos(num):
    primos=[]
    for i in range(2,num+1):
        if es_primo(i):
            primos.append(i)
            
    return primos