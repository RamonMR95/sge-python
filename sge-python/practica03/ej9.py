# Escribir un programa para calcular superficies. Constará de un menú que solicitará la figura a
# la que se va a calcular la superficie, pedirá los datos (lado, base y altura, radio ...) según la figura
# de la que se trate y visualizará el resultado. El programa deberá calcular superficies de las
# siguientes figuras: cuadrados, triángulos y círculos. Ejemplo:
import math


def area_cuadrado():
    lado = float(input("Lado: "))
    print(f"La superficie es de {lado ** 2} cm^2", end="\n\n")


def area_triangulo():
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    print(f"La superficie es de {(base * altura) / 2} cm^2", end="\n\n")


def area_circulo():
    radio = float(input("Radio: "))
    print(f"La superficie es de {math.pi * radio ** 2} cm^2", end="\n\n")


while True:
    print("Cálculo de superficies:")
    print("1.- Cuadrados")
    print("2.- triángulos")
    print("3.- Círculos")
    print("4.- Salir")
    opcion = int(input("Elija opción (1-4): "))
    if opcion == 4:
        print("Hasta pronto")
        break
    if opcion == 1:
        area_cuadrado()
    elif opcion == 2:
        area_triangulo()
    elif opcion == 3:
        area_circulo()
    print("Elija opción (1-4): ")


