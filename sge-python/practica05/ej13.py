# !/usr/bin/env python3
# 12.- Diseña una función que reciba una matriz (generada a partir de la función del ejercicio anterior) y, si
# es cuadrada (es decir, tiene igual número de filas que de columnas), devuelva la suma de todos los
# componentes dispuestos en la diagonal principal (es decir, todos los elementos de la forma Ai,i). Si la
# matriz no es cuadrada, la función devolverá None.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

from practica05.ej12 import generar_matriz

matriz = generar_matriz()

if len(matriz) == len(matriz[0]):
    suma = 0
    for i in range(len(matriz)):
        print(matriz[i][i])
        suma += matriz[i][i]
else:
    print(f"La matriz no es cuadrada! ({len(matriz)} X {len(matriz[0])})")
