Algoritmo Tabla_Multiplicar_Mientras
    Definir numero, contador, resultado Como Entero
	
    Escribir "Ingrese un número del 1 al 10: "
    Leer numero
    contador <- 1
    Mientras contador <= 10 Hacer
        resultado <- numero * contador
        Escribir numero, "x", contador, "=", resultado
        contador <- contador + 1
    Fin Mientras
Fin Algoritmo
