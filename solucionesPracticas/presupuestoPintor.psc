Algoritmo Calculo_Costo_Mano_De_Obra_Pintura
	// Declaraci�n de variables
	Definir largo, ancho, costo_por_metro_cuadrado, area_pared, costo_mano_de_obra Como Real
	// Solicitar al usuario los datos necesarios
	Escribir "Ingrese el largo de la pared en metros: "
	Leer largo
	Escribir "Ingrese el ancho de la pared en metros: "
	Leer ancho
	Escribir "Ingrese el costo por metro cuadrado de pintura en d�lares: "
	Leer costo_por_metro_cuadrado
	// Calcular el �rea de la pared
	area_pared <- largo * ancho
	// Calcular el costo de mano de obra
	costo_mano_de_obra <- area_pared * costo_por_metro_cuadrado
	// Mostrar el resultado al usuario
	Escribir "El costo de mano de obra para pintar la pared es: $",costo_mano_de_obra
FinAlgoritmo
