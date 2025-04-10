""""
ejercico:
Un equipo jugo 10 partidos calcular cuantos puntos obtuvo el equipo siendo 
1 punto  partido empatado 
3 puntos partido ganado 
0 puntos partido perdido
"""

ganados = int(input("cuantos partidos ganados? "))
empatados = int(input("cuantos partidos empatados? "))
perdidos = int(input("cuantos partidos perdidos? "))

total_partidos = ganados + empatados + perdidos
# Validar que la suma de partidos ganados, empatados y perdidos sea 10
if total_partidos != 10:
    print("La suma de partidos ganados, empatados y perdidos debe ser 10.")
    exit(1)

# Calcular puntos
puntos = (ganados * 3) + (empatados * 1)
print(f"El equipo obtuvo {puntos} puntos.")

