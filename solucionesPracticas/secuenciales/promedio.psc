Algoritmo Calculo_Promedio_Notas
	// Declaración de variables
	Definir nota1, nota2, nota3, nota4, nota5 Como Real
    Definir suma, promedio Como Real
	// Solicitar al usuario que ingrese las notas
	Escribir "Ingrese la nota 1:"
    Leer nota1
    Escribir "Ingrese la nota 2:"
    Leer nota2
    Escribir "Ingrese la nota 3:"
    Leer nota3
    Escribir "Ingrese la nota 4:"
    Leer nota4
    Escribir "Ingrese la nota 5:"
    Leer nota5	
    // Calcular la suma de las notas
    suma <- nota1 + nota2 + nota3 + nota4 + nota5	
    // Calcular el promedio de las notas
    promedio <- suma / 5	
    // Mostrar el resultado al usuario
    Escribir "El promedio de las notas es:", promedio
FinAlgoritmo
