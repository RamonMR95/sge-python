# !/usr/bin/env python3
# 10.- Escribir un programa que juegue al ahorcado, el programa deberá pensar unaa palabra
# aleatoria de un diccionario fijo de 20 palabras. Una vez "pensada" la palabra, el ordenador dibujará el tablero y
# pondrá tantos huecos como letras tenga la palabra: Se permitirá un total de 6 fallos (cabeza, tronco,
# brazo izquierdo, brazo derecho, pierna izquierda, pierna derecha), al dibujar la pierna derecha aún quedará una
# posibilidad, un fallo más y el jugador quedará ahorcado. Cada vez que el usuario dice una letra el programa deberá
# redibujar de nuevo el tablero haciendo los cambios precisos.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

import random

palabras = {
    1: "PROGRAMACIÓN",
    2: "LIBRO",
    3: "ORDENADOR",
    4: "CASA",
    5: "ALFOMBRILLA",
    6: "RATON",
    7: "PANTALLA",
    8: "TELEVISION",
    9: "ROUTER",
    10: "TECLADO",
    11: "MANDO",
    12: "SILLA",
    13: "ESCRITORIO",
    14: "LLAVES",
    15: "USB",
    16: "CAJON",
    17: "ARMARIO",
    18: "VENTANA",
    19: "CORTINA",
    20: "SOFA"
}

n_intentos = 0
letras_jugadas = 0
letras_int = set()

palabra = random.randint(1, 20)
shadow = ["_"] * len(palabras[palabra])
print(palabras[palabra])


def draw():
    int1 = f"-------------|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"|                  {shadow}\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"---\n" \
           f"Letras jugadas: {letras_jugadas} ({letras_int})\n" \
           f"Diga una letra: _\n"

    int2 = f"-------------|\n" \
           f"|           ###\n" \
           f"|           ###\n" \
           f"|            |\n" \
           f"|            |      {shadow}\n" \
           f"|            |\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"---\n" \
           f"Letras jugadas: {letras_jugadas} ({letras_int})\n" \
           f"Diga una letra: _\n"

    int3 = f"-------------|\n" \
           f"|           ###\n" \
           f"|           ###\n" \
           f"|            |\n" \
           f"|            |      {shadow}\n" \
           f"|        ----|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"---\n" \
           f"Letras jugadas: {letras_jugadas} ({letras_int})\n" \
           f"Diga una letra: _\n"

    int4 = f"-------------|\n" \
           f"|           ###\n" \
           f"|           ###\n" \
           f"|            |\n" \
           f"|            |      {shadow}\n" \
           f"|        ----|----\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"---\n" \
           f"Letras jugadas: {letras_jugadas} ({letras_int})\n" \
           f"Diga una letra: _\n"

    int5 = f"-------------|\n" \
           f"|           ###\n" \
           f"|           ###\n" \
           f"|            |\n" \
           f"|            |      {shadow}\n" \
           f"|        ----|----\n" \
           f"|           /\n" \
           f"|          /\n" \
           f"|         /\n" \
           f"|\n" \
           f"---\n" \
           f"Letras jugadas: {letras_jugadas} ({letras_int})\n" \
           f"Diga una letra: _\n"

    int6 = f"-------------|\n" \
           f"|           ###\n" \
           f"|           ###\n" \
           f"|            |\n" \
           f"|            |      {shadow}\n" \
           f"|        ----|----\n" \
           f"|           / \\\n" \
           f"|          /   \\\n" \
           f"|         /     \\\n" \
           f"|\n" \
           f"---\n" \
           f"Letras jugadas: {letras_jugadas} ({letras_int})\n" \
           f"Diga una letra: _\n"
    screens = [int1, int2, int3, int4, int5, int6]
    return screens[screen_counter]


acierto = False
screen_counter = 0
while not acierto and n_intentos < 6:
    letra = input(draw()).upper()
    letras_jugadas += 1
    if letra in palabras[palabra] and letra not in letras_int:
        for i in range(len(palabras[palabra])):
            if letra == palabras[palabra][i]:
                shadow[i] = letra
    else:
        screen_counter += 1
        n_intentos += 1
        letras_int.add(letra)
    if shadow.count("_") == 0:
        print(draw())
        continuar = input(f"Ha acertado la palabra: {palabras[palabra]}, quiere continuar? S/N").upper()
        if continuar == "N":
            acierto = True
        else:
            n_intentos = 0
            letras_int = set()
            palabra = random.randint(1, 20)
            letras_jugadas = 0
            shadow = ["_"] * len(palabras[palabra])

if not acierto:
    print("Ha perdido")
