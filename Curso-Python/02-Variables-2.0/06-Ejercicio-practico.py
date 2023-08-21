# Pedir el nombre y la edad de las personas


def obtener_personas(cantidad):
    personas = []

    for i in range(0,cantidad):
        nombre = input("Nombre de la persona: ")        # key[0]
        edad = int(input("Edad de la persona: "))       # key[1]
        p = (nombre,edad) #Tupla
        personas.append(p)
        
    personas.sort(key=lambda x:x[1])                    # Ordenar por la key[1], es decir por la edad
    
    menor_edad = personas[0][0]
    mayor_edad = personas[-1][0]
    
    return personas, menor_edad, mayor_edad


#Listado_personas, menor, mayor = obtener_personas(4)
#print(f"""El listado de personas es: {Listado_personas}
#La persona de menor edad es: {menor}
#Y la de mayor edad es: {mayor}
#""")









#####################################################################################
# Crear una funcion que genera numeros primos hasta el numero que le pasamos

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

listado = numeros_primos(100)

print(listado)
#####################################################################################