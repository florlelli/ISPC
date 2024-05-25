Algoritmo Rendimiento_Alumnos
    Definir total_alumnos, i Como Entero
    Definir suma_notas, nota, promedio Como Real
	
    Escribir "Ingrese la cantidad de alumnos que rindieron el examen: "
    Leer total_alumnos
    suma_notas <- 0
    Para i <- 1 Hasta total_alumnos Con Paso 1 Hacer
        Escribir "Ingrese la nota del alumno ", i, ": "
        Leer nota
        suma_notas <- suma_notas + nota
    Fin Para
    promedio <- suma_notas / total_alumnos
	Si promedio > 8 Entonces
		Escribir "El rendimiento es elevado"
	SiNo
		Si promedio >= 6 Entonces
			Escribir "El rendimiento es aceptable"
		SiNo
			Escribir "El rendimiento es bajo"
		Fin Si
	Fin Si
	Fin Algoritmo
