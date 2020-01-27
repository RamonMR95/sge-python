# Escribir un programa que haga que el usuario piense un número entero de 1 a 100, el
# programa deberá adivinarlo en el menor número de intentos posible. Al final debe decir en
# cuántos intentos lo ha conseguido, un “posible” simulacro (no óptimo) del juego podría ser:

import random


print("Piense un número del 0 al 100 (no me engañe ni cambie de número)")
input("Pulse enter para comenzar")

acierto = False
n_intentos = 0
intentos = {-1}
limInf = 1
limSup = 100

while not acierto:
    n_intentos += 1
    num = random.randint(limInf, limSup)
    while num in intentos:
        num = random.randint(limInf, limSup)
        if num not in intentos:
            intentos.add(num)
    resp = input(f"¿es el {num}? (m-mayor, n-menor, i-igual)")

    if resp == "m":
        if num > limInf:
            limInf = num
    if resp == "n":
        if num < limSup:
            limSup = num
    if resp == "i":
        print(f"¡¡¡Qué bueno soy, lo he acertado en tan sólo {n_intentos} intentos!!!")
        volver_jugar = input("¿Desea jugar otra vez (S/N)?").upper()
        if volver_jugar == "N":
            acierto = True
            print("Hasta la vista")

    cambiar = input("Quiere cambiar el número? (S/N)").upper()
    if cambiar == "S" and not acierto:
        n_intentos = 0
        limInf = 0
        limSup = 100
        intentos = {-1}




