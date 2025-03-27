import matplotlib.pyplot as plt

def collatz_sequence(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

# Lista para almacenar los números y sus iteraciones
numbers = []
iterations = []

# Generar las secuencias de Collatz para los números entre 1 y 10000
for i in range(1, 10001):
    numbers.append(i)
    iterations.append(collatz_sequence(i))

# Crear el gráfico
plt.plot(iterations, numbers, marker='o', linestyle='-', color='b')
plt.title("Conjetura de Collatz: Número de Iteraciones vs. Número Inicial




