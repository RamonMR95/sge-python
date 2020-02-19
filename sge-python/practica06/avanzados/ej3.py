# !/usr/bin/env python3
# 3.- Crear una aplicacion para gestionar un videoclub. El videoclub cuenta con varios tipos
# de producto
#   – Todos los productos tienen:
#   Referencia (Titulo, tipo(pelicula/videojuego), precio alquiler, plazo alquiler (dias),
#   alquilado (si/no)
#   – Pelicula
#   Genero (accion, fantastica, drama, aventuras, puzzle, infantil), año, director,
#   interpretes.
#   – Videojuego
#   Estilo (accion, deportes, aventuras, puzzle, infantil), plataforma (Xbox, playstation,
#   wii)
#   – Se mantiene un listado de clientes
#    Nº cliente, nombre, direccion, telefono, productos alquilado
#   – Se guarda un listado de registros de alquiler
#   – Cliente, producto, fecha alquiler, fecha devolucion, importe
# Crear una aplicacion de consola con el siguiente menú:
#   – Lista productos
#   – Añadir producto
#   – Ficha producto
#   – Lista clientes
#   – Añadir cliente
#   – Ficha cliente
#   – Alquiler producto
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


class Producto:

    def __init__(self, referencia, precio_alquiler, plazo_alquiler, alquilado):
        self.referencia = referencia
        self.precio_alquiler = precio_alquiler
        self.alquilado = False


class Pelicula(Producto):

    def __init__(self, referencia, precio_alquiler, plazo_alquiler, alquilado, genero, anyo, director, interpretes):
        Producto.__init__(self, referencia, precio_alquiler, plazo_alquiler, alquilado)
        self.genero = genero
        self.anyo = anyo
        self.director = director
        self.interpretes = interpretes


class Videojuego(Producto):

    def __init__(self, referencia, precio_alquiler, plazo_alquiler, alquilado, estilo, plataforma):
        Producto.__init__(self, referencia, precio_alquiler, plazo_alquiler, alquilado)
        self.estilo = estilo
        self.plataforma = plataforma


class Cliente:

    def __init__(self, numero, nombre, direccion, telefono, productos_alquilados):
        self.numero = numero
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos_alquilados = productos_alquilados


if __name__ == '__main__':
    lst_productos = []
    lst_clientes = []
    salir = False

    while not salir:
        opcion = int(input("\n1 – Lista productos\n"
                           "2 – Añadir producto\n"
                           "3 – Ficha producto\n"
                           "4 – Lista clientes\n"
                           "5 – Añadir cliente\n"
                           "6 – Ficha cliente\n"
                           "7 – Alquiler producto\n"
                           "8 - Salir"))
