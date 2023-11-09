"""
Iker Jiménez López, Aitor Palma, Xavier Cabello
8/11/2023
e2 "areGrowingNumbers"
"""
# Pide tres numeros
num1 = int(input("Cual es el primer numero? "))
num2 = int(input("Cual es el segundo numero? "))
num3 = int(input("Cual es el tercer numero? "))

# Estan en orden creciente?
if num1 < num2 < num3:
    print("Los numeros estan en orden creciente.")
else:
    print("Los numeros no estan en orden creciente.")

print("Programa finalizado")
