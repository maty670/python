import re
def validarCorreo(correo):
    x = re.search("^[a-zA-Z][a-zA-Z0-9]+@{1}[a-zA-Z]+.{1}com$", correo)
    return x,correo.count("@")


correos = ["qweqw@sdas.com","/asd@sdas.com","qweqw@sdas@.com","aadsz--@.co"]

for c in correos:
    x,arrobas = validarCorreo(c)
    if x:
        print(f"El correo {c} es válido")
    else:
        print(f"El correo {c} tiene un formato incorrecto")
    
    
################################################

# El caracter especial *args en de funciones se utiliza para 
# pasar un número variable de Argumentos a una función
def suma(parametro1,*numeros):
    return sum(numeros)

suma("parametro1",4,6,78,4,6,7,8)    

################################################









##########################################################

def frase(palabra1,palabra2,palabra3):
    print (f"{palabra1} - {palabra2} - {palabra3}")

#frase(palabra3 = "999", palabra1= "111", palabra2="666")

##########################################################
