# Escribir un programa que calcule el factorial de un número dado. Ejemplo:
import math
num = int(input("Introduce un número: "))

print(f"{num}! {math.factorial(num)}")


# Otra forma

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


if num > 0:
    print(f"{num}! {factorial(num)}")
else:
    print("El factorial de un número negativo no existe")

