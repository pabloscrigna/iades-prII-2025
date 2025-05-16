"""
Vamos a crear un archivo que se llame alumnos.txt y vamos a escribir una linea
"""

# abre un archivo en modo escritura en el directorio archivos
file = open("./archivos/alumnos.txt", "a")

file.write("mica,27,pyton\n")
file.write("maria,30,java\n")
file.close()
