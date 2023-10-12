def operar(op,n1,n2):
    if(op=="Suma"):
        return n1+n2
    elif(op=="Resta"):
        return n1-n2
    elif(op=="Multiplicacion"):
        return n1*n2
    elif(op=="Division"):
        if(n2==0):
            print("ERROR: Entero dividido por 0")
        else:
            return n1/n2
    
resultado = operar("Multiplicacion",5,5)
print(resultado)