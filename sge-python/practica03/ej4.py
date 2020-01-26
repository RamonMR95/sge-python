#  Escribir un programa que solicite un número positivo, acto seguido debe calcular la suma de
# todos los números pares comprendidos entre 0 y el numero solicitado. Ejemplo:

num = int(input("Introduce un número positivo: "))
suma = 0

if num > 0:
    for i in range(0, num, 2):
        suma += i
    print(f"La suma es: {suma}")
else:
    print("Error: El número debe ser positivo")


