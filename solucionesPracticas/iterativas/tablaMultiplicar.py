numero = int(input("Ingrese un número del 1 al 10: "))
contador = 1
while contador <= 10:
    resultado = numero * contador
    print("{}x{}={}".format(numero, contador, resultado))
    contador += 1
