# !/usr/bin/env python3
# 8.- Escribe un programa para la emisión de facturas. El programa permitirá dar de alta un
# máximo de 20 artículos con su marca, modelo y descripción. Para realizar una factura el programa solicitará el
# nombre, DNI y dirección completa del comprador, acto seguido permitirá elegir qué componentes y cantidades
# figurarán en la factura, los imprimirá desglosados y calculará el importe base, el IVA (16%) y el importe total.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

articulos = []
continuar = ""

while len(articulos) <= 20 and continuar != "n":
    articulos.append(input("Introduce cantidad, marca, modelo, descripción y precio del articulo separados por comas: ")
                     .replace(" ", "").split(","))
    continuar = input("Quiere introducir más artículos? S/N: ")

print(articulos)

nombre = input("Introduzca su nombre: ")
dni = input("Introduzca su dni: ")
dir_completa = input("Introduzca su dirección completa: ")

continuar = ""
factura = []

while continuar != "n":
    componente = input("Qué componente quiere?: ")
    encontrado = False
    i = 0
    precio = 0

    while not encontrado and i < len(articulos):
        if articulos[i][2] == componente:
            precio = articulos[i][4]
            encontrado = True
        i += 1

    if encontrado:
        cantidad = int(input("Cantidad?"))
        if int(articulos[i - 1][0]) >= cantidad:
            precio_base = float(precio) * int(cantidad)
            articulos[i - 1][0] = str(int(articulos[i - 1][0]) - cantidad)
            factura.append([componente, int(cantidad), precio_base, precio_base * 0.16, precio_base * 1.16])
        else:
            print(f"No hay existencias del componente {componente}")
    else:
        print("Componente no encontrado en la lista de articulos\n")

    continuar = input("Quiere introducir más componentes? S/N: ")


if len(factura) > 0:
    print(f"Cliente: {nombre}")

    for i in range(len(factura)):
        print(f"\nFactura nº: {i + 1}")
        print(f"Component: {factura[i][0]}")
        print(f"Cantidad: {factura[i][1]}")
        print(f"Precio Base: {factura[i][2]}")
        print(f"IVA: {factura[i][3]}")
        print(f"Importe Total: {factura[i][3]}\n")
else:
    print("Factura vacía!")




