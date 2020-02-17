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


def calcular_letra(v_nif):
    nums = int(v_nif[:8])
    letra = tabla[nums % 23]
    return letra


def es_nif(v_nif):
    letra = calcular_letra(v_nif)
    if letra == str(v_nif[8:]):
        return True
    return False


if __name__ == '__main__':
    nif = input("Introduce el NIF: ")
    n_numeros = len(re.findall(r"\d", nif))
    n_letras = len(re.findall(r"[a-zA-Z]", nif))

    if n_numeros == 8 and n_letras == 1:
        if es_nif(nif):
            print("NIF Válido")
        else:
            print(f"La letra válida sería {calcular_letra(nif)}")
    else:
        print("Longitud del nif es inválida")
