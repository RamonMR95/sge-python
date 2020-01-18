# Escribir un programa que dada una fecha en el formato DIA/MES/AÑO, diga si la fecha es correcta o incorrecta. Si la
# fecha es correcta el programa debe escribirla con el formato DIA de Mes de AÑO.

fecha = input("Introduce una fecha con formato DIA/MES/AÑO: ")
dia = fecha.split("/", 1)
mes = fecha.split("/", 2)
anyo = fecha.split("/", 3)


def isBisiesto(anyo):
    if anyo % 4 == 0 and not anyo % 100 == 0 or anyo % 400 == 0:
        return True
    return False



