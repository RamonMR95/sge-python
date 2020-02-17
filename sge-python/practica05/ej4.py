# !/usr/bin/env python3
# 4.- Escribe un programa que lea un NIF sin letra por teclado, a continuación debe mostrar el
# NIF con la letra asociada. El programa debe contar con la función letra_nif que devuelve la letra correspondiente.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

from practica05.ej3 import calcular_letra

if __name__ == '__main__':
    numeros_nif = input("Introduce el NIF: ")

    if len(str(numeros_nif)) == 8:
        print(f"La letra correspondiente es {calcular_letra(numeros_nif)}")
    else:
        print("El nif debe tener 8 números")



