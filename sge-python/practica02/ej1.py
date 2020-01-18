# Escribir un programa que pida tres números enteros por teclado y determine el mayor y el menor de los tres números.

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))

lst = [num1, num2, num3]
lst.sort()
print(f"Mayor número: {lst[2]}")
print(f"Menor número: {lst[0]}")

