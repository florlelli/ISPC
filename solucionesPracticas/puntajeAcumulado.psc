Algoritmo Calculo_Puntos_Equipo
    // Declaración de variables
    Definir partidos_ganados, partidos_empatados, partidos_perdidos, puntos Como Entero
    // Solicitar al usuario la cantidad de partidos ganados, empatados y perdidos
    Escribir "Ingrese la cantidad de partidos ganados:"
    Leer partidos_ganados
    Escribir "Ingrese la cantidad de partidos empatados:"
    Leer partidos_empatados
    Escribir "Ingrese la cantidad de partidos perdidos:"
    Leer partidos_perdidos
    // Calcular la cantidad de puntos acumulados
    puntos <- (partidos_ganados * 3) + partidos_empatados
    // Mostrar el resultado al usuario
    Escribir "El equipo tiene", puntos, "puntos en el campeonato."
	
FinAlgoritmo






