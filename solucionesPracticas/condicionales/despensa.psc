Algoritmo Calculo_Pago_Leche
	
    // Declaración de variables
    Definir cantidad_leche Como Entero
    Definir es_jubilado Como Cadena
    Definir precio_unitario, precio_total, descuento Como Real
	
    // Solicitar al usuario la cantidad de litros de leche comprados y si es jubilado
	Escribir "Ingrese la cantidad de litros de leche comprados:"
    Leer cantidad_leche
	Escribir "¿Es usted jubilado? responda si o no:"
    Leer es_jubilado
	
    // Calcular el precio total sin descuentos
    precio_unitario <- 1000
    precio_total <- cantidad_leche * precio_unitario
	
    // Aplicar descuentos según la cantidad de litros comprados
    Si cantidad_leche > 24 Entonces
        descuento <- 0.15
    Sino
        Si cantidad_leche > 12 Entonces
            descuento <- 0.10
        Sino
            descuento <- 0
        FinSi
    FinSi
	
    // Aplicar descuento adicional para jubilados
    Si es_jubilado = "si" Entonces
        descuento <- descuento + 0.10
    FinSi
	
    // Calcular el precio con descuentos
    precio_con_descuento <- precio_total * (1 - descuento)
	
    // Mostrar el monto a pagar al cliente
    Escribir "El monto a pagar es:", precio_con_descuento, "pesos."
	
FinAlgoritmo
