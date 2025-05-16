"""
Leer el contenido de un archivo

"""

# open() -> open(file, mode)
file = open("ejemplo.txt", "r")

# read()
# read lee todo el archivo
texto = file.read()

# cerramos el archivo
file.close()

# imprimimos el contenido del archivo
print(texto)

