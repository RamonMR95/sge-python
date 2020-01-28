#!/usr/bin/env python3
# Escribir un programa que tome 100 números aleatorios entre 0 y 99. A continuación debe 2
# mostrar cuántos números están comprendidos en los intervalos [0-19], [20-39], [40-59], [60-79] y
# [80-99]. Ejemplo:
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

import random

interv1 = 0
interv2 = 0
interv3 = 0
interv4 = 0
interv5 = 0

for i in range(100):
    num = random.randint(0, 99)
    if 0 <= num <= 19:
        interv1 += 1
    elif 20 <= num <= 39:
        interv2 += 1
    elif 40 <= num <= 59:
        interv3 += 1
    elif 60 <= num <= 79:
        interv4 += 1
    elif 80 <= num <= 99:
        interv5 += 1

print(f"[0-19]: {interv1}")
print(f"[20-39]: {interv2}")
print(f"[40-59]: {interv3}")
print(f"[60-79]: {interv4}")
print(f"[80-99]: {interv5}")
print(f"Total: {interv1 + interv2 + interv3 + interv4 + interv5}")
