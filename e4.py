# Solicita al usuario que ingrese el importe con IVA incluido.
importe_factura = float(input("Ingresa el importe con IVA incluido: "))

# Comprueba si el importe es igual o superior a 100 €
if importe_factura >= 100:
    descompte = importe_factura * 0.21  # Calcula el 21% de descuento
    importe_final = importe_factura - descompte  # Calcula el importe final con descuento
else:
    importe_final = importe_factura  # Sin descuento si el importe es inferior a 100 €

# Solicita al usuario que ingrese el tipo de IVA (21%, 10%, etc.)
tipo_iva = float(input("Ingresa el tipo de IVA (en porcentaje): "))

# Calcula el importe con IVA
importe_con_iva = importe_final * (1 + (tipo_iva / 100))

# Muestra los resultados
print(f"Importe final con descuento: {importe_final} €")
print(f"Importe final con IVA ({tipo_iva}%): {importe_con_iva} €")

