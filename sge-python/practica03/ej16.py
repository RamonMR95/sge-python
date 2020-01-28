#!/usr/bin/env python3
# Escribir un programa para que dada una cantidad de euros la devuelva en el menor número
# de billetes y monedas de curso legal posible (billetes: 500 €, 200 €, 100 €, 50 €, 20 €, 10 € y 5€.
# Monedas: 2 €, 1 €. Ejemplo:
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


cantidad = int(input("Introduzca una cantidad: "))
b_500 = 0
b_200 = 0
b_100 = 0
b_50 = 0
b_20 = 0
b_10 = 0
b_5 = 0
m_2 = 0
m_1 = 0

while cantidad > 0:
    if cantidad >= 500:
        b_500 = cantidad // 500
        cantidad -= b_500 * 500
    elif 500 > cantidad >= 200:
        b_200 = cantidad // 200
        cantidad -= b_200 * 200
    elif 200 > cantidad >= 100:
        b_100 = cantidad // 100
        cantidad -= b_100 * 100
    elif 100 > cantidad >= 50:
        b_50 = cantidad // 50
        cantidad -= b_50 * 50
    elif 50 > cantidad >= 20:
        b_20 = cantidad // 20
        cantidad -= b_20 * 20
    elif 20 > cantidad >= 10:
        b_10 = cantidad // 10
        cantidad -= b_10 * 10
    elif 10 > cantidad >= 5:
        b_5 = cantidad // 5
        cantidad -= b_5 * 5
    elif 5 > cantidad >= 2:
        m_2 = cantidad // 2
        cantidad -= m_2 * 2
    else:
        m_1 = cantidad
        cantidad = 0

if b_500 > 0:
    print(f"{b_500} billetes de 500")

if b_200 > 0:
    print(f"{b_200} billetes de 200")

if b_100 > 0:
    print(f"{b_100} billetes de 100")

if b_50 > 0:
    print(f"{b_50} billetes de 50")

if b_20 > 0:
    print(f"{b_20} billetes de 20")

if b_10 > 0:
    print(f"{b_10} billetes de 10")

if b_5 > 0:
    print(f"{b_5} billetes de 5")

if m_2 > 0:
    print(f"{m_2} moneda de 2")

if m_1 > 0:
    print(f"{m_1} moneda de 1")
