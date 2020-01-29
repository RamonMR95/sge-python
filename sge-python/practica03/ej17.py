#!/usr/bin/env python3
# Escribir un programa que haga que el usuario piense un número entero de 1 a 100, el
# programa deberá adivinarlo en el menor número de intentos posible. Al final debe decir en
# cuántos intentos lo ha conseguido, un “posible” simulacro (no óptimo) del juego podría ser:
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

import random

print("Piense un número del 1 al 100 (no me engañe ni cambie de número)")
input("Pulse enter para comenzar")

acierto = False


def reset():
    global n_intentos
    global intentos
    global limInf
    global limSup
    n_intentos = 0
    intentos = {-1}
    limInf = 1
    limSup = 100


reset()


while not acierto:
    n_intentos += 1
    num = random.randint(limInf, limSup)
    while num in intentos:
        num = random.randint(limInf, limSup)
        if num not in intentos:
            intentos.add(num)
    resp = input(f"¿es el {num}? (m-mayor, n-menor, i-igual)")

    if resp == "m":
        limInf = num + 1
    if resp == "n":
        limSup = num - 1
    if resp == "i":
        print(f"¡¡¡Qué bueno soy, lo he acertado en tan sólo {n_intentos} intentos!!!")
        volver_jugar = input("¿Desea jugar otra vez (S/N)?").upper()
        if volver_jugar == "N":
            acierto = True
            print("\nHasta la vista!!")
        else:
            reset()
    if limSup - limInf <= 1:
        print(f"No puede cambiar el número a mitad del juego")
        acierto = True
        reset()
