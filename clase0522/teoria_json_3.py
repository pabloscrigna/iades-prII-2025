"""
Vamos a leer un json desde un archivo: usuarios.json
y guardar el contenido del json en un archivo backup.json
"""

# 1. importamos el modulo
import json

# 2. abrir el archivo y leemos el contenido en formato json
with open("usuarios.json", "r") as file:
    usuarios = json.load(file)

# datos tenemos el contenido del archivo en una estructura de datos de python
print("usuarios: ", usuarios)     # lista
print("type usuarios: ", type(usuarios))

for usuario in usuarios:    # usuario ---->  diccionario  
    print(usuario)

# creamos un nuevo usuario
nuevo_usuario = {
    "id": "u5000",
    "status": True
}

# agregamos el nuevo usuario en la lista de usuarios
usuarios.append(nuevo_usuario)

print(usuarios)


# abrimos el archivo en modo escritura
with open("usuarios.json", "w") as file:
    json.dump(usuarios, file, indent= 4)

print("FIN")




