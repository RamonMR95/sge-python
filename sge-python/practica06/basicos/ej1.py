# !/usr/bin/env python3
# 1.- Cree una clase COrdenador para simular el trabajo con ordenadores. La clase COrdenador
# puede incluir los siguientes atributos:
# b).- Modificar el ejercicio anterior para:- Tener en cuenta que la
# propiedad Cpeso es una propiedad privada y debe accederse através de su propiedad virtual Peso.  Al asignarles
# valor, estos procedimientos debencomprobar que al peso no se le asigna un valor < 1.- Sustituir el método Estado
# del ordenador por __str__
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


class COrdenador:

    def __init__(self, c_marca, c_procesador, c_peso, c_estado, c_pantalla):
        self.c_marca = c_marca
        self.c_procesador = c_procesador
        self.__c_peso = c_peso
        self.c_estado = c_estado
        self.c_pantalla = c_pantalla

    def encender_pc(self):
        if self.c_estado:
            print(f"El ordenador está encendido")
        else:
            self.c_estado = True
            self.c_pantalla = True
            print(f"Ordenador y pantalla han sido encendidas")

    def apagar_pc(self):
        if not self.c_estado:
            print("El pc ya estaba apagado")
        else:
            self.c_estado = False
            print("El pc ha sido apagado")

    def desactivar_pantalla(self):
        if not self.c_pantalla:
            print("La pantalla ya estaba apagada")
        else:
            self.c_pantalla = False
            print("La pantalla ha sido apagada")

    def activar_pantalla(self):
        if self.c_pantalla:
            print("La pantalla ya estaba encendida")
        else:
            self.c_pantalla = True
            print("La pantalla ha sido apagada")

#    def estado_ordenador(self):
#        print(f"Marca: {self.c_marca}, Procesador: {self.c_procesador}, Peso: {self.__c_peso}"
#              f", Pantalla: {self.c_pantalla}, Ordenador: {self.c_estado} ")

    def __str__(self):
        return f"Marca: {self.c_marca}, Procesador: {self.c_procesador}, Peso: {self.__c_peso}"\
              f", Pantalla: {self.c_pantalla}, Ordenador: {self.c_estado} "

    def get_peso(self):
        return self.__c_peso

    def set_peso(self, peso):
        if peso >= 1:
            self.__c_peso = peso

    weigth = property(get_peso, set_peso)


if __name__ == '__main__':
    ordenador_trabajo = COrdenador("MSI", "I9", 1, False, True)
    ordenador_casa = COrdenador("Toshiba", "I7", 1.4, True, True)

    ordenador_casa.apagar_pc()
    ordenador_trabajo.encender_pc()

#    ordenador_trabajo.estado_ordenador()
#    ordenador_casa.estado_ordenador()

    print(ordenador_trabajo.__str__())
    print(ordenador_casa.__str__())

    ordenador_trabajo.desactivar_pantalla()
#    ordenador_trabajo.estado_ordenador()
    print(ordenador_trabajo.__str__())

    ordenador_trabajo.apagar_pc()



