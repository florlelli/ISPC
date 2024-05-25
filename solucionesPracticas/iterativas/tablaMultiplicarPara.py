numero = int(input("Ingrese un número del 1 al 10: "))
for contador in range(1, 11):
    resultado = numero * contador
    print("{}x{}={}".format(numero, contador, resultado))
