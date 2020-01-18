# Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno. Escribir un programa que calcule el sueldo
# bruto mensual en euros a partir de los siguientes datos.

dias_trabajados = int(input("Días trabajados: "))
dias_festivos_trabajados = int(input("Días festivos trabajados: "))
turno = input("Turno (M-Mañana, T-Tarde, N-Noche: ")

if dias_trabajados + dias_festivos_trabajados <= 30:
    sueldo = dias_trabajados * 12 * 8 + dias_festivos_trabajados * 24 * 8

    if turno == "N":
        sueldo = sueldo * 1.2

    print(f"Sueldo: {round(sueldo)} euros.")
else:
    print("Número inválido de días trabajados.")


