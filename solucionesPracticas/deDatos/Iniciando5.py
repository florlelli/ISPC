# Ejercicio 5
n = int(input("Ingrese la cantidad de números pares a guardar: "))
pares = tuple(i for i in range(2 * n) if i % 2 == 0)
print("Números pares:", pares)
