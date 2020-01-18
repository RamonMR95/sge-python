# Escribe un programa que calcule la longitud de una circunferencia. El programa debe pedir el radio y a continuación
# calcular la longitud. Podemos tomar el valor de pi desde el módulo math:

import math
radio = float(input("Dame el radio (en cm por favor): "))
print(f"La longitud de la O es: {2 * math.pi * radio} cm")
