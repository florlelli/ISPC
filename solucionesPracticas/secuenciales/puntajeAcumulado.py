partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))

puntos = (partidos_ganados * 3) + partidos_empatados

print("El equipo tiene", puntos, "puntos en el campeonato.")