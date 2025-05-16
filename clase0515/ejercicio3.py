"""
ingresar un nuevo alumno en alumnos.csv

Si el dni ya existe, no ingresar.
"""

nombre = input("Ingrese su nombre: ")
dni = input("Ingrese su dni: ")
sexo = input("ingrese su sexo: ")


file = open("alumnos.csv", "r+")


alumnos = file.readlines()
print("alumnos: ", alumnos)
#nombre,dni,sexo

for alumno in alumnos:
    if dni == alumno.split(",")[1]:
        print("El alumno ya existe")
        exit(1)

file.write(f"{nombre},{dni},{sexo}\n")
file.close()