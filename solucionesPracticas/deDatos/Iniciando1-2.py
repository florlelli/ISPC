# Parte 1: Iniciando
# Ejercicio 1
nombres = []
while len(nombres) < 10:
    nombre = input("Ingrese un nombre: ")
    if nombre not in nombres:
        nombres.append(nombre)
    else:
        print("El nombre ya está en la lista, ingrese uno diferente.")

print("Lista de nombres ingresados:", nombres)
# Ejercicio 2
if len(nombres) >= 3:
    nombres.pop(2)  # Eliminar la tercera persona
nombres.pop()  # Eliminar la última persona
nombres.sort()
print("Lista de nombres después de eliminar y ordenar:", nombres)
