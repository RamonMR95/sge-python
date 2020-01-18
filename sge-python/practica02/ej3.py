# Escribe un programa que dada una nota numérica entre 0 y 10 con dos decimales, diga la nota literal que tiene el
# alumno.

nota = float(input("Introduzca la nota: "))

if 0 <= nota < 5:
    resp = "Suspenso"
elif 5 <= nota < 6:
    resp = "Suficiente"
elif 6 <= nota < 7:
    resp = "Bien"
elif 7 <= nota < 9:
    resp = "Notable"
elif 9 <= nota <= 10:
    resp = "Sobresaliente"
elif nota > 10:
    resp = "M Honor"
else:
    resp = "Nota negativa no valida"

print(resp)
