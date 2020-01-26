# Escribir un programa que solicite un número n y a continuación muestre si el número es o no
# primo. Ejemplos:

num = int(input("Introduzca un número: "))
c_div = 0

for i in range(1, num + 1):
    if num % i == 0:
        c_div += 1


if c_div == 2:
    print("El número es primo")
else:
    print("El número NO es primo")
