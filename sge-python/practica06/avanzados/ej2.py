# !/usr/bin/env python3
# 2.- La empresa informática “IPMTech” necesita llevar un registro de todos sus empleados
# que se encuentran en la oficina central, para eso ha creado un diagrama de clases que debe
# incluir lo siguiente:
# A) Empleado
# Atributos:
#   -nombre: tipo cadena (Debe ser nombre y apellido)
#   -- edad : entero (Rango entre 18 y 45 años)
#   - salario: tipo numérico doble
# Métodos:
#   - Constructor con y sin parámetros de entrada (no hay dos constructores, es poner lo de
# los parámetros opcionales)
#   - Método que permita mostrar la clasificación según la edad de acuerdo al siguiente
#   algoritmo:
#   Si edad es menor o igual a 21, Principiante
#   Si edad es >=22 y 35,Senior.-
#   - Imprimir los datos del empleado por pantalla (utilizar salto de línea \n para separar los
#   atributos.
#   - Un método que permita aumentar el salario en un porcentaje que sería pasado como
# parámetro al método.
# B) Programador (Especialización de Empleado). Clase que hereda de Empleado todos los
# atributos y métodos.
#   - Atributos:
#   - lineasDeCodigoPorHora : tipo entero
#   -lenguajeDominante: tipo cadena
#   - Metodos:
#   - Constructor con y sin parámetos de entrada. (no hay dos constructores, es poner lo de
#   los parámetros opcionales)
# Implementar mediante una lista de empleados y un menú la funcionalidad necesaria para
# dar crear empleados de los diferentes tipos y poder aumentar su sueldo.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


class Empleado:

    def __init__(self, nombre="test", edad=11, salario=1111.1):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def clasificacion_segun_edad(self):
        if self.edad <= 21:
            print("Principiante!")
        elif 22 <= self.edad:
            print("Senior!")

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nSalario: {self.salario}\n"

    def aumentar_salario(self, porc):
        self.salario *= ((porc / 100) + 1)


class Programador(Empleado):

    def __init__(self, nombre, edad, salario, lineas_codigo_por_hora=2, lenguaje_dominante="Java"):
        Empleado.__init__(self, nombre, edad, salario)
        self.lineas_codigo_por_hora = lineas_codigo_por_hora
        self.lenguaje_dominante = lenguaje_dominante

    def __str__(self):
        return Empleado.__str__(self) + f"Lineas: {lineas_codigo}\nLenguaje dominante: {lenguaje_dominante}"


if __name__ == '__main__':
    lst_empleados = []

    salir = False
    while not salir:
        opcion = int(input("\n1- Crear Empleado.\n"
                           "2- Crear programador.\n"
                           "3- Aumentar sueldo programador (nombre).\n"
                           "4- Mostrar empleados.\n"
                           "5- Salir."))

        if opcion == 1:
            nombre = input("Introduce el nombre del empleado: ")
            edad = int(input("Introduce la edad del empleado: "))
            salario = float(input("Introduce el salario del empleado: "))
            lst_empleados.append(Empleado(nombre, edad, salario))
        elif opcion == 2:
            nombre = input("Introduce el nombre del programador: ")
            edad = int(input("Introduce la edad del programador: "))
            salario = float(input("Introduce el salario del programador: "))
            lineas_codigo = int(input("Introduce el número de líneas de código por hora: "))
            lenguaje_dominante = input("Introduce el lenguaje dominante: ")
            lst_empleados.append(Programador(nombre, edad, salario, lineas_codigo, lenguaje_dominante))
        elif opcion == 3:
            if len(lst_empleados) > 0:
                nombre = input("Introduce el nombre del empleado: ")
                encontrado = False
                i = 0
                while not encontrado:
                    if lst_empleados[i].nombre == nombre:
                        porcentaje = float(input("Introduce el porcentaje de subida de sueldo: "))
                        lst_empleados[i].aumentar_salario(porcentaje)
                        encontrado = True
                    else:
                        i += 1
                if encontrado:
                    print(f"Aumentado el salario de {nombre} en un {porcentaje}%")
                else:
                    print(f"No existe empleado con nombre {nombre} en la lista!")
            else:
                print("No existe ningún empleado en la lista!")
        elif opcion == 4:
            if len(lst_empleados) > 0:
                for emp in lst_empleados:
                    print(f"Empleado: {emp}")
            else:
                print("No existe ningún empleado en la lista!")
        elif opcion == 5:
            print("Hasta la vista!")
            salir = True
