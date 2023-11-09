"""
Iker Jiménez López, Aitor Palma, Xavier Cabello
8/11/2023
e6 "calculateMyWaterBill"
"""

# Letra de tipo vivienda i número de m3 de agua
t_h = int(input("CUal es la letra de tipo vivienda? "))
m3_a_g = int(input("Cual es el nombre de m3 gastados? "))

# Constante precio base
p_base = 6.40

# Constante precio por m3
p_por_m3 = 0.5849

# Precio total de la factura de agua
p_total = m3_a_g * p_por_m3 + p_base

# Precio total de la factura de agua redondeado a 2 decimales
print(f"El precio total de la factura de agua és: {p_total:.2f} €")

print("Programa finalizado")
