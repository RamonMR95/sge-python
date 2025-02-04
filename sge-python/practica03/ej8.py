#!/usr/bin/env python3
# Escribir un programa que “dibuje” un mes del calendario. El programa recibirá como entrada el
# número de días del mes y el día de la semana del primer día del mes. Ejemplo:
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

n_dias = int(input("Número de dias del mes: "))
dia1 = int(input("Dia 1 es (0 lunes, 6 domingo): "))

print("L\tM\tX\tJ\tV\tS\tD")
for i in range(dia1):
    print("\t", end="")

for i in range(1, 7 - dia1 + 1):
    print(f"{i}\t", end="")
print()

counter = 0
for i in range(7 - dia1 + 1, n_dias + 1):
    if counter == 7:
        print()
        counter = 0
    print(f"{i}\t", end="")
    counter += 1
