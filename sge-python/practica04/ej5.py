# !/usr/bin/env python3
# 5.- Escribir un programa para que dada una cantidad de euros la devuelva en el menor número
# de billetes y monedas de curso legal posibles (billetes: 500€, 200€, 100€, 50€, 20€, 10€, 5€. Monedas 2€,
# 1€. El programa debe tener una lista con los billetes y monedas de curso legal. Ejemplo:
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

billetes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
c_billetes = [0, 0, 0, 0, 0, 0, 0, 0, 0]

cantidad = int(input("Introduzca una cantidad: "))

i = 0
while i <= len(billetes) and cantidad > 0:
    if cantidad >= billetes[i]:
        c_billetes[i] += cantidad // billetes[i]
        cantidad = cantidad % billetes[i]
    i += 1


if cantidad > 0:
    print("Billetes")

    for i in range(len(billetes)):
        print(f"{billetes[i]}: {c_billetes[i]}")
else:
    print("Introduzca una cantidad válida")
