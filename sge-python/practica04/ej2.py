# !/usr/bin/env python3
# 2.- Una empresa multinacional dispone de una secuencia FEMPLE (se harán dos versiones una con
# una lista y otra con un diccionario), con los datos de sus empleados. Cada elemento tiene la siguiente información
# (en la primera versión se pueden poner los datos fijos de la secuencia):
# Número de empleado, Nombre, Categoría, País al que pertenece.
# Las categorías laborales son A, B, C, D, E, F. La empresa tiene empleados destinados en 7
# países (Francia, España, Portugal, Alemania, Suiza, Noruega, China). A partir de esta secuencia se desea obtener la
# siguiente información:
# - Número total de empleados por categoría,
# - Número total de empleados por país,
# - País con máximo número de empleados (se supone que no hay dos países coincidentes en ello).
# Versión 2.b - Permitir que la
# secuencia sea introducida al principio o que se coja la que está por defecto.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


lst_paises = ['Francia', 'España', 'Portugal', 'Alemania', 'Suiza', 'Noruega', 'China']
lst_categorias = ['A', 'B', 'C', 'D', 'E', 'F']

# A
# LISTAS

categorias = []
paises = []


lst_empleados = [
    [1, 'Ramón', 'A', 'Francia'],
    [2, 'Antonio', 'B', 'China'],
    [3, 'Alberto', 'B', 'Francia']
]

print("Resolucion con listas")

res = []

for i in range(len(lst_empleados)):
    categorias.append(lst_empleados[i][2])
    paises.append(lst_empleados[i][3])

print("Paises")

for i in range(len(lst_paises)):
    if paises.count(lst_paises[i]) > 0:
        print(f"{lst_paises[i]} : {paises.count(lst_paises[i])} repetido")

print("\nCategorias")

for i in range(len(lst_categorias)):
    if categorias.count(lst_categorias[i]) > 0:
        print(f"{lst_categorias[i]} : {categorias.count(lst_categorias[i])} repetido")


# DICCIONARIO
categorias = {}
paises = {}

dict_empleados = {
    1: ['Ramón', 'A', 'Francia'],
    2: ['Antonio', 'B', 'China'],
    3: ['Alberto', 'B', 'Francia']
}

print("\nResolucion con diccionarios")

for i in dict_empleados:
    if (dict_empleados[i])[1] not in categorias:
        categorias[(dict_empleados[i])[1]] = 1
    else:
        categorias[(dict_empleados[i])[1]] += 1

    if (dict_empleados[i])[2] not in paises:
        paises[(dict_empleados[i])[2]] = 1
    else:
        paises[(dict_empleados[i])[2]] += 1


print(f"Categorias: {categorias}")
print(f"Paises: {paises}")
print(f"País con mayor número de empleados: {max(paises.values())}")



