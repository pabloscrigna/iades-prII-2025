"""
Escribir Hola mundo en un archivo 
"""

nombre_de_archivo = "archivo.txt"

file = open(nombre_de_archivo, "w")

mensaje = "Hola mundo!!!\n"

file.write(mensaje)

file.write("saliendo....")

file.close()