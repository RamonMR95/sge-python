# Escribe un programa que calcule el tiempo que se tarda en llegar a un sitio dada la velocidad y la distancia.

posicion = input("Me falla el GPS :( ¿Dónde estamos?")
direccion = input("¿A dónde vamos?")
velocidad = float(input("¿A que velocidad?"))
distancia = float(input("¿Te sabes la distancia?"))
print(f"A {velocidad} Km/h tardaríamos {distancia / velocidad} horas")
print(f"A 120 Km/h tardaríamos {round(distancia / 120)} horas")
