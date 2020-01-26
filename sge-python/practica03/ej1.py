# 1.- Programa que lee un número y muestra la tabla de multiplicar de dicho número. Hacer el
# ejercicio de dos formas, con bucle while y con bucle for.

num = int(input("Número: "))

for i in range(11):
    print(f"{num} * {i} = ", num * i)


counter = 0
while counter <= 10:
    print(f"{num} * {counter} = ", num * counter)
    counter += 1
