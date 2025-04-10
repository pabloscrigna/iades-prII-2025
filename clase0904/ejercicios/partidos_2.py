""" "
ejercico:
Un equipo jugo 10 partidos calcular cuantos puntos obtuvo el equipo siendo
1 punto  partido empatado
3 puntos partido ganado
0 puntos partido perdido
"""

cantidad_de_partidos = 10
puntos = 0
opciones = ["g", "e", "p"]

# "g" ganado "e" empatado "p" perdido
for i in range(cantidad_de_partidos):
    mensaje = f"Resultado del partido numero {i+1}"
    mensaje = f"{mensaje} (g) ganado, (e) empatado, (p) perdido: "
    opcion = input(mensaje)

    # si la opcion ingresada es invalida
    var = opcion in opciones
    if not var:
        print("Opcion no valida")
        exit(1)

    if opcion == "g": 
        puntos += 3

    elif opcion == "e":
        puntos += 1

    print(f"debug: partido n: {i+1} opcion: {opcion} -- puntos: {puntos}")


print(f"El equipo obtuvo {puntos} puntos")
