"""
Iker Jiménez López, Aitor Palma, Xavier Cabello
8/11/2023
e5 "isACorrectDate"
"""

# Solicita una fecha en formato DD/MM/AAAA
fecha = input("Pon una fecha (en formato DD/MM/AAAA): ")

try:
    dia, mes, año = map(int, fecha.split('/'))

    # Lista de días por mes
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Comprueba si el año es bisiesto y ajusta el mes febrero si es necesario
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dias_por_mes[2] = 29

    if 1 <= mes <= 12 and 1 <= dia <= dias_por_mes[mes]:
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")
except ValueError:
    print("Formato de fecha incorrecto")

