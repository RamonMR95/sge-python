#!/usr/bin/env python3
# 1.- Escribe un programa que cuente el número de vocales de una frase.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

frase = input("Introduzca una frase: ").lower()

# A
print(f"A: {frase.count('a')}, E: {frase.count('e')}, I: {frase.count('i')}, O: {frase.count('o')}, "
      f"U: {frase.count('u')}")

# B

dic = {}

for i in frase.replace(" ", ""):
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

print(dic)
