"""
Hacer un programa que cuente la cantidad de veces que aparece una palabra en un archivo
"""

file = open("archivo.txt", "r")

lineas = file.readlines()

print("lineas: ", lineas)

file.close()

contador = 0

for linea in lineas