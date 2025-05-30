import json

def guardar(file_name, datos):

    with open(file_name, "w") as file:
        json.dump(datos,file,indent=4)