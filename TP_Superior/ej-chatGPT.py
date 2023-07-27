import numpy as np
import matplotlib.pyplot as plt

# Listado de radios R (longitudes de los epiciclos)
radios = [1.5, 2.0, 0.8]

# Listado de constantes complejas Ck
constantes_cplx = [1 + 0.5j,   # C1
                   0.7 - 0.3j,  # C2
                   0.4 + 0.9j]  # C3

# Frecuencia angular ω0
frecuencia_omega = 2 * np.pi

# Número de puntos en el tiempo para el gráfico
num_puntos_tiempo = 1000

# Calcula las coordenadas x e y en función del tiempo t
t = np.linspace(0, 2 * np.pi, num_puntos_tiempo)
x = np.zeros(num_puntos_tiempo)
y = np.zeros(num_puntos_tiempo)

for k, R, C in zip(range(len(radios)), radios, constantes_cplx):
    x += np.real(C) * np.cos(k * frecuencia_omega * t)
    y += np.real(C) * np.sin(k * frecuencia_omega * t)

# Grafica los epiciclos
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de los epiciclos')
plt.grid()
plt.show()