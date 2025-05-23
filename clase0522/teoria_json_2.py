"""
Vamos a leer un dato json desde un archivo
"""

# 1. importamos el modulo
import json

# 2. abrir el archivo y leemos el contenido en formato json
with open("usuario.json", "r") as file:
    datos = json.load(file)

# datos tenemos el contenido del archivo en una estructura de datos de python
print("datos: ", datos)
print("type datos: ", type(datos))
print("nombre: ", datos["nombre"])

# cambiamos el nombre de la clave "nombre"
datos["nombre"] = "Ernesto"


# almacenar el diccionario en un archivo en formato json
with open("usuario.json", "w") as file:
    json.dump(datos, file, indent=4)


print("FIN")