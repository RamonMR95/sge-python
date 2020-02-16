# !/usr/bin/env python3
# 6.- Diseña una función llamada es_repetición que reciba una cadena y nos diga si la cadena está formada
# mediante la concatenación de una cadena consigo misma. Por ejemplo, es_repetición(‘abab’) devolverá
# True, pues la cadena está formada con la cadena ‘ab’ repetida; por contra es_repetición(‘ababab’)
# devolverá False.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

cadena = input("Introduzca cadena: ")


def repeticion(cad):
    return cadena[:len(cadena) // 2] == cadena[len(cadena) // 2:]


if repeticion(cadena):
    print("Cadena formada por repeticion")
else:
    print("Cadena no formada por repeticion")
