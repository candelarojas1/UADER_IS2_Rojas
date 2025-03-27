#!/usr/bin/python

#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Si no se pasa ningún argumento, solicitar el número al usuario
if len(sys.argv) == 1:
    num = input("Debe ingresar un número: ")
    try:
        num = int(num)  # Convertir a entero
    except ValueError:
        print("Por favor ingrese un número válido.")
        sys.exit()
else:
    num = int(sys.argv[1])

print("Factorial de", num, "es", factorial(num))


