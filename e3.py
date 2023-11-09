"""
Iker Jiménez López, Aitor Palma, Xavier Cabello
8/11/2023
e3 "fastAndFurios"
"""

# Velocidad inicial aceleración y tiempo
v_i = float(input("Cual es velocidad inicial? "))
aceleracion = float(input("Cual es la aceleración? "))
tiempo = float(input("Cual es el tiempo? "))

# El objeto esta parado?
if (v_i + (aceleracion * tiempo)) <= 0:
    print("El objeto está parado, por lo tanto no se puede calcular la velocidad media.")
else:
    # Velocidad media
    v_m = v_i + (aceleracion * tiempo) / 2
    print("La velocidad instantánea es:", v_i + (aceleracion * tiempo), "m/s")
    print("La velocidad media es:", v_m, "m/s")

print("Programa finalizado")
