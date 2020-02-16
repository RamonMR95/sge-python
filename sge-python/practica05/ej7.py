# !/usr/bin/env python3
# 7.- Diseña una función que, dada una lista de cadenas, devuelva una lista con todas las cadenas más
# largas, es decir, si dos o más cadenas miden lo mismo y son las más largas, la lista las contendrá a todas.
# (Ejemplo: dada la lista [“Pepe”, “Ana”, “Juan”, “Paz”], la función devolverá la lista de dos elementos
# [“Pepe”, “Juan”]).
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

lst = ["Pepe", "Ana", "Juan", "Paz"]

mayor_n_letras = len(lst[0])

for i in range(len(lst)):
    if len(lst[i]) > mayor_n_letras:
        mayor_n_letras = len(lst[i])

res = []

for i in range(len(lst)):
    if len(lst[i]) == mayor_n_letras:
        res.append(lst[i])


print(res)
