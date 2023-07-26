#import matplotlib.pyplot as plt
#import numpy as np
#from sympy import *

#w = Symbol('w')
#t = Symbol('t', Real=True)

if __name__ == "__main__":
    # Leer los puntos desde el archivo
    with open("C:/Users/NELIA/Desktop/Matias/python/TP_Superior/epiciclos.txt", "r") as file:
        lines = file.readlines()[1:]    #Skipear la primer linea

def parseRad(f):    
    f = f.split("    ")
    radio = f[0].strip()
    return float(radio)

def parseCk(f):    
    f = f.split("    ")
    Ck = f[1].strip().replace("i","").replace(" ","") + "j"
    return complex(Ck)
    


for x in lines:
    Radio = parseRad(x)
    Ck = parseCk(x)
    print(f"{type(Radio)} {Radio}       {type(Ck)} {Ck}")

    

    

#https://www.youtube.com/watch?v=0J31ACZ6jtk&ab_channel=SistemasInteligentes

 
