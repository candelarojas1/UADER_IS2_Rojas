# factorial_OOP.py
# Modificado para usar Programación Orientada a Objetos (OOP) para calcular el factorial
# de un número en un rango específico.
# Dr.P.E.Colla (c) 2022
# Creative commons

class Factorial:
    def __init__(self):
        """Constructor de la clase. Inicializa la instancia de la clase Factorial."""
        pass
    
    def run(self, min, max):
        """Método que calcula el factorial de los números en el rango [min, max]."""
        results = {}
        for num in range(min, max + 1):
            results[num] = self.factorial(num)
        return results
    
    def factorial(self, num):
        """Calcula el factorial de un número de forma recursiva."""
        if num < 0:
            return "El factorial de un número negativo no existe"
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

# Verificación de la funcionalidad del programa
if __name__ == "__main__":
    # Solicitar los valores de min y max al usuario
    try:
        min_val = int(input("Ingrese el valor mínimo: "))
        max_val = int(input("Ingrese el valor máximo: "))
    except ValueError:
        print("Por favor ingrese números válidos.")
        exit()

    factorial_calculator = Factorial()
    results = factorial_calculator.run(min_val, max_val)
    
    # Mostrar los resultados
    print(f"Factoriales entre {min_val} y {max_val}:")
    for num, fact in results.items():
        print(f"{num}! = {fact}")
