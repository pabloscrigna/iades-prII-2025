"""
Pedir al usuario ingresar nombre dni sexo y guardarlo en un archivo separado por coma

Repetir dos veces

nombre,dni,sexo

"""

file = open("alumnos.csv", "w+")

for _ in range(2):
    nombre = input("Ingrese su nombre: ")
    dni = input("Ingrese su dni: ")
    sexo = input("ingrese su sexo: ")
    file.write(f"{nombre},{dni},{sexo}\n")

file.close()
