
print(f"""
◄◄◄◄-----------------------------------------------------►►►
                        BIENVENIDO
                    ¿Cual es su nombre ?
◄◄◄◄-----------------------------------------------------►►►
""")

usuario = input("")

print(f"""
◄◄◄◄-----------------------------------------------------►►►
BIENVENIDO USUARIO: {usuario}

• Actualmente tiene 20 manzanas disponibles y puede
comprar cada una a un precio de $5 pesos.

¿ Cuantas manzanas desea comprar ?
◄◄◄◄-----------------------------------------------------►►►
""")

manzanas_disp=20
manzanas_solicit = int(input(""))
manzanas_restantes = manzanas_disp - manzanas_solicit

print(f"""
◄◄◄◄-----------------------------------------------------►►►
• Usted compro {manzanas_solicit} manzanas a ${manzanas_solicit*5}
• Le quedan {manzanas_restantes} manzanas para comprar
◄◄◄◄-----------------------------------------------------►►►
""")