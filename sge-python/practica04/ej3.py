# !/usr/bin/env python3
# 3.- Escribe un programa que vaya leyendo notas de alumnos, el programa dejará de pedir notas
# cuando se pulse la tecla ENTER, al terminar el programa mostrará las notas de los alumnos y un resumen de aprobados
# y suspensos incluyendo la nota media:
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

n_alumnos = 0
n_aprobados = 0
hist_notas = []

print("Introduzca las notas, ENTER para terminar ")
nota = input(f"Nota del alumno {n_alumnos + 1}: ")


while nota != "":
    hist_notas.append(float(nota))

    n_alumnos += 1

    if float(nota) >= 5:
        n_aprobados += 1

    nota = input(f"Nota del alumno {n_alumnos + 1}: ")


for i in range(len(hist_notas)):
    print(f"Alumno {i}: { hist_notas[i] }")


if n_alumnos > 0:
    print(f"Resumen: ")
    print(f"Aprobados: {n_aprobados}")
    print(f"\tSuspensos: {len(hist_notas) - n_aprobados}")
    print(f"\tNota media: {sum(hist_notas) / (len(hist_notas))}")
else:
    print("No ha introducido ningún alumno")