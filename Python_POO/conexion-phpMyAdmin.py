import mysql.connector

"""
Host: http://db4free.net
Base de datos: bd_maty
Nombre de usuario: maty_f5asacz3xc1
Contraseña: G6ad9Lq5ZYnCr63
Puerto: 3006
Correo electrónico: espositomatias4@gmail.com
"""

# Configura la información de conexión a la base de datos
conexion = mysql.connector.connect(
    host="db4free.net",  # Por lo general, 'localhost' si es local
    user="maty_f5asacz3xc1",
    password="G6ad9Lq5ZYnCr63",
    database="bd_maty"
)

# Comprueba si la conexión fue exitosa
if conexion.is_connected():
    print("Conexión exitosa a la base de datos")
else:
    print("Error en la conexión")

# Crea un objeto cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Ejemplo 1: Consultar todos los registros de una tabla
tabla = "registros"
consulta = f"SELECT * FROM {tabla}"

# Ejecutar consulta
cursor.execute(consulta)

# Recorrer los registros y mostrarlos
for x in cursor.fetchall():
    print(x[0])
    
# Obtener los nombres de las columnas
nombres_columnas = [desc[0] for desc in cursor.description]
print(nombres_columnas)


"""
# Ejemplo 2: Insertar un nuevo registro en una tabla
nuevo_registro = ("Valor1", "Valor2", "Valor3")
consulta_insert = "INSERT INTO nombre_de_la_tabla (columna1, columna2, columna3) VALUES (%s, %s, %s)"
cursor.execute(consulta_insert, nuevo_registro)

# Asegúrate de hacer commit para guardar los cambios
conexion.commit()
"""



# Cierra el cursor y la conexión cuando hayas terminado
cursor.close()

# Cierra la conexión cuando hayas terminado
conexion.close()
