# Programa que usa la funcion recortes

from examen.ejercicios.ej1 import recortes

test = [[1, 2, 3], [4, 5], [6, 7], [8, 9, 10]]


def mostrar_matriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end="")
        print()


def mostrar_label(num):
    if num == 0:
        print("\nMatriz original")
    elif num == 1:
        print("\nMatriz recortada")
    elif num == 2:
        print("\nMatriz sobrante")


if __name__ == '__main__':
    my_tup = recortes(test)

    mostrar_label(0)
    mostrar_matriz(test)

    for i in range(len(my_tup)):
        mostrar_label(i)
        mostrar_matriz(my_tup[i])
