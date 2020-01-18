# Escribir un programa que calcule ecuaciones de segundo grado del tipo ax2+bx+c=0. El programa solicitará los
# coeficientes a, b y c. A continuación mostrará las soluciones.

import math

a = int(input("Introduce a: "))
b = int(input("Introduce b: "))
c = int(input("Introduce c: "))

if a == 0 and b == 0:
    print("Ecuacion denegada")
elif a == 0 and b != 0:
    print(f"Solución única: {-c / b}")
else:
    discriminante_sin_raiz = math.pow(b, 2) - (4 * a * c)

    if discriminante_sin_raiz > 0:
        valorPositivo = -b / 2 * a + math.sqrt(discriminante_sin_raiz) / 2 * a
        valorNegativo = -b / 2 * a - math.sqrt(discriminante_sin_raiz) / 2 * a
        print(f"x1: {valorPositivo} y x2: {valorNegativo}")
    elif discriminante_sin_raiz == 0:
        valorPositivo = -b / 2 * a + math.sqrt(discriminante_sin_raiz) / 2 * a
        print(f"Solución única doble x1: {valorPositivo}")
    else:
        print("La ecuación no tiene una solución real")
