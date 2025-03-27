#!/usr/bin/python3
# Programa en Python para mostrar todos los números primos dentro de un intervalo

# Definimos los límites del intervalo
lower = 1  # Límite inferior
upper = 500  # Límite superior

# Imprimimos un mensaje indicando el rango en el que buscaremos números primos
print("Números primos entre", lower, "y", upper, "son:")

# Recorremos todos los números dentro del intervalo especificado
for num in range(lower, upper + 1):
    # Los números primos son mayores que 1
    if num > 1:
        # Verificamos si el número es divisible por algún otro número menor que él mismo
        for i in range(2, num):
            # Si es divisible por otro número distinto de 1 y de sí mismo, no es primo
            if (num % i) == 0:
                break  # Salimos del bucle si encontramos un divisor
        else:
            # Si no encontramos divisores, el número es primo y lo imprimimos
            print(num)
