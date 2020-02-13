# !/usr/bin/env python3
# 7.- Escribe un programa que lea una matriz 5 x 5 de enteros y calcule y muestre la suma de sus fias y de sus columnas:
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

matriz = []
fila = []

# demo = [
#     [2, 5, 3, 4, 5],
#     [2, 6, 8, 4, 5],
#     [9, 8, 3, 5, 2],
#     [5, 3, 8, 5, 6],
#     [0, 1, 4, 3, 4]
# ]

for i in range(1, 6):
    fila = input(f"Introduzca fila {i}: ")
    matriz.append(list(map(int, fila.split())))

sum_colums = []
sum_filas = []
aux_colums = 0
aux_filas = 0

for f in range(len(matriz)):
    for c in range(len(matriz)):
        aux_colums += matriz[c][f]
        aux_filas += matriz[f][c]
    sum_filas.append(aux_filas)
    sum_colums.append(aux_colums)
    aux_colums = 0
    aux_filas = 0


print(f"\nTotales filas: {sum_filas}")
print(f"Totales columnas: {sum_colums}")


