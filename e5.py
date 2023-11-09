"""
Iker Jiménez López, Aitor Palma, Xavier Cabello
8/11/2023
e5 "isACorrectDate"
"""

# Pon la fecha
fecha = input("Cual es la fecha? (Ponla en formato DD/MM/AAAA) ")

try:
    d, m, a = map(int, fecha.split('/'))

    # Comprobación si el año es bisiesto y ajustar el mes febrero si es necesario
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        d_febrero = 29
    else:
        d_febrero = 28

    # La fecha es valida
    if 1 <= m <= 12 and 1 <= d <= [0, 31, d_febrero, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m]:
        print("La fecha es válida.")
    # La fecha no es valida
    else:
        print("La fecha no es válida.")
except ValueError:
    print("El formato de fecha no es correcto")

print("Programa finalizado")
