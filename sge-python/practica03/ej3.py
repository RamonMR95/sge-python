#!/usr/bin/env python3
# Programa que lee notas de los alumnos y dice cuántos están aprobados y cuál es la nota
# media. El programa dejará de pedir notas, cuando se pulse la tecla ENTER.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

nota = input("Introduzca las notas, Enter para terminar: ")
n_alumnos = 0
n_aprobados = 0
n_suspensos = 0
suma_notas = 0

while nota != "":
    print(f"Nota del alumno {n_alumnos + 1}: {float(nota)}")
    if float(nota) >= 5:
        n_aprobados += 1
    else:
        n_suspensos += 1
    suma_notas += float(nota)
    n_alumnos += 1
    nota = input("Introduzca las notas, Enter para terminar: ")

print(f"Número de alumnos: {n_alumnos}")
print(f"Aprobados: {n_aprobados}")
print(f"Suspensos: {n_suspensos}")
print(f"Nota media: {suma_notas / n_alumnos}")