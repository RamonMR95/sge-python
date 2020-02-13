# !/usr/bin/env python3
# 6.- En Matemáticas, la sucesión de Fibonacci es la siguiente sucesión infinita de números
# naturales. Genera 100 primeros.
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


lst = [0, 1]

for i in range(2, 101):
    lst.append(lst[i - 1] + lst[i - 2])

print(lst)
