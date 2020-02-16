# !/usr/bin/env python3
# 3.- Escribe un programa que lea una cadena de texto, acto seguido debe comprobar que se trata
# de un número de NIF correcto, 8 dígitos y una letra. El programa debe contar con la función es_nif que devuelva si
# el NIF es o no correcto. La función debe calcular la letra según el parámetro pasado, calcular la letra
# correspondiente a un NIF es bastante sencillo, hay que realizar la división entera del número del NIF entre 23,
# se toma el resto y se asigna una letra según la siguiente tabla.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

import re

tabla = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
         "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

nif = input("Introduce el NIF: ")
n_numeros = len(re.findall(r"\d", nif))
n_letras = len(re.findall(r"[a-zA-Z]", nif))


def es_nif():
    nums = int(nif[:8])
    letra = tabla[nums % 23]
    if letra == str(nif[8:]):
        print("NIF Válido")
    else:
        print(f"La letra válida sería {letra}")


if n_numeros == 8 and n_letras == 1:
    es_nif()
else:
    print("Longitud del nif es inválida")
