# Mejora el programa para que no acepte ni números menores de 10 ni mayores de 99.

numero = int(input("Dame un número: "))
if 10 <= numero:
    if numero <= 99:
        print(f"El número al revés es: {str(numero)[::-1]}")
    else:
        print(f"El número {numero} no me sirve, tiene que menor o igual que 99.")
else:
    print(f"El número {numero} no me sirve, tiene que ser mayor o igual que 10.")
