#!/usr/bin/env python3
# Escribe un programa que dado un número, muestre todos los múltiplos de 11 desde el cero
# hasta el número.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


num = int(input("Introduzca un número: "))
mult = []

for i in range(0, num, 11):
    mult.append(i)

print(f"Los múltiplos son: {mult}")
