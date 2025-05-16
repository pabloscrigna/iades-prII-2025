"""
readline   ----> devuelve un str con la linea --> un str vacio al final del archivo
readlines  ----> devuelve una lista de str, cada elemento de la lista es una linea del archivo
"""

"""
Hacer un programa que cuente la cantidad de lineas de un archivo
"""

# usando readline

file = open("demo.txt", "r")

contador = 0

condicion = True


while condicion:
    condicion = False
    linea = file.readline()
    # print("linea: ", linea)
    print("largo: ", len(linea))

    if linea:
        contador += 1
        condicion = True

print(f"el archivo tiene {contador} lineas")
file.close()


# Tarea lo mismo con readlines
