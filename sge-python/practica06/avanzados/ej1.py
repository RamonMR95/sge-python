# !/usr/bin/env python3
# 1.-Modelar la Clase Diccionario.
# Un Diccionario dispondrá de como mínimo la siguiente información:
#   - Nombre del diccionario
#   - Editorial
#   - Nivel
#   - Palabras y cada palabra podrá tener una o varias acepciones.

# Se permitirá mediante un menú:
#   - Crear el diccionario,
#   - Introducir las palabras
#   - Introducir acepciones a una palabra (en cualquier momento),
#   - consultar palabras y sus acepciones.
#   - sacar las palabras que empiecen por una letra ordenadas alfabéticamente
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


class Diccionario:

    def __init__(self, nom="dict1", edit="Santillana", niv="Basico", pal=None):
        self.nombre = nom
        self.editorial = edit
        self.nivel = niv
        self.palabras = pal

    def add_palabras(self):
        if self.palabras is not None:
            pal = input("Introduce palabra: ")
            acep = input("Introduce acepciones: separadas por ,").replace(" ", "").split(",")
            self.palabras[pal] = acep
        else:
            print("Primero crea el diccionario!")

    def add_acepciones(self, word, acep):
        if self.palabras is not None:
            self.palabras[word].append(acep)
        else:
            print("Primero crea el diccionario!")

    def mostrar_palabra_acepciones(self):
        if self.palabras is not None:
            for p in palabras:
                print(f"{p}: {palabras[p]}")
        else:
            print("Primero crea el diccionario!")

    def mostrar_palabras_alfab(self):
        if self.palabras is not None:
            for p in diccionario.palabras.items():
                print(p)
        else:
            print("Primero crea el diccionario!")


if __name__ == '__main__':
    salir = False
    diccionario = Diccionario()

    while not salir:
        opcion = int(input(f"\n1- Crear el diccionario.\n"
                           f"2- Introducir las palabras.\n"
                           f"3- Introducir acepciones a una palabra (en cualquier momento).\n"
                           f"4- consultar palabras y sus acepciones.\n"
                           f"5- sacar las palabras que empiecen por una letra ordenadas alfabéticamente.\n"
                           f"6- Salir.\n"))

        if opcion == 1:
            nombre = input("Introduce el nombre: ")
            editorial = input("Introduce el editorial: ")
            nivel = input("Introduce el nivel: ")
            palabra = input("Introduce palabra: ")
            acepciones = input("Introduce acepciones: separadas por ,").replace(" ", "").split(",")
            palabras = {palabra: acepciones}
            diccionario = Diccionario(nombre, editorial, nivel, palabras)

        elif opcion == 2:
            diccionario.add_palabras()

        elif opcion == 3:
            palabra = input("Introduce la palabra: ")
            if palabra in diccionario.palabras:
                acepciones = input("Introduce acepciones: separadas por ,").replace(" ", "").split(",")
                for acepcion in acepciones:
                    diccionario.add_acepciones(palabra, acepcion)

        elif opcion == 4:
            diccionario.mostrar_palabra_acepciones()

        elif opcion == 5:
            diccionario.mostrar_palabras_alfab()

        elif opcion == 6:
            print("Hasta la vista!")
            salir = True

