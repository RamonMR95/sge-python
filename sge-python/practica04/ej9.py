# !/usr/bin/env python3
# 9.- Escribe un programa que permita catalogar coches. El programa presentará las siguientes opciones al usuario:
#   1.- Alta coche.
#   2.- Baja coche.
#   3.- Listar coches.
#   4.- Salir.
#   Elija opción (1-4)
# El programa podrá almacenar las características de un máximo de 20 coches, cada una de las opciones realizará las
# siguiente acciones:
#   1. Alta coche: Solicitará los datos de un coche y los introducirá en el catálogo. No pueden existir dos coches
#   con la misma marca y modelo. Las características que deben almacenarse son:
#       - Marca.
#       - Modelo.
#       - Cilindrada.
#       - Potencia (CV).
#       - Velocidad máxima
#   2. Baja coche: Borrará un coche indicando la marca y el modelo.
#   3. Listar coches: Sacará un listado en pantalla mostrando marca, modelo, cilindrara y vel máxima.
#   4. Salir: Sale del programa después de preguntar al usuario si está seguro.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

catalogo = {}
n_coches = 0
n_max_coches = 20
salir = False


def alta():
    marca = input("Introduce marca: ")
    modelo = input("Introduce el modelo: ")

    if marca not in catalogo or modelo not in catalogo[marca]:
        cilindrada = input("Introduce cilindrada: ")
        potencia = input("Introduce la potencia: ")
        vel_max = float(input("Introduce la velocidad máxima: "))
        catalogo[marca] = {modelo: [cilindrada, potencia, vel_max]}
        print(f"Coche con marca {marca} y modelo {modelo} dado de alta en el catálogo: ")
    else:
        print("Ya existe ese coche en el catálogo")


def baja():
    if len(catalogo) > 0:
        marca = input("Introduce marca: ")
        modelo = input("Introduce el modelo: ")
        if marca in catalogo and modelo in catalogo[marca]:
            del (catalogo[marca])[modelo]
            print(f"\nCoche con marca {marca} y modelo {modelo} eliminado del catálogo: ")
        else:
            print("\nCoche no disponible en el catálogo: ")
    else:
        print("No existe ningún coche en el catálogo")


def listar():
    print(catalogo)
    if len(catalogo) > 0:
        for marca in catalogo:
            for modelo in catalogo[marca]:
                print(marca, catalogo[marca][modelo])
                print(f"Coche con marca: {marca}, modelo: {modelo}, cilindrada: {catalogo[marca][modelo][0]}, "
                      f"potencia: {catalogo[marca][modelo][1]}, velocidad máxima: {catalogo[marca][modelo][2]}")
    else:
        print("No existe ningún coche en el catálogo")


while not salir:
    opcion = int(input("\n1.- Alta coche.\n"
                       "2.- Baja coche\n"
                       "3.- Listar coches.\n"
                       "4.- Salir.\n"
                       "Elija opción (1-4): "))

    if opcion == 1:
        alta()
    elif opcion == 2:
        baja()
    elif opcion == 3:
        listar()
    elif opcion == 4:
        salir = True
    else:
        print("Opción no válida")
