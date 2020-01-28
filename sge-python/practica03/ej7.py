#!/usr/bin/env python3
# Escribir un programa que solicite números (enteros o reales), el programa terminará cuando
# se introduzca el cero. A continuación debe mostrar el mayor número. Ejemplo:
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


num = float(input("Introduzca un número (cero para terminar):"))
mayor = num

while num != 0:
    num = float(input("Introduzca un número (cero para terminar):"))
    if num > mayor:
        mayor = num

print(f"Mayor: {mayor}")
