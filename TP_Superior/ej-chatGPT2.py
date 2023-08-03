import numpy as np
import matplotlib.pyplot as plt

def epiciclo_sum(R, omega_0, k):
  suma = 0
  for Ri, omegai in zip(R, omega_0):
    suma += np.sum([Ri * (np.cos(omegai * k) + 1j * np.sin(omegai * k))])
  return suma

N = 1000

# Definir los valores para Ri y ωi
R = [598.165, 173.078, 60.656, 118.358, 33.712, 37.211, 1.909, 20.38, 17.58, 13.373, 18.116, 28.32, 8.121, 5.364, 4.242, 3.992, 2.867, 8.578, 5.386, 4.937, 1.752, 0.677, 1.521, 0.997, 1.428, 1.918, 3.182, 0.659, 2.524, 2.596, 2.314, 1.379, 2.788, 2.54, 3.026, 3.596, 2.557, 1.57, 0.512, 1.833, 0.769, 1.582, 1.28, 0.192, 0.997, 0.814, 1.028, 1.619, 1.752, 0.447, 0.225, 0.541, 0.701, 0.826, 1.147, 0.928, 0.688, 0.322, 0.777, 0.246, 0.651, 0.499, 0.362, 0.43, 0.407, 0.297, 0.352, 0.595, 0.608, 0.61, 0.281, 0.364, 0.441, 0.407, 0.499, 0.186, 0.098, 0.484, 0.659, 0.502, 0.21, 0.424, 0.697, 0.648, 0.511, 0.576, 0.519, 0.167, 0.33, 0.152, 0.083, 0.096, 0.163, 0.364, 0.354, 0.608, 0.282, 0.418, 0.131, 0.458, 0.452]  # Radio de cada epiciclo
omega_0 = [(2 * np.pi)/N,((2 * np.pi)/N)*5]  # Frecuencia angular de cada epiciclo

# Definir el rango de tiempo
k = np.linspace(1, N, N)

# Calcular las coordenadas (x, y) para cada instante de tiempo k
coords = [epiciclo_sum(R, omega_0, ki) for ki in k]

# Obtener las coordenadas x e y por separado
x = np.real(coords)
y = np.imag(coords)

# Graficar
plt.figure(figsize=(6, 6))
plt.plot(x, y, label="Epiciclo")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Epiciclos girando sobre un deferente')
plt.axis('equal')
plt.grid()
plt.legend()
plt.show()
