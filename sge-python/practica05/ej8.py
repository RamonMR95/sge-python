# !/usr/bin/env python3
# 8.- Supón que mantenemos dos listas con igual número de elementos. Una de ellas,
# llamada alumnos, contiene una serie de nombres y la otra, llamada notas, una serie de números flotantes 0.0 y 10.0.
# En notas guardamos la calificación obtenida por los alumnos cuyos nombres están en alumnos. La nota notas[i]
# corresponde al estudiante alumnos[i]. Una posible configuración de las listas sería esta:
# alumnos = ['Ana_Pi','Pau_Lopez', 'Luis_Sol', 'Mar_Vega', 'Paz_Mir']
# notas = [10, 5.5, 2.0, 8.5, 7.0]
# De acuerdo con ella, el alumno Pau López, por ejemplo, fue calificado con un 5.5. Nos piden diseñar un procedimiento
# que recibe como datos las dos listas y una cadena con el nombre de un estudiante. Si el estudiante pertenece a la
# clase, el procedimiento imprimirá su nombre y nota en pantalla. Si no es un alumno incluido en la lista, se imprimirá
# un mensaje que lo advierta.

# Realizar las siguientes funciones:
# 1) Diseñar una función que reciba las dos listas y que devuelva el nombre de todos los estudiantes
# que aprobaron el examen
# 2) Diseñar una función que reciba la lista de notas y devuelva el número de aprobados
# 3) Diseñar una función que reciba las dos listas y devuelva el nombre de todos los estudiantes que
# obtuvieron la máxima nota.
# 4) Diseñar una función que reciba las dos listas y devuelva el nombre de todos los estudiantes cuya
# calificación es igual o superior a la calificación media.
# 5) Diseñar una función que reciba las dos listas y un nombre (una cadena); si el nombre está en la
# lista de estudiantes, devolverá su nota, si no, devolverá None.
# Haciendo uso de las funciones anteriores y diseñando nuevas funciones si es necesario. Construir un
# programa que presente el siguiente menú y permita ejecutar las acciones correspondientes a cada opción:
# 1) Añadir estudiante y calificación
# 2) Mostrar lista de estudiantes con sus calificaciones
# 3) Mostrar estudiantes aprobados
# 4) Número de aprobados
# 5) Estudiantes con máxima nota
# 6) Estudiantes con nota mayor o igual a la media
# 7) Nota estudiante
# 8) Finalizar ejecución del programa
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"

alumnos = ['Ana_Pi', 'Pau_Lopez', 'Luis_Sol', 'Mar_Vega', 'Paz_Mir']
notas = [10, 5.5, 2.0, 8.5, 7.0]


def mostrar_aprobados(alums, nots):
    aprobados = []
    for i in range(len(notas)):
        if notas[i] >= 5:
            aprobados.append(alumnos[i])
    return aprobados


def mostrar_numero_aprobados(nots):
    n_aprobados = 0
    for nota in nots:
        if nota >= 5:
            n_aprobados += 1
    return n_aprobados


def mostrar_alumnos_max_nota(alums, nots):
    alumnos_max_nota = []
    max_nota = max(nots)
    for i in range(len(nots)):
        if nots[i] == max_nota:
            alumnos_max_nota.append(alumnos[i])
    return alumnos_max_nota


def mostrar_alumnos_nota_sup_media(alums, nots):
    alumnos_media = []
    media = sum(nots) / len(nots)
    for i in range(len(nots)):
        if nots[i] >= media:
            alumnos_media.append(alumnos[i])
    return alumnos_media


def is_in_alumnos(alums, nots, nombre):
    for i in range(len(alums)):
        if alumnos[i] == nombre:
            return nots[i]
    return None


def mostrar_alumnos_calificaciones(alums, nots):
    for i in range(len(alums)):
        print(f"Alumno: {alums[i]}: {nots[i]}")


menu = f"1) Añadir estudiante y calificación\n" \
       f"2) Mostrar lista de estudiantes con sus calificaciones\n" \
       f"3) Mostrar estudiantes aprobados\n" \
       f"4) Número de aprobados\n" \
       f"5) Estudiantes con máxima nota\n" \
       f"6) Estudiantes con nota mayor o igual a la media\n" \
       f"7) Nota estudiante\n" \
       f"8) Finalizar ejecución del programa\n"

opcion = int(input(menu))

while opcion != 8:
    if opcion == 1:
        print("Añadir estudiante: ")
        nombre = input("Introduce nombre del estudiante: ")
        calificacion = float(input("Introduce la nota del estudiante: "))
        alumnos.append(nombre)
        notas.append(calificacion)
    elif opcion == 2:
        mostrar_alumnos_calificaciones(alumnos, notas)
    elif opcion == 3:
        print(mostrar_aprobados(alumnos, notas))
    elif opcion == 4:
        print(mostrar_numero_aprobados(notas))
    elif opcion == 5:
        print(mostrar_alumnos_max_nota(alumnos, notas))
    elif opcion == 6:
        print(mostrar_alumnos_nota_sup_media(alumnos, notas))
    elif opcion == 7:
        nombre = input("Introduce el nombre del estudiante: ")
        nota = is_in_alumnos(alumnos, notas, nombre)
        if nota:
            print(f" Alumno: {nombre}, Nota {nota}")
        else:
            print("El estudiante no existe en la lista")

    opcion = int(input(menu))
