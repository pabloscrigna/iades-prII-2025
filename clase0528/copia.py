# usage: python3 copia.py origen destino

import sys

print(sys.argv)
print(len(sys.argv))

if len(sys.argv) < 3:
    print("Faltan argumentos") 
    exit(1)

print("archivo origen: ", sys.argv[1])
print("archivo destino: ", sys.argv[2])

archivo_origen = sys.argv[1]  # Lectura
archivo_destino = sys.argv[2] # Escritura

with open(archivo_origen, "r") as file:
    datos = file.read()     # en datos tengo el contenido del archivo "archivo_origen"

with open(archivo_destino, "w") as file:
    file.write(datos)

print("copia exitosa")
