import re

texto = '''¡Saludos! Es un placer poder ayudarte con esta muestra de texto para tus pruebas de expresiones regulares. En este párraño encontrarás una variedad de símbolos y caracteres que podrás utilizar en tus patrones:
- Los operadores aritméticos básicos como +, -, * y / son fundamentales en matemáticas.
- Las direcciones de correo electrónico, como ejemplo@dominio.com, son esenciales en la comunicación moderna.
- Los números de teléfono, como +1-123-456-7890, varían en formato en diferentes regiones.
- Las fechas pueden aparecer en diferentes estilos, como 31/08/2023 o 2023-08-31.
- Los personajes de programación como { llaves }, [ corchetes ] y ( paréntesis ) son comunes en la codificación.
- Los símbolos monetarios como $ y € son utilizados en transacciones financieras.
- Las expresiones regulares, también conocidas como regex, son patrones de búsqueda flexibles y poderosos.
- Los hashtags como #regex y menciones como @usuario son comunes en las redes sociales.
- Los caracteres especiales como %, &, @, ^, * tienen significados específicos en distintos contextos.
- Los puntos suspensivos... se utilizan para indicar omisiones en el texto.
- Las URLs, como https://www.ejemplo.com, son fundamentales en la navegación web.
- Las horas pueden escribirse en formatos de 12 horas (2:30 PM) o 24 horas (14:30).
¡Espero que este texto te sea útil para tus pruebas de expresiones regulares! Recuerda que los patrones que crees pueden ayudarte a encontrar y manipular cadenas de texto de manera eficiente y precisa.
¡Mucho éxito en tus pruebas y programación!
'''


# Buscar una expresion con search
serach1 = re.search("Python",texto)

if serach1:
    print("Se encontro el texto")
    
    
    
# Retornar una lista con las apariciones del texto con findall, ignorando minusculasd y mayusculas 
findall1 = re.findall("las",texto,flags=re.IGNORECASE)

# \d -> Retorna todos los digitos numericos del 0 al 9
findall_d= re.findall(r"\d",texto)

# \D -> Retorna todos los caracteres que no sean digitos numericos
findall_D= re.findall(r"\D",texto)

# \w -> Retorna todos los caracteres que sean alfanumericos: [a-z A-Z 0-9 _]
findall_w= re.findall(r"\w",texto)

# \W -> Retorna todos los caracteres que NO sean alfanumericos: 
findall_W= re.findall(r"\W",texto)

# \s -> Retorna espacios en blanco: espacios, tabulaciones y saltos de linea(\n)
findall_s = re.findall(r"\s",texto)

# \S -> Retorna todos los caracteres que no sean espacios en blanco
findall_S = re.findall(r"\S",texto)

# \n -> Retorna todos los saltos de linea
findall_n = re.findall(r"\n",texto)

# . -> Retorna todo lo que no sea saltos de linea
findall_ = re.findall(r".",texto)

# \ -> Cancelar caracteres especiales: por ej para retornar los puntos en el texto
findall__ = re.findall(r"\.",texto)





################################################################################

# Buscando una cadena que busque un numero, seguido de un punto
resultado = re.findall(r"\d\.",texto)

# ^ -> Buscar en la parte inicial de un string
principio = re.findall(r"^¡",texto)

# ^ -> Buscar en la parte inicial de cada linea de un string
principio_multilinea = re.findall(r"^- La",texto,flags=re.M)

# $ -> Buscar en la parte final de un string
final = re.findall(r"programación!$",texto)

# $ -> Buscar en la parte final de cada linea de un string
final_multilinea = re.findall(r"os.$",texto,flags=re.M)


#07:43:50