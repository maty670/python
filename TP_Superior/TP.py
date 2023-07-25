import matplotlib.pyplot as plt
import numpy as np
from sympy import *

w = Symbol('w')
t = Symbol('t', Real=True)

if __name__ == "__main__":
    # Leer los puntos desde el archivo
    with open("D:/Datos/Desktop/python/TP_Superior/epiciclos.txt", "r") as file:
        
        lines = file.readlines()[1:]    #Skipear la primer linea

def parse(l):    
    n = l.split("    ")
    n[0] = n[0].strip()
    n[1] = n[1].strip().replace("i","").replace(" ","") + "j"
    return [float(n[0]),complex(n[1])]

for x in lines:
    parse(x)
    Radios=[]
    Ck=[]
    Radios.append(parse(x)[0])
    Ck.append(parse(x)[1])
    print(f"{type(Radios)} {Radios}    {type(Ck)} {Ck}")
    

    

#https://www.youtube.com/watch?v=0J31ACZ6jtk&ab_channel=SistemasInteligentes

 
