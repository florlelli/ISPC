cantidad_leche = int(input("Ingrese la cantidad de litros de leche comprados: "))
es_jubilado = input("¿Es usted jubilado? (responda 'si' o 'no'): ").lower()

precio_unitario = 1000
precio_total = cantidad_leche * precio_unitario

if cantidad_leche > 24:
    descuento = 0.15
elif cantidad_leche > 12:
    descuento = 0.10
else:
    descuento = 0

if es_jubilado == 'si':
    descuento += 0.10

precio_con_descuento = precio_total * (1 - descuento)

print("El monto a pagar es:", precio_con_descuento, "pesos.")
