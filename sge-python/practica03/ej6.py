#!/usr/bin/env python3
# Escribir un programa que muestre la tabla ASCII. Extracto:
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

print("Tabla ASCII (Caracteres de 32 a 126")

for i in range(32, 127):
    print(f"{i} => {chr(i)}")

