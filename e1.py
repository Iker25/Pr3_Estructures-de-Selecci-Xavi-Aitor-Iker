"""
Iker Jiménez López, Aitor Palma, Xavier Cabello
8/11/2023
e1 "Is bigger"
"""

# Pide dos numeros
num1, num2 = map(float, input("Añade dos números separados por un espacio: ").split())

# Garantiza que el numero1 sea mas pequeño que el numero2
if num1 > num2:
    num1, num2 = num2, num1

# Muestra los valores por pantalla
print("El primer número és:", num1)
print("El segundo número és:", num2)
