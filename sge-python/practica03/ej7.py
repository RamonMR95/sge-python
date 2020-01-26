# Escribir un programa que solicite números (enteros o reales), el programa terminará cuando
# se introduzca el cero. A continuación debe mostrar el mayor número. Ejemplo:

num = float(input("Introduzca un número (cero para terminar):"))
mayor = num

while num != 0:
    num = float(input("Introduzca un número (cero para terminar):"))
    if num > mayor:
        mayor = num

print(f"Mayor: {mayor}")
