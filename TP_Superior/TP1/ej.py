import matplotlib.pyplot as plt
import numpy as np

# Función para calcular las coordenadas polares del epiciclo
def calculate_epicycle_coords(radius_epicycle, frequency_epicycle, angle):
    return radius_epicycle * np.cos(frequency_epicycle * angle), radius_epicycle * np.sin(frequency_epicycle * angle)

# Función para calcular las coordenadas polares de la deferente
def calculate_deferent_coords(radius_deferent, frequency_deferent, angle):
    return radius_deferent * np.cos(frequency_deferent * angle), radius_deferent * np.sin(frequency_deferent * angle)

# Parámetros del modelo para Marte (valores hipotéticos)
radius_deferent_mars = 5  # Radio de la deferente para Marte
frequency_deferent_mars = 0.2  # Frecuencia de movimiento de la deferente para Marte (hipotético)
radius_epicycle_mars = 2  # Radio del epiciclo para Marte
frequency_epicycle_mars = 1.5  # Frecuencia de movimiento del epiciclo para Marte (hipotético)

# Ángulos de 0 a 2π para trazar el movimiento completo
angles = np.linspace(0, 2*np.pi, 1000)

# Calcular las coordenadas polares del epiciclo y la deferente para Marte
epicycle_x, epicycle_y = calculate_epicycle_coords(radius_epicycle_mars, frequency_epicycle_mars, angles)
deferent_x, deferent_y = calculate_deferent_coords(radius_deferent_mars, frequency_deferent_mars, angles)

# Graficar el modelo de Ptolomeo para Marte
plt.figure(figsize=(8, 8))
plt.plot(deferent_x, deferent_y, label='Deferente')
plt.plot(epicycle_x + deferent_x, epicycle_y + deferent_y, label='Epiciclo')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Modelo de Ptolomeo - Marte')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()