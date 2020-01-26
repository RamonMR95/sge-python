# Escribir un programa que solicite un número n y a continuación imprima todos los números
# primos comprendidos en el intervalo [2-n]. Ejemplo

num = int(input("Introduzca un número: "))
primos = []

for i in range(2, num + 1):
    c_div = 0
    for j in range(1, num + 1):
        if i % j == 0:
            c_div += 1
    if c_div == 2:
        primos.append(i)

print(primos)
