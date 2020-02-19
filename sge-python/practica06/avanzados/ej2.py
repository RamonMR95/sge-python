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

    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

