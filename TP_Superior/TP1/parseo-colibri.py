import matplotlib.pyplot as plt

# Datos de la secuencia
datos = [
    (-1.6, -3.1), (-2.3, -2.4), (-3, -1.5), (-4, 0), (-4.5, 0.4),
    (-5, 0.5), (-6, 0.6), (-7, 0.65), (-8, 0.63), (-9, 0.3),
    (-8.5, 1.2), (-8, 1.8), (-7.5, 2.5), (-7, 2.9), (-6.5, 2.5),
    (-7, 2), (-8, 1.3), (-9, 0.3), (-10, -0.5), (-11, -1.5),
    (-12, -2.5), (-13, -3.4), (-14.2, -4.4), (-13, -2.9), (-12, -1.8),
    (-11, -0.7), (-10.4, 0), (-10, 0.5), (-9.5, 1.5), (-9, 3),
    (-8.5, 4), (-8, 4.8), (-7, 5.6), (-6, 5.9), (-5, 5.8),
    (-4, 5.5), (-3, 5.2), (-2.4, 5.1), (-1.8, 5.05), (-1, 5),
    (0, 4.9), (0.7, 4.9), (1.4, 5.5), (1.5, 6.3), (1.8, 7),
    (1.8, 8), (2, 9), (1.8, 10), (1.9, 10.8), (1.7, 11.5),
    (1.8, 12.4), (1.6, 13.2), (1.6, 14), (1.5, 14.7), (1, 14.4),
    (0.5, 13.5), (0, 12.3), (-0.6, 11), (-1.2, 10), (-1.6, 9),
    (-1.8, 8), (-1.8, 7), (-2.1, 6), (-2.4, 5.1), (-1.8, 5.05),
    (-1, 5), (0, 4.9), (0.7, 4.9), (2, 5.5), (3, 6.1),
    (3.5, 6.5), (4, 7.2), (5, 7.9), (6, 8.5), (7, 9),
    (8, 9.5), (9, 10), (10, 10.6), (11, 11.2), (12, 11.8),
    (13, 12.3), (13.5, 12.5), (13.6, 12), (13, 11.2), (13.1, 10.7),
    (12.7, 10.2), (12.1, 10), (12, 9.1), (11.3, 8.4), (11, 7.6),
    (10.2, 7), (9.8, 6.1), (9.3, 5.7), (9.3, 5), (8.7, 4.4),
    (8.1, 4.3), (8, 3.6), (7.5, 3.2), (7.2, 2.4), (6.5, 2),
    (6, 1.3), (5.5, 1.2), (5, 0.4), (4.4, 0.2), (4.3, -0.2),
    (3.8, -0.2), (4, -1), (4.4, -2), (4.7, -3), (5, -4),
    (5.4, -5.5), (5.65, -6.6), (5.8, -7.7), (6, -9), (6, -10),
    (5.8, -11.3), (5, -11.4), (4.4, -10.8), (4.2, -9.7), (3.6, -10.5),
    (2.6, -10.3), (2, -9), (1.6, -9.8), (1, -10.5), (0.5, -10.5),
    (0, -10), (-0.2, -8), (-1, -9), (-2, -9.5), (-2.3, -8.8),
    (-2, -7), (-3, -8), (-3.7, -7.4), (-3.4, -6.3), (-3, -5.1),
    (-2.3, -4), (-1.6, -3.1)
]

# Dividir datos en partes real e imaginaria
parte_real = [x for x, y in datos]
parte_imaginaria = [y for x, y in datos]

# Graficar en el plano complejo
plt.figure(figsize=(8, 6))
plt.scatter(parte_real, parte_imaginaria, color='#072', marker='o', label='Datos')
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginaria')
plt.title('Secuencia de Datos en el Plano Complejo')
plt.grid()
plt.legend()
plt.show()