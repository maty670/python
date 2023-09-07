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

# Buscar una expresion que tiene una letra desde la a-zA-Z0-9 seguido de un simbolo -,
resultado = re.findall(r"[a-zA-Z0-9][-,]",texto)

# ^ -> Buscar en la parte inicial de un string
principio = re.findall(r"^¡",texto)

# ^ -> Buscar en la parte inicial de cada linea de un string
principio_multilinea = re.findall(r"^- La",texto,flags=re.M)

# $ -> Buscar en la parte final de un string
final = re.findall(r"programación!$",texto)

# $ -> Buscar en la parte final de cada linea de un string
final_multilinea = re.findall(r"os.$",texto,flags=re.M)

# | -> Buscar la expresion a la derecha o a la izquierda
resultado_o = re.findall(r"[-_+/*]\d|\d[-_+/*]",texto,flags=re.M)     # Buscar expresiones que sean simbolos -_+/* seguidos de un numero O un numero seguido de -_+/*






################################## GRUPOS ##################################

# + -> Busca que ocurra como MINIMO una vez el elemento de la izquierda
resultado = re.findall(r"\d+\s",texto)   # Buscar como minimo 1 digito/s seguidos de un espacio, tabulacion o salto de linea(\n)

# {n} -> Busca n cantidad de veces el valor de la izquierda
resultado_n = re.findall(r"\d{3}-",texto)   # Buscar 3 digitos seguidos de el caracter -

# {n,m} -> Busca como minimo n y como maximo m cantidad de veces el valor de la izquierda
resultado_nm = re.findall(r"\d{1,3}-",texto) # Buscar de 1 a 3 digitos seguidos de el caracter -

resultado_nm = re.findall(r"\d{1,}-",texto) # Buscar de 1 a infinitos digitos seguidos de el caracter -









################################## Ejemplo de como validar que un correo electronico ##################################



# • Comience con un caracter a-zA-Z
# • Luego puede tener cualquier caracter a-zA-Z0-9 junto con los simbolos -_/ al menos 1 vez
# • Despues tener SOLO 1 arroba
# • Siguiendo con AL MENOS TRES caracteres a-zA-Z sin limite de maximo
# • Luego debe tener un solo punto (con el \ como caracter de escape para buscar el punto)
# • Y FINALIZAR ($) con el termino com

def validarCorreo(correo):
    x = re.search("^[a-zA-Z][a-zA-Z0-9-_]+@[a-zA-Z]{3,}\.com$", correo)
    return x,correo.count("@")


correos = ["qwe_qw@sdas.com","/asd@sdas.com","qweqw@sdas@.com","aa_dsz--@qwe.com"]

for c in correos:
    x,arrobas = validarCorreo(c)
    #if x:
        #print(f"El correo {c} es válido")
    #else:
        #print(f"El correo {c} tiene un formato incorrecto")













################################################# Ejemplo buscar y reemplazar patron de fechas #################################################

texto2 = """Las fechas de los próximos eventos son las siguientes: 05-09-2023, 20/12/2023, 07-09-2023 y 01/01/2024.

Aquí hay algunas fechas históricas importantes: 04-07-1776 (Declaración de Independencia de EE. UU.), 14-07-1789 (Revolución Francesa).

Además, en nuestros registros, encontramos estas fechas: 11-30-2021, 03/15/2022, 25-10-2023 y 02/01/2024."""

# Definir la expresión regular para buscar fechas en el formato dd-mm-aaaa
patron = r'(\d{2})-(\d{2})-(\d{4})'

# Función de reemplazo que cambia '-' por '/'
def reemplazar_fecha(match):
    fecha = match.group()           # Para acceder a las subcadenas que coinciden con esos grupos
    fecha = fecha.split("-") 
    return fecha[0] + '/' + fecha[1] + '/' + fecha[2]

# Realizar la sustitución utilizando la expresión regular y la función de reemplazo
texto_modificado = re.sub(patron, reemplazar_fecha, texto2)

# Imprimir el resultado
#print(texto_modificado)