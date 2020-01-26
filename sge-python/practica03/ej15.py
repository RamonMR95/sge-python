#  Escribir un programa que dándole un número (entre 2 y 40) imprima un rombo como el de la
# figura. Ejemplo


num = int(input("Nivel (2-40): "))


def dibujar(num):
    for i in range(num):
        for j in range(num):
            print("X", end="")

        print(" " * (2 * i), end="")

        for j in range(num):
            print("X", end="")
        print("")
        num -= 1


if 2 <= num <= 40:
    dibujar(num)
else:
    print(f"{num} se sale del intervalo (2-40)")
