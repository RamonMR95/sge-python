# !/usr/bin/env python3 5.- Escribir un programa para que dada una cantidad de euros la devuelva en el menor número
# de billetes y monedas de curso legal posibles (billetes: 500€, 200€, 100€, 50€, 20€, 10€, 5€. Monedas 2€,
# 1€. El programa debe tener una lista con los billetes y monedas de curso legal. Ejemplo:
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

billetes = [500, 200, 100, 50, 20, 10 ,5]
c_billetes = [0, 0, 0, 0, 0, 0, 0]

monedas = [2, 1]
c_monedas = [0, 0]

cantidad = int(input("Introduzca una cantidaD: "))


for i in billetes:


