total_alumnos = int(input("Ingrese la cantidad de alumnos que rindieron el examen: "))
suma_notas = 0
for i in range(total_alumnos):
    nota = float(input("Ingrese la nota del alumno {}: ".format(i + 1)))
    suma_notas += nota
promedio = suma_notas / total_alumnos
if promedio > 8:
    print("El rendimiento es elevado")
elif 6 <= promedio <= 8:
    print("El rendimiento es aceptable")
else:
    print("El rendimiento es bajo")
