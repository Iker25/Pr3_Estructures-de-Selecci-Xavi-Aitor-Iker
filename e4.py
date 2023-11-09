"""
Iker Jiménez López, Aitor Palma, Xavier Cabello
8/11/2023
e4 "customerLoyaltyCard.py “dia sense IVA”"
"""

# Importe con IVA incluido
i_factura = int(input("Cual es el importe con iva? "))

# Importe igual o superior a 100 €?
# Si es igual o superior a 100 €, descuento del 21%
descuento = 0.21 if i_factura >= 100 else 0

# Calcula el importe final con descuento
i_final = i_factura - (i_factura * descuento)

# Ingresar el tipo de IVA (21%, 10%, etc.)
t_iva = int(input("Cual es el tipo de IVA? "))

# Importe con IVA
i_con_iva = i_final * (1 + (t_iva / 100))

# Resultados
print(f"Importe final con descuento: {i_final:.2f} €")
print(f"Importe final con IVA ({t_iva}%): {i_con_iva:.2f} €")

print("Programa finalizado")
