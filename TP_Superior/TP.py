if __name__ == "__main__":
    # Leer los puntos desde el archivo
    with open("C:/Users/NELIA/Desktop/Matias/tp_superior/epiciclos-parseado.txt", "r") as file:
        lines = file.readlines()

def parse(l):    
    n = l.split("    ")
    n[0] = n[0].strip()
    n[1] = n[1].strip().replace(" ","") + "j"
    return [float(n[0]),complex(n[1])]

parse(lines[0])
for x in lines:
    Radios = parse(x)[0]
    Ck = parse(x)[1]
    print(f"{type(Radios)} {Radios}    {type(Ck)} {Ck}")
    

    

 
