# !/usr/bin/env python3
# 12.- Realizar una función que genere matrices. Esta función no tendrá parámetros. Haciendo uso del
# módulo random generará matrices de tamaño entre 2 y 6 tanto en filas como en columnas (pudiendo ser
# diferente). Luego el contenido de la matriz también se generará aleatoriamente con números entre 0 y
# 100.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

import random


def generar_matriz():
    n_fila = random.randint(2, 6)
    n_col = random.randint(2, 6)

    matriz = [None] * n_col

    for i in range(len(matriz)):
        matriz[i] = [None] * n_fila
        for j in range(len(matriz[i])):
            rand = random.randint(0, 100)
            matriz[i][j] = rand
    return matriz


print(f"La matriz generada es: {generar_matriz()}")
