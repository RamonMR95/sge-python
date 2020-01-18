# Una tienda que vende ropa está de rebajas. La tiene ofrece un 10% de descuento para compras por un importe por
# debajo de los 20€. Para compras de 20€ en adelante el descuento es del 20%. Escribe un programa que dada la
# cantidad total de la compra aplique el descuento correctamente y muestra la cantidad final.

importe = float(input("Importe total: "))

if importe < 20:
    print(f"Descuento: {importe * 0.1} (10%)")
    print(f"Importe tras descuento: {round(importe * 0.9)} €")
elif importe >= 20:
    print(f"Descuento: {importe * 0.2} (20%)")
    print(f"Importe tras descuento: {importe * 0.8} €")

