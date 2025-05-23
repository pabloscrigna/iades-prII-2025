"""
Como convertir un diccionario en python a json
"""

# 1. importamos el 
import json

# 2. creamos un diccionario
alumno = {
    "nombre": "Pablo",
    "edad": 30,
    "hijos": None,
    "estado": True
}

# 3. convertimos el diccionario a json 
alumno_json = json.dumps(alumno)

print("alumno diccionario: ", alumno)
print("alumno en json: ",alumno_json)


print("type alumno diccionario: ", type(alumno))
print("type alumno_json: ", type(alumno_json))


# 4. convertimos el string json en un diccionario

alumno_dict = json.loads(alumno_json)

print("alumno dict: ", alumno_dict)