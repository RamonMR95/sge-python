# !/usr/bin/env python3
# 1.- Cree una clase Ccoche que represente coches. Incluya las propiedades marca,
# modelo y color y los métodos que simulen las acciones Arrancar motor, acelerar, subir marcha, bajar marcha, frenar,
# y parar motor. Establecer que cuando se ejecuta el módulo directamente (no es llamado por otro módulo),
# cree un objeto coche. Arrancad el coche, acelerarlo, subir marcha, acelerar más, volver a subir marcha, frenar,
# bajar marcha, frenar bajar marcha y parar el motor. Se irán poniendo mensaje que muestren el cambio de estado en
# cada momento
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


class Ccoche:

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    @staticmethod
    def arrancar_motor():
        print("Arrancando motor!")

    @staticmethod
    def acelerar():
        print("Acelerando!")

    @staticmethod
    def subir_marcha():
        print("Subiendo marca!")

    @staticmethod
    def frenar():
        print("Frenando!")

    @staticmethod
    def bajar_marcha():
        print("Bajando marcha!")

    @staticmethod
    def apagar_motor():
        print("Apagando motor!")


if __name__ == '__main__':
    opel = Ccoche("Open", "Astra", "Rojo")
    opel.arrancar_motor()
    opel.acelerar()
    opel.subir_marcha()
    opel.acelerar()
    opel.subir_marcha()
    opel.frenar()
    opel.bajar_marcha()
    opel.apagar_motor()
