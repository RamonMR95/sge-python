# Estás en un largo viaje en coche, la distancia a la próxima gasolinera es de 200km. Escribe un programa que
# preguntando el tamaño del depósito, el % del combustible restante y el consumo, muestra si puedes o no llegar a la
# gasolinera

tam_deposito = float(input("Tamaño del depósito (litros): "))
porc_combustible = int(input("% de combustible: "))
consumo = float(input("Consumo (1/100 Km): "))

print(f"Puedes recorrer {tam_deposito * porc_combustible/100 * consumo} Km más.")

if tam_deposito * porc_combustible/100 * consumo >= 200:
    print("Espera a la próxima gasolinera.")
else:
    print("La gasolinera está a 200 Km. ¡¡ Echa gasolina !!")



