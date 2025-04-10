""""
ejercico:
Un equipo jugo 10 partidos calcular cuantos puntos obtuvo el equipo siendo 
1 punto  partido empatado 
3 puntos partido ganado 
0 puntos partido perdido
"""

cantidad_de_partidos = 10
# ganados = 0
# empatados = 0
puntos = 0

# "g" ganado "e" empatado "p" perdido
for i in range(cantidad_de_partidos):
    opcion = input(f"Resultado del partido numero {i+1} g: ganado e empatado p perdido ")
    # si la opcion ingresada es valida
    if opcion in ["g", "e", "p"]:
        if opcion == "g":
            puntos += 3
            # print(f"opcion: {opcion} -- puntos: {puntos}")
            # puntos = puntos + 3
        elif opcion == "e":
            puntos += 1
            # print(f"opcion: {opcion} -- puntos: {puntos}")
            # puntos = puntos + 1
        # else:
            # print(f"opcion: {opcion} -- puntos: {puntos}")
            # puntos = puntos + 0
        
        print(f"debug: partido n: {i+1} opcion: {opcion} -- puntos: {puntos}")

    else:
        print("Opcion no valida")
        exit(1)

print(f"El equipo obtuvo {puntos} puntos")

