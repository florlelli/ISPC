# Definición de variables
largo = float(input("Ingrese el largo de la pared en metros: "))
ancho = float(input("Ingrese el ancho de la pared en metros: "))
costo_por_metro_cuadrado = float(input("Ingrese el costo por metro cuadrado de pintura en dólares: "))

# Cálculo del área de la pared
area_pared = largo * ancho

# Cálculo del costo de mano de obra
costo_mano_de_obra = area_pared * costo_por_metro_cuadrado

# Impresión del resultado
print("El costo de mano de obra para pintar la pared es: $", costo_mano_de_obra)