"""
Lectura de un archivo 

funcion: readlines

"""

# abrimos el archivo en modo lectura
file = open("data", "r")

# leemos el texto completo
# readlines retorna una lista
# cada elemento de la lista es 
texto = file.readlines()


print("texto: ", texto)

for linea in texto:
    print(linea.strip())

# cerramos el archivo
file.close()

