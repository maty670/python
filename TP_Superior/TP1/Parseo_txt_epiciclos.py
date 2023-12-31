#import matplotlib.pyplot as plt
#import numpy as np
#from sympy import *

#w = Symbol('w')
#t = Symbol('t', Real=True)

if __name__ == "__main__":
    # Leer los puntos desde el archivo
    with open("D:/Datos/Desktop/python/TP_Superior/epiciclos.txt", "r") as file:
        lines = file.readlines()[1:]    #Skipear la primer linea

def parseRad(f):    
    f = f.split("    ")
    radio = f[0].strip()
    return float(radio)

def parseCk(f):    
    f = f.split("    ")
    Ck = f[1].strip().replace("i","").replace(" ","") + "j"
    return complex(Ck)
    

Radios=[]
Ck=[]
y=0
for x in lines:
    if(y<=1000):
        Radios.append(parseRad(x))
        Ck.append(parseCk(x))
        y=y+1
    

print(Radios)

#plt.plot(Radios, label = "line 1")
    
#plt.show()


#https://bestiariotopologico.blogspot.com/2020/05/interpolacion-trigonometrica-usando-la.html