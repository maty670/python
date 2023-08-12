def riemann_sum(points):
    Z = points[0]
    
    riemann_sum = 0
    
    for i in range(1, len(points)):
        Z = (points[i] + points[i-1])/2
        riemann_sum += Z
    return riemann_sum


complex_points = [3 + 1j,
                  -2 - 3j,
                  -7 - 4j,
                  8 + 3j]

result = riemann_sum(complex_points)
print("La suma de Riemann es:", result)