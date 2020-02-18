# !/usr/bin/env python3
# 3.- Crear una clase Persona con los siguientes miembros:
# ----------------------Propiedades------------------------
# nifnombre apellidos edad
# ------------------------Métodos----------------------------------
# medad mnombre mnif() mapellidos()mostrar nombreCompleto
# En la clase persona el método constructor podrá tener valores por defecto.Crear una clase derivada
# de la clase persona que se llame Alumno. Esta clase heredará los métodos de la clase base y además tendrá una
# propiedad curso y un método mcurso() para visualizar el curso en el que se encuentra el alumno. Hay que redefinir
# en la clase derivada el método mostrar() ya que además de mostrar los atributos de la clase persona debe mostrar el
# curso del alumno.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


class Persona:

    def __init__(self, nif, nombre, apellidos, edad):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def medad(self):
        print(self.edad)

    def mnombre(self):
        print(self.nombre)

    def mnif(self):
        print(self.nif)

    def mapellidos(self):
        print(self.apellidos)

    def mostrar_nombre_completo(self):
        print(f"Nombre: {self.nombre}, Apellidos: {self.apellidos}")


class Alumno(Persona):

    def __init__(self, nif, nombre, apellidos, edad, curso):
        Persona.__init__(self, nif, nombre, apellidos, edad)
        self.curso = curso

    def mcurso(self):
        print(self.curso)

    def mostrar_nombre_completo(self):
        print(f"Nombre: {self.nombre}, Apellidos: {self.apellidos}, Curso: {self.curso}")


if __name__ == '__main__':
    persona = Persona("5525252T", "Roberto", "Bastida", 23)
    alumno = Alumno("43434343X", "Ramon", "Moñino", 24, "2º DAM")
    persona.mostrar_nombre_completo()
    alumno.mostrar_nombre_completo()
    alumno.mcurso()
