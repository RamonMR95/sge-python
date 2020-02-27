# !/usr/bin/env python3
# 1
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

test = [[1, 2, 3], [4, 5], [6, 7], [8, 9, 10]]


def recortes(mat):
    n_min_cols = len(mat[0])

    for i in range(len(mat)):
        if len(mat[i]) < n_min_cols:
            n_min_cols = len(mat[i])

    matriz_recorte = []
    matriz_sobrante = []

    for i in range(n_min_cols):
        aux = []
        for j in range(n_min_cols):
            aux.append(mat[i][j])
        matriz_recorte.append(aux)

    for i in range(len(mat)):
        aux2 = []
        for j in range(len(mat[i])):
            if j >= n_min_cols or i >= n_min_cols:
                aux2.append(mat[i][j])
        if len(aux2) > 0:
            matriz_sobrante.append(aux2)

    return matriz_recorte, matriz_sobrante
