"""
Hacer un programa que cuente la cantidad de veces que aparece una palabra en un archivo de texto.

Buscar en un string la cantidad de veces que aparece una palabra
"""

palabra_buscar = "es"

# abrir el archivo --- context manager
# leer
# cerrarlo el archivo

# context manager
# archivo = open().....
with open("texto.txt", "r") as archivo:
    texto_lineas = archivo.readlines()
    # el context manager cierra el archivo

print("texto lineas: ", texto_lineas)
print(f"el archivo tiene {len(texto_lineas)} lineas.")

# buscar cuantas veces aparece la palabra
# texto_lineas es una lista

# texto_lineas: ['Este es un archivo de ejemplo - linea 1\n']
# contador = texto_lineas.count("linea")

contador = 0

# iteramos sobre cada linea del archivo
for linea in texto_lineas:
    # sacamos el \n del final y spliteamos la linea separada por espacios
    # linea_lista es una lista donde cada elemento es una palabra de "linea"
    linea_lista = linea.strip().split()
    # sumamos la cantidad de veces que aparece la palabra a buscar
    contador += linea_lista.count(palabra_buscar)

print(f"la palabra {palabra_buscar} aparece {contador} veces")

