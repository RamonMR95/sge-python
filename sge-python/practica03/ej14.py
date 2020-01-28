#!/usr/bin/env python3
# Escribir un programa que dándole un número (entre 2 y 40) imprima un triángulo como el de
# la figura.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


num = int(input("Nivel (2-40): "))

def dibujar(num):
    n_blancos = num
    for i in range(1, num + 1):
        print(" " * n_blancos, end="")
        if num % 2 == 0:
            print("XX" * i)
        else:
            if i == 1:
                print("X" * i)
            else:
                for j in range(1 + (2 * (i - 1))):
                    print("X", end="")
                print("")
        n_blancos -= 1


if 2 <= num <= 40:
    dibujar(num)
else:
    print(f"{num} se sale del intervalo (2-40)")
