# !/usr/bin/env python3
# 4.- Escribe un programa que lea un NIF sin letra por teclado, a continuación debe mostrar el
# NIF con la letra asociada. El programa debe contar con la función letra_nif que devuelve la letra correspondiente.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


numeros_nif = int(input("Introduce el NIF: "))

tabla = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
         "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

def es_nif():
    letra = tabla[numeros_nif % 23]
    print(f"El nif sería {str(numeros_nif) + letra}")

if len(str(numeros_nif)) == 8:
    es_nif()
else:
    print("El nif debe tener 8 números")


