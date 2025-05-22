"""
buscar en un string la cantidad de veces que aparece una palabra
"""

palabra_buscar = "linea

linea = "Este es un texto de prueba que contiene una sola linea - linea"

# transformamos el string en una lista con las palabras
linea_lista = linea.split()

print("mensaje: ", linea)
print("mensaje lista: ", linea_lista)

# contamos cuantas veces aparece el elemento palabra_buscar en la lista 
contador = linea_lista.count(palabra_buscar)



print(f"la palabra {palabra_buscar} aparece {contador} veces")