import random

string = "CadEnA De EjeMplo"
int = 4
float = 4.37
from fractions import Fraction as frac

#El método dir devuelve la lista de atributos válidos del objeto pasado
print(f"""
{dir(string)}

{dir(int)}

{dir(float)}
""")

print(string.upper())
print(string.lower())
print(len(string))
print((string.replace("EjeMplo","Reemplazo")))  # Reemplaza un valor de la cadena por otro
print(string.capitalize())                      # Primera letra en mayuscula, el resto en minuscula
print(string.find("EjeM"))                      # Retorna la posicion en la que se encuentra la subcadena
print(string.isnumeric())                       # Retorna True si la cadena es numerica
print(string.count("d"))                        # Retorna la cantidad de coincidencias de la subcadena en la cadena
print(string.startswith("CadE"))                # Retorna True si la cadena empieza con la subcadena
print(string.split(" "))                        # Separa la cadena a partir de un valor, generando una lista

print("############################################################################################################################################################")
print(pow(int,3))
print(round(float,0))

