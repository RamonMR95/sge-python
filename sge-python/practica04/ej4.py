# !/usr/bin/env python3
# 3.- Introduce un programa que pida nombres. Tras pedirlos debe mostrarlos ordenados.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

nombres = []
nombre = input("Introduce nombres. ENTER para terminar")

while nombre != "":
    nombres.append(nombre)
    nombre = input()

if len(nombres) > 0:
    nombres.sort()

    print("Los nombres son: ")

    for i in nombres:
        print(i)
else:
    print("No ha introducido ningún nombre")