#!/usr/bin/env python3
# 1.- Escribe un programa que cuente el número de vocales de una frase.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

frase = input("Introduzca una frase: ").lower()

# A
print(f"A: {frase.count('a')}, E: {frase.count('e')}, I: {frase.count('i')}, O: {frase.count('o')}, U: {frase.count('u')}")

# B
lst = [0, 0, 0, 0, 0]

for i in frase:
    if i == 'a':
        lst[0] += 1
    elif i == 'e':
        lst[1] += 1
    elif i == 'i':
        lst[2] += 1
    elif i == 'o':
        lst[3] += 1
    elif i == 'u':
        lst[4] += 1

print(f"A: {lst[0]}, E: {lst[1]}, I: {lst[2]}, O: {lst[3]}, U: {lst[4]}")

