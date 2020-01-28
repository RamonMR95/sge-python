#!/usr/bin/env python3
# Escribir un programa que imprima las 10 tablas de multiplicar
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

for i in range(1, 11):
    for j in range(11):
        print(f"{i} * {j} = ", i * j)
