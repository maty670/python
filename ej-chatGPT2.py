import numpy as np
import matplotlib.pyplot as plt

def epiciclo_sum(R, omega, t):
    return np.sum([Ri * (np.cos(omegai * t) + 1j * np.sin(omegai * t)) for Ri, omegai in zip(R, omega)])

# Definir los valores para Ri y ωi
R = [1, 0.5, 0.3]  # Radio de cada epiciclo
omega = [1, 2, 3]  # Frecuencia angular de cada epiciclo

# R = [5000, 1000, 500, 100, 1]
# omega = [1, 6, 1, 6, 1, 6]


# Definir el rango de tiempo
t = np.linspace(0, 2 * np.pi, 100)

# Calcular las coordenadas (x, y) para cada instante de tiempo t
coords = [epiciclo_sum(R, omega, ti) for ti in t]

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